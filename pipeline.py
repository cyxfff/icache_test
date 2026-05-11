#!/usr/bin/env python3

import argparse
from pathlib import Path
from typing import List, Optional

if __package__ in (None, ""):
    from modules.manager import SynthesisModuleManager
    from modules.mixed_region import MixedRegionBuilder
else:
    from .modules.manager import SynthesisModuleManager
    from .modules.mixed_region import MixedRegionBuilder


MODULES = SynthesisModuleManager()
FETCH_AMPLIFIER = MODULES.fetch_amplifier
MIXED_REGION = MixedRegionBuilder()
MAIN_LAYOUT_CHOICES = ("linear", "page_shuffle", "in_page_shuffle", "full_shuffle")
ATTACHED_DATA_SPECS = (
    {"key": "hot_l1", "label": "hot_region_loop", "prefix": "hot_l1_attached", "seed": 0x16A3B1C5},
    {"key": "fetch", "label": "fetch_amplifier", "prefix": "fetch_attached", "seed": 0x27D4EB2F},
    {"key": "itlb", "label": "itlb", "prefix": "itlb_attached", "seed": 0x38F112D9},
    {"key": "main", "label": "cold_block_sequence", "prefix": "main_attached", "seed": 0x49A77C63},
)

MEMORY_ALLOCATOR_CHOICES = ("posix", "arena")
MEMORY_ADVICE_CHOICES = ("default", "random", "sequential", "hugepage", "nohugepage")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate an Android/AArch64 I-cache microbenchmark.")
    parser.add_argument("--out", required=True, help="Output C file path")

    parser.add_argument("--main-blocks", type=int, default=0, help="Number of block-loop basic blocks")
    parser.add_argument("--block-align", type=int, default=64, help="Alignment for block-loop blocks, in bytes")
    parser.add_argument(
        "--direct-run-len",
        type=int,
        default=16,
        help="Direct-branch streak length before one block-loop indirect dispatch",
    )
    parser.add_argument(
        "--main-region-reps",
        type=int,
        default=1,
        help="Block-loop replay count per outer iteration",
    )
    parser.add_argument(
        "--main-layout",
        "--layout",
        dest="main_layout",
        choices=list(MAIN_LAYOUT_CHOICES),
        default="in_page_shuffle",
        help="Physical layout policy for the block-loop module",
    )
    parser.add_argument("--main-pos", type=int, default=6, help="Execution order position of the block-loop module")

    parser.add_argument("--fetch-blocks", type=int, default=0, help="Number of fetch-amplifier basic blocks")
    parser.add_argument("--fetch-block-align", type=int, default=64, help="Alignment for fetch-amplifier blocks, in bytes")
    parser.add_argument(
        "--fetch-direct-run-len",
        type=int,
        default=1,
        help="Direct-branch streak length before one fetch-amplifier indirect dispatch",
    )
    parser.add_argument(
        "--fetch-branch-pairs-per-block",
        type=int,
        default=0,
        help="How many always-not-taken conditional branch pairs to emit in each fetch block",
    )
    parser.add_argument(
        "--fetch-block-slots",
        type=int,
        default=16,
        help="Number of 4-byte instruction slots to emit in each fetch block",
    )
    parser.add_argument(
        "--fetch-region-reps",
        type=int,
        default=0,
        help="Fetch-amplifier replay count per outer iteration",
    )
    parser.add_argument(
        "--fetch-layout",
        choices=list(MAIN_LAYOUT_CHOICES),
        default="linear",
        help="Physical layout policy for the fetch-amplifier module",
    )
    parser.add_argument("--fetch-pos", type=int, default=3, help="Execution order position of the fetch-amplifier module")

    parser.add_argument("--hot-l1-size", type=int, default=0, help="Hot L1 loop region size in bytes")
    parser.add_argument(
        "--hot-l1-branch-pairs-per-unit",
        type=int,
        default=3,
        help="How many always-not-taken conditional branch pairs to emit in each 64B hot unit",
    )
    parser.add_argument("--hot-l1-region-reps", type=int, default=0, help="Hot L1 replay count per outer iteration")
    parser.add_argument("--hot-l1-pos", type=int, default=1, help="Execution order position of the hot L1 module")

    parser.add_argument("--itlb-funcs", type=int, default=0, help="Number of 4KB-aligned code pages in the ITLB pool")
    parser.add_argument(
        "--itlb-lines-per-page",
        type=int,
        default=1,
        help="How many 64B cache lines to execute on each ITLB page",
    )
    parser.add_argument("--itlb-region-reps", type=int, default=0, help="ITLB replay count per outer iteration")
    parser.add_argument(
        "--itlb-mode",
        choices=["chain", "for"],
        default="chain",
        help="Execute the ITLB region as a chained function sequence or via a direct call loop",
    )
    parser.add_argument(
        "--itlb-direct-run-len",
        type=int,
        default=0,
        help="Direct-branch streak length before one ITLB indirect dispatch in chain mode",
    )
    parser.add_argument("--itlb-pos", type=int, default=2, help="Execution order position of the ITLB module")

    parser.add_argument(
        "--memory-allocator",
        choices=list(MEMORY_ALLOCATOR_CHOICES),
        default="posix",
        help="How to allocate benchmark data regions: independent posix_memalign buffers or one shared mmap arena.",
    )
    parser.add_argument(
        "--memory-advice",
        choices=list(MEMORY_ADVICE_CHOICES),
        default="default",
        help="Optional madvise hint for anonymous data regions. hugepage/nohugepage probes THP influence.",
    )
    parser.add_argument(
        "--memory-arena-gap-bytes",
        type=int,
        default=0,
        help="Padding bytes to insert between data regions when --memory-allocator=arena.",
    )
    parser.add_argument(
        "--memory-arena-hint",
        type=lambda value: int(value, 0),
        default=0,
        help="Optional virtual-address hint for the shared arena mmap, e.g. 0x4000000000.",
    )
    parser.add_argument(
        "--memory-prefault",
        type=int,
        choices=[0, 1],
        default=0,
        help="Touch each allocated page once after allocation so first-touch faults do not leak into the run.",
    )
    parser.add_argument(
        "--warmup-iters",
        type=int,
        default=0,
        help="Warmup loop iterations before PROXYBENCH_READY; not counted by perf.",
    )
    parser.add_argument("--seed", type=int, default=1337, help="Shuffle seed for the benchmark")
    return parser.parse_args()


def format_u32_array(name: str, values: List[int]) -> str:
    safe_values = values if values else [0]
    chunks = []
    for start in range(0, len(safe_values), 12):
        part = ", ".join(str(v) for v in safe_values[start:start + 12])
        chunks.append(f"    {part},")
    body = "\n".join(chunks)
    return f"static const uint32_t {name}[{len(safe_values)}] = {{\n{body}\n}};\n\n"


def emit_direct_call_runner(name: str, prefix: str, count: int) -> str:
    out = [
        "__attribute__((used, noinline))\n",
        f"static void {name}(void) {{\n",
    ]
    if count > 0:
        out.append('    asm volatile("mov x9, xzr\\n\\t" "mov x10, xzr\\n\\t" ::: "x9", "x10", "cc", "memory");\n')
        for func_id in range(count):
            out.append(f"    {prefix}_{func_id}();\n")
    out.append("}\n\n")
    return "".join(out)


def emit_chain_runner(name: str, entry_symbol: Optional[str]) -> str:
    out = [
        "__attribute__((used, noinline))\n",
        f"static void {name}(void) {{\n",
    ]
    if entry_symbol is not None:
        out.append('    asm volatile("mov x9, xzr\\n\\t" "mov x10, xzr\\n\\t" ::: "x9", "x10", "cc", "memory");\n')
        out.append(f"    {entry_symbol}();\n")
    out.append("}\n\n")
    return "".join(out)


def emit_module_loop(reps_macro: str, enable_macro: str, body: str) -> str:
    return (
        f"        for (uint32_t rep = 0; rep < {reps_macro} && !g_abort; ++rep) {{\n"
        f"            if ({enable_macro}) {body}\n"
        "        }\n"
    )


def build_attached_data_slot(module_key: str, args: argparse.Namespace, seed: int, instruction_units: int, region_reps: int) -> dict:
    pool_nodes = max(
        0,
        int(
            getattr(
                args,
                f"{module_key}_data_pool_nodes",
                0,
            )
            or 0
        ),
    )
    nodes_per_page = MIXED_REGION.normalize_nodes_per_page(int(getattr(args, f"{module_key}_data_nodes_per_page", 8)))
    data_mode = MIXED_REGION.normalize_data_mode(str(getattr(args, f"{module_key}_data_mode", "linear")))
    stride_nodes = MIXED_REGION.normalize_stride(
        int(
            getattr(
                args,
                f"{module_key}_data_stride_nodes",
                getattr(args, f"{module_key}_data_stride_lines", 1),
            )
        )
    )
    stride_pages = MIXED_REGION.normalize_stride(int(getattr(args, f"{module_key}_data_stride_pages", 1)))
    ldr_per_unit = MIXED_REGION.normalize_ldr_count_per_unit(int(getattr(args, f"{module_key}_fusion_ldr_per_unit", 0)))
    pages = MIXED_REGION.normalize_pages(int(getattr(args, f"{module_key}_data_pages", 0)))
    if pool_nodes > 0:
        pages = max(pages, (pool_nodes + nodes_per_page - 1) // nodes_per_page)
    else:
        pool_nodes = pages * nodes_per_page

    slot = {
        "pool_nodes": pool_nodes,
        "pages": pages,
        "nodes_per_page": nodes_per_page,
        "data_mode": data_mode,
        "stride_nodes": stride_nodes,
        "stride_lines": stride_nodes,
        "stride_pages": stride_pages,
        "ldr_per_unit": ldr_per_unit,
        "instruction_units": max(0, int(instruction_units)),
        "region_reps": max(0, int(region_reps)),
    }

    slot["loads_per_call"] = slot["instruction_units"] * ldr_per_unit
    if pages <= 0 or slot["loads_per_call"] <= 0 or slot["region_reps"] <= 0:
        slot["offsets"] = []
        slot["node_count"] = 0
        slot["pool_bytes"] = 0
        return slot

    offsets = MIXED_REGION.build_pointer_offsets(
        pages,
        nodes_per_page,
        data_mode,
        seed,
        stride_lines=stride_nodes,
        stride_pages=stride_pages,
        nodes_per_page=nodes_per_page,
        stride_nodes=stride_nodes,
    )
    slot["offsets"] = offsets
    slot["node_count"] = len(offsets)
    slot["pool_bytes"] = pages * 4096
    return slot


def emit_attached_data_alloc_calls(attached_data_slots) -> str:
    calls = []
    for spec in ATTACHED_DATA_SPECS:
        slot = attached_data_slots[spec["key"]]
        if slot["pool_bytes"] <= 0:
            continue
        calls.append(
            emit_memory_allocation_call(
                spec["label"],
                f"g_{spec["prefix"]}_pool",
                f"CONFIG_{spec["key"].upper()}_ATTACHED_POOL_BYTES",
                4096,
            )
        )
    return "".join(calls)


def emit_memory_layout_printer(attached_data_slots) -> str:
    regions = []
    for spec in ATTACHED_DATA_SPECS:
        slot = attached_data_slots[spec["key"]]
        regions.append(
            (
                "attached-data",
                spec["label"],
                f"g_{spec["prefix"]}_pool",
                f"CONFIG_{spec["key"].upper()}_ATTACHED_POOL_BYTES",
                f"CONFIG_{spec["key"].upper()}_ATTACHED_PAGE_COUNT",
                f"CONFIG_{spec["key"].upper()}_ATTACHED_NODE_COUNT",
                f"CONFIG_{spec["key"].upper()}_ATTACHED_REPS",
            )
        )
    entries = "".join(
        (
            f'        {{"{kind}", "{name}", {base}, (uint64_t)({bytes_macro}), '
            f"(uint64_t)({pages_macro}), (uint64_t)({nodes_macro}), (uint64_t)({reps_macro})}},\n"
        )
        for kind, name, base, bytes_macro, pages_macro, nodes_macro, reps_macro in regions
    )
    code_regions = []
    for spec in ATTACHED_DATA_SPECS:
        slot = attached_data_slots[spec["key"]]
        if slot["loads_per_call"] <= 0 or slot["pool_bytes"] <= 0:
            continue
        key_upper = spec["key"].upper()
        code_regions.append(
            (
                "attached-code",
                spec["label"],
                f"{spec["prefix"]}_burst",
                f"CONFIG_{key_upper}_ATTACHED_INSTR_BYTES",
                f"CONFIG_{key_upper}_ATTACHED_LDR_PER_UNIT",
                f"CONFIG_{key_upper}_ATTACHED_REPS",
            )
        )

    code_entries = "".join(
        (
            f'        {{"{kind}", "{name}", "{entry}", (const void *)(uintptr_t)&{entry}, '
            f"(uint64_t)({bytes_macro}), "
            f"(uint64_t)(({bytes_macro}) / 64u), "
            f"(uint64_t)({ldr_macro}), (uint64_t)({reps_macro})}},\n"
        )
        for kind, name, entry, bytes_macro, ldr_macro, reps_macro in code_regions
    )
    if not code_entries:
        code_entries = '        {"code", "none", "none", NULL, 0u, 0u, 0u, 0u},\n'

    return (
        "typedef struct memory_region_info {\n"
        "    const char *kind;\n"
        "    const char *name;\n"
        "    const void *base;\n"
        "    uint64_t bytes;\n"
        "    uint64_t pages;\n"
        "    uint64_t nodes;\n"
        "    uint64_t reps;\n"
        "} memory_region_info_t;\n\n"
        "typedef struct code_region_info {\n"
        "    const char *kind;\n"
        "    const char *name;\n"
        "    const char *symbol;\n"
        "    const void *entry;\n"
        "    uint64_t payload_bytes;\n"
        "    uint64_t cache_lines;\n"
        "    uint64_t ldr_per_unit;\n"
        "    uint64_t reps;\n"
        "} code_region_info_t;\n\n"
        "static int compare_memory_region_info(const void *lhs, const void *rhs) {\n"
        "    const memory_region_info_t *left = (const memory_region_info_t *)lhs;\n"
        "    const memory_region_info_t *right = (const memory_region_info_t *)rhs;\n"
        "    uintptr_t left_addr = (uintptr_t)left->base;\n"
        "    uintptr_t right_addr = (uintptr_t)right->base;\n"
        "    return (left_addr > right_addr) - (left_addr < right_addr);\n"
        "}\n\n"
        "static int compare_code_region_info(const void *lhs, const void *rhs) {\n"
        "    const code_region_info_t *left = (const code_region_info_t *)lhs;\n"
        "    const code_region_info_t *right = (const code_region_info_t *)rhs;\n"
        "    uintptr_t left_addr = (uintptr_t)left->entry;\n"
        "    uintptr_t right_addr = (uintptr_t)right->entry;\n"
        "    return (left_addr > right_addr) - (left_addr < right_addr);\n"
        "}\n\n"
        "static void print_memory_layout(uint64_t iters) {\n"
        "    memory_region_info_t regions[] = {\n"
        f"{entries}"
        "    };\n"
        "    code_region_info_t code_regions[] = {\n"
        f"{code_entries}"
        "    };\n"
        "    const size_t region_count = sizeof(regions) / sizeof(regions[0]);\n"
        "    const size_t code_region_count = sizeof(code_regions) / sizeof(code_regions[0]);\n"
        "    qsort(regions, region_count, sizeof(regions[0]), compare_memory_region_info);\n"
        "    qsort(code_regions, code_region_count, sizeof(code_regions[0]), compare_code_region_info);\n"
        "    uint64_t total_data_bytes = 0;\n"
        "    size_t active_regions = 0;\n"
        "    uintptr_t active_start = UINTPTR_MAX;\n"
        "    uintptr_t active_end = 0u;\n"
        "    for (size_t idx = 0; idx < region_count; ++idx) {\n"
        "        if (regions[idx].bytes == 0 || regions[idx].reps == 0) continue;\n"
        "        uintptr_t start = (uintptr_t)regions[idx].base;\n"
        "        uintptr_t end = start + (uintptr_t)regions[idx].bytes;\n"
        "        if (start < active_start) active_start = start;\n"
        "        if (end > active_end) active_end = end;\n"
        "        total_data_bytes += regions[idx].bytes;\n"
        "        ++active_regions;\n"
        "    }\n"
        "    puts(\"===== memory layout =====\");\n"
        "    printf(\"iters=%\" PRIu64 \" active_data_regions=%zu total_data_bytes=%\" PRIu64 \" allocator=%s advice=%s arena_gap_bytes=%\" PRIu64 \" arena_bytes=%\" PRIu64 \" arena_hint=0x%\" PRIx64 \" prefault=%u warmup_iters=%\" PRIu64 \"\\n\",\n"
        "           iters,\n"
        "           active_regions,\n"
        "           total_data_bytes,\n"
        "           CONFIG_MEMORY_ALLOCATOR_STR,\n"
        "           CONFIG_MEMORY_ADVICE_STR,\n"
        "           (uint64_t)CONFIG_MEMORY_ARENA_GAP_BYTES,\n"
        "           (uint64_t)CONFIG_MEMORY_ARENA_BYTES,\n"
        "           (uint64_t)CONFIG_MEMORY_ARENA_HINT,\n"
        "           (unsigned)CONFIG_MEMORY_PREFAULT,\n"
        "           (uint64_t)CONFIG_WARMUP_ITERS);\n"
        "    if (strcmp(CONFIG_MEMORY_ALLOCATOR_STR, \"arena\") == 0 && active_regions > 0 && active_start != UINTPTR_MAX) {\n"
        "        printf(\"arena_span start=0x%\" PRIxPTR \" end=0x%\" PRIxPTR \" span_bytes=%\" PRIu64 \" mapped_bytes=%\" PRIu64 \"\\n\",\n"
        "               active_start,\n"
        "               active_end,\n"
        "               (uint64_t)(active_end - active_start),\n"
        "               (uint64_t)CONFIG_MEMORY_ARENA_BYTES);\n"
        "    }\n"
        "    for (size_t idx = 0; idx < region_count; ++idx) {\n"
        "        if (regions[idx].bytes == 0 || regions[idx].reps == 0) continue;\n"
        "        uintptr_t start = (uintptr_t)regions[idx].base;\n"
        "        uintptr_t end = start + (uintptr_t)regions[idx].bytes;\n"
        "        if (strcmp(CONFIG_MEMORY_ALLOCATOR_STR, \"arena\") == 0 && active_start != UINTPTR_MAX) {\n"
        "            printf(\"data_region kind=%s name=%s start=0x%\" PRIxPTR \" end=0x%\" PRIxPTR \" bytes=%\" PRIu64 \" pages=%\" PRIu64 \" nodes=%\" PRIu64 \" reps=%\" PRIu64 \" arena_off=0x%\" PRIxPTR \"\\n\",\n"
        "                   regions[idx].kind,\n"
        "                   regions[idx].name,\n"
        "                   start,\n"
        "                   end,\n"
        "                   regions[idx].bytes,\n"
        "                   regions[idx].pages,\n"
        "                   regions[idx].nodes,\n"
        "                   regions[idx].reps,\n"
        "                   (uintptr_t)(start - active_start));\n"
        "        } else {\n"
        "            printf(\"data_region kind=%s name=%s start=0x%\" PRIxPTR \" end=0x%\" PRIxPTR \" bytes=%\" PRIu64 \" pages=%\" PRIu64 \" nodes=%\" PRIu64 \" reps=%\" PRIu64 \"\\n\",\n"
        "                   regions[idx].kind,\n"
        "                   regions[idx].name,\n"
        "                   start,\n"
        "                   end,\n"
        "                   regions[idx].bytes,\n"
        "                   regions[idx].pages,\n"
        "                   regions[idx].nodes,\n"
        "                   regions[idx].reps);\n"
        "        }\n"
        "    }\n"
        "    for (size_t idx = 0; idx < code_region_count; ++idx) {\n"
        "        if (code_regions[idx].payload_bytes == 0) continue;\n"
        "        uintptr_t entry = (uintptr_t)code_regions[idx].entry;\n"
        "        uintptr_t approx_end = entry + (uintptr_t)code_regions[idx].payload_bytes;\n"
        "        printf(\"code_region kind=%s name=%s symbol=%s entry=0x%\" PRIxPTR \" approx_payload_end=0x%\" PRIxPTR \" payload_bytes=%\" PRIu64 \" cache_lines=%\" PRIu64 \" ldr_per_unit=%\" PRIu64 \" reps=%\" PRIu64 \"\\n\",\n"
        "               code_regions[idx].kind,\n"
        "               code_regions[idx].name,\n"
        "               code_regions[idx].symbol,\n"
        "               entry,\n"
        "               approx_end,\n"
        "               code_regions[idx].payload_bytes,\n"
        "               code_regions[idx].cache_lines,\n"
        "               code_regions[idx].ldr_per_unit,\n"
        "               code_regions[idx].reps);\n"
        "    }\n"
        "    fflush(stdout);\n"
        "}\n\n"
    )


def emit_memory_region_allocator() -> str:
    return (
        "static uint8_t *g_memory_arena_base = NULL;\n"
        "static uint64_t g_memory_arena_size = 0;\n"
        "static uint64_t g_memory_arena_cursor = 0;\n\n"
        "static uint64_t round_up_u64(uint64_t value, uint64_t align) {\n"
        "    if (align <= 1u) return value;\n"
        "    uint64_t rem = value % align;\n"
        "    return rem == 0u ? value : value + (align - rem);\n"
        "}\n\n"
        "static void prefault_memory_region(void *ptr, uint64_t bytes) {\n"
        "    if (!ptr || bytes == 0 || !CONFIG_MEMORY_PREFAULT) return;\n"
        "    volatile uint8_t *cursor = (volatile uint8_t *)ptr;\n"
        "    const uint64_t page_bytes = 4096u;\n"
        "    for (uint64_t off = 0; off < bytes; off += page_bytes) {\n"
        "        cursor[off] = 0;\n"
        "    }\n"
        "    cursor[bytes - 1u] = 0;\n"
        "}\n\n"
        "static void apply_memory_advice(void *ptr, uint64_t bytes, const char *name) {\n"
        "    if (!ptr || bytes == 0) return;\n"
        "#if defined(__linux__)\n"
        "    int advice = 0;\n"
        "    const uintptr_t page_bytes = 4096u;\n"
        "    uintptr_t start = ((uintptr_t)ptr) & ~(page_bytes - 1u);\n"
        "    uintptr_t end = round_up_u64((uint64_t)((uintptr_t)ptr + bytes), page_bytes);\n"
        "    size_t advise_len = (size_t)(end - start);\n"
        "    if (strcmp(CONFIG_MEMORY_ADVICE_STR, \"random\") == 0) {\n"
        "#ifdef MADV_RANDOM\n"
        "        advice = MADV_RANDOM;\n"
        "#endif\n"
        "    } else if (strcmp(CONFIG_MEMORY_ADVICE_STR, \"sequential\") == 0) {\n"
        "#ifdef MADV_SEQUENTIAL\n"
        "        advice = MADV_SEQUENTIAL;\n"
        "#endif\n"
        "    } else if (strcmp(CONFIG_MEMORY_ADVICE_STR, \"hugepage\") == 0) {\n"
        "#ifdef MADV_HUGEPAGE\n"
        "        advice = MADV_HUGEPAGE;\n"
        "#endif\n"
        "    } else if (strcmp(CONFIG_MEMORY_ADVICE_STR, \"nohugepage\") == 0) {\n"
        "#ifdef MADV_NOHUGEPAGE\n"
        "        advice = MADV_NOHUGEPAGE;\n"
        "#endif\n"
        "    }\n"
        "    if (advice != 0) {\n"
        "        int rc = madvise((void *)start, advise_len, advice);\n"
        "        if (rc != 0) {\n"
        "            fprintf(stderr, \"[WARN] madvise failed for %s advice=%s start=0x%\" PRIxPTR \" len=%zu errno=%d\\n\", name, CONFIG_MEMORY_ADVICE_STR, start, advise_len, errno);\n"
        "        }\n"
        "    }\n"
        "#else\n"
        "    (void)name;\n"
        "#endif\n"
        "}\n\n"
        "static bool ensure_memory_arena(void) {\n"
        "    if (strcmp(CONFIG_MEMORY_ALLOCATOR_STR, \"arena\") != 0) return true;\n"
        "    if (g_memory_arena_base != NULL) return true;\n"
        "#if defined(__linux__)\n"
        "    if (CONFIG_MEMORY_ARENA_BYTES == 0u) return true;\n"
        "    void *hint = CONFIG_MEMORY_ARENA_HINT == 0u ? NULL : (void *)(uintptr_t)CONFIG_MEMORY_ARENA_HINT;\n"
        "    void *base = mmap(hint, (size_t)CONFIG_MEMORY_ARENA_BYTES, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);\n"
        "    if (base == MAP_FAILED) {\n"
        "        fprintf(stderr, \"[ERROR] mmap arena failed bytes=%\" PRIu64 \" hint=0x%\" PRIx64 \" errno=%d\\n\", (uint64_t)CONFIG_MEMORY_ARENA_BYTES, (uint64_t)CONFIG_MEMORY_ARENA_HINT, errno);\n"
        "        return false;\n"
        "    }\n"
        "    g_memory_arena_base = (uint8_t *)base;\n"
        "    g_memory_arena_size = (uint64_t)CONFIG_MEMORY_ARENA_BYTES;\n"
        "    g_memory_arena_cursor = 0u;\n"
        "    return true;\n"
        "#else\n"
        "    fprintf(stderr, \"[WARN] arena allocator requested but mmap arena is only implemented on linux; falling back to posix allocator\\n\");\n"
        "    return true;\n"
        "#endif\n"
        "}\n\n"
        "static bool allocate_memory_region(void **ptr, uint64_t bytes, size_t alignment, const char *name) {\n"
        "    if (bytes == 0) return true;\n"
        "    if (bytes > (uint64_t)((size_t)-1)) {\n"
        "        fprintf(stderr, \"[ERROR] %s bytes=%\" PRIu64 \" exceeds size_t max\\n\", name, bytes);\n"
        "        return false;\n"
        "    }\n"
        "    *ptr = NULL;\n"
        "    if (strcmp(CONFIG_MEMORY_ALLOCATOR_STR, \"arena\") == 0) {\n"
        "        if (!ensure_memory_arena()) return false;\n"
        "#if defined(__linux__)\n"
        "        if (g_memory_arena_base != NULL) {\n"
        "            uint64_t offset = round_up_u64(g_memory_arena_cursor, (uint64_t)alignment);\n"
        "            if (offset + bytes > g_memory_arena_size) {\n"
        "                fprintf(stderr, \"[ERROR] arena overflow for %s need=%\" PRIu64 \" offset=%\" PRIu64 \" arena=%\" PRIu64 \"\\n\", name, bytes, offset, g_memory_arena_size);\n"
        "                return false;\n"
        "            }\n"
        "            *ptr = (void *)(g_memory_arena_base + offset);\n"
        "            g_memory_arena_cursor = offset + bytes + (uint64_t)CONFIG_MEMORY_ARENA_GAP_BYTES;\n"
        "            apply_memory_advice(*ptr, bytes, name);\n"
        "            prefault_memory_region(*ptr, bytes);\n"
        "            return true;\n"
        "        }\n"
        "#endif\n"
        "    }\n"
        "    int rc = posix_memalign(ptr, alignment, (size_t)bytes);\n"
        "    if (rc != 0 || *ptr == NULL) {\n"
        "        fprintf(stderr, \"[ERROR] failed to allocate %s bytes=%\" PRIu64 \" align=%zu rc=%d\\n\", name, bytes, alignment, rc);\n"
        "        return false;\n"
        "    }\n"
        "    apply_memory_advice(*ptr, bytes, name);\n"
        "    prefault_memory_region(*ptr, bytes);\n"
        "    return true;\n"
        "}\n\n"
    )


def emit_memory_allocation_call(name: str, symbol: str, bytes_macro: str, align: int) -> str:
    return (
        f"    if (!allocate_memory_region((void **)&{symbol}, (uint64_t)({bytes_macro}), "
        f"{align}u, \"{name}\")) return 2;\n"
    )


def emit_memory_allocation_calls(attached_data_slots) -> str:
    calls = []
    calls.append(emit_attached_data_alloc_calls(attached_data_slots))
    return "".join(calls)


def generate(args: argparse.Namespace) -> str:
    main_total_blocks = max(0, args.main_blocks)
    main_region_reps = 0 if main_total_blocks == 0 else max(1, args.main_region_reps)
    main_layout = args.main_layout
    main_pos = args.main_pos
    hot_l1_size = max(0, args.hot_l1_size)
    hot_l1_branch_pairs_per_unit = max(0, int(args.hot_l1_branch_pairs_per_unit))
    hot_l1_region_reps = 0 if hot_l1_size == 0 else max(1, args.hot_l1_region_reps)
    hot_l1_pos = args.hot_l1_pos

    fetch_total_blocks = max(0, args.fetch_blocks)

    memory_allocator = str(args.memory_allocator)
    if memory_allocator not in MEMORY_ALLOCATOR_CHOICES:
        raise ValueError(f"unsupported memory allocator: {memory_allocator}")
    memory_advice = str(args.memory_advice)
    if memory_advice not in MEMORY_ADVICE_CHOICES:
        raise ValueError(f"unsupported memory advice: {memory_advice}")
    memory_arena_gap_bytes = max(0, int(args.memory_arena_gap_bytes))
    memory_arena_hint = max(0, int(args.memory_arena_hint))
    memory_prefault = 1 if int(args.memory_prefault) else 0
    warmup_iters = max(0, int(args.warmup_iters))

    fetch_region_reps = 0 if fetch_total_blocks == 0 else max(1, args.fetch_region_reps)
    fetch_branch_pairs_per_block = max(0, int(args.fetch_branch_pairs_per_block))
    fetch_block_slots = max(1, int(args.fetch_block_slots))
    fetch_layout = args.fetch_layout
    fetch_pos = args.fetch_pos

    itlb_funcs = max(0, args.itlb_funcs)
    itlb_lines_per_page = MODULES.tlb_region.normalize_lines_per_page(args.itlb_lines_per_page)
    itlb_region_reps = 0 if itlb_funcs == 0 else max(1, args.itlb_region_reps)
    itlb_mode = args.itlb_mode
    itlb_pos = args.itlb_pos

    attached_data_slots = {
        "hot_l1": build_attached_data_slot("hot_l1", args, args.seed ^ 0x16A3B1C5, hot_l1_size / 64, hot_l1_region_reps),
        "fetch": build_attached_data_slot("fetch", args, args.seed ^ 0x27D4EB2F, fetch_total_blocks, fetch_region_reps),
        "itlb": build_attached_data_slot("itlb", args, args.seed ^ 0x38F112D9, itlb_funcs * itlb_lines_per_page, itlb_region_reps),
        "main": build_attached_data_slot("main", args, args.seed ^ 0x49A77C63, main_total_blocks, main_region_reps),
    }
    attached_data_enabled = any(
        slot["pool_bytes"] > 0 and slot["loads_per_call"] > 0
        for slot in attached_data_slots.values()
    )

    if (
        main_total_blocks == 0
        and fetch_total_blocks == 0
        and hot_l1_size == 0
        and itlb_funcs == 0
    ):
        raise ValueError("At least one module must be non-zero")

    main_block_align = max(64, args.block_align)
    fetch_block_align = max(64, args.fetch_block_align)
    hot_l1_align = 64
    hot_l2_size = 0
    hot_l2_align = 64

    if main_layout in ("page_shuffle", "in_page_shuffle") and (4096 % main_block_align != 0):
        raise ValueError(
            f"layout={main_layout} requires block_align to divide 4096 exactly, got {main_block_align}"
        )
    if fetch_layout in ("page_shuffle", "in_page_shuffle") and (4096 % fetch_block_align != 0):
        raise ValueError(
            f"layout={fetch_layout} requires fetch_block_align to divide 4096 exactly, got {fetch_block_align}"
        )

    main_direct_run_len = MODULES.block_loop.normalize_direct_run_len(main_total_blocks, args.direct_run_len)
    fetch_direct_run_len = FETCH_AMPLIFIER.normalize_direct_run_len(fetch_total_blocks, args.fetch_direct_run_len)
    itlb_direct_run_len = MODULES.tlb_region.normalize_direct_run_len(itlb_funcs, args.itlb_direct_run_len)

    main_physical_order = MODULES.block_loop.shuffled_block_order(
        main_total_blocks,
        main_block_align,
        args.seed,
        main_layout,
    )
    fetch_physical_order = FETCH_AMPLIFIER.shuffled_block_order(
        fetch_total_blocks,
        fetch_block_align,
        args.seed ^ 0x517CC1B7,
        fetch_layout,
    )
    itlb_phys_order = MODULES.tlb_region.shuffled_itlb_phys_order(itlb_funcs, args.seed ^ 0x9E3779B1)
    itlb_exec_order = MODULES.tlb_region.constrained_itlb_exec_order(itlb_phys_order, args.seed ^ 0x85EBCA77, 4)
    itlb_next_map, itlb_chain_pos_map = MODULES.tlb_region.build_chain_maps(itlb_funcs, itlb_exec_order, itlb_mode)

    arena_regions = [
        *[(slot["pool_bytes"], 4096) for slot in attached_data_slots.values()],
    ]
    memory_arena_bytes = 0
    for bytes_value, align_value in arena_regions:
        if bytes_value <= 0:
            continue
        memory_arena_bytes += int(bytes_value) + int(align_value) + memory_arena_gap_bytes
    if memory_arena_bytes > 0:
        memory_arena_bytes += 4096

    hot_l1_insns = hot_l1_size // 4 if hot_l1_size > 0 else 0

    main_exec_samples = list(range(min(main_total_blocks, 8)))
    main_phys_samples = main_physical_order[: min(main_total_blocks, 8)]
    itlb_samples = itlb_exec_order[: min(itlb_funcs, 8)] if itlb_exec_order else []

    main_indirect_blocks_per_chain = MODULES.block_loop.count_indirect_blocks(main_total_blocks, main_direct_run_len)
    fetch_indirect_blocks_per_chain = FETCH_AMPLIFIER.count_indirect_blocks(fetch_total_blocks, fetch_direct_run_len)
    itlb_indirect_funcs_per_chain = MODULES.tlb_region.count_indirect_functions(
        itlb_funcs,
        itlb_mode,
        itlb_direct_run_len,
    )

    hot_l1_entries_per_iter = hot_l1_region_reps
    itlb_calls_per_iter = itlb_region_reps if itlb_mode == "chain" else itlb_funcs * itlb_region_reps
    main_block_entries_per_iter = main_total_blocks * main_region_reps
    fetch_block_entries_per_iter = fetch_total_blocks * fetch_region_reps
    attached_data_accesses_per_iter = sum(
        slot["loads_per_call"] * slot["region_reps"]
        for slot in attached_data_slots.values()
        if slot["pool_bytes"] > 0
    )

    total_frontend_units_per_iter = (
        hot_l1_entries_per_iter
        + attached_data_accesses_per_iter
        + fetch_block_entries_per_iter
        + itlb_calls_per_iter
        + main_block_entries_per_iter
    )

    ordered_module_loops = [
        (hot_l1_pos, "hot_l1", "CONFIG_HOT_L1_REGION_REPS", "CONFIG_HOT_L1_SIZE > 0", "run_hot_l1_once();"),
        (
            fetch_pos,
            "fetch_amplifier",
            "CONFIG_FETCH_REGION_REPS",
            "CONFIG_FETCH_TOTAL_BLOCKS > 0",
            "run_fetch_amplifier_once();",
        ),
        (itlb_pos, "itlb", "CONFIG_ITLB_REGION_REPS", "CONFIG_ITLB_FUNCS > 0", "run_itlb_region_once();"),
        (
            main_pos,
            "block_loop",
            "CONFIG_MAIN_REGION_REPS",
            "CONFIG_MAIN_TOTAL_BLOCKS > 0",
            "run_block_loop_once();",
        ),
    ]
    active_loop_names = set()
    if hot_l1_size > 0 and hot_l1_region_reps > 0:
        active_loop_names.add("hot_l1")
    if fetch_total_blocks > 0 and fetch_region_reps > 0:
        active_loop_names.add("fetch_amplifier")
    if itlb_funcs > 0 and itlb_region_reps > 0:
        active_loop_names.add("itlb")
    if main_total_blocks > 0 and main_region_reps > 0:
        active_loop_names.add("block_loop")

    ordered_module_loops = [
        item
        for item in ordered_module_loops
        if item[1] in active_loop_names
    ]

    ordered_module_loops.sort(key=lambda item: (item[0], item[1]))

    out = []
    out.append("#define _GNU_SOURCE\n")
    out.append("#include <errno.h>\n")
    out.append("#include <inttypes.h>\n")
    out.append("#include <signal.h>\n")
    out.append("#include <stdbool.h>\n")
    out.append("#include <stdint.h>\n")
    out.append("#include <stdio.h>\n")
    out.append("#include <stdlib.h>\n")
    out.append("#include <string.h>\n")
    out.append("#include <time.h>\n")
    out.append("#include <unistd.h>\n\n")
    out.append("#if defined(__linux__)\n")
    out.append("#include <sys/mman.h>\n")
    out.append("#endif\n\n")

    out.append(f"#define CONFIG_HOT_L1_SIZE {hot_l1_size}u\n")
    out.append(f"#define CONFIG_HOT_L1_INSNS {hot_l1_insns}u\n")
    out.append(f"#define CONFIG_HOT_L1_REGION_REPS {hot_l1_region_reps}u\n")
    out.append(f"#define CONFIG_HOT_L1_POS {hot_l1_pos}u\n")
    out.append(f"#define CONFIG_HOT_L1_ALIGN {hot_l1_align}u\n")

    for spec in ATTACHED_DATA_SPECS:
        slot = attached_data_slots[spec["key"]]
        key_upper = spec["key"].upper()
        out.append(f"#define CONFIG_{key_upper}_ATTACHED_PAGE_COUNT {slot['pages']}u\n")
        out.append(f"#define CONFIG_{key_upper}_ATTACHED_NODES_PER_PAGE {slot['nodes_per_page']}u\n")
        out.append(f"#define CONFIG_{key_upper}_ATTACHED_NODE_COUNT {slot['node_count']}u\n")
        out.append(f"#define CONFIG_{key_upper}_ATTACHED_STRIDE_LINES {slot['stride_lines']}u\n")
        out.append(f"#define CONFIG_{key_upper}_ATTACHED_STRIDE_PAGES {slot['stride_pages']}u\n")
        out.append(f"#define CONFIG_{key_upper}_ATTACHED_LDR_PER_UNIT {slot['ldr_per_unit']}u\n")
        out.append(f"#define CONFIG_{key_upper}_ATTACHED_INSTR_UNITS {slot['instruction_units']}u\n")
        out.append(f"#define CONFIG_{key_upper}_ATTACHED_INSTR_BYTES {slot['instruction_units'] * 64}u\n")
        out.append(f"#define CONFIG_{key_upper}_ATTACHED_POOL_BYTES {slot['pool_bytes']}u\n")
        out.append(f"#define CONFIG_{key_upper}_ATTACHED_REPS {slot['region_reps']}u\n")
        out.append(f'#define CONFIG_{key_upper}_ATTACHED_DATA_MODE_STR "{slot["data_mode"]}"\n')

    out.append(f"#define CONFIG_FETCH_TOTAL_BLOCKS {fetch_total_blocks}u\n")
    out.append(f"#define CONFIG_FETCH_BLOCK_ALIGN {fetch_block_align}u\n")
    out.append(f"#define CONFIG_FETCH_DIRECT_RUN_LEN {fetch_direct_run_len}u\n")
    out.append(f"#define CONFIG_FETCH_BRANCH_PAIRS_PER_BLOCK {fetch_branch_pairs_per_block}u\n")
    out.append(f"#define CONFIG_FETCH_BLOCK_SLOTS {fetch_block_slots}u\n")
    out.append(f"#define CONFIG_FETCH_REGION_REPS {fetch_region_reps}u\n")
    out.append(f"#define CONFIG_FETCH_POS {fetch_pos}u\n")
    out.append(f'#define CONFIG_FETCH_LAYOUT_STR "{fetch_layout}"\n')

    out.append(f"#define CONFIG_ITLB_FUNCS {itlb_funcs}u\n")
    out.append(f"#define CONFIG_ITLB_LINES_PER_PAGE {itlb_lines_per_page}u\n")
    out.append(f"#define CONFIG_ITLB_REGION_REPS {itlb_region_reps}u\n")
    out.append("#define CONFIG_ITLB_FUNC_ALIGN 4096u\n")
    out.append(f"#define CONFIG_ITLB_DIRECT_RUN_LEN {itlb_direct_run_len}u\n")
    out.append(f"#define CONFIG_ITLB_POS {itlb_pos}u\n")
    out.append(f'#define CONFIG_ITLB_MODE_STR "{itlb_mode}"\n')

    out.append(f"#define CONFIG_MAIN_TOTAL_BLOCKS {main_total_blocks}u\n")
    out.append(f"#define CONFIG_MAIN_BLOCK_ALIGN {main_block_align}u\n")
    out.append(f"#define CONFIG_MAIN_DIRECT_RUN_LEN {main_direct_run_len}u\n")
    out.append(f"#define CONFIG_MAIN_REGION_REPS {main_region_reps}u\n")
    out.append(f"#define CONFIG_MAIN_POS {main_pos}u\n")
    out.append(f'#define CONFIG_MAIN_LAYOUT_STR "{main_layout}"\n')
    out.append(f'#define CONFIG_MEMORY_ALLOCATOR_STR "{memory_allocator}"\n')
    out.append(f'#define CONFIG_MEMORY_ADVICE_STR "{memory_advice}"\n')
    out.append(f"#define CONFIG_MEMORY_ARENA_GAP_BYTES {memory_arena_gap_bytes}ull\n")
    out.append(f"#define CONFIG_MEMORY_ARENA_HINT 0x{memory_arena_hint:x}ull\n")
    out.append(f"#define CONFIG_MEMORY_ARENA_BYTES {memory_arena_bytes}ull\n")
    out.append(f"#define CONFIG_MEMORY_PREFAULT {memory_prefault}u\n")
    out.append(f"#define CONFIG_WARMUP_ITERS {warmup_iters}ull\n")
    out.append(f"#define CONFIG_SEED {args.seed}u\n")

    out.append(f"#define CONFIG_HOT_L1_ENTRIES_PER_ITER {hot_l1_entries_per_iter}u\n")
    out.append(f"#define CONFIG_FETCH_BLOCK_ENTRIES_PER_ITER {fetch_block_entries_per_iter}u\n")
    out.append(f"#define CONFIG_ITLB_CALLS_PER_ITER {itlb_calls_per_iter}u\n")
    out.append(f"#define CONFIG_MAIN_BLOCK_ENTRIES_PER_ITER {main_block_entries_per_iter}u\n")
    out.append(f"#define CONFIG_TOTAL_FRONTEND_UNITS_PER_ITER {total_frontend_units_per_iter}u\n")
    out.append(f"#define CONFIG_FETCH_INDIRECT_BLOCKS_PER_CHAIN {fetch_indirect_blocks_per_chain}u\n")
    out.append(f"#define CONFIG_MAIN_INDIRECT_BLOCKS_PER_CHAIN {main_indirect_blocks_per_chain}u\n")
    out.append(f"#define CONFIG_ITLB_INDIRECT_FUNCS_PER_CHAIN {itlb_indirect_funcs_per_chain}u\n")
    out.append("#define DEFAULT_ITERS 10000ull\n\n")

    out.append(format_u32_array("kMainExecSamples", main_exec_samples))
    out.append(format_u32_array("kMainPhysicalOrder", main_physical_order))
    out.append(format_u32_array("kMainPhysSamples", main_phys_samples))
    out.append(format_u32_array("kFetchPhysicalOrder", fetch_physical_order))
    out.append(format_u32_array("kItlbPhysicalOrder", itlb_phys_order))
    out.append(format_u32_array("kItlbExecOrder", itlb_exec_order))
    out.append(format_u32_array("kItlbSamples", itlb_samples))
    for spec in ATTACHED_DATA_SPECS:
        slot = attached_data_slots[spec["key"]]
        symbol = "k" + "".join(part.capitalize() for part in spec["prefix"].split("_")) + "Offsets"
        out.append(format_u32_array(symbol, slot["offsets"]))

    for spec in ATTACHED_DATA_SPECS:
        out.append(MIXED_REGION.emit_storage(spec["prefix"], f"CONFIG_{spec['key'].upper()}_ATTACHED_POOL_BYTES"))

    out.append("typedef void (*bench_func_t)(void);\n\n")
    out.append("static void *g_itlb_func_table[CONFIG_ITLB_FUNCS > 0 ? CONFIG_ITLB_FUNCS : 1u];\n")
    out.append("static void *g_fetch_table[CONFIG_FETCH_TOTAL_BLOCKS > 0 ? CONFIG_FETCH_TOTAL_BLOCKS : 1u];\n")
    out.append("static void *g_main_table[CONFIG_MAIN_TOTAL_BLOCKS > 0 ? CONFIG_MAIN_TOTAL_BLOCKS : 1u];\n")
    out.append(emit_memory_region_allocator())

    out.append(
        '__attribute__((used, noinline))\n'
        'static void dispatch_fetch_indirect(uint64_t idx) {\n'
        '    ((bench_func_t)g_fetch_table[idx])();\n'
        '}\n\n'
    )

    out.append(
        '__attribute__((used, noinline))\n'
        'static void dispatch_main_indirect(uint64_t idx) {\n'
        '    ((bench_func_t)g_main_table[idx])();\n'
        '}\n\n'
    )

    if itlb_mode == "chain" and itlb_direct_run_len > 0:
        out.append(
            '__attribute__((used, noinline))\n'
            'static void dispatch_itlb_indirect(uint64_t idx) {\n'
            '    ((bench_func_t)g_itlb_func_table[idx])();\n'
            '}\n\n'
        )

    out.append(
        MODULES.hot_region.emit_region_function(
            "hot_l1_blob",
            hot_l1_size,
            hot_l1_align,
            hot_l1_branch_pairs_per_unit,
        )
    )
    out.append(MODULES.hot_region.emit_region_function("hot_l2_blob", hot_l2_size, hot_l2_align))
    for spec in ATTACHED_DATA_SPECS:
        key_upper = spec["key"].upper()
        symbol = "k" + "".join(part.capitalize() for part in spec["prefix"].split("_")) + "Offsets"
        out.append(
            MIXED_REGION.emit_init_function(
                spec["prefix"],
                symbol,
                f"CONFIG_{key_upper}_ATTACHED_NODE_COUNT",
            )
        )
    for spec in ATTACHED_DATA_SPECS:
        slot = attached_data_slots[spec["key"]]
        out.append(MIXED_REGION.emit_pointer_burst_function(spec["prefix"], slot["loads_per_call"]))

    for logical_id in fetch_physical_order:
        out.append(
            FETCH_AMPLIFIER.emit_segment_function(
                "fetch",
                logical_id,
                fetch_total_blocks,
                fetch_block_align,
                "dispatch_fetch_indirect",
                fetch_direct_run_len,
                fetch_branch_pairs_per_block,
                fetch_block_slots,
            )
        )

    itlb_dispatcher = "dispatch_itlb_indirect" if itlb_mode == "chain" and itlb_direct_run_len > 0 else None
    for func_id in itlb_phys_order:
        out.append(
            MODULES.tlb_region.emit_function(
                "itlb",
                func_id,
                itlb_next_map[func_id],
                itlb_lines_per_page,
                itlb_mode,
                itlb_dispatcher,
                itlb_direct_run_len,
                itlb_chain_pos_map.get(func_id),
            )
        )

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_hot_l1_once(void) {\n")
    if hot_l1_size > 0:
        if attached_data_slots["hot_l1"]["pool_bytes"] > 0 and attached_data_slots["hot_l1"]["loads_per_call"] > 0:
            out.append("    hot_l1_attached_burst();\n")
        out.append("    hot_l1_blob();\n")
    out.append("}\n\n")

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_hot_l2_once(void) {\n")
    if hot_l2_size > 0:
        out.append("    hot_l2_blob();\n")
    out.append("}\n\n")

    out.append(emit_memory_layout_printer(attached_data_slots))

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_fetch_amplifier_once(void) {\n")
    if fetch_total_blocks > 0:
        if attached_data_slots["fetch"]["pool_bytes"] > 0 and attached_data_slots["fetch"]["loads_per_call"] > 0:
            out.append("    fetch_attached_burst();\n")
        out.append("    ((bench_func_t)g_fetch_table[0])();\n")
    out.append("}\n\n")

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_itlb_region_once(void) {\n")
    if itlb_funcs > 0:
        if attached_data_slots["itlb"]["pool_bytes"] > 0 and attached_data_slots["itlb"]["loads_per_call"] > 0:
            out.append("    itlb_attached_burst();\n")
        out.append("    asm volatile(\"mov x9, xzr\\n\\t\" \"mov x10, xzr\\n\\t\" ::: \"x9\", \"x10\", \"cc\", \"memory\");\n")
        if itlb_mode == "chain":
            if itlb_exec_order:
                out.append(f"    itlb_func_{itlb_exec_order[0]}();\n")
        else:
            for func_id in range(itlb_funcs):
                out.append(f"    itlb_func_{func_id}();\n")
    out.append("}\n\n")

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_block_loop_once(void) {\n")
    if main_total_blocks > 0:
        if attached_data_slots["main"]["pool_bytes"] > 0 and attached_data_slots["main"]["loads_per_call"] > 0:
            out.append("    main_attached_burst();\n")
        out.append("    ((bench_func_t)g_main_table[0])();\n")
    out.append("}\n\n")

    for logical_id in main_physical_order:
        out.append(
            MODULES.block_loop.emit_segment_function(
                "main",
                logical_id,
                main_total_blocks,
                main_block_align,
                "dispatch_main_indirect",
                main_direct_run_len,
            )
        )

    out.append("static volatile sig_atomic_t g_start = 0;\n")
    out.append("static volatile sig_atomic_t g_abort = 0;\n\n")

    out.append(
        "static void on_start(int signo) {\n"
        "    (void)signo;\n"
        "    g_start = 1;\n"
        "}\n\n"
    )
    out.append(
        "static void on_abort(int signo) {\n"
        "    (void)signo;\n"
        "    g_abort = 1;\n"
        "}\n\n"
    )
    out.append(
        "static uint64_t parse_u64(const char *text, uint64_t fallback) {\n"
        "    if (!text || !*text) return fallback;\n"
        "    errno = 0;\n"
        "    char *end = NULL;\n"
        "    unsigned long long value = strtoull(text, &end, 10);\n"
        "    if (errno != 0 || !end || *end != '\\0') {\n"
        "        return fallback;\n"
        "    }\n"
        "    return (uint64_t)value;\n"
        "}\n\n"
    )
    out.append(
        "static void wait_for_start_signal(void) {\n"
        "    sigset_t mask;\n"
        "    sigemptyset(&mask);\n"
        "    while (!g_start && !g_abort) {\n"
        "        sigsuspend(&mask);\n"
        "    }\n"
        "}\n\n"
    )

    out.append("int main(int argc, char **argv) {\n")
    out.append("    struct sigaction sa_start;\n")
    out.append("    struct sigaction sa_abort;\n")
    out.append("    sa_start.sa_handler = on_start;\n")
    out.append("    sigemptyset(&sa_start.sa_mask);\n")
    out.append("    sa_start.sa_flags = 0;\n")
    out.append("    sa_abort.sa_handler = on_abort;\n")
    out.append("    sigemptyset(&sa_abort.sa_mask);\n")
    out.append("    sa_abort.sa_flags = 0;\n")
    out.append("    sigaction(SIGUSR1, &sa_start, NULL);\n")
    out.append("    sigaction(SIGTERM, &sa_abort, NULL);\n")
    out.append("    sigaction(SIGINT, &sa_abort, NULL);\n\n")

    out.append("    uint64_t iters = DEFAULT_ITERS;\n")
    out.append("    if (argc > 1) iters = parse_u64(argv[1], iters);\n")
    out.append("    if (iters == 0) iters = 1;\n\n")

    for func_id in range(itlb_funcs):
        out.append(f"    g_itlb_func_table[{func_id}] = (void *)&itlb_func_{func_id};\n")
    if itlb_funcs == 0:
        out.append("    g_itlb_func_table[0] = NULL;\n")
    out.append("\n")

    for logical_id in range(fetch_total_blocks):
        out.append(f"    g_fetch_table[{logical_id}] = (void *)&fetch_block_{logical_id};\n")
    if fetch_total_blocks == 0:
        out.append("    g_fetch_table[0] = NULL;\n")
    out.append("\n")

    for logical_id in range(main_total_blocks):
        out.append(f"    g_main_table[{logical_id}] = (void *)&main_block_{logical_id};\n")
    if main_total_blocks == 0:
        out.append("    g_main_table[0] = NULL;\n")
    out.append("\n")

    out.append(emit_memory_allocation_calls(attached_data_slots))
    out.append("\n")
    out.append("    print_memory_layout(iters);\n\n")

    for spec in ATTACHED_DATA_SPECS:
        slot = attached_data_slots[spec["key"]]
        if slot["pool_bytes"] > 0 and slot["loads_per_call"] > 0:
            out.append(f"    init_{spec['prefix']}_pool();\n")
    out.append("\n")

    out.append("    if (CONFIG_WARMUP_ITERS > 0u) {\n")
    out.append("        uint64_t warmup_done = 0;\n")
    out.append("        while (!g_abort && warmup_done < CONFIG_WARMUP_ITERS) {\n")
    for _, _, reps_macro, enable_macro, body in ordered_module_loops:
        out.append(emit_module_loop(reps_macro, enable_macro, body))
    out.append("            ++warmup_done;\n")
    out.append("        }\n")
    out.append("    }\n\n")

    out.append("    fflush(stdout);\n")
    out.append('    puts("PROXYBENCH_READY");\n')
    out.append("    fflush(stdout);\n")
    out.append("    wait_for_start_signal();\n")
    out.append("    struct timespec bench_start;\n")
    out.append("    struct timespec bench_end;\n")
    out.append("    clock_gettime(CLOCK_MONOTONIC, &bench_start);\n")
    out.append("    uint64_t completed_iters = 0;\n")
    out.append("    while (!g_abort && completed_iters < iters) {\n")
    for _, _, reps_macro, enable_macro, body in ordered_module_loops:
        out.append(emit_module_loop(reps_macro, enable_macro, body))

    out.append("        ++completed_iters;\n")
    out.append("    }\n\n")
    out.append("    clock_gettime(CLOCK_MONOTONIC, &bench_end);\n")
    out.append(
        "    double bench_seconds = (double)(bench_end.tv_sec - bench_start.tv_sec) + "
        "1e-9 * (double)(bench_end.tv_nsec - bench_start.tv_nsec);\n"
    )
    out.append('    printf("completed_iters=%" PRIu64 "\\n", completed_iters);\n')
    out.append('    printf("bench_seconds=%.9f\\n", bench_seconds);\n')
    out.append("    fflush(stdout);\n")
    out.append("    return g_abort ? 130 : 0;\n")
    out.append("}\n")

    return "".join(out)


def namespace_from_flat_cfg(out_path, flat_cfg) -> argparse.Namespace:
    cfg = dict(flat_cfg)

    def _mixed_slot_extra(slot_id):
        # canonical names first, fall back to legacy names
        return {
            "size": int(cfg.get(f"mixed_region_loop_{slot_id}_instr_size_bytes", cfg.get(f"mixed_region_loop_{slot_id}_size", 0))),
            "ldr_count_per_unit": int(cfg.get(f"mixed_region_loop_{slot_id}_fusion_ldr_per_unit", cfg.get(f"mixed_region_loop_{slot_id}_ldr_count_per_unit", 0))),
            "data_mode": str(cfg.get(f"mixed_region_loop_{slot_id}_data_mode", "linear")),
            "pool_nodes": int(cfg.get(f"mixed_region_loop_{slot_id}_data_pool_nodes", cfg.get(f"mixed_region_loop_{slot_id}_pool_nodes", 0))),
            "pages": int(cfg.get(f"mixed_region_loop_{slot_id}_data_pages", cfg.get(f"mixed_region_loop_{slot_id}_pages", 1))),
            "lines_per_page": int(cfg.get(f"mixed_region_loop_{slot_id}_data_nodes_per_page", cfg.get(f"mixed_region_loop_{slot_id}_nodes_per_page", cfg.get(f"mixed_region_loop_{slot_id}_lines_per_page", 8)))),
            "nodes_per_page": int(cfg.get(f"mixed_region_loop_{slot_id}_data_nodes_per_page", cfg.get(f"mixed_region_loop_{slot_id}_nodes_per_page", cfg.get(f"mixed_region_loop_{slot_id}_lines_per_page", 8)))),
            "stride_nodes": int(cfg.get(f"mixed_region_loop_{slot_id}_data_stride_nodes", cfg.get(f"mixed_region_loop_{slot_id}_stride_nodes", cfg.get(f"mixed_region_loop_{slot_id}_data_stride_lines", cfg.get(f"mixed_region_loop_{slot_id}_stride_lines", 1))))),
            "stride_lines": int(cfg.get(f"mixed_region_loop_{slot_id}_data_stride_lines", cfg.get(f"mixed_region_loop_{slot_id}_stride_lines", 1))),
            "stride_pages": int(cfg.get(f"mixed_region_loop_{slot_id}_data_stride_pages", cfg.get(f"mixed_region_loop_{slot_id}_stride_pages", 1))),
            "region_reps": int(cfg.get(f"mixed_region_loop_{slot_id}_region_reps", 0)),
            "pos": int(cfg.get(f"mixed_region_loop_{slot_id}_pos", 2 + slot_id)),
        }

    mixed_region_extra_slots = [_mixed_slot_extra(slot_id) for slot_id in range(1, 7)]
    return argparse.Namespace(
        out=str(out_path),
        main_blocks=int(cfg["cold_block_sequence_blocks"]),
        block_align=int(cfg["cold_block_sequence_block_align"]),
        direct_run_len=int(cfg["cold_block_sequence_direct_run_len"]),
        main_region_reps=int(cfg["cold_block_sequence_region_reps"]),
        main_layout=str(cfg["cold_block_sequence_layout"]),
        main_pos=int(cfg["cold_block_sequence_pos"]),
        main_data_pool_nodes=int(cfg.get("cold_block_sequence_data_pool_nodes", 0)),
        main_data_pages=int(cfg.get("cold_block_sequence_data_pages", 0)),
        main_data_nodes_per_page=int(cfg.get("cold_block_sequence_data_nodes_per_page", 8)),
        main_data_mode=str(cfg.get("cold_block_sequence_data_mode", "linear")),
        main_data_stride_nodes=int(cfg.get("cold_block_sequence_data_stride_nodes", cfg.get("cold_block_sequence_data_stride_lines", 1))),
        main_data_stride_lines=int(cfg.get("cold_block_sequence_data_stride_lines", 1)),
        main_data_stride_pages=int(cfg.get("cold_block_sequence_data_stride_pages", 1)),
        main_fusion_ldr_per_unit=int(cfg.get("cold_block_sequence_fusion_ldr_per_unit", 0)),
        fetch_blocks=int(cfg["fetch_amplifier_blocks"]),
        fetch_block_align=int(cfg["fetch_amplifier_block_align"]),
        fetch_direct_run_len=int(cfg["fetch_amplifier_direct_run_len"]),
        fetch_branch_pairs_per_block=int(cfg["fetch_amplifier_branch_pairs_per_block"]),
        fetch_block_slots=int(cfg.get("fetch_amplifier_block_slots", 16)),
        fetch_region_reps=int(cfg["fetch_amplifier_region_reps"]),
        fetch_layout=str(cfg["fetch_amplifier_layout"]),
        fetch_pos=int(cfg["fetch_amplifier_pos"]),
        fetch_data_pool_nodes=int(cfg.get("fetch_amplifier_data_pool_nodes", 0)),
        fetch_data_pages=int(cfg.get("fetch_amplifier_data_pages", 0)),
        fetch_data_nodes_per_page=int(cfg.get("fetch_amplifier_data_nodes_per_page", 8)),
        fetch_data_mode=str(cfg.get("fetch_amplifier_data_mode", "linear")),
        fetch_data_stride_nodes=int(cfg.get("fetch_amplifier_data_stride_nodes", cfg.get("fetch_amplifier_data_stride_lines", 1))),
        fetch_data_stride_lines=int(cfg.get("fetch_amplifier_data_stride_lines", 1)),
        fetch_data_stride_pages=int(cfg.get("fetch_amplifier_data_stride_pages", 1)),
        fetch_fusion_ldr_per_unit=int(cfg.get("fetch_amplifier_fusion_ldr_per_unit", 0)),
        hot_l1_size=int(cfg["hot_region_loop_size"]),
        hot_l1_branch_pairs_per_unit=int(cfg["hot_region_loop_branch_pairs_per_unit"]),
        hot_l1_region_reps=int(cfg["hot_region_loop_region_reps"]),
        hot_l1_pos=int(cfg["hot_region_loop_pos"]),
        hot_l1_data_pool_nodes=int(cfg.get("hot_region_loop_data_pool_nodes", 0)),
        hot_l1_data_pages=int(cfg.get("hot_region_loop_data_pages", 0)),
        hot_l1_data_nodes_per_page=int(cfg.get("hot_region_loop_data_nodes_per_page", 8)),
        hot_l1_data_mode=str(cfg.get("hot_region_loop_data_mode", "linear")),
        hot_l1_data_stride_nodes=int(cfg.get("hot_region_loop_data_stride_nodes", cfg.get("hot_region_loop_data_stride_lines", 1))),
        hot_l1_data_stride_lines=int(cfg.get("hot_region_loop_data_stride_lines", 1)),
        hot_l1_data_stride_pages=int(cfg.get("hot_region_loop_data_stride_pages", 1)),
        hot_l1_fusion_ldr_per_unit=int(cfg.get("hot_region_loop_fusion_ldr_per_unit", 0)),
        hot_l2_size=0,
        hot_l2_region_reps=0,
        hot_l2_pos=max(int(cfg["hot_region_loop_pos"]) + 1, 7),
        mixed_region_size=int(cfg.get("mixed_region_loop_instr_size_bytes", cfg.get("mixed_region_loop_size", 0))),
        mixed_region_ldr_count_per_unit=int(cfg.get("mixed_region_loop_fusion_ldr_per_unit", cfg.get("mixed_region_loop_ldr_count_per_unit", 0))),
        mixed_region_data_mode=str(cfg.get("mixed_region_loop_data_mode", "linear")),
        mixed_region_pool_nodes=int(cfg.get("mixed_region_loop_data_pool_nodes", cfg.get("mixed_region_loop_pool_nodes", 0))),
        mixed_region_pages=int(cfg.get("mixed_region_loop_data_pages", cfg.get("mixed_region_loop_pages", 1))),
        mixed_region_lines_per_page=int(cfg.get("mixed_region_loop_data_nodes_per_page", cfg.get("mixed_region_loop_lines_per_page", 8))),
        mixed_region_nodes_per_page=int(
            cfg.get("mixed_region_loop_data_nodes_per_page", cfg.get("mixed_region_loop_nodes_per_page", cfg.get("mixed_region_loop_lines_per_page", 8)))
        ),
        mixed_region_stride_nodes=int(cfg.get("mixed_region_loop_data_stride_nodes", cfg.get("mixed_region_loop_stride_nodes", cfg.get("mixed_region_loop_data_stride_lines", cfg.get("mixed_region_loop_stride_lines", 1))))),
        mixed_region_stride_lines=int(cfg.get("mixed_region_loop_data_stride_lines", cfg.get("mixed_region_loop_stride_lines", 1))),
        mixed_region_stride_pages=int(cfg.get("mixed_region_loop_data_stride_pages", cfg.get("mixed_region_loop_stride_pages", 1))),
        mixed_region_region_reps=int(cfg.get("mixed_region_loop_region_reps", 0)),
        mixed_region_pos=int(cfg.get("mixed_region_loop_pos", 2)),
        mixed_region_extra_slots=mixed_region_extra_slots,
        data_stream_size=int(cfg.get("data_stream_size", 0)),
        data_stream_stride=int(cfg.get("data_stream_stride", 64)),
        data_stream_region_reps=int(cfg.get("data_stream_region_reps", 0)),
        data_stream_pos=int(cfg.get("data_stream_pos", 5)),
        data_pointer_chase_pages=int(cfg.get("data_pointer_chase_pages", 0)),
        data_pointer_chase_lines_per_page=int(cfg.get("data_pointer_chase_lines_per_page", 1)),
        data_pointer_chase_region_reps=int(cfg.get("data_pointer_chase_region_reps", 0)),
        data_pointer_chase_pos=int(cfg.get("data_pointer_chase_pos", 6)),
        data_page_stride_pages=int(cfg.get("data_page_stride_pages", 0)),
        data_page_stride_page_stride=int(cfg.get("data_page_stride_page_stride", 1)),
        data_page_stride_line_index=int(cfg.get("data_page_stride_line_index", 0)),
        data_page_stride_region_reps=int(cfg.get("data_page_stride_region_reps", 0)),
        data_page_stride_pos=int(cfg.get("data_page_stride_pos", 7)),
        data_indirect_gather_pages=int(cfg.get("data_indirect_gather_pages", 0)),
        data_indirect_gather_lines_per_page=int(cfg.get("data_indirect_gather_lines_per_page", 1)),
        data_indirect_gather_index_stride=int(cfg.get("data_indirect_gather_index_stride", 1)),
        data_indirect_gather_region_reps=int(cfg.get("data_indirect_gather_region_reps", 0)),
        data_indirect_gather_pos=int(cfg.get("data_indirect_gather_pos", 8)),
        data_hot_stride_access_count=int(cfg.get("data_hot_stride_access_count", 0)),
        data_hot_stride_stride=int(cfg.get("data_hot_stride_stride", 4)),
        data_hot_stride_region_reps=int(cfg.get("data_hot_stride_region_reps", 0)),
        data_hot_stride_pos=int(cfg.get("data_hot_stride_pos", 9)),
        data_cold_stride_access_count=int(cfg.get("data_cold_stride_access_count", 0)),
        data_cold_stride_stride=int(cfg.get("data_cold_stride_stride", 256)),
        data_cold_stride_region_reps=int(cfg.get("data_cold_stride_region_reps", 0)),
        data_cold_stride_pos=int(cfg.get("data_cold_stride_pos", 10)),
        data_tlb_indirect_pages=int(cfg.get("data_tlb_indirect_pages", 0)),
        data_tlb_indirect_line_index=int(cfg.get("data_tlb_indirect_line_index", 0)),
        data_tlb_indirect_region_reps=int(cfg.get("data_tlb_indirect_region_reps", 0)),
        data_tlb_indirect_pos=int(cfg.get("data_tlb_indirect_pos", 11)),
        itlb_funcs=int(cfg["itlb_funcs"]),
        itlb_lines_per_page=int(cfg["itlb_lines_per_page"]),
        itlb_region_reps=int(cfg["itlb_region_reps"]),
        itlb_mode=str(cfg["itlb_mode"]),
        itlb_direct_run_len=int(cfg["itlb_direct_run_len"]),
        itlb_pos=int(cfg["itlb_pos"]),
        itlb_data_pool_nodes=int(cfg.get("itlb_data_pool_nodes", 0)),
        itlb_data_pages=int(cfg.get("itlb_data_pages", 0)),
        itlb_data_nodes_per_page=int(cfg.get("itlb_data_nodes_per_page", 8)),
        itlb_data_mode=str(cfg.get("itlb_data_mode", "linear")),
        itlb_data_stride_nodes=int(cfg.get("itlb_data_stride_nodes", cfg.get("itlb_data_stride_lines", 1))),
        itlb_data_stride_lines=int(cfg.get("itlb_data_stride_lines", 1)),
        itlb_data_stride_pages=int(cfg.get("itlb_data_stride_pages", 1)),
        itlb_fusion_ldr_per_unit=int(cfg.get("itlb_fusion_ldr_per_unit", 0)),
        call_ret_funcs=int(cfg.get("call_ret_funcs", 0)),
        call_ret_lines_per_func=int(cfg.get("call_ret_lines_per_func", 1)),
        call_ret_region_reps=int(cfg.get("call_ret_region_reps", 0)),
        call_ret_pos=int(cfg.get("call_ret_pos", 4)),
        plt_stub_funcs=int(cfg.get("plt_stub_funcs", 0)),
        plt_stub_region_reps=int(cfg.get("plt_stub_region_reps", 0)),
        plt_stub_pos=int(cfg.get("plt_stub_pos", 5)),
        indirect_target_count=int(cfg.get("indirect_target_count", 0)),
        indirect_target_block_align=int(cfg.get("indirect_target_block_align", 64)),
        indirect_target_region_reps=int(cfg.get("indirect_target_region_reps", 0)),
        indirect_target_pos=int(cfg.get("indirect_target_pos", 6)),
        memory_allocator=str(cfg.get("memory_allocator", "posix")),
        memory_advice=str(cfg.get("memory_advice", "default")),
        memory_arena_gap_bytes=int(cfg.get("memory_arena_gap_bytes", 0)),
        memory_arena_hint=int(cfg.get("memory_arena_hint", 0)),
        memory_prefault=int(cfg.get("memory_prefault", 0)),
        warmup_iters=int(cfg.get("warmup_iters", 0)),
        seed=int(cfg["seed"]),
    )


def write_source(out_path, source: str) -> None:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="ascii") as handle:
        handle.write(source)


def generate_from_flat_cfg(out_path, flat_cfg) -> str:
    args = namespace_from_flat_cfg(out_path, flat_cfg)
    source = generate(args)
    write_source(out_path, source)
    return source


def main() -> None:
    args = parse_args()
    source = generate(args)
    write_source(args.out, source)


if __name__ == "__main__":
    main()
