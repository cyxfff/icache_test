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
#define CONFIG_HOT_L1_POS 1u
#define CONFIG_HOT_L1_ALIGN 64u
#define CONFIG_HOT_L2_SIZE 0u
#define CONFIG_HOT_L2_INSNS 0u
#define CONFIG_HOT_L2_REGION_REPS 0u
#define CONFIG_HOT_L2_POS 7u
#define CONFIG_HOT_L2_ALIGN 64u
#define CONFIG_FETCH_TOTAL_BLOCKS 32u
#define CONFIG_FETCH_BLOCK_ALIGN 64u
#define CONFIG_FETCH_DIRECT_RUN_LEN 2u
#define CONFIG_FETCH_BRANCH_PAIRS_PER_BLOCK 4u
#define CONFIG_FETCH_REGION_REPS 1u
#define CONFIG_FETCH_POS 1u
#define CONFIG_FETCH_LAYOUT_STR "linear"
#define CONFIG_ITLB_FUNCS 0u
#define CONFIG_ITLB_LINES_PER_PAGE 1u
#define CONFIG_ITLB_REGION_REPS 0u
#define CONFIG_ITLB_FUNC_ALIGN 4096u
#define CONFIG_ITLB_DIRECT_RUN_LEN 0u
#define CONFIG_ITLB_POS 2u
#define CONFIG_ITLB_MODE_STR "chain"
#define CONFIG_CALL_RET_FUNCS 0u
#define CONFIG_CALL_RET_LINES_PER_FUNC 1u
#define CONFIG_CALL_RET_REGION_REPS 0u
#define CONFIG_CALL_RET_POS 3u
#define CONFIG_PLT_STUB_FUNCS 0u
#define CONFIG_PLT_STUB_REGION_REPS 0u
#define CONFIG_PLT_STUB_POS 4u
#define CONFIG_INDIRECT_TARGET_COUNT 0u
#define CONFIG_INDIRECT_TARGET_BLOCK_ALIGN 64u
#define CONFIG_INDIRECT_TARGET_REGION_REPS 0u
#define CONFIG_INDIRECT_TARGET_POS 5u
#define CONFIG_MAIN_TOTAL_BLOCKS 0u
#define CONFIG_MAIN_BLOCK_ALIGN 64u
#define CONFIG_MAIN_DIRECT_RUN_LEN 0u
#define CONFIG_MAIN_REGION_REPS 0u
#define CONFIG_MAIN_POS 6u
#define CONFIG_MAIN_LAYOUT_STR "in_page_shuffle"
#define CONFIG_SEED 1337u
#define CONFIG_HOT_L1_ENTRIES_PER_ITER 0u
#define CONFIG_HOT_L2_ENTRIES_PER_ITER 0u
#define CONFIG_FETCH_BLOCK_ENTRIES_PER_ITER 32u
#define CONFIG_ITLB_CALLS_PER_ITER 0u
#define CONFIG_CALL_RET_CALLS_PER_ITER 0u
#define CONFIG_PLT_STUB_CALLS_PER_ITER 0u
#define CONFIG_INDIRECT_TARGET_CALLS_PER_ITER 0u
#define CONFIG_MAIN_BLOCK_ENTRIES_PER_ITER 0u
#define CONFIG_TOTAL_FRONTEND_UNITS_PER_ITER 32u
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

static const uint32_t kFetchPhysicalOrder[32] = {
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
    12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
    24, 25, 26, 27, 28, 29, 30, 31,
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
        ".rept 7\n\t"
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
        ".rept 6\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #2\n\t"
        "b dispatch_fetch_indirect\n\t"
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
        ".rept 7\n\t"
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
        ".rept 6\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #4\n\t"
        "b dispatch_fetch_indirect\n\t"
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
        ".rept 7\n\t"
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
        ".rept 6\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #6\n\t"
        "b dispatch_fetch_indirect\n\t"
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
        ".rept 7\n\t"
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
        ".rept 6\n\t"
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
        ".rept 7\n\t"
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
        ".rept 6\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #10\n\t"
        "b dispatch_fetch_indirect\n\t"
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
        ".rept 7\n\t"
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
        ".rept 6\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #12\n\t"
        "b dispatch_fetch_indirect\n\t"
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
        ".rept 7\n\t"
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
        ".rept 6\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #14\n\t"
        "b dispatch_fetch_indirect\n\t"
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
        ".rept 7\n\t"
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
        ".rept 6\n\t"
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
        ".rept 7\n\t"
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
        ".rept 6\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #18\n\t"
        "b dispatch_fetch_indirect\n\t"
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
        ".rept 7\n\t"
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
        ".rept 6\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #20\n\t"
        "b dispatch_fetch_indirect\n\t"
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
        ".rept 7\n\t"
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
        ".rept 6\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #22\n\t"
        "b dispatch_fetch_indirect\n\t"
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
        ".rept 7\n\t"
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
        ".rept 6\n\t"
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
        ".rept 7\n\t"
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
        ".rept 6\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #26\n\t"
        "b dispatch_fetch_indirect\n\t"
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
        ".rept 7\n\t"
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
        ".rept 6\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #28\n\t"
        "b dispatch_fetch_indirect\n\t"
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
        ".rept 7\n\t"
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
        ".rept 6\n\t"
        "nop\n\t"
        ".endr\n\t"
        "movz x0, #30\n\t"
        "b dispatch_fetch_indirect\n\t"
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
        ".rept 7\n\t"
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
        ".rept 7\n\t"
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
        for (uint32_t rep = 0; rep < CONFIG_HOT_L1_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_HOT_L1_SIZE > 0) hot_l1_blob();
        }
        for (uint32_t rep = 0; rep < CONFIG_ITLB_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_ITLB_FUNCS > 0) run_itlb_region_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_CALL_RET_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_CALL_RET_FUNCS > 0) run_call_ret_chain_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_PLT_STUB_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_PLT_STUB_FUNCS > 0) run_plt_stub_chain_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_INDIRECT_TARGET_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_INDIRECT_TARGET_COUNT > 0) run_indirect_target_set_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_MAIN_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_MAIN_TOTAL_BLOCKS > 0) run_block_loop_once();
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
