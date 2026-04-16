#!/bin/sh
set -eu

WORKDIR="${WORKDIR:-/data/local/tmp/synthesis_hiperf}"
BIN="${BIN:-${WORKDIR}/icache_bench}"
ITERS="${ITERS:-${1:-1000}}"
ROUNDS="${ROUNDS:-1}"
CPU_MASK="${CPU_MASK:-}"

LOGFILE="${WORKDIR}/synthesis_hiperf_run.log"
PERFLOG="${WORKDIR}/synthesis_hiperf_perf.log"

EVENT_GROUPS="
raw-cpu-cycles:u,raw-instruction-retired:u,raw-br-mis-pred:u,raw-br-retired:u
raw-instruction-retired:u,raw-l1-icache:u,raw-l1-icache-refill:u,raw-l2-icache:u,raw-l2-icache-refill:u
raw-instruction-retired:u,raw-l1-itlb:u,raw-l1-itlb-refill:u,raw-l2-itlb:u,raw-l2-itlb-refill:u
"

mkdir -p "${WORKDIR}"

if ! command -v hiperf >/dev/null 2>&1; then
    echo "[ERROR] hiperf not found"
    exit 1
fi

chmod +x "${BIN}"

start_target() {
    : > "${LOGFILE}"

    if [ -n "${CPU_MASK}" ] && command -v taskset >/dev/null 2>&1; then
        (
            cd "${WORKDIR}"
            exec taskset "${CPU_MASK}" "${BIN}" "${ITERS}" > "${LOGFILE}" 2>&1
        ) &
    else
        if [ -n "${CPU_MASK}" ]; then
            echo "[WARN] taskset not found, running without CPU affinity"
        fi
        (
            cd "${WORKDIR}"
            exec "${BIN}" "${ITERS}" > "${LOGFILE}" 2>&1
        ) &
    fi

    LAUNCH_PID=$!
}

wait_ready() {
    pid="$1"
    timeout=200
    while [ "${timeout}" -gt 0 ]; do
        if ! kill -0 "${pid}" 2>/dev/null; then
            echo "[ERROR] benchmark exited before ready"
            cat "${LOGFILE}"
            return 1
        fi
        if grep -q "PROXYBENCH_READY" "${LOGFILE}" 2>/dev/null; then
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

    : > "${PERFLOG}"

    OLD_IFS="$IFS"
    IFS=','
    set -- stat
    for ev in ${events}; do
        set -- "$@" -e "$ev"
    done
    IFS="$OLD_IFS"

    set -- "$@" -p "${pid}"
    hiperf "$@" > "${PERFLOG}" 2>&1 &
    PERF_PID=$!
}

run_once() {
    events="$1"
    [ -z "${events}" ] && return 0

    start_target || return 1
    wait_ready "${LAUNCH_PID}"

    BIN_NAME=$(basename "${BIN}")
    pid="$(pidof "${BIN_NAME}" 2>/dev/null || true)"
    pid="${pid%% *}"
    if [ -z "${pid}" ]; then
        echo "[ERROR] failed to locate ${BIN_NAME} pid"
        cat "${LOGFILE}"
        return 1
    fi

    echo "===== perf group ====="
    echo "events=${events}"
    echo "iters=${ITERS}"
    echo "cpu_mask=${CPU_MASK:-<none>}"
    echo "PID is ${pid}"

    start_hiperf "${events}" "${pid}"

    sleep 0.2
    if ! kill -0 "${PERF_PID}" 2>/dev/null; then
        echo "[ERROR] hiperf exited immediately"
        cat "${PERFLOG}"
        kill -TERM "${pid}" 2>/dev/null || true
        wait "${pid}" 2>/dev/null || true
        return 1
    fi

    kill -USR1 "${pid}"

    wait "${PERF_PID}" || true
    cat "${PERFLOG}"

    wait "${pid}" 2>/dev/null || true
    cat "${LOGFILE}"
    sleep 0.2
    echo
}

round=1
while [ "${round}" -le "${ROUNDS}" ]; do
    echo "===== round ${round}/${ROUNDS} ====="
    while IFS= read -r events; do
        [ -z "${events}" ] && continue
        run_once "${events}"
    done <<EOF
${EVENT_GROUPS}
EOF
    round=$((round + 1))
done
