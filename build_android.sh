#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
OUT_C="${OUT_C:-${SCRIPT_DIR}/build/icache_bench.c}"
OUT_BIN="${OUT_BIN:-${SCRIPT_DIR}/build/icache_bench}"

PRESET="${PRESET:-custom}"

case "${PRESET}" in
    custom)
        : "${COLD_BLOCK_SEQUENCE_BLOCKS:=0}"
        : "${COLD_BLOCK_SEQUENCE_BLOCK_ALIGN:=64}"
        : "${COLD_BLOCK_SEQUENCE_DIRECT_RUN_LEN:=0}"
        : "${COLD_BLOCK_SEQUENCE_REGION_REPS:=1}"
        : "${COLD_BLOCK_SEQUENCE_LAYOUT:=in_page_shuffle}"
        : "${COLD_BLOCK_SEQUENCE_POS:=3}"
        : "${FETCH_AMPLIFIER_BLOCKS:=0}"
        : "${FETCH_AMPLIFIER_BLOCK_ALIGN:=64}"
        : "${FETCH_AMPLIFIER_DIRECT_RUN_LEN:=1}"
        : "${FETCH_AMPLIFIER_BRANCH_PAIRS_PER_BLOCK:=0}"
        : "${FETCH_AMPLIFIER_REGION_REPS:=0}"
        : "${FETCH_AMPLIFIER_LAYOUT:=linear}"
        : "${FETCH_AMPLIFIER_POS:=4}"
        : "${HOT_REGION_LOOP_SIZE:=0}"
        : "${HOT_REGION_LOOP_BRANCH_PAIRS_PER_UNIT:=3}"
        : "${HOT_REGION_LOOP_REGION_REPS:=0}"
        : "${HOT_REGION_LOOP_POS:=1}"
        : "${ITLB_FUNCS:=0}"
        : "${ITLB_LINES_PER_PAGE:=1}"
        : "${ITLB_REGION_REPS:=1}"
        : "${ITLB_MODE:=chain}"
        : "${ITLB_DIRECT_RUN_LEN:=0}"
        : "${ITLB_POS:=2}"
        : "${SEED:=1337}"
        : "${OPT_LEVEL:=0}"
        ;;
    *)
        echo "unknown PRESET=${PRESET}" >&2
        echo "supported presets: custom" >&2
        exit 1
        ;;
esac

CC="${CC:-/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/native/llvm/bin/clang}"
SYSROOT="${SYSROOT:-/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/native/sysroot}"

mkdir -p "$(dirname "${OUT_C}")" "$(dirname "${OUT_BIN}")"

python3 "${SCRIPT_DIR}/pipeline.py" \
    --out "${OUT_C}" \
    --main-blocks "${COLD_BLOCK_SEQUENCE_BLOCKS}" \
    --block-align "${COLD_BLOCK_SEQUENCE_BLOCK_ALIGN}" \
    --direct-run-len "${COLD_BLOCK_SEQUENCE_DIRECT_RUN_LEN}" \
    --main-region-reps "${COLD_BLOCK_SEQUENCE_REGION_REPS}" \
    --main-layout "${COLD_BLOCK_SEQUENCE_LAYOUT}" \
    --main-pos "${COLD_BLOCK_SEQUENCE_POS}" \
    --fetch-blocks "${FETCH_AMPLIFIER_BLOCKS}" \
    --fetch-block-align "${FETCH_AMPLIFIER_BLOCK_ALIGN}" \
    --fetch-direct-run-len "${FETCH_AMPLIFIER_DIRECT_RUN_LEN}" \
    --fetch-branch-pairs-per-block "${FETCH_AMPLIFIER_BRANCH_PAIRS_PER_BLOCK}" \
    --fetch-region-reps "${FETCH_AMPLIFIER_REGION_REPS}" \
    --fetch-layout "${FETCH_AMPLIFIER_LAYOUT}" \
    --fetch-pos "${FETCH_AMPLIFIER_POS}" \
    --hot-l1-size "${HOT_REGION_LOOP_SIZE}" \
    --hot-l1-branch-pairs-per-unit "${HOT_REGION_LOOP_BRANCH_PAIRS_PER_UNIT}" \
    --hot-l1-region-reps "${HOT_REGION_LOOP_REGION_REPS}" \
    --hot-l1-pos "${HOT_REGION_LOOP_POS}" \
    --hot-l2-size "0" \
    --hot-l2-region-reps "0" \
    --hot-l2-pos "7" \
    --itlb-funcs "${ITLB_FUNCS}" \
    --itlb-lines-per-page "${ITLB_LINES_PER_PAGE}" \
    --itlb-region-reps "${ITLB_REGION_REPS}" \
    --itlb-mode "${ITLB_MODE}" \
    --itlb-direct-run-len "${ITLB_DIRECT_RUN_LEN}" \
    --itlb-pos "${ITLB_POS}" \
    --seed "${SEED}"

"${CC}" \
    -target aarch64-linux-ohos \
    --sysroot "${SYSROOT}" \
    -o "${OUT_BIN}" \
    "-O${OPT_LEVEL}" \
    -march=armv8-a+simd \
    -std=gnu11 \
    -w \
    "${OUT_C}"

echo "built ${OUT_BIN}"
echo "preset ${PRESET}"
echo "cc ${CC}"
echo "sysroot ${SYSROOT}"
