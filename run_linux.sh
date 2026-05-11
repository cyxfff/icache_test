#!/bin/sh
set -eu

# Linux/local runner.
# This script is intended to execute the benchmark binary on the current machine
# and collect counters with perf.

BIN="${BIN:-./icache_bench}"
ITERS="${ITERS:-${1:-1000}}"
ROUNDS="${ROUNDS:-1}"
CPU_CORE="${CPU_CORE:-0}"
WORKDIR="${WORKDIR:-$(CDPATH= cd -- "$(dirname "$BIN")" && pwd)}"

LOGFILE="${WORKDIR}/icache_test_run.log"
PERFLOG="${WORKDIR}/icache_test_perf.log"

DEFAULT_EVENT_GROUPS="
cpu-cycles:u,instructions:u,br_retired:u,br_mis_pred:u,l1i_cache:u,l1i_cache_refill:u,l1i_tlb:u,l1i_tlb_refill:u,l2i_cache:u,l2i_cache_refill:u,l2i_tlb:u,l2i_tlb_refill:u
cpu-cycles:u,instructions:u,l1d_cache:u,l1d_cache_refill:u,l1d_tlb:u,l1d_tlb_refill:u,l2d_cache:u,l2d_cache_refill:u,l2d_tlb:u,l2d_tlb_refill:u,ll_cache:u,ll_cache_miss:u
"
EVENT_GROUPS="${EVENT_GROUPS:-${DEFAULT_EVENT_GROUPS}}"

mkdir -p "${WORKDIR}"

chmod +x "${BIN}"

start_target() {
    : > "${LOGFILE}"

    if command -v taskset >/dev/null 2>&1; then
        (
            cd "${WORKDIR}"
            exec taskset -c "${CPU_CORE}" "${BIN}" "${ITERS}" > "${LOGFILE}" 2>&1
        ) &
    else
        echo "[WARN] taskset not found, running without CPU affinity"
        (
            cd "${WORKDIR}"
            exec "${BIN}" "${ITERS}" > "${LOGFILE}" 2>&1
        ) &
    fi

    BPID=$!
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

run_once() {
    events="$1"
    [ -z "${events}" ] && return 0

    : > "${PERFLOG}"
    start_target || return 1
    pid="${BPID}"
    wait_ready "${pid}"

    echo "===== perf group ====="
    # echo "events=${events}"
    echo "iters=${ITERS}"
    echo "cpu_core=${CPU_CORE}"

    perf stat -e "${events}" -p "${pid}" > "${PERFLOG}" 2>&1 &
    PERF_PID=$!

    sleep 1
    if ! kill -0 "${PERF_PID}" 2>/dev/null; then
        echo "[ERROR] perf exited before benchmark start"
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
    sleep 0.5
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
