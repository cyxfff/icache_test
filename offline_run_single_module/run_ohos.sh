#!/bin/sh
set -eu

WORKDIR="${WORKDIR:-/data/local/tmp/synthesis_hiperf}"
MANIFEST="${MANIFEST:-${WORKDIR}/manifest.tsv}"
LOGDIR="${LOGDIR:-${WORKDIR}/logs}"
TMPDIR="${TMPDIR:-${WORKDIR}/tmp}"

DEFAULT_ITERS="${ITERS:-1000}"
DEFAULT_ROUNDS="${ROUNDS:-1}"
DEFAULT_CPU_MASK="${CPU_MASK:-}"

DEFAULT_EVENT_GROUPS="
raw-cpu-cycles:u,raw-instruction-retired:u,raw-br-mis-pred:u,raw-br-retired:u
raw-instruction-retired:u,raw-l1-icache:u,raw-l1-icache-refill:u,raw-l2-icache:u,raw-l2-icache-refill:u
raw-instruction-retired:u,raw-l1-itlb:u,raw-l1-itlb-refill:u,raw-l2-itlb:u,raw-l2-itlb-refill:u
"
EVENT_GROUPS="${EVENT_GROUPS:-${DEFAULT_EVENT_GROUPS}}"

mkdir -p "${WORKDIR}" "${LOGDIR}" "${TMPDIR}"

if ! command -v hiperf >/dev/null 2>&1; then
    echo "[ERROR] hiperf not found"
    exit 1
fi

if [ ! -f "${MANIFEST}" ]; then
    echo "[ERROR] manifest not found: ${MANIFEST}"
    exit 1
fi

abs_path() {
    path="$1"
    case "${path}" in
        /*) echo "${path}" ;;
        *) echo "${WORKDIR}/${path}" ;;
    esac
}

start_target() {
    bin="$1"
    iters="$2"
    cpu_mask="$3"
    target_log="$4"

    : > "${target_log}"

    chmod +x "${bin}"

    if [ -n "${cpu_mask}" ] && command -v taskset >/dev/null 2>&1; then
        (
            cd "${WORKDIR}"
            exec taskset "${cpu_mask}" "${bin}" "${iters}" > "${target_log}" 2>&1
        ) &
    else
        if [ -n "${cpu_mask}" ]; then
            echo "[WARN] taskset not found, running without CPU affinity" >> "${target_log}"
        fi
        (
            cd "${WORKDIR}"
            exec "${bin}" "${iters}" > "${target_log}" 2>&1
        ) &
    fi

    LAUNCH_PID=$!
}

wait_ready() {
    pid="$1"
    target_log="$2"
    timeout=200

    while [ "${timeout}" -gt 0 ]; do
        if ! kill -0 "${pid}" 2>/dev/null; then
            echo "[ERROR] benchmark exited before ready"
            cat "${target_log}"
            return 1
        fi

        if grep -q "PROXYBENCH_READY" "${target_log}" 2>/dev/null; then
            return 0
        fi

        sleep 0.05
        timeout=$((timeout - 1))
    done

    echo "[ERROR] timeout waiting for PROXYBENCH_READY"
    kill -9 "${pid}" 2>/dev/null || true
    return 1
}

start_hiperf() {
    events="$1"
    pid="$2"
    perf_log="$3"

    : > "${perf_log}"

    OLD_IFS="$IFS"
    IFS=','
    set -- stat
    for ev in ${events}; do
        set -- "$@" -e "$ev"
    done
    IFS="$OLD_IFS"

    set -- "$@" -p "${pid}"
    hiperf "$@" > "${perf_log}" 2>&1 &
    PERF_PID=$!
}

run_once() {
    case_id="$1"
    bin="$2"
    iters="$3"
    cpu_mask="$4"
    events="$5"
    round="$6"
    group_id="$7"
    case_log="$8"

    [ -z "${events}" ] && return 0

    target_log="${TMPDIR}/${case_id}.round${round}.group${group_id}.target.log"
    perf_log="${TMPDIR}/${case_id}.round${round}.group${group_id}.perf.log"

    echo "===== perf group =====" >> "${case_log}"
    echo "case_id=${case_id}" >> "${case_log}"
    echo "round=${round}" >> "${case_log}"
    echo "group_id=${group_id}" >> "${case_log}"
    echo "events=${events}" >> "${case_log}"
    echo "iters=${iters}" >> "${case_log}"
    echo "cpu_mask=${cpu_mask:-<none>}" >> "${case_log}"
    echo "bin=${bin}" >> "${case_log}"

    start_target "${bin}" "${iters}" "${cpu_mask}" "${target_log}"

    if ! wait_ready "${LAUNCH_PID}" "${target_log}" >> "${case_log}" 2>&1; then
        cat "${target_log}" >> "${case_log}" 2>/dev/null || true
        echo "===== group failed before ready =====" >> "${case_log}"
        return 1
    fi

    pid="${LAUNCH_PID}"
    echo "PID is ${pid}" >> "${case_log}"

    start_hiperf "${events}" "${pid}" "${perf_log}"

    sleep 0.5
    if ! kill -0 "${PERF_PID}" 2>/dev/null; then
        echo "[ERROR] hiperf exited immediately" >> "${case_log}"
        cat "${perf_log}" >> "${case_log}" 2>/dev/null || true
        kill -TERM "${pid}" 2>/dev/null || true
        wait "${pid}" 2>/dev/null || true
        return 1
    fi

    kill -USR1 "${pid}" 2>/dev/null || true

    wait "${PERF_PID}" || true
    cat "${perf_log}" >> "${case_log}" 2>/dev/null || true

    wait "${pid}" 2>/dev/null || true
    cat "${target_log}" >> "${case_log}" 2>/dev/null || true

    echo "===== group end =====" >> "${case_log}"
    echo >> "${case_log}"

    sleep 1
}

run_case() {
    case_id="$1"
    bin_path="$2"
    iters="$3"
    rounds="$4"
    cpu_mask="$5"

    [ -z "${iters}" ] && iters="${DEFAULT_ITERS}"
    [ -z "${rounds}" ] && rounds="${DEFAULT_ROUNDS}"
    [ -z "${cpu_mask}" ] && cpu_mask="${DEFAULT_CPU_MASK}"

    bin="$(abs_path "${bin_path}")"
    case_log="${LOGDIR}/${case_id}.log"

    if [ ! -x "${bin}" ]; then
        echo "[ERROR] binary not executable or missing: ${bin}"
        return 1
    fi

    if [ -s "${case_log}" ]; then
        echo "[SKIP] ${case_id} -> ${case_log} exists"
        return 0
    fi

    echo "[RUN] ${case_id}"

    {
        echo "===== case start ====="
        echo "case_id=${case_id}"
        echo "bin=${bin}"
        echo "iters=${iters}"
        echo "rounds=${rounds}"
        echo "cpu_mask=${cpu_mask:-<none>}"
        echo "start_time=$(date '+%F %T')"
        echo
    } > "${case_log}"

    round=1
    while [ "${round}" -le "${rounds}" ]; do
        echo "===== round ${round}/${rounds} =====" >> "${case_log}"

        group_id=0
        while IFS= read -r events; do
            [ -z "${events}" ] && continue
            group_id=$((group_id + 1))

            if ! run_once "${case_id}" "${bin}" "${iters}" "${cpu_mask}" "${events}" "${round}" "${group_id}" "${case_log}"; then
                echo "[ERROR] case=${case_id} round=${round} group=${group_id}" >> "${case_log}"
            fi
        done <<EOF
${EVENT_GROUPS}
EOF

        round=$((round + 1))
    done

    {
        echo "end_time=$(date '+%F %T')"
        echo "===== case end ====="
    } >> "${case_log}"

    echo "[DONE] ${case_id}"
}

while IFS='|' read -r case_id bin_path iters rounds cpu_mask; do
    case "${case_id}" in
        ""|\#*) continue ;;
    esac

    run_case "${case_id}" "${bin_path}" "${iters}" "${rounds}" "${cpu_mask}"
done < "${MANIFEST}"