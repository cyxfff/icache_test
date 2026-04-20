#define _GNU_SOURCE
#include <errno.h>
#include <inttypes.h>
#include <signal.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define CONFIG_HOT_L1_SIZE 0u
#define CONFIG_HOT_L1_INSNS 0u
#define CONFIG_HOT_L1_REGION_REPS 0u
#define CONFIG_HOT_L1_POS 3u
#define CONFIG_HOT_L1_ALIGN 64u
#define CONFIG_HOT_L2_SIZE 0u
#define CONFIG_HOT_L2_INSNS 0u
#define CONFIG_HOT_L2_REGION_REPS 0u
#define CONFIG_HOT_L2_POS 7u
#define CONFIG_HOT_L2_ALIGN 64u
#define CONFIG_FETCH_TOTAL_BLOCKS 128u
#define CONFIG_FETCH_BLOCK_ALIGN 64u
#define CONFIG_FETCH_DIRECT_RUN_LEN 8u
#define CONFIG_FETCH_BRANCH_PAIRS_PER_BLOCK 6u
#define CONFIG_FETCH_BLOCK_SLOTS 16u
#define CONFIG_FETCH_REGION_REPS 1000u
#define CONFIG_FETCH_POS 1u
#define CONFIG_FETCH_LAYOUT_STR "linear"
#define CONFIG_ITLB_FUNCS 0u
#define CONFIG_ITLB_LINES_PER_PAGE 1u
#define CONFIG_ITLB_REGION_REPS 0u
#define CONFIG_ITLB_FUNC_ALIGN 4096u
#define CONFIG_ITLB_DIRECT_RUN_LEN 0u
#define CONFIG_ITLB_POS 4u
#define CONFIG_ITLB_MODE_STR "chain"
#define CONFIG_CALL_RET_FUNCS 0u
#define CONFIG_CALL_RET_LINES_PER_FUNC 1u
#define CONFIG_CALL_RET_REGION_REPS 0u
#define CONFIG_CALL_RET_POS 4u
#define CONFIG_PLT_STUB_FUNCS 0u
#define CONFIG_PLT_STUB_REGION_REPS 0u
#define CONFIG_PLT_STUB_POS 5u
#define CONFIG_INDIRECT_TARGET_COUNT 0u
#define CONFIG_INDIRECT_TARGET_BLOCK_ALIGN 64u
#define CONFIG_INDIRECT_TARGET_REGION_REPS 0u
#define CONFIG_INDIRECT_TARGET_POS 6u
#define CONFIG_MAIN_TOTAL_BLOCKS 0u
#define CONFIG_MAIN_BLOCK_ALIGN 64u
#define CONFIG_MAIN_DIRECT_RUN_LEN 0u
#define CONFIG_MAIN_REGION_REPS 0u
#define CONFIG_MAIN_POS 2u
#define CONFIG_MAIN_LAYOUT_STR "in_page_shuffle"
#define CONFIG_SEED 1337u
#define CONFIG_HOT_L1_ENTRIES_PER_ITER 0u
#define CONFIG_HOT_L2_ENTRIES_PER_ITER 0u
#define CONFIG_FETCH_BLOCK_ENTRIES_PER_ITER 128000u
#define CONFIG_ITLB_CALLS_PER_ITER 0u
#define CONFIG_CALL_RET_CALLS_PER_ITER 0u
#define CONFIG_PLT_STUB_CALLS_PER_ITER 0u
#define CONFIG_INDIRECT_TARGET_CALLS_PER_ITER 0u
#define CONFIG_MAIN_BLOCK_ENTRIES_PER_ITER 0u
#define CONFIG_TOTAL_FRONTEND_UNITS_PER_ITER 128000u
#define CONFIG_FETCH_INDIRECT_BLOCKS_PER_CHAIN 15u
#define CONFIG_MAIN_INDIRECT_BLOCKS_PER_CHAIN 0u
#define CONFIG_ITLB_INDIRECT_FUNCS_PER_CHAIN 0u
#define DEFAULT_ITERS 10000ull

static const uint32_t kMainExecSamples[1] = {
    0,
};

static const uint32_t kMainPhysicalOrder[1] = {
    0,
};

static const uint32_t kMainPhysSamples[1] = {
    0,
};

static const uint32_t kFetchPhysicalOrder[128] = {
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
    12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
    24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
    36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
    48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
    60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
    72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
    84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95,
    96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107,
    108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
    120, 121, 122, 123, 124, 125, 126, 127,
};

static const uint32_t kItlbPhysicalOrder[1] = {
    0,
};

static const uint32_t kItlbExecOrder[1] = {
    0,
};

static const uint32_t kItlbSamples[1] = {
    0,
};

static const uint32_t kCallRetPhysicalOrder[1] = {
    0,
};

static const uint32_t kCallRetExecOrder[1] = {
    0,
};

static const uint32_t kCallRetSamples[1] = {
    0,
};

typedef void (*bench_func_t)(void);

static void *g_itlb_func_table[CONFIG_ITLB_FUNCS > 0 ? CONFIG_ITLB_FUNCS : 1u];
static void *g_fetch_table[CONFIG_FETCH_TOTAL_BLOCKS > 0 ? CONFIG_FETCH_TOTAL_BLOCKS : 1u];
static void *g_main_table[CONFIG_MAIN_TOTAL_BLOCKS > 0 ? CONFIG_MAIN_TOTAL_BLOCKS : 1u];
static void *g_indirect_target_table[CONFIG_INDIRECT_TARGET_COUNT > 0 ? CONFIG_INDIRECT_TARGET_COUNT : 1u];

__attribute__((used, noinline))
static void dispatch_fetch_indirect(uint64_t idx) {
    ((bench_func_t)g_fetch_table[idx])();
}

__attribute__((used, noinline))
static void dispatch_main_indirect(uint64_t idx) {
    ((bench_func_t)g_main_table[idx])();
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_0(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_1\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_1(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_2\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_2(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_3\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_3(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_4\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_4(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_5\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_5(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_6\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_6(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_7\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_7(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 2\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #8\n\t"
        "b dispatch_fetch_indirect\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_8(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_9\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_9(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_10\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_10(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_11\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_11(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_12\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_12(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_13\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_13(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_14\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_14(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_15\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_15(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 2\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #16\n\t"
        "b dispatch_fetch_indirect\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_16(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_17\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_17(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_18\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_18(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_19\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_19(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_20\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_20(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_21\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_21(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_22\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_22(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_23\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_23(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 2\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #24\n\t"
        "b dispatch_fetch_indirect\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_24(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_25\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_25(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_26\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_26(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_27\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_27(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_28\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_28(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_29\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_29(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_30\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_30(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_31\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_31(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 2\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #32\n\t"
        "b dispatch_fetch_indirect\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_32(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_33\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_33(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_34\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_34(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_35\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_35(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_36\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_36(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_37\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_37(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_38\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_38(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_39\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_39(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 2\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #40\n\t"
        "b dispatch_fetch_indirect\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_40(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_41\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_41(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_42\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_42(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_43\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_43(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_44\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_44(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_45\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_45(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_46\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_46(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_47\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_47(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 2\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #48\n\t"
        "b dispatch_fetch_indirect\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_48(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_49\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_49(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_50\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_50(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_51\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_51(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_52\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_52(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_53\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_53(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_54\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_54(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_55\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_55(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 2\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #56\n\t"
        "b dispatch_fetch_indirect\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_56(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_57\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_57(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_58\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_58(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_59\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_59(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_60\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_60(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_61\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_61(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_62\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_62(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_63\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_63(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 2\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #64\n\t"
        "b dispatch_fetch_indirect\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_64(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_65\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_65(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_66\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_66(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_67\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_67(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_68\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_68(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_69\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_69(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_70\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_70(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_71\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_71(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 2\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #72\n\t"
        "b dispatch_fetch_indirect\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_72(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_73\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_73(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_74\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_74(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_75\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_75(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_76\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_76(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_77\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_77(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_78\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_78(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_79\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_79(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 2\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #80\n\t"
        "b dispatch_fetch_indirect\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_80(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_81\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_81(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_82\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_82(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_83\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_83(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_84\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_84(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_85\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_85(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_86\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_86(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_87\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_87(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 2\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #88\n\t"
        "b dispatch_fetch_indirect\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_88(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_89\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_89(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_90\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_90(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_91\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_91(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_92\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_92(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_93\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_93(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_94\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_94(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_95\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_95(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 2\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #96\n\t"
        "b dispatch_fetch_indirect\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_96(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_97\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_97(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_98\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_98(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_99\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_99(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_100\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_100(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_101\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_101(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_102\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_102(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_103\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_103(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 2\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #104\n\t"
        "b dispatch_fetch_indirect\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_104(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_105\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_105(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_106\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_106(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_107\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_107(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_108\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_108(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_109\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_109(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_110\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_110(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_111\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_111(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 2\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #112\n\t"
        "b dispatch_fetch_indirect\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_112(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_113\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_113(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_114\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_114(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_115\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_115(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_116\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_116(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_117\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_117(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_118\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_118(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_119\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_119(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 2\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #120\n\t"
        "b dispatch_fetch_indirect\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_120(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_121\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_121(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_122\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_122(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_123\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_123(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_124\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_124(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_125\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_125(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_126\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_126(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_127\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, naked, noinline, aligned(64)))
static void fetch_block_127(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"
        "2:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 4f\n\t"
        "4:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 5f\n\t"
        "5:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 6f\n\t"
        "6:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        "ret\n\t"
        ::: "x0", "x9", "x16", "x17", "cc", "memory");
}

__attribute__((used, noinline))
static void run_fetch_amplifier_once(void) {
    ((bench_func_t)g_fetch_table[0])();
}

__attribute__((used, noinline))
static void run_itlb_region_once(void) {
}

__attribute__((used, noinline))
static void run_call_ret_chain_once(void) {
}

__attribute__((used, noinline))
static void run_plt_stub_chain_once(void) {
}

__attribute__((used, noinline))
static void run_indirect_target_set_once(void) {
}

__attribute__((used, noinline))
static void run_block_loop_once(void) {
}

static volatile sig_atomic_t g_start = 0;
static volatile sig_atomic_t g_abort = 0;

static void on_start(int signo) {
    (void)signo;
    g_start = 1;
}

static void on_abort(int signo) {
    (void)signo;
    g_abort = 1;
}

static uint64_t parse_u64(const char *text, uint64_t fallback) {
    if (!text || !*text) return fallback;
    errno = 0;
    char *end = NULL;
    unsigned long long value = strtoull(text, &end, 10);
    if (errno != 0 || !end || *end != '\0') {
        return fallback;
    }
    return (uint64_t)value;
}

static void wait_for_start_signal(void) {
    sigset_t mask;
    sigemptyset(&mask);
    while (!g_start && !g_abort) {
        sigsuspend(&mask);
    }
}

int main(int argc, char **argv) {
    struct sigaction sa_start;
    struct sigaction sa_abort;
    sa_start.sa_handler = on_start;
    sigemptyset(&sa_start.sa_mask);
    sa_start.sa_flags = 0;
    sa_abort.sa_handler = on_abort;
    sigemptyset(&sa_abort.sa_mask);
    sa_abort.sa_flags = 0;
    sigaction(SIGUSR1, &sa_start, NULL);
    sigaction(SIGTERM, &sa_abort, NULL);
    sigaction(SIGINT, &sa_abort, NULL);

    uint64_t iters = DEFAULT_ITERS;
    if (argc > 1) iters = parse_u64(argv[1], iters);
    if (iters == 0) iters = 1;

    g_itlb_func_table[0] = NULL;

    g_fetch_table[0] = (void *)&fetch_block_0;
    g_fetch_table[1] = (void *)&fetch_block_1;
    g_fetch_table[2] = (void *)&fetch_block_2;
    g_fetch_table[3] = (void *)&fetch_block_3;
    g_fetch_table[4] = (void *)&fetch_block_4;
    g_fetch_table[5] = (void *)&fetch_block_5;
    g_fetch_table[6] = (void *)&fetch_block_6;
    g_fetch_table[7] = (void *)&fetch_block_7;
    g_fetch_table[8] = (void *)&fetch_block_8;
    g_fetch_table[9] = (void *)&fetch_block_9;
    g_fetch_table[10] = (void *)&fetch_block_10;
    g_fetch_table[11] = (void *)&fetch_block_11;
    g_fetch_table[12] = (void *)&fetch_block_12;
    g_fetch_table[13] = (void *)&fetch_block_13;
    g_fetch_table[14] = (void *)&fetch_block_14;
    g_fetch_table[15] = (void *)&fetch_block_15;
    g_fetch_table[16] = (void *)&fetch_block_16;
    g_fetch_table[17] = (void *)&fetch_block_17;
    g_fetch_table[18] = (void *)&fetch_block_18;
    g_fetch_table[19] = (void *)&fetch_block_19;
    g_fetch_table[20] = (void *)&fetch_block_20;
    g_fetch_table[21] = (void *)&fetch_block_21;
    g_fetch_table[22] = (void *)&fetch_block_22;
    g_fetch_table[23] = (void *)&fetch_block_23;
    g_fetch_table[24] = (void *)&fetch_block_24;
    g_fetch_table[25] = (void *)&fetch_block_25;
    g_fetch_table[26] = (void *)&fetch_block_26;
    g_fetch_table[27] = (void *)&fetch_block_27;
    g_fetch_table[28] = (void *)&fetch_block_28;
    g_fetch_table[29] = (void *)&fetch_block_29;
    g_fetch_table[30] = (void *)&fetch_block_30;
    g_fetch_table[31] = (void *)&fetch_block_31;
    g_fetch_table[32] = (void *)&fetch_block_32;
    g_fetch_table[33] = (void *)&fetch_block_33;
    g_fetch_table[34] = (void *)&fetch_block_34;
    g_fetch_table[35] = (void *)&fetch_block_35;
    g_fetch_table[36] = (void *)&fetch_block_36;
    g_fetch_table[37] = (void *)&fetch_block_37;
    g_fetch_table[38] = (void *)&fetch_block_38;
    g_fetch_table[39] = (void *)&fetch_block_39;
    g_fetch_table[40] = (void *)&fetch_block_40;
    g_fetch_table[41] = (void *)&fetch_block_41;
    g_fetch_table[42] = (void *)&fetch_block_42;
    g_fetch_table[43] = (void *)&fetch_block_43;
    g_fetch_table[44] = (void *)&fetch_block_44;
    g_fetch_table[45] = (void *)&fetch_block_45;
    g_fetch_table[46] = (void *)&fetch_block_46;
    g_fetch_table[47] = (void *)&fetch_block_47;
    g_fetch_table[48] = (void *)&fetch_block_48;
    g_fetch_table[49] = (void *)&fetch_block_49;
    g_fetch_table[50] = (void *)&fetch_block_50;
    g_fetch_table[51] = (void *)&fetch_block_51;
    g_fetch_table[52] = (void *)&fetch_block_52;
    g_fetch_table[53] = (void *)&fetch_block_53;
    g_fetch_table[54] = (void *)&fetch_block_54;
    g_fetch_table[55] = (void *)&fetch_block_55;
    g_fetch_table[56] = (void *)&fetch_block_56;
    g_fetch_table[57] = (void *)&fetch_block_57;
    g_fetch_table[58] = (void *)&fetch_block_58;
    g_fetch_table[59] = (void *)&fetch_block_59;
    g_fetch_table[60] = (void *)&fetch_block_60;
    g_fetch_table[61] = (void *)&fetch_block_61;
    g_fetch_table[62] = (void *)&fetch_block_62;
    g_fetch_table[63] = (void *)&fetch_block_63;
    g_fetch_table[64] = (void *)&fetch_block_64;
    g_fetch_table[65] = (void *)&fetch_block_65;
    g_fetch_table[66] = (void *)&fetch_block_66;
    g_fetch_table[67] = (void *)&fetch_block_67;
    g_fetch_table[68] = (void *)&fetch_block_68;
    g_fetch_table[69] = (void *)&fetch_block_69;
    g_fetch_table[70] = (void *)&fetch_block_70;
    g_fetch_table[71] = (void *)&fetch_block_71;
    g_fetch_table[72] = (void *)&fetch_block_72;
    g_fetch_table[73] = (void *)&fetch_block_73;
    g_fetch_table[74] = (void *)&fetch_block_74;
    g_fetch_table[75] = (void *)&fetch_block_75;
    g_fetch_table[76] = (void *)&fetch_block_76;
    g_fetch_table[77] = (void *)&fetch_block_77;
    g_fetch_table[78] = (void *)&fetch_block_78;
    g_fetch_table[79] = (void *)&fetch_block_79;
    g_fetch_table[80] = (void *)&fetch_block_80;
    g_fetch_table[81] = (void *)&fetch_block_81;
    g_fetch_table[82] = (void *)&fetch_block_82;
    g_fetch_table[83] = (void *)&fetch_block_83;
    g_fetch_table[84] = (void *)&fetch_block_84;
    g_fetch_table[85] = (void *)&fetch_block_85;
    g_fetch_table[86] = (void *)&fetch_block_86;
    g_fetch_table[87] = (void *)&fetch_block_87;
    g_fetch_table[88] = (void *)&fetch_block_88;
    g_fetch_table[89] = (void *)&fetch_block_89;
    g_fetch_table[90] = (void *)&fetch_block_90;
    g_fetch_table[91] = (void *)&fetch_block_91;
    g_fetch_table[92] = (void *)&fetch_block_92;
    g_fetch_table[93] = (void *)&fetch_block_93;
    g_fetch_table[94] = (void *)&fetch_block_94;
    g_fetch_table[95] = (void *)&fetch_block_95;
    g_fetch_table[96] = (void *)&fetch_block_96;
    g_fetch_table[97] = (void *)&fetch_block_97;
    g_fetch_table[98] = (void *)&fetch_block_98;
    g_fetch_table[99] = (void *)&fetch_block_99;
    g_fetch_table[100] = (void *)&fetch_block_100;
    g_fetch_table[101] = (void *)&fetch_block_101;
    g_fetch_table[102] = (void *)&fetch_block_102;
    g_fetch_table[103] = (void *)&fetch_block_103;
    g_fetch_table[104] = (void *)&fetch_block_104;
    g_fetch_table[105] = (void *)&fetch_block_105;
    g_fetch_table[106] = (void *)&fetch_block_106;
    g_fetch_table[107] = (void *)&fetch_block_107;
    g_fetch_table[108] = (void *)&fetch_block_108;
    g_fetch_table[109] = (void *)&fetch_block_109;
    g_fetch_table[110] = (void *)&fetch_block_110;
    g_fetch_table[111] = (void *)&fetch_block_111;
    g_fetch_table[112] = (void *)&fetch_block_112;
    g_fetch_table[113] = (void *)&fetch_block_113;
    g_fetch_table[114] = (void *)&fetch_block_114;
    g_fetch_table[115] = (void *)&fetch_block_115;
    g_fetch_table[116] = (void *)&fetch_block_116;
    g_fetch_table[117] = (void *)&fetch_block_117;
    g_fetch_table[118] = (void *)&fetch_block_118;
    g_fetch_table[119] = (void *)&fetch_block_119;
    g_fetch_table[120] = (void *)&fetch_block_120;
    g_fetch_table[121] = (void *)&fetch_block_121;
    g_fetch_table[122] = (void *)&fetch_block_122;
    g_fetch_table[123] = (void *)&fetch_block_123;
    g_fetch_table[124] = (void *)&fetch_block_124;
    g_fetch_table[125] = (void *)&fetch_block_125;
    g_fetch_table[126] = (void *)&fetch_block_126;
    g_fetch_table[127] = (void *)&fetch_block_127;

    g_main_table[0] = NULL;

    g_indirect_target_table[0] = NULL;

    fflush(stdout);
    puts("PROXYBENCH_READY");
    fflush(stdout);
    wait_for_start_signal();
    struct timespec bench_start;
    struct timespec bench_end;
    clock_gettime(CLOCK_MONOTONIC, &bench_start);
    uint64_t completed_iters = 0;
    while (!g_abort && completed_iters < iters) {
        for (uint32_t rep = 0; rep < CONFIG_FETCH_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_FETCH_TOTAL_BLOCKS > 0) run_fetch_amplifier_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_MAIN_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_MAIN_TOTAL_BLOCKS > 0) run_block_loop_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_HOT_L1_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_HOT_L1_SIZE > 0) hot_l1_blob();
        }
        for (uint32_t rep = 0; rep < CONFIG_CALL_RET_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_CALL_RET_FUNCS > 0) run_call_ret_chain_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_ITLB_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_ITLB_FUNCS > 0) run_itlb_region_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_PLT_STUB_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_PLT_STUB_FUNCS > 0) run_plt_stub_chain_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_INDIRECT_TARGET_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_INDIRECT_TARGET_COUNT > 0) run_indirect_target_set_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_HOT_L2_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_HOT_L2_SIZE > 0) hot_l2_blob();
        }
        ++completed_iters;
    }

    clock_gettime(CLOCK_MONOTONIC, &bench_end);
    double bench_seconds = (double)(bench_end.tv_sec - bench_start.tv_sec) + 1e-9 * (double)(bench_end.tv_nsec - bench_start.tv_nsec);
    printf("completed_iters=%" PRIu64 "\n", completed_iters);
    printf("bench_seconds=%.9f\n", bench_seconds);
    fflush(stdout);
    return g_abort ? 130 : 0;
}
