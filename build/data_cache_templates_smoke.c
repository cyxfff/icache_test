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
#define CONFIG_DATA_STREAM_SIZE 8192u
#define CONFIG_DATA_STREAM_STRIDE 64u
#define CONFIG_DATA_STREAM_REGION_REPS 1u
#define CONFIG_DATA_STREAM_POS 5u
#define CONFIG_DATA_POINTER_CHASE_PAGE_COUNT 32u
#define CONFIG_DATA_POINTER_CHASE_LINES_PER_PAGE 4u
#define CONFIG_DATA_POINTER_CHASE_NODE_COUNT 128u
#define CONFIG_DATA_POINTER_CHASE_POOL_BYTES 131072u
#define CONFIG_DATA_POINTER_CHASE_REGION_REPS 1u
#define CONFIG_DATA_POINTER_CHASE_POS 6u
#define CONFIG_DATA_PAGE_STRIDE_PAGE_COUNT 64u
#define CONFIG_DATA_PAGE_STRIDE_PAGE_STRIDE 17u
#define CONFIG_DATA_PAGE_STRIDE_LINE_INDEX 7u
#define CONFIG_DATA_PAGE_STRIDE_OFFSET_COUNT 64u
#define CONFIG_DATA_PAGE_STRIDE_POOL_BYTES 262144u
#define CONFIG_DATA_PAGE_STRIDE_REGION_REPS 1u
#define CONFIG_DATA_PAGE_STRIDE_POS 7u
#define CONFIG_DATA_INDIRECT_GATHER_PAGE_COUNT 32u
#define CONFIG_DATA_INDIRECT_GATHER_LINES_PER_PAGE 4u
#define CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT 128u
#define CONFIG_DATA_INDIRECT_GATHER_POOL_BYTES 131072u
#define CONFIG_DATA_INDIRECT_GATHER_INDEX_STRIDE 5u
#define CONFIG_DATA_INDIRECT_GATHER_REGION_REPS 1u
#define CONFIG_DATA_INDIRECT_GATHER_POS 8u
#define CONFIG_FETCH_TOTAL_BLOCKS 0u
#define CONFIG_FETCH_BLOCK_ALIGN 64u
#define CONFIG_FETCH_DIRECT_RUN_LEN 0u
#define CONFIG_FETCH_BRANCH_PAIRS_PER_BLOCK 0u
#define CONFIG_FETCH_BLOCK_SLOTS 16u
#define CONFIG_FETCH_REGION_REPS 0u
#define CONFIG_FETCH_POS 3u
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
#define CONFIG_DATA_STREAM_ACCESSES_PER_CALL 128u
#define CONFIG_DATA_STREAM_ACCESSES_PER_ITER 128u
#define CONFIG_DATA_POINTER_CHASE_NODES 128u
#define CONFIG_DATA_POINTER_CHASE_ACCESSES_PER_ITER 128u
#define CONFIG_DATA_PAGE_STRIDE_ACCESSES_PER_CALL 64u
#define CONFIG_DATA_PAGE_STRIDE_ACCESSES_PER_ITER 64u
#define CONFIG_DATA_INDIRECT_GATHER_NODES 128u
#define CONFIG_DATA_INDIRECT_GATHER_ACCESSES_PER_ITER 128u
#define CONFIG_FETCH_BLOCK_ENTRIES_PER_ITER 0u
#define CONFIG_ITLB_CALLS_PER_ITER 0u
#define CONFIG_CALL_RET_CALLS_PER_ITER 0u
#define CONFIG_PLT_STUB_CALLS_PER_ITER 0u
#define CONFIG_INDIRECT_TARGET_CALLS_PER_ITER 0u
#define CONFIG_MAIN_BLOCK_ENTRIES_PER_ITER 0u
#define CONFIG_TOTAL_FRONTEND_UNITS_PER_ITER 448u
#define CONFIG_FETCH_INDIRECT_BLOCKS_PER_CHAIN 0u
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

static const uint32_t kFetchPhysicalOrder[1] = {
    0,
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

static const uint32_t kDataPointerChaseOffsets[128] = {
    114688, 114816, 114880, 114752, 16512, 16448, 16576, 16384, 90240, 90304, 90176, 90112,
    128, 0, 64, 192, 69632, 69760, 69824, 69696, 28736, 28800, 28672, 28864,
    78016, 77824, 77888, 77952, 126976, 127168, 127104, 127040, 86080, 86016, 86144, 86208,
    106560, 106496, 106688, 106624, 57472, 57408, 57536, 57344, 94336, 94208, 94400, 94272,
    32768, 32960, 32896, 32832, 110592, 110720, 110656, 110784, 61632, 61440, 61568, 61504,
    24640, 24576, 24768, 24704, 12416, 12352, 12480, 12288, 82048, 81920, 82112, 81984,
    118784, 118976, 118848, 118912, 20544, 20672, 20608, 20480, 36864, 37056, 36992, 36928,
    45184, 45120, 45056, 45248, 65536, 65728, 65600, 65664, 49344, 49280, 49152, 49216,
    53312, 53248, 53376, 53440, 122880, 122944, 123072, 123008, 8192, 8256, 8320, 8384,
    102528, 102592, 102464, 102400, 41152, 40960, 41088, 41024, 4096, 4224, 4288, 4160,
    73792, 73856, 73728, 73920, 98432, 98304, 98496, 98368,
};

static const uint32_t kDataPageStrideOffsets[64] = {
    180672, 250304, 57792, 127424, 197056, 4544, 74176, 143808, 213440, 20928, 90560, 160192,
    229824, 37312, 106944, 176576, 246208, 53696, 123328, 192960, 448, 70080, 139712, 209344,
    16832, 86464, 156096, 225728, 33216, 102848, 172480, 242112, 49600, 119232, 188864, 258496,
    65984, 135616, 205248, 12736, 82368, 152000, 221632, 29120, 98752, 168384, 238016, 45504,
    115136, 184768, 254400, 61888, 131520, 201152, 8640, 78272, 147904, 217536, 25024, 94656,
    164288, 233920, 41408, 111040,
};

static const uint32_t kDataIndirectGatherOffsets[128] = {
    94272, 94208, 94336, 94400, 110720, 110784, 110656, 110592, 123072, 122944, 122880, 123008,
    53248, 53376, 53440, 53312, 45056, 45184, 45120, 45248, 98496, 98304, 98368, 98432,
    114688, 114816, 114880, 114752, 78016, 77952, 77888, 77824, 12416, 12288, 12480, 12352,
    24768, 24704, 24576, 24640, 86016, 86208, 86144, 86080, 57344, 57472, 57536, 57408,
    81920, 82112, 82048, 81984, 127040, 127104, 126976, 127168, 102400, 102592, 102464, 102528,
    118784, 118976, 118848, 118912, 16448, 16576, 16384, 16512, 49280, 49344, 49152, 49216,
    61504, 61568, 61632, 61440, 32832, 32768, 32960, 32896, 65600, 65728, 65664, 65536,
    106496, 106624, 106688, 106560, 4224, 4160, 4096, 4288, 0, 128, 64, 192,
    41088, 40960, 41152, 41024, 69824, 69696, 69632, 69760, 20544, 20608, 20480, 20672,
    90240, 90176, 90304, 90112, 73856, 73792, 73920, 73728, 28864, 28736, 28800, 28672,
    8256, 8320, 8384, 8192, 36928, 37056, 36992, 36864,
};

static uint8_t g_data_stream_buf[CONFIG_DATA_STREAM_SIZE > 0 ? CONFIG_DATA_STREAM_SIZE : 64u] __attribute__((aligned(64)));
static uint64_t g_data_stream_sink = 0;

static uint8_t g_data_pointer_chase_pool[CONFIG_DATA_POINTER_CHASE_POOL_BYTES > 0 ? CONFIG_DATA_POINTER_CHASE_POOL_BYTES : 64u] __attribute__((aligned(4096)));
static uint32_t g_data_pointer_chase_cursor = 0;
static uint64_t g_data_pointer_chase_sink = 0;

static uint8_t g_data_page_stride_buf[CONFIG_DATA_PAGE_STRIDE_POOL_BYTES > 0 ? CONFIG_DATA_PAGE_STRIDE_POOL_BYTES : 64u] __attribute__((aligned(4096)));
static uint64_t g_data_page_stride_sink = 0;

static uint8_t g_data_indirect_gather_pool[CONFIG_DATA_INDIRECT_GATHER_POOL_BYTES > 0 ? CONFIG_DATA_INDIRECT_GATHER_POOL_BYTES : 64u] __attribute__((aligned(4096)));
static uint32_t g_data_indirect_gather_next[CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT > 0 ? CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT : 1u];
static uint32_t g_data_indirect_gather_offsets[CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT > 0 ? CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT : 1u];
static uint32_t g_data_indirect_gather_cursor = 0;
static uint64_t g_data_indirect_gather_sink = 0;

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

__attribute__((used, noinline))
static void init_data_stream_buffer(void) {
    for (uint32_t idx = 0; idx < CONFIG_DATA_STREAM_SIZE; ++idx) {
        g_data_stream_buf[idx] = (uint8_t)(((idx * 131u) + CONFIG_SEED) & 0xFFu);
    }
}

__attribute__((used, noinline))
static void data_stream_kernel(void) {
    if (CONFIG_DATA_STREAM_SIZE == 0) return;
    uint64_t acc = g_data_stream_sink;
    for (uint32_t offset = 0; offset < CONFIG_DATA_STREAM_SIZE; offset += CONFIG_DATA_STREAM_STRIDE) {
        acc += *(const volatile uint64_t *)(g_data_stream_buf + offset);
    }
    g_data_stream_sink = acc;
}

__attribute__((used, noinline))
static void init_data_pointer_chase_pool(void) {
    if (CONFIG_DATA_POINTER_CHASE_NODE_COUNT == 0) return;
    for (uint32_t idx = 0; idx < CONFIG_DATA_POINTER_CHASE_NODE_COUNT; ++idx) {
        uint32_t cur = kDataPointerChaseOffsets[idx];
        uint32_t nxt = kDataPointerChaseOffsets[(idx + 1) % CONFIG_DATA_POINTER_CHASE_NODE_COUNT];
        *(uint32_t *)(g_data_pointer_chase_pool + cur) = nxt;
        *(uint64_t *)(g_data_pointer_chase_pool + cur + 8u) = (uint64_t)(cur ^ nxt ^ CONFIG_SEED) + (uint64_t)(idx + 1u);
    }
    g_data_pointer_chase_cursor = kDataPointerChaseOffsets[0];
}

__attribute__((used, noinline))
static void data_pointer_chase_kernel(void) {
    if (CONFIG_DATA_POINTER_CHASE_NODE_COUNT == 0) return;
    uint32_t offset = g_data_pointer_chase_cursor;
    uint64_t acc = g_data_pointer_chase_sink;
    for (uint32_t step = 0; step < CONFIG_DATA_POINTER_CHASE_NODE_COUNT; ++step) {
        offset = *(volatile uint32_t *)(g_data_pointer_chase_pool + offset);
        acc += *(volatile uint64_t *)(g_data_pointer_chase_pool + offset + 8u);
    }
    g_data_pointer_chase_cursor = offset;
    g_data_pointer_chase_sink = acc;
}

__attribute__((used, noinline))
static void init_data_page_stride_buffer(void) {
    for (uint32_t idx = 0; idx < CONFIG_DATA_PAGE_STRIDE_POOL_BYTES; ++idx) {
        g_data_page_stride_buf[idx] = (uint8_t)(((idx * 131u) + CONFIG_SEED) & 0xFFu);
    }
}

__attribute__((used, noinline))
static void data_page_stride_kernel(void) {
    if (CONFIG_DATA_PAGE_STRIDE_OFFSET_COUNT == 0) return;
    uint64_t acc = g_data_page_stride_sink;
    for (uint32_t idx = 0; idx < CONFIG_DATA_PAGE_STRIDE_OFFSET_COUNT; ++idx) {
        uint32_t offset = kDataPageStrideOffsets[idx];
        acc += *(const volatile uint64_t *)(g_data_page_stride_buf + offset);
    }
    g_data_page_stride_sink = acc;
}

__attribute__((used, noinline))
static void init_data_indirect_gather_pool(void) {
    for (uint32_t idx = 0; idx < CONFIG_DATA_INDIRECT_GATHER_POOL_BYTES; ++idx) {
        g_data_indirect_gather_pool[idx] = (uint8_t)(((idx * 29u) + CONFIG_SEED) & 0xFFu);
    }
    if (CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT == 0) return;
    for (uint32_t idx = 0; idx < CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT; ++idx) {
        uint32_t offset = kDataIndirectGatherOffsets[idx];
        g_data_indirect_gather_offsets[idx] = offset;
        g_data_indirect_gather_next[idx] = (idx + CONFIG_DATA_INDIRECT_GATHER_INDEX_STRIDE) % CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT;
        *(uint64_t *)(g_data_indirect_gather_pool + offset + 8u) = (uint64_t)(offset ^ CONFIG_SEED) + (uint64_t)(idx + 1u);
    }
    g_data_indirect_gather_cursor = 0;
}

__attribute__((used, noinline))
static void data_indirect_gather_kernel(void) {
    if (CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT == 0) return;
    uint32_t idx = g_data_indirect_gather_cursor;
    uint64_t acc = g_data_indirect_gather_sink;
    for (uint32_t step = 0; step < CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT; ++step) {
        idx = *(volatile uint32_t *)(g_data_indirect_gather_next + idx);
        uint32_t offset = *(volatile uint32_t *)(g_data_indirect_gather_offsets + idx);
        acc += *(volatile uint64_t *)(g_data_indirect_gather_pool + offset + 8u);
    }
    g_data_indirect_gather_cursor = idx;
    g_data_indirect_gather_sink = acc;
}

__attribute__((used, noinline))
static void run_hot_l1_once(void) {
}

__attribute__((used, noinline))
static void run_hot_l2_once(void) {
}

__attribute__((used, noinline))
static void run_fetch_amplifier_once(void) {
}

__attribute__((used, noinline))
static void run_data_stream_once(void) {
    data_stream_kernel();
}

__attribute__((used, noinline))
static void run_data_pointer_chase_once(void) {
    data_pointer_chase_kernel();
}

__attribute__((used, noinline))
static void run_data_page_stride_once(void) {
    data_page_stride_kernel();
}

__attribute__((used, noinline))
static void run_data_indirect_gather_once(void) {
    data_indirect_gather_kernel();
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

    g_fetch_table[0] = NULL;

    g_main_table[0] = NULL;

    g_indirect_target_table[0] = NULL;

    init_data_stream_buffer();
    init_data_pointer_chase_pool();
    init_data_page_stride_buffer();
    init_data_indirect_gather_pool();

    fflush(stdout);
    puts("PROXYBENCH_READY");
    fflush(stdout);
    wait_for_start_signal();
    struct timespec bench_start;
    struct timespec bench_end;
    clock_gettime(CLOCK_MONOTONIC, &bench_start);
    uint64_t completed_iters = 0;
    while (!g_abort && completed_iters < iters) {
        for (uint32_t rep = 0; rep < CONFIG_HOT_L1_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_HOT_L1_SIZE > 0) run_hot_l1_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_ITLB_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_ITLB_FUNCS > 0) run_itlb_region_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_CALL_RET_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_CALL_RET_FUNCS > 0) run_call_ret_chain_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_FETCH_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_FETCH_TOTAL_BLOCKS > 0) run_fetch_amplifier_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_PLT_STUB_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_PLT_STUB_FUNCS > 0) run_plt_stub_chain_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_DATA_STREAM_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_DATA_STREAM_SIZE > 0) run_data_stream_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_INDIRECT_TARGET_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_INDIRECT_TARGET_COUNT > 0) run_indirect_target_set_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_MAIN_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_MAIN_TOTAL_BLOCKS > 0) run_block_loop_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_DATA_POINTER_CHASE_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_DATA_POINTER_CHASE_PAGE_COUNT > 0) run_data_pointer_chase_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_DATA_PAGE_STRIDE_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_DATA_PAGE_STRIDE_PAGE_COUNT > 0) run_data_page_stride_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_HOT_L2_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_HOT_L2_SIZE > 0) run_hot_l2_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_DATA_INDIRECT_GATHER_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_DATA_INDIRECT_GATHER_PAGE_COUNT > 0) run_data_indirect_gather_once();
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
