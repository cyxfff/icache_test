#!/bin/sh
set -eu

# Offline multi-binary Linux/local runner.
# Directory layout:
#   run.sh
#   manifest.tsv
#   bin/<case_id>
#   logs/<case_id>.log
#   tmp/

WORKDIR="${WORKDIR:-$(CDPATH= cd -- "$(dirname "$0")" && pwd)}"
MANIFEST="${MANIFEST:-${WORKDIR}/manifest.tsv}"
LOGDIR="${LOGDIR:-${WORKDIR}/logs}"
TMPDIR="${TMPDIR:-${WORKDIR}/tmp}"

ITERS="${ITERS:-1000}"
ROUNDS="${ROUNDS:-1}"
CPU_CORE="${CPU_CORE:-0}"
SKIP_EXISTING="${SKIP_EXISTING:-1}"

DEFAULT_EVENT_GROUPS="
cpu-cycles:u,instructions:u,br_retired:u,br_mis_pred:u,l1i_cache:u,l1i_cache_refill:u,l1i_tlb:u,l1i_tlb_refill:u,l2i_cache:u,l2i_cache_refill:u,l2i_tlb:u,l2i_tlb_refill:u,l1d_cache:u,l1d_cache_refill:u,l1d_tlb:u,l1d_tlb_refill:u,l2d_cache:u,l2d_cache_refill:u,l2d_tlb:u,l2d_tlb_refill:u,ll_cache:u,ll_cache_miss:u
"
EVENT_GROUPS="${EVENT_GROUPS:-${DEFAULT_EVENT_GROUPS}}"

mkdir -p "${WORKDIR}" "${LOGDIR}" "${TMPDIR}"

if ! command -v perf >/dev/null 2>&1; then
    echo "[ERROR] perf not found"
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
    target_log="$2"

    : > "${target_log}"
    chmod +x "${bin}"

    if command -v taskset >/dev/null 2>&1; then
        (
            cd "${WORKDIR}"
            exec taskset -c "${CPU_CORE}" "${bin}" "${ITERS}" > "${target_log}" 2>&1
        ) &
    else
        echo "[WARN] taskset not found, running without CPU affinity" >> "${target_log}"
        (
            cd "${WORKDIR}"
            exec "${bin}" "${ITERS}" > "${target_log}" 2>&1
        ) &
    fi

    BPID=$!
}

wait_ready() {
    pid="$1"
    target_log="$2"
    timeout=200

    while [ "${timeout}" -gt 0 ]; do
        if ! kill -0 "${pid}" 2>/dev/null; then
            echo "[ERROR] benchmark exited before ready"
            cat "${target_log}" 2>/dev/null || true
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

run_group() {
    case_id="$1"
    bin="$2"
    case_log="$3"
    round="$4"
    group_id="$5"
    events="$6"

    target_log="${TMPDIR}/${case_id}.r${round}.g${group_id}.target.log"
    perf_log="${TMPDIR}/${case_id}.r${round}.g${group_id}.perf.log"

    {
        echo "===== perf group ====="
        echo "case_id=${case_id}"
        echo "round=${round}"
        echo "group_id=${group_id}"
        echo "events=${events}"
        echo "iters=${ITERS}"
        echo "cpu_core=${CPU_CORE}"
        echo "bin=${bin}"
    } >> "${case_log}"

    : > "${perf_log}"

    start_target "${bin}" "${target_log}"

    if ! wait_ready "${BPID}" "${target_log}" >> "${case_log}" 2>&1; then
        cat "${target_log}" >> "${case_log}" 2>/dev/null || true
        echo "===== group failed before ready =====" >> "${case_log}"
        echo >> "${case_log}"
        return 1
    fi

    pid="${BPID}"
    echo "PID is ${pid}" >> "${case_log}"

    perf stat -e "${events}" -p "${pid}" > "${perf_log}" 2>&1 &
    PERF_PID=$!

    sleep 1

    if ! kill -0 "${PERF_PID}" 2>/dev/null; then
        echo "[ERROR] perf exited before benchmark start" >> "${case_log}"
        cat "${perf_log}" >> "${case_log}" 2>/dev/null || true
        kill -TERM "${pid}" 2>/dev/null || true
        wait "${pid}" 2>/dev/null || true
        echo "===== group failed: perf exited early =====" >> "${case_log}"
        echo >> "${case_log}"
        return 1
    fi

    kill -USR1 "${pid}" 2>/dev/null || true

    wait "${PERF_PID}" || true
    cat "${perf_log}" >> "${case_log}" 2>/dev/null || true

    wait "${pid}" 2>/dev/null || true
    cat "${target_log}" >> "${case_log}" 2>/dev/null || true

    echo "===== group end =====" >> "${case_log}"
    echo >> "${case_log}"

    sleep 0.5
}

run_case() {
    case_id="$1"
    bin_path="$2"
    log_path="$3"

    bin="$(abs_path "${bin_path}")"
    case_log="$(abs_path "${log_path}")"

    if [ ! -f "${bin}" ]; then
        echo "[ERROR] missing binary for ${case_id}: ${bin}"
        return 1
    fi

    mkdir -p "$(dirname "${case_log}")"

    if [ "${SKIP_EXISTING}" = "1" ] && [ -s "${case_log}" ]; then
        echo "[SKIP] ${case_id} -> ${case_log}"
        return 0
    fi

    echo "[RUN] ${case_id}"

    {
        echo "===== case start ====="
        echo "case_id=${case_id}"
        echo "bin=${bin}"
        echo "iters=${ITERS}"
        echo "rounds=${ROUNDS}"
        echo "cpu_core=${CPU_CORE}"
        echo "start_time=$(date '+%F %T')"
        echo
    } > "${case_log}"

    round=1
    while [ "${round}" -le "${ROUNDS}" ]; do
        echo "===== round ${round}/${ROUNDS} =====" >> "${case_log}"

        group_id=0
        while IFS= read -r events; do
            [ -z "${events}" ] && continue
            group_id=$((group_id + 1))

            if ! run_group "${case_id}" "${bin}" "${case_log}" "${round}" "${group_id}" "${events}"; then
                echo "[ERROR] case=${case_id} round=${round} group=${group_id}" >> "${case_log}"
                echo >> "${case_log}"
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

while IFS="$(printf '\t')" read -r case_id bin_path log_path; do
    case "${case_id}" in
        ""|\#*) continue ;;
        "case_id") continue ;;
    esac

    if [ -z "${log_path:-}" ]; then
        log_path="logs/${case_id}.log"
    fi

    run_case "${case_id}" "${bin_path}" "${log_path}"
done < "${MANIFEST}"