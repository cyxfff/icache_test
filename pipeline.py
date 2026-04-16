#!/usr/bin/env python3

import argparse
from pathlib import Path
from typing import List, Optional

if __package__ in (None, ""):
    from modules.manager import SynthesisModuleManager
else:
    from .modules.manager import SynthesisModuleManager


MODULES = SynthesisModuleManager()
FETCH_AMPLIFIER = getattr(MODULES, "fetch_amplifier", MODULES.cold_block_sequence)
MAIN_LAYOUT_CHOICES = ("linear", "page_shuffle", "in_page_shuffle", "full_shuffle")


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
    parser.add_argument("--hot-l2-size", type=int, default=0, help="Hot L2 loop region size in bytes")
    parser.add_argument("--hot-l2-region-reps", type=int, default=0, help="Hot L2 replay count per outer iteration")
    parser.add_argument("--hot-l2-pos", type=int, default=7, help="Execution order position of the hot L2 module")

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

    parser.add_argument("--call-ret-funcs", type=int, default=0, help="Number of call/ret functions")
    parser.add_argument(
        "--call-ret-lines-per-func",
        type=int,
        default=1,
        help="How many 64B lines to execute in each call/ret function",
    )
    parser.add_argument(
        "--call-ret-region-reps",
        type=int,
        default=0,
        help="Call/ret replay count per outer iteration",
    )
    parser.add_argument("--call-ret-pos", type=int, default=3, help="Execution order position of the call/ret module")

    parser.add_argument("--plt-stub-funcs", type=int, default=0, help="Number of PLT-style caller/stub/callee triplets")
    parser.add_argument(
        "--plt-stub-region-reps",
        type=int,
        default=0,
        help="PLT-style replay count per outer iteration",
    )
    parser.add_argument("--plt-stub-pos", type=int, default=4, help="Execution order position of the PLT-style module")

    parser.add_argument("--indirect-target-count", type=int, default=0, help="Number of indirect-branch targets")
    parser.add_argument(
        "--indirect-target-block-align",
        type=int,
        default=64,
        help="Alignment for indirect target blocks, in bytes",
    )
    parser.add_argument(
        "--indirect-target-region-reps",
        type=int,
        default=0,
        help="Indirect-target replay count per outer iteration",
    )
    parser.add_argument(
        "--indirect-target-pos",
        type=int,
        default=5,
        help="Execution order position of the indirect-target module",
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


def generate(args: argparse.Namespace) -> str:
    main_total_blocks = max(0, args.main_blocks)
    main_region_reps = 0 if main_total_blocks == 0 else max(1, args.main_region_reps)
    main_layout = args.main_layout
    main_pos = args.main_pos
    hot_l1_size = max(0, args.hot_l1_size)
    hot_l1_branch_pairs_per_unit = max(0, int(args.hot_l1_branch_pairs_per_unit))
    hot_l1_region_reps = 0 if hot_l1_size == 0 else max(1, args.hot_l1_region_reps)
    hot_l1_pos = args.hot_l1_pos
    hot_l2_size = max(0, args.hot_l2_size)
    hot_l2_region_reps = 0 if hot_l2_size == 0 else max(1, args.hot_l2_region_reps)
    hot_l2_pos = args.hot_l2_pos

    fetch_total_blocks = max(0, args.fetch_blocks)
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

    call_ret_funcs = max(0, args.call_ret_funcs)
    call_ret_lines_per_func = MODULES.call_ret_chain.normalize_lines_per_func(args.call_ret_lines_per_func)
    call_ret_region_reps = 0 if call_ret_funcs == 0 else max(1, args.call_ret_region_reps)
    call_ret_pos = args.call_ret_pos

    plt_stub_funcs = max(0, args.plt_stub_funcs)
    plt_stub_region_reps = 0 if plt_stub_funcs == 0 else max(1, args.plt_stub_region_reps)
    plt_stub_pos = args.plt_stub_pos

    indirect_target_count = max(0, args.indirect_target_count)
    indirect_target_block_align = max(64, args.indirect_target_block_align)
    indirect_target_region_reps = 0 if indirect_target_count == 0 else max(1, args.indirect_target_region_reps)
    indirect_target_pos = args.indirect_target_pos

    if (
        main_total_blocks == 0
        and fetch_total_blocks == 0
        and hot_l1_size == 0
        and hot_l2_size == 0
        and itlb_funcs == 0
        and call_ret_funcs == 0
        and plt_stub_funcs == 0
        and indirect_target_count == 0
    ):
        raise ValueError("At least one frontend module must be non-zero")

    main_block_align = max(64, args.block_align)
    fetch_block_align = max(64, args.fetch_block_align)
    hot_l1_align = 64
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

    call_ret_phys_order = MODULES.tlb_region.shuffled_itlb_phys_order(call_ret_funcs, args.seed ^ 0x165667B1)
    call_ret_exec_order = MODULES.tlb_region.constrained_itlb_exec_order(
        call_ret_phys_order,
        args.seed ^ 0xD3A2646C,
        4,
    )
    call_ret_next_map, _ = MODULES.tlb_region.build_chain_maps(call_ret_funcs, call_ret_exec_order, "chain")

    hot_l1_insns = hot_l1_size // 4 if hot_l1_size > 0 else 0
    hot_l2_insns = hot_l2_size // 4 if hot_l2_size > 0 else 0

    main_exec_samples = list(range(min(main_total_blocks, 8)))
    main_phys_samples = main_physical_order[: min(main_total_blocks, 8)]
    itlb_samples = itlb_exec_order[: min(itlb_funcs, 8)] if itlb_exec_order else []
    call_ret_samples = call_ret_exec_order[: min(call_ret_funcs, 8)] if call_ret_exec_order else []

    main_indirect_blocks_per_chain = MODULES.block_loop.count_indirect_blocks(main_total_blocks, main_direct_run_len)
    fetch_indirect_blocks_per_chain = FETCH_AMPLIFIER.count_indirect_blocks(fetch_total_blocks, fetch_direct_run_len)
    itlb_indirect_funcs_per_chain = MODULES.tlb_region.count_indirect_functions(
        itlb_funcs,
        itlb_mode,
        itlb_direct_run_len,
    )

    hot_l1_entries_per_iter = hot_l1_region_reps
    hot_l2_entries_per_iter = hot_l2_region_reps
    itlb_calls_per_iter = itlb_region_reps if itlb_mode == "chain" else itlb_funcs * itlb_region_reps
    call_ret_calls_per_iter = call_ret_region_reps
    plt_stub_calls_per_iter = plt_stub_funcs * plt_stub_region_reps
    indirect_target_calls_per_iter = indirect_target_count * indirect_target_region_reps
    main_block_entries_per_iter = main_total_blocks * main_region_reps
    fetch_block_entries_per_iter = fetch_total_blocks * fetch_region_reps

    total_frontend_units_per_iter = (
        hot_l1_entries_per_iter
        + hot_l2_entries_per_iter
        + fetch_block_entries_per_iter
        + itlb_calls_per_iter
        + call_ret_calls_per_iter
        + plt_stub_calls_per_iter
        + indirect_target_calls_per_iter
        + main_block_entries_per_iter
    )

    ordered_module_loops = [
        (hot_l1_pos, "hot_l1", "CONFIG_HOT_L1_REGION_REPS", "CONFIG_HOT_L1_SIZE > 0", "hot_l1_blob();"),
        (hot_l2_pos, "hot_l2", "CONFIG_HOT_L2_REGION_REPS", "CONFIG_HOT_L2_SIZE > 0", "hot_l2_blob();"),
        (
            fetch_pos,
            "fetch_amplifier",
            "CONFIG_FETCH_REGION_REPS",
            "CONFIG_FETCH_TOTAL_BLOCKS > 0",
            "run_fetch_amplifier_once();",
        ),
        (itlb_pos, "itlb", "CONFIG_ITLB_REGION_REPS", "CONFIG_ITLB_FUNCS > 0", "run_itlb_region_once();"),
        (
            call_ret_pos,
            "call_ret",
            "CONFIG_CALL_RET_REGION_REPS",
            "CONFIG_CALL_RET_FUNCS > 0",
            "run_call_ret_chain_once();",
        ),
        (
            plt_stub_pos,
            "plt_stub",
            "CONFIG_PLT_STUB_REGION_REPS",
            "CONFIG_PLT_STUB_FUNCS > 0",
            "run_plt_stub_chain_once();",
        ),
        (
            indirect_target_pos,
            "indirect_target",
            "CONFIG_INDIRECT_TARGET_REGION_REPS",
            "CONFIG_INDIRECT_TARGET_COUNT > 0",
            "run_indirect_target_set_once();",
        ),
        (
            main_pos,
            "block_loop",
            "CONFIG_MAIN_REGION_REPS",
            "CONFIG_MAIN_TOTAL_BLOCKS > 0",
            "run_block_loop_once();",
        ),
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
    out.append("#include <time.h>\n")
    out.append("#include <unistd.h>\n\n")

    out.append(f"#define CONFIG_HOT_L1_SIZE {hot_l1_size}u\n")
    out.append(f"#define CONFIG_HOT_L1_INSNS {hot_l1_insns}u\n")
    out.append(f"#define CONFIG_HOT_L1_REGION_REPS {hot_l1_region_reps}u\n")
    out.append(f"#define CONFIG_HOT_L1_POS {hot_l1_pos}u\n")
    out.append(f"#define CONFIG_HOT_L1_ALIGN {hot_l1_align}u\n")

    out.append(f"#define CONFIG_HOT_L2_SIZE {hot_l2_size}u\n")
    out.append(f"#define CONFIG_HOT_L2_INSNS {hot_l2_insns}u\n")
    out.append(f"#define CONFIG_HOT_L2_REGION_REPS {hot_l2_region_reps}u\n")
    out.append(f"#define CONFIG_HOT_L2_POS {hot_l2_pos}u\n")
    out.append(f"#define CONFIG_HOT_L2_ALIGN {hot_l2_align}u\n")

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

    out.append(f"#define CONFIG_CALL_RET_FUNCS {call_ret_funcs}u\n")
    out.append(f"#define CONFIG_CALL_RET_LINES_PER_FUNC {call_ret_lines_per_func}u\n")
    out.append(f"#define CONFIG_CALL_RET_REGION_REPS {call_ret_region_reps}u\n")
    out.append(f"#define CONFIG_CALL_RET_POS {call_ret_pos}u\n")

    out.append(f"#define CONFIG_PLT_STUB_FUNCS {plt_stub_funcs}u\n")
    out.append(f"#define CONFIG_PLT_STUB_REGION_REPS {plt_stub_region_reps}u\n")
    out.append(f"#define CONFIG_PLT_STUB_POS {plt_stub_pos}u\n")

    out.append(f"#define CONFIG_INDIRECT_TARGET_COUNT {indirect_target_count}u\n")
    out.append(f"#define CONFIG_INDIRECT_TARGET_BLOCK_ALIGN {indirect_target_block_align}u\n")
    out.append(f"#define CONFIG_INDIRECT_TARGET_REGION_REPS {indirect_target_region_reps}u\n")
    out.append(f"#define CONFIG_INDIRECT_TARGET_POS {indirect_target_pos}u\n")

    out.append(f"#define CONFIG_MAIN_TOTAL_BLOCKS {main_total_blocks}u\n")
    out.append(f"#define CONFIG_MAIN_BLOCK_ALIGN {main_block_align}u\n")
    out.append(f"#define CONFIG_MAIN_DIRECT_RUN_LEN {main_direct_run_len}u\n")
    out.append(f"#define CONFIG_MAIN_REGION_REPS {main_region_reps}u\n")
    out.append(f"#define CONFIG_MAIN_POS {main_pos}u\n")
    out.append(f'#define CONFIG_MAIN_LAYOUT_STR "{main_layout}"\n')
    out.append(f"#define CONFIG_SEED {args.seed}u\n")

    out.append(f"#define CONFIG_HOT_L1_ENTRIES_PER_ITER {hot_l1_entries_per_iter}u\n")
    out.append(f"#define CONFIG_HOT_L2_ENTRIES_PER_ITER {hot_l2_entries_per_iter}u\n")
    out.append(f"#define CONFIG_FETCH_BLOCK_ENTRIES_PER_ITER {fetch_block_entries_per_iter}u\n")
    out.append(f"#define CONFIG_ITLB_CALLS_PER_ITER {itlb_calls_per_iter}u\n")
    out.append(f"#define CONFIG_CALL_RET_CALLS_PER_ITER {call_ret_calls_per_iter}u\n")
    out.append(f"#define CONFIG_PLT_STUB_CALLS_PER_ITER {plt_stub_calls_per_iter}u\n")
    out.append(f"#define CONFIG_INDIRECT_TARGET_CALLS_PER_ITER {indirect_target_calls_per_iter}u\n")
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
    out.append(format_u32_array("kCallRetPhysicalOrder", call_ret_phys_order))
    out.append(format_u32_array("kCallRetExecOrder", call_ret_exec_order))
    out.append(format_u32_array("kCallRetSamples", call_ret_samples))

    out.append("typedef void (*bench_func_t)(void);\n\n")
    out.append("static void *g_itlb_func_table[CONFIG_ITLB_FUNCS > 0 ? CONFIG_ITLB_FUNCS : 1u];\n")
    out.append("static void *g_fetch_table[CONFIG_FETCH_TOTAL_BLOCKS > 0 ? CONFIG_FETCH_TOTAL_BLOCKS : 1u];\n")
    out.append("static void *g_main_table[CONFIG_MAIN_TOTAL_BLOCKS > 0 ? CONFIG_MAIN_TOTAL_BLOCKS : 1u];\n")
    out.append(
        "static void *g_indirect_target_table[CONFIG_INDIRECT_TARGET_COUNT > 0 ? CONFIG_INDIRECT_TARGET_COUNT : 1u];\n\n"
    )

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

    if indirect_target_count > 0:
        out.append(
            '__attribute__((used, noinline))\n'
            'static void dispatch_indirect_target(uint64_t idx) {\n'
            '    ((bench_func_t)g_indirect_target_table[idx])();\n'
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

    for func_id in call_ret_phys_order:
        out.append(
            MODULES.call_ret_chain.emit_function(
                func_id,
                call_ret_next_map[func_id],
                call_ret_lines_per_func,
            )
        )

    for func_id in range(plt_stub_funcs):
        out.append(MODULES.plt_stub_chain.emit_caller(func_id))
        out.append(MODULES.plt_stub_chain.emit_stub(func_id))
        out.append(MODULES.plt_stub_chain.emit_callee(func_id))

    for target_id in range(indirect_target_count):
        out.append(
            MODULES.indirect_target_set.emit_target_function(
                target_id,
                indirect_target_count,
                indirect_target_block_align,
                "dispatch_indirect_target",
            )
        )

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_fetch_amplifier_once(void) {\n")
    if fetch_total_blocks > 0:
        out.append("    ((bench_func_t)g_fetch_table[0])();\n")
    out.append("}\n\n")

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_itlb_region_once(void) {\n")
    if itlb_funcs > 0:
        out.append('    asm volatile("mov x9, xzr\\n\\t" "mov x10, xzr\\n\\t" ::: "x9", "x10", "cc", "memory");\n')
        if itlb_mode == "chain":
            if itlb_exec_order:
                out.append(f"    itlb_func_{itlb_exec_order[0]}();\n")
        else:
            for func_id in range(itlb_funcs):
                out.append(f"    itlb_func_{func_id}();\n")
    out.append("}\n\n")

    out.append(
        emit_chain_runner(
            "run_call_ret_chain_once",
            None if not call_ret_exec_order else f"call_ret_func_{call_ret_exec_order[0]}",
        )
    )
    out.append(emit_direct_call_runner("run_plt_stub_chain_once", "plt_caller", plt_stub_funcs))

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_indirect_target_set_once(void) {\n")
    if indirect_target_count > 0:
        out.append('    asm volatile("mov x9, xzr\\n\\t" "mov x10, xzr\\n\\t" ::: "x9", "x10", "cc", "memory");\n')
        out.append("    dispatch_indirect_target(0);\n")
    out.append("}\n\n")

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_block_loop_once(void) {\n")
    if main_total_blocks > 0:
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

    for target_id in range(indirect_target_count):
        out.append(f"    g_indirect_target_table[{target_id}] = (void *)&indirect_target_{target_id};\n")
    if indirect_target_count == 0:
        out.append("    g_indirect_target_table[0] = NULL;\n")
    out.append("\n")

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
    return argparse.Namespace(
        out=str(out_path),
        main_blocks=int(cfg["cold_block_sequence_blocks"]),
        block_align=int(cfg["cold_block_sequence_block_align"]),
        direct_run_len=int(cfg["cold_block_sequence_direct_run_len"]),
        main_region_reps=int(cfg["cold_block_sequence_region_reps"]),
        main_layout=str(cfg["cold_block_sequence_layout"]),
        main_pos=int(cfg["cold_block_sequence_pos"]),
        fetch_blocks=int(cfg["fetch_amplifier_blocks"]),
        fetch_block_align=int(cfg["fetch_amplifier_block_align"]),
        fetch_direct_run_len=int(cfg["fetch_amplifier_direct_run_len"]),
        fetch_branch_pairs_per_block=int(cfg["fetch_amplifier_branch_pairs_per_block"]),
        fetch_block_slots=int(cfg.get("fetch_amplifier_block_slots", 16)),
        fetch_region_reps=int(cfg["fetch_amplifier_region_reps"]),
        fetch_layout=str(cfg["fetch_amplifier_layout"]),
        fetch_pos=int(cfg["fetch_amplifier_pos"]),
        hot_l1_size=int(cfg["hot_region_loop_size"]),
        hot_l1_branch_pairs_per_unit=int(cfg["hot_region_loop_branch_pairs_per_unit"]),
        hot_l1_region_reps=int(cfg["hot_region_loop_region_reps"]),
        hot_l1_pos=int(cfg["hot_region_loop_pos"]),
        hot_l2_size=0,
        hot_l2_region_reps=0,
        hot_l2_pos=max(int(cfg["hot_region_loop_pos"]) + 1, 7),
        itlb_funcs=int(cfg["itlb_funcs"]),
        itlb_lines_per_page=int(cfg["itlb_lines_per_page"]),
        itlb_region_reps=int(cfg["itlb_region_reps"]),
        itlb_mode=str(cfg["itlb_mode"]),
        itlb_direct_run_len=int(cfg["itlb_direct_run_len"]),
        itlb_pos=int(cfg["itlb_pos"]),
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
