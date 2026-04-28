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
FETCH_AMPLIFIER = getattr(MODULES, "fetch_amplifier", MODULES.cold_block_sequence)
MIXED_REGION = getattr(MODULES, "mixed_region", getattr(MODULES, "mixed_region_loop", MixedRegionBuilder()))
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

    parser.add_argument("--mixed-region-size", type=int, default=0, help="Mixed I+D region size in bytes")
    parser.add_argument(
        "--mixed-region-ldr-count-per-unit",
        type=int,
        default=0,
        help="How many pointer-chasing ldr instructions to interleave into each 64B mixed-region unit",
    )
    parser.add_argument(
        "--mixed-region-data-mode",
        choices=list(MIXED_REGION.DATA_MODE_CHOICES),
        default="linear",
        help="Pointer-chain layout policy for mixed-region data accesses",
    )
    parser.add_argument(
        "--mixed-region-pages",
        type=int,
        default=1,
        help="How many 4KB pages to allocate for the mixed-region pointer pool",
    )
    parser.add_argument(
        "--mixed-region-lines-per-page",
        type=int,
        default=8,
        help="How many 64B pointer nodes to place on each mixed-region page",
    )
    parser.add_argument(
        "--mixed-region-region-reps",
        type=int,
        default=0,
        help="Mixed-region replay count per outer iteration",
    )
    parser.add_argument(
        "--mixed-region-pos",
        type=int,
        default=2,
        help="Execution order position of the mixed I+D region module",
    )

    parser.add_argument("--data-stream-size", type=int, default=0, help="Working-set bytes for the data-stream module")
    parser.add_argument(
        "--data-stream-stride",
        type=int,
        default=64,
        help="Stride in bytes between consecutive data-stream loads",
    )
    parser.add_argument("--data-stream-region-reps", type=int, default=0, help="Data-stream replay count per outer iteration")
    parser.add_argument("--data-stream-pos", type=int, default=5, help="Execution order position of the data-stream module")

    parser.add_argument("--data-pointer-chase-pages", type=int, default=0, help="Page count for the data pointer-chase pool")
    parser.add_argument(
        "--data-pointer-chase-lines-per-page",
        type=int,
        default=1,
        help="How many 64B lines to thread through on each data pointer-chase page",
    )
    parser.add_argument(
        "--data-pointer-chase-region-reps",
        type=int,
        default=0,
        help="Data pointer-chase replay count per outer iteration",
    )
    parser.add_argument(
        "--data-pointer-chase-pos",
        type=int,
        default=6,
        help="Execution order position of the data pointer-chase module",
    )

    parser.add_argument("--data-page-stride-pages", type=int, default=0, help="Page count for the cross-page stride module")
    parser.add_argument(
        "--data-page-stride-page-stride",
        type=int,
        default=1,
        help="Stride in pages between successive cross-page loads",
    )
    parser.add_argument(
        "--data-page-stride-line-index",
        type=int,
        default=0,
        help="Which 64B line inside each page to touch in the cross-page stride module",
    )
    parser.add_argument(
        "--data-page-stride-region-reps",
        type=int,
        default=0,
        help="Cross-page stride replay count per outer iteration",
    )
    parser.add_argument(
        "--data-page-stride-pos",
        type=int,
        default=7,
        help="Execution order position of the cross-page stride module",
    )

    parser.add_argument("--data-indirect-gather-pages", type=int, default=0, help="Page count for the indirect-gather pool")
    parser.add_argument(
        "--data-indirect-gather-lines-per-page",
        type=int,
        default=1,
        help="How many 64B lines to sample on each page in the indirect-gather pool",
    )
    parser.add_argument(
        "--data-indirect-gather-index-stride",
        type=int,
        default=1,
        help="Stride through the indirect index array for the indirect-gather module",
    )
    parser.add_argument(
        "--data-indirect-gather-region-reps",
        type=int,
        default=0,
        help="Indirect-gather replay count per outer iteration",
    )
    parser.add_argument(
        "--data-indirect-gather-pos",
        type=int,
        default=8,
        help="Execution order position of the indirect-gather module",
    )

    parser.add_argument(
        "--data-hot-stride-access-count",
        type=int,
        default=0,
        help="How many fixed-stride accesses to issue before the hot-stride module wraps to the start",
    )
    parser.add_argument(
        "--data-hot-stride-stride",
        type=int,
        default=4,
        help="Byte stride for the hot-stride module",
    )
    parser.add_argument(
        "--data-hot-stride-region-reps",
        type=int,
        default=0,
        help="Hot-stride replay count per outer iteration",
    )
    parser.add_argument(
        "--data-hot-stride-pos",
        type=int,
        default=9,
        help="Execution order position of the hot-stride module",
    )

    parser.add_argument(
        "--data-cold-stride-access-count",
        type=int,
        default=0,
        help="How many fixed-stride accesses to issue before the cold-stride module wraps to the start",
    )
    parser.add_argument(
        "--data-cold-stride-stride",
        type=int,
        default=256,
        help="Byte stride for the cold-stride module",
    )
    parser.add_argument(
        "--data-cold-stride-region-reps",
        type=int,
        default=0,
        help="Cold-stride replay count per outer iteration",
    )
    parser.add_argument(
        "--data-cold-stride-pos",
        type=int,
        default=10,
        help="Execution order position of the cold-stride module",
    )

    parser.add_argument(
        "--data-tlb-indirect-pages",
        type=int,
        default=0,
        help="How many pages to thread through in the TLB-indirect module",
    )
    parser.add_argument(
        "--data-tlb-indirect-line-index",
        type=int,
        default=0,
        help="Which 64B line inside each page to touch in the TLB-indirect module",
    )
    parser.add_argument(
        "--data-tlb-indirect-region-reps",
        type=int,
        default=0,
        help="TLB-indirect replay count per outer iteration",
    )
    parser.add_argument(
        "--data-tlb-indirect-pos",
        type=int,
        default=11,
        help="Execution order position of the TLB-indirect module",
    )

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
    mixed_region_size = MIXED_REGION.normalize_size_bytes(args.mixed_region_size)
    mixed_region_ldr_count_per_unit = MIXED_REGION.normalize_ldr_count_per_unit(
        args.mixed_region_ldr_count_per_unit
    )
    mixed_region_data_mode = MIXED_REGION.normalize_data_mode(args.mixed_region_data_mode)
    mixed_region_pages = MIXED_REGION.normalize_pages(args.mixed_region_pages)
    mixed_region_lines_per_page = MIXED_REGION.normalize_lines_per_page(args.mixed_region_lines_per_page)
    mixed_region_region_reps = (
        0
        if mixed_region_size == 0 or mixed_region_pages == 0
        else max(1, args.mixed_region_region_reps)
    )
    mixed_region_pos = args.mixed_region_pos
    mixed_region_slots = [
        {
            "slot_id": 0,
            "prefix": "mixed_region",
            "label": "mixed_region_loop",
            "size": mixed_region_size,
            "ldr_count_per_unit": mixed_region_ldr_count_per_unit,
            "data_mode": mixed_region_data_mode,
            "pages": mixed_region_pages,
            "lines_per_page": mixed_region_lines_per_page,
            "region_reps": mixed_region_region_reps,
            "pos": mixed_region_pos,
        }
    ]
    for slot_id, raw_slot in enumerate(getattr(args, "mixed_region_extra_slots", []), start=1):
        slot_size = MIXED_REGION.normalize_size_bytes(raw_slot.get("size", 0))
        slot_ldr_count = MIXED_REGION.normalize_ldr_count_per_unit(raw_slot.get("ldr_count_per_unit", 0))
        slot_data_mode = MIXED_REGION.normalize_data_mode(raw_slot.get("data_mode", "linear"))
        slot_pages = MIXED_REGION.normalize_pages(raw_slot.get("pages", 1))
        slot_lines_per_page = MIXED_REGION.normalize_lines_per_page(raw_slot.get("lines_per_page", 8))
        slot_region_reps = 0 if slot_size == 0 or slot_pages == 0 else max(1, raw_slot.get("region_reps", 0))
        mixed_region_slots.append(
            {
                "slot_id": slot_id,
                "prefix": f"mixed_region_{slot_id}",
                "label": f"mixed_region_loop_{slot_id}",
                "size": slot_size,
                "ldr_count_per_unit": slot_ldr_count,
                "data_mode": slot_data_mode,
                "pages": slot_pages,
                "lines_per_page": slot_lines_per_page,
                "region_reps": slot_region_reps,
                "pos": raw_slot.get("pos", mixed_region_pos + slot_id),
            }
        )
    mixed_region_enabled = any(slot["size"] > 0 and slot["pages"] > 0 for slot in mixed_region_slots)
    data_stream_size = MODULES.data_stream.normalize_size_bytes(args.data_stream_size)
    data_stream_stride = MODULES.data_stream.normalize_stride_bytes(data_stream_size, args.data_stream_stride)
    data_stream_region_reps = 0 if data_stream_size == 0 else max(1, args.data_stream_region_reps)
    data_stream_pos = args.data_stream_pos
    data_pointer_chase_pages = MODULES.data_pointer_chase.normalize_page_count(args.data_pointer_chase_pages)
    data_pointer_chase_lines_per_page = MODULES.data_pointer_chase.normalize_lines_per_page(
        args.data_pointer_chase_lines_per_page
    )
    data_pointer_chase_region_reps = 0 if data_pointer_chase_pages == 0 else max(1, args.data_pointer_chase_region_reps)
    data_pointer_chase_pos = args.data_pointer_chase_pos
    data_page_stride_pages = MODULES.data_page_stride.normalize_page_count(args.data_page_stride_pages)
    data_page_stride_line_index = MODULES.data_page_stride.normalize_line_index(args.data_page_stride_line_index)
    data_page_stride_page_stride = MODULES.data_page_stride.normalize_cycle_stride(
        data_page_stride_pages,
        args.data_page_stride_page_stride,
    )
    data_page_stride_region_reps = 0 if data_page_stride_pages == 0 else max(1, args.data_page_stride_region_reps)
    data_page_stride_pos = args.data_page_stride_pos
    data_indirect_gather_pages = MODULES.data_indirect_gather.normalize_page_count(args.data_indirect_gather_pages)
    data_indirect_gather_lines_per_page = MODULES.data_indirect_gather.normalize_lines_per_page(
        args.data_indirect_gather_lines_per_page
    )
    data_indirect_gather_region_reps = (
        0 if data_indirect_gather_pages == 0 else max(1, args.data_indirect_gather_region_reps)
    )
    data_indirect_gather_pos = args.data_indirect_gather_pos
    data_hot_stride_access_count = MODULES.data_hot_stride.normalize_access_count(args.data_hot_stride_access_count)
    data_hot_stride_stride = MODULES.data_hot_stride.normalize_word_stride_bytes(args.data_hot_stride_stride)
    data_hot_stride_region_reps = 0 if data_hot_stride_access_count == 0 else max(1, args.data_hot_stride_region_reps)
    data_hot_stride_pos = args.data_hot_stride_pos
    data_cold_stride_access_count = MODULES.data_cold_stride.normalize_access_count(args.data_cold_stride_access_count)
    data_cold_stride_stride = MODULES.data_cold_stride.normalize_word_stride_bytes(args.data_cold_stride_stride)
    data_cold_stride_region_reps = (
        0 if data_cold_stride_access_count == 0 else max(1, args.data_cold_stride_region_reps)
    )
    data_cold_stride_pos = args.data_cold_stride_pos
    data_tlb_indirect_pages = MODULES.data_tlb_indirect.normalize_page_count(args.data_tlb_indirect_pages)
    data_tlb_indirect_line_index = MODULES.data_tlb_indirect.normalize_line_index(args.data_tlb_indirect_line_index)
    data_tlb_indirect_region_reps = (
        0 if data_tlb_indirect_pages == 0 else max(1, args.data_tlb_indirect_region_reps)
    )
    data_tlb_indirect_pos = args.data_tlb_indirect_pos

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
        and not mixed_region_enabled
        and data_stream_size == 0
        and data_pointer_chase_pages == 0
        and data_page_stride_pages == 0
        and data_indirect_gather_pages == 0
        and data_hot_stride_access_count == 0
        and data_cold_stride_access_count == 0
        and data_tlb_indirect_pages == 0
        and itlb_funcs == 0
        and call_ret_funcs == 0
        and plt_stub_funcs == 0
        and indirect_target_count == 0
    ):
        raise ValueError("At least one frontend or data-cache module must be non-zero")

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
    data_pointer_chase_offsets = MODULES.data_pointer_chase.build_pointer_chase_offsets(
        data_pointer_chase_pages,
        data_pointer_chase_lines_per_page,
        args.seed ^ 0x4CF5AD43,
    )
    data_page_stride_offsets = MODULES.data_page_stride.build_page_stride_offsets(
        data_page_stride_pages,
        data_page_stride_page_stride,
        data_page_stride_line_index,
        args.seed ^ 0x7F4A7C15,
    )
    data_indirect_gather_offsets = MODULES.data_indirect_gather.build_pointer_chase_offsets(
        data_indirect_gather_pages,
        data_indirect_gather_lines_per_page,
        args.seed ^ 0xA24BAED4,
    )
    data_indirect_gather_node_count = len(data_indirect_gather_offsets)
    data_indirect_gather_index_stride = MODULES.data_indirect_gather.normalize_cycle_stride(
        data_indirect_gather_node_count,
        args.data_indirect_gather_index_stride,
    )
    data_hot_stride_offsets = MODULES.data_hot_stride.build_stride_offsets(
        data_hot_stride_access_count,
        data_hot_stride_stride,
    )
    data_hot_stride_buffer_bytes = 0 if not data_hot_stride_offsets else data_hot_stride_offsets[-1] + 4
    data_cold_stride_offsets = MODULES.data_cold_stride.build_stride_offsets(
        data_cold_stride_access_count,
        data_cold_stride_stride,
    )
    data_cold_stride_buffer_bytes = 0 if not data_cold_stride_offsets else data_cold_stride_offsets[-1] + 4
    data_tlb_indirect_offsets = MODULES.data_tlb_indirect.build_tlb_indirect_offsets(
        data_tlb_indirect_pages,
        data_tlb_indirect_line_index,
        args.seed ^ 0xC2B2AE35,
    )
    data_tlb_indirect_access_count = len(data_tlb_indirect_offsets)
    data_tlb_indirect_pool_bytes = data_tlb_indirect_pages * 4096
    mixed_region_offsets = MIXED_REGION.build_pointer_offsets(
        mixed_region_pages,
        mixed_region_lines_per_page,
        mixed_region_data_mode,
        args.seed ^ 0xB5297A4D,
    )
    mixed_region_node_count = len(mixed_region_offsets)
    mixed_region_pool_bytes = mixed_region_pages * 4096
    mixed_region_loads_per_call = (mixed_region_size // 64) * mixed_region_ldr_count_per_unit
    for slot in mixed_region_slots[1:]:
        slot["offsets"] = MIXED_REGION.build_pointer_offsets(
            slot["pages"],
            slot["lines_per_page"],
            slot["data_mode"],
            args.seed ^ 0xB5297A4D ^ (slot["slot_id"] * 0x45D9F3B),
        )
        slot["node_count"] = len(slot["offsets"])
        slot["pool_bytes"] = slot["pages"] * 4096
        slot["loads_per_call"] = (slot["size"] // 64) * slot["ldr_count_per_unit"]

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
    mixed_region_accesses_per_iter = mixed_region_loads_per_call * mixed_region_region_reps
    for slot in mixed_region_slots[1:]:
        mixed_region_accesses_per_iter += slot["loads_per_call"] * slot["region_reps"]
    data_stream_accesses_per_call = 0 if data_stream_size == 0 else ((data_stream_size - 1) // data_stream_stride) + 1
    data_stream_accesses_per_iter = data_stream_accesses_per_call * data_stream_region_reps
    data_pointer_chase_nodes = len(data_pointer_chase_offsets)
    data_pointer_chase_accesses_per_iter = data_pointer_chase_nodes * data_pointer_chase_region_reps
    data_page_stride_accesses_per_call = len(data_page_stride_offsets)
    data_page_stride_accesses_per_iter = data_page_stride_accesses_per_call * data_page_stride_region_reps
    data_indirect_gather_accesses_per_iter = data_indirect_gather_node_count * data_indirect_gather_region_reps
    data_hot_stride_accesses_per_iter = data_hot_stride_access_count * data_hot_stride_region_reps
    data_cold_stride_accesses_per_iter = data_cold_stride_access_count * data_cold_stride_region_reps
    data_tlb_indirect_accesses_per_iter = data_tlb_indirect_access_count * data_tlb_indirect_region_reps
    itlb_calls_per_iter = itlb_region_reps if itlb_mode == "chain" else itlb_funcs * itlb_region_reps
    call_ret_calls_per_iter = call_ret_region_reps
    plt_stub_calls_per_iter = plt_stub_funcs * plt_stub_region_reps
    indirect_target_calls_per_iter = indirect_target_count * indirect_target_region_reps
    main_block_entries_per_iter = main_total_blocks * main_region_reps
    fetch_block_entries_per_iter = fetch_total_blocks * fetch_region_reps

    total_frontend_units_per_iter = (
        hot_l1_entries_per_iter
        + hot_l2_entries_per_iter
        + mixed_region_accesses_per_iter
        + data_stream_accesses_per_iter
        + data_pointer_chase_accesses_per_iter
        + data_page_stride_accesses_per_iter
        + data_indirect_gather_accesses_per_iter
        + data_hot_stride_accesses_per_iter
        + data_cold_stride_accesses_per_iter
        + data_tlb_indirect_accesses_per_iter
        + fetch_block_entries_per_iter
        + itlb_calls_per_iter
        + call_ret_calls_per_iter
        + plt_stub_calls_per_iter
        + indirect_target_calls_per_iter
        + main_block_entries_per_iter
    )

    ordered_module_loops = [
        (hot_l1_pos, "hot_l1", "CONFIG_HOT_L1_REGION_REPS", "CONFIG_HOT_L1_SIZE > 0", "run_hot_l1_once();"),
        (hot_l2_pos, "hot_l2", "CONFIG_HOT_L2_REGION_REPS", "CONFIG_HOT_L2_SIZE > 0", "run_hot_l2_once();"),
        (
            mixed_region_pos,
            "mixed_region_loop",
            "CONFIG_MIXED_REGION_REPS",
            "CONFIG_MIXED_REGION_SIZE > 0 && CONFIG_MIXED_REGION_PAGE_COUNT > 0",
            "run_mixed_region_once();",
        ),
        *[
            (
                slot["pos"],
                slot["label"],
                f"CONFIG_MIXED_REGION_{slot['slot_id']}_REPS",
                f"CONFIG_MIXED_REGION_{slot['slot_id']}_SIZE > 0 && CONFIG_MIXED_REGION_{slot['slot_id']}_PAGE_COUNT > 0",
                f"run_mixed_region_{slot['slot_id']}_once();",
            )
            for slot in mixed_region_slots[1:]
        ],
        (
            data_stream_pos,
            "data_stream",
            "CONFIG_DATA_STREAM_REGION_REPS",
            "CONFIG_DATA_STREAM_SIZE > 0",
            "run_data_stream_once();",
        ),
        (
            data_pointer_chase_pos,
            "data_pointer_chase",
            "CONFIG_DATA_POINTER_CHASE_REGION_REPS",
            "CONFIG_DATA_POINTER_CHASE_PAGE_COUNT > 0",
            "run_data_pointer_chase_once();",
        ),
        (
            data_page_stride_pos,
            "data_page_stride",
            "CONFIG_DATA_PAGE_STRIDE_REGION_REPS",
            "CONFIG_DATA_PAGE_STRIDE_PAGE_COUNT > 0",
            "run_data_page_stride_once();",
        ),
        (
            data_indirect_gather_pos,
            "data_indirect_gather",
            "CONFIG_DATA_INDIRECT_GATHER_REGION_REPS",
            "CONFIG_DATA_INDIRECT_GATHER_PAGE_COUNT > 0",
            "run_data_indirect_gather_once();",
        ),
        (
            data_hot_stride_pos,
            "data_hot_stride",
            "CONFIG_DATA_HOT_STRIDE_REGION_REPS",
            "CONFIG_DATA_HOT_STRIDE_ACCESS_COUNT > 0",
            "run_data_hot_stride_once();",
        ),
        (
            data_cold_stride_pos,
            "data_cold_stride",
            "CONFIG_DATA_COLD_STRIDE_REGION_REPS",
            "CONFIG_DATA_COLD_STRIDE_ACCESS_COUNT > 0",
            "run_data_cold_stride_once();",
        ),
        (
            data_tlb_indirect_pos,
            "data_tlb_indirect",
            "CONFIG_DATA_TLB_INDIRECT_REGION_REPS",
            "CONFIG_DATA_TLB_INDIRECT_PAGE_COUNT > 0",
            "run_data_tlb_indirect_once();",
        ),
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

    out.append(f"#define CONFIG_MIXED_REGION_SIZE {mixed_region_size}u\n")
    out.append(f"#define CONFIG_MIXED_REGION_LDR_COUNT_PER_UNIT {mixed_region_ldr_count_per_unit}u\n")
    out.append(f"#define CONFIG_MIXED_REGION_PAGE_COUNT {mixed_region_pages}u\n")
    out.append(f"#define CONFIG_MIXED_REGION_LINES_PER_PAGE {mixed_region_lines_per_page}u\n")
    out.append(f"#define CONFIG_MIXED_REGION_NODE_COUNT {mixed_region_node_count}u\n")
    out.append(f"#define CONFIG_MIXED_REGION_POOL_BYTES {mixed_region_pool_bytes}u\n")
    out.append(f"#define CONFIG_MIXED_REGION_REPS {mixed_region_region_reps}u\n")
    out.append(f"#define CONFIG_MIXED_REGION_POS {mixed_region_pos}u\n")
    out.append(f'#define CONFIG_MIXED_REGION_DATA_MODE_STR "{mixed_region_data_mode}"\n')
    for slot in mixed_region_slots[1:]:
        slot_id = slot["slot_id"]
        out.append(f"#define CONFIG_MIXED_REGION_{slot_id}_SIZE {slot['size']}u\n")
        out.append(f"#define CONFIG_MIXED_REGION_{slot_id}_LDR_COUNT_PER_UNIT {slot['ldr_count_per_unit']}u\n")
        out.append(f"#define CONFIG_MIXED_REGION_{slot_id}_PAGE_COUNT {slot['pages']}u\n")
        out.append(f"#define CONFIG_MIXED_REGION_{slot_id}_LINES_PER_PAGE {slot['lines_per_page']}u\n")
        out.append(f"#define CONFIG_MIXED_REGION_{slot_id}_NODE_COUNT {slot['node_count']}u\n")
        out.append(f"#define CONFIG_MIXED_REGION_{slot_id}_POOL_BYTES {slot['pool_bytes']}u\n")
        out.append(f"#define CONFIG_MIXED_REGION_{slot_id}_REPS {slot['region_reps']}u\n")
        out.append(f"#define CONFIG_MIXED_REGION_{slot_id}_POS {slot['pos']}u\n")
        out.append(f'#define CONFIG_MIXED_REGION_{slot_id}_DATA_MODE_STR "{slot["data_mode"]}"\n')

    out.append(f"#define CONFIG_DATA_STREAM_SIZE {data_stream_size}u\n")
    out.append(f"#define CONFIG_DATA_STREAM_STRIDE {data_stream_stride}u\n")
    out.append(f"#define CONFIG_DATA_STREAM_REGION_REPS {data_stream_region_reps}u\n")
    out.append(f"#define CONFIG_DATA_STREAM_POS {data_stream_pos}u\n")

    out.append(f"#define CONFIG_DATA_POINTER_CHASE_PAGE_COUNT {data_pointer_chase_pages}u\n")
    out.append(f"#define CONFIG_DATA_POINTER_CHASE_LINES_PER_PAGE {data_pointer_chase_lines_per_page}u\n")
    out.append(f"#define CONFIG_DATA_POINTER_CHASE_NODE_COUNT {len(data_pointer_chase_offsets)}u\n")
    out.append(f"#define CONFIG_DATA_POINTER_CHASE_POOL_BYTES {data_pointer_chase_pages * 4096}u\n")
    out.append(f"#define CONFIG_DATA_POINTER_CHASE_REGION_REPS {data_pointer_chase_region_reps}u\n")
    out.append(f"#define CONFIG_DATA_POINTER_CHASE_POS {data_pointer_chase_pos}u\n")

    out.append(f"#define CONFIG_DATA_PAGE_STRIDE_PAGE_COUNT {data_page_stride_pages}u\n")
    out.append(f"#define CONFIG_DATA_PAGE_STRIDE_PAGE_STRIDE {data_page_stride_page_stride}u\n")
    out.append(f"#define CONFIG_DATA_PAGE_STRIDE_LINE_INDEX {data_page_stride_line_index}u\n")
    out.append(f"#define CONFIG_DATA_PAGE_STRIDE_OFFSET_COUNT {len(data_page_stride_offsets)}u\n")
    out.append(f"#define CONFIG_DATA_PAGE_STRIDE_POOL_BYTES {data_page_stride_pages * 4096}u\n")
    out.append(f"#define CONFIG_DATA_PAGE_STRIDE_REGION_REPS {data_page_stride_region_reps}u\n")
    out.append(f"#define CONFIG_DATA_PAGE_STRIDE_POS {data_page_stride_pos}u\n")

    out.append(f"#define CONFIG_DATA_INDIRECT_GATHER_PAGE_COUNT {data_indirect_gather_pages}u\n")
    out.append(f"#define CONFIG_DATA_INDIRECT_GATHER_LINES_PER_PAGE {data_indirect_gather_lines_per_page}u\n")
    out.append(f"#define CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT {data_indirect_gather_node_count}u\n")
    out.append(f"#define CONFIG_DATA_INDIRECT_GATHER_POOL_BYTES {data_indirect_gather_pages * 4096}u\n")
    out.append(f"#define CONFIG_DATA_INDIRECT_GATHER_INDEX_STRIDE {data_indirect_gather_index_stride}u\n")
    out.append(f"#define CONFIG_DATA_INDIRECT_GATHER_REGION_REPS {data_indirect_gather_region_reps}u\n")
    out.append(f"#define CONFIG_DATA_INDIRECT_GATHER_POS {data_indirect_gather_pos}u\n")

    out.append(f"#define CONFIG_DATA_HOT_STRIDE_ACCESS_COUNT {data_hot_stride_access_count}u\n")
    out.append(f"#define CONFIG_DATA_HOT_STRIDE_STRIDE {data_hot_stride_stride}u\n")
    out.append(f"#define CONFIG_DATA_HOT_STRIDE_BUFFER_BYTES {data_hot_stride_buffer_bytes}u\n")
    out.append(f"#define CONFIG_DATA_HOT_STRIDE_REGION_REPS {data_hot_stride_region_reps}u\n")
    out.append(f"#define CONFIG_DATA_HOT_STRIDE_POS {data_hot_stride_pos}u\n")

    out.append(f"#define CONFIG_DATA_COLD_STRIDE_ACCESS_COUNT {data_cold_stride_access_count}u\n")
    out.append(f"#define CONFIG_DATA_COLD_STRIDE_STRIDE {data_cold_stride_stride}u\n")
    out.append(f"#define CONFIG_DATA_COLD_STRIDE_BUFFER_BYTES {data_cold_stride_buffer_bytes}u\n")
    out.append(f"#define CONFIG_DATA_COLD_STRIDE_REGION_REPS {data_cold_stride_region_reps}u\n")
    out.append(f"#define CONFIG_DATA_COLD_STRIDE_POS {data_cold_stride_pos}u\n")

    out.append(f"#define CONFIG_DATA_TLB_INDIRECT_PAGE_COUNT {data_tlb_indirect_pages}u\n")
    out.append(f"#define CONFIG_DATA_TLB_INDIRECT_LINE_INDEX {data_tlb_indirect_line_index}u\n")
    out.append(f"#define CONFIG_DATA_TLB_INDIRECT_ACCESS_COUNT {data_tlb_indirect_access_count}u\n")
    out.append(f"#define CONFIG_DATA_TLB_INDIRECT_POOL_BYTES {data_tlb_indirect_pool_bytes}u\n")
    out.append(f"#define CONFIG_DATA_TLB_INDIRECT_REGION_REPS {data_tlb_indirect_region_reps}u\n")
    out.append(f"#define CONFIG_DATA_TLB_INDIRECT_POS {data_tlb_indirect_pos}u\n")

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
    out.append(f"#define CONFIG_MIXED_REGION_LOADS_PER_CALL {mixed_region_loads_per_call}u\n")
    out.append(f"#define CONFIG_MIXED_REGION_ACCESSES_PER_ITER {mixed_region_accesses_per_iter}u\n")
    for slot in mixed_region_slots[1:]:
        out.append(f"#define CONFIG_MIXED_REGION_{slot['slot_id']}_LOADS_PER_CALL {slot['loads_per_call']}u\n")
    out.append(f"#define CONFIG_DATA_STREAM_ACCESSES_PER_CALL {data_stream_accesses_per_call}u\n")
    out.append(f"#define CONFIG_DATA_STREAM_ACCESSES_PER_ITER {data_stream_accesses_per_iter}u\n")
    out.append(f"#define CONFIG_DATA_POINTER_CHASE_NODES {data_pointer_chase_nodes}u\n")
    out.append(f"#define CONFIG_DATA_POINTER_CHASE_ACCESSES_PER_ITER {data_pointer_chase_accesses_per_iter}u\n")
    out.append(f"#define CONFIG_DATA_PAGE_STRIDE_ACCESSES_PER_CALL {data_page_stride_accesses_per_call}u\n")
    out.append(f"#define CONFIG_DATA_PAGE_STRIDE_ACCESSES_PER_ITER {data_page_stride_accesses_per_iter}u\n")
    out.append(f"#define CONFIG_DATA_INDIRECT_GATHER_NODES {data_indirect_gather_node_count}u\n")
    out.append(f"#define CONFIG_DATA_INDIRECT_GATHER_ACCESSES_PER_ITER {data_indirect_gather_accesses_per_iter}u\n")
    out.append(f"#define CONFIG_DATA_HOT_STRIDE_ACCESSES_PER_CALL {data_hot_stride_access_count}u\n")
    out.append(f"#define CONFIG_DATA_HOT_STRIDE_ACCESSES_PER_ITER {data_hot_stride_accesses_per_iter}u\n")
    out.append(f"#define CONFIG_DATA_COLD_STRIDE_ACCESSES_PER_CALL {data_cold_stride_access_count}u\n")
    out.append(f"#define CONFIG_DATA_COLD_STRIDE_ACCESSES_PER_ITER {data_cold_stride_accesses_per_iter}u\n")
    out.append(f"#define CONFIG_DATA_TLB_INDIRECT_ACCESSES_PER_CALL {data_tlb_indirect_access_count}u\n")
    out.append(f"#define CONFIG_DATA_TLB_INDIRECT_ACCESSES_PER_ITER {data_tlb_indirect_accesses_per_iter}u\n")
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
    out.append(format_u32_array("kMixedRegionOffsets", mixed_region_offsets))
    for slot in mixed_region_slots[1:]:
        out.append(format_u32_array(f"kMixedRegion{slot['slot_id']}Offsets", slot["offsets"]))
    out.append(format_u32_array("kDataPointerChaseOffsets", data_pointer_chase_offsets))
    out.append(format_u32_array("kDataPageStrideOffsets", data_page_stride_offsets))
    out.append(format_u32_array("kDataIndirectGatherOffsets", data_indirect_gather_offsets))
    out.append(format_u32_array("kDataHotStrideOffsets", data_hot_stride_offsets))
    out.append(format_u32_array("kDataColdStrideOffsets", data_cold_stride_offsets))
    out.append(format_u32_array("kDataTlbIndirectOffsets", data_tlb_indirect_offsets))

    out.append(MIXED_REGION.emit_storage("mixed_region", "CONFIG_MIXED_REGION_POOL_BYTES"))
    for slot in mixed_region_slots[1:]:
        out.append(
            MIXED_REGION.emit_storage(
                slot["prefix"],
                f"CONFIG_MIXED_REGION_{slot['slot_id']}_POOL_BYTES",
            )
        )
    out.append(MODULES.data_stream.emit_stream_storage("data_stream", "CONFIG_DATA_STREAM_SIZE"))
    out.append(
        MODULES.data_pointer_chase.emit_pointer_chase_storage(
            "data_pointer_chase",
            "CONFIG_DATA_POINTER_CHASE_POOL_BYTES",
        )
    )
    out.append(
        MODULES.data_page_stride.emit_stream_storage(
            "data_page_stride",
            "CONFIG_DATA_PAGE_STRIDE_POOL_BYTES",
            align=4096,
        )
    )
    out.append(
        MODULES.data_indirect_gather.emit_indirect_gather_storage(
            "data_indirect_gather",
            "CONFIG_DATA_INDIRECT_GATHER_POOL_BYTES",
            "CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT",
        )
    )
    out.append(MODULES.data_hot_stride.emit_stream_storage("data_hot_stride", "CONFIG_DATA_HOT_STRIDE_BUFFER_BYTES"))
    out.append(
        MODULES.data_cold_stride.emit_stream_storage(
            "data_cold_stride",
            "CONFIG_DATA_COLD_STRIDE_BUFFER_BYTES",
            align=4096,
        )
    )
    out.append(
        MODULES.data_tlb_indirect.emit_stream_storage(
            "data_tlb_indirect",
            "CONFIG_DATA_TLB_INDIRECT_POOL_BYTES",
            align=4096,
        )
    )

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
    out.append(
        MIXED_REGION.emit_init_function(
            "mixed_region",
            "kMixedRegionOffsets",
            "CONFIG_MIXED_REGION_NODE_COUNT",
        )
    )
    for slot in mixed_region_slots[1:]:
        out.append(
            MIXED_REGION.emit_init_function(
                slot["prefix"],
                f"kMixedRegion{slot['slot_id']}Offsets",
                f"CONFIG_MIXED_REGION_{slot['slot_id']}_NODE_COUNT",
            )
        )
    out.append(
        MIXED_REGION.emit_region_function(
            "mixed_region",
            mixed_region_size,
            mixed_region_ldr_count_per_unit,
        )
    )
    for slot in mixed_region_slots[1:]:
        out.append(
            MIXED_REGION.emit_region_function(
                slot["prefix"],
                slot["size"],
                slot["ldr_count_per_unit"],
            )
        )
    out.append(
        MODULES.data_stream.emit_stream_init_function(
            "data_stream",
            "CONFIG_DATA_STREAM_SIZE",
            "CONFIG_SEED",
        )
    )
    out.append(
        MODULES.data_stream.emit_stream_function(
            "data_stream",
            "CONFIG_DATA_STREAM_SIZE",
            "CONFIG_DATA_STREAM_STRIDE",
        )
    )
    out.append(
        MODULES.data_pointer_chase.emit_pointer_chase_init_function(
            "data_pointer_chase",
            "kDataPointerChaseOffsets",
            "CONFIG_DATA_POINTER_CHASE_NODE_COUNT",
            "CONFIG_SEED",
        )
    )
    out.append(
        MODULES.data_pointer_chase.emit_pointer_chase_function(
            "data_pointer_chase",
            "CONFIG_DATA_POINTER_CHASE_NODE_COUNT",
        )
    )
    out.append(
        MODULES.data_page_stride.emit_stream_init_function(
            "data_page_stride",
            "CONFIG_DATA_PAGE_STRIDE_POOL_BYTES",
            "CONFIG_SEED",
        )
    )
    out.append(
        MODULES.data_page_stride.emit_offset_gather_function(
            "data_page_stride",
            "kDataPageStrideOffsets",
            "CONFIG_DATA_PAGE_STRIDE_OFFSET_COUNT",
        )
    )
    out.append(
        MODULES.data_indirect_gather.emit_indirect_gather_init_function(
            "data_indirect_gather",
            "kDataIndirectGatherOffsets",
            "CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT",
            "CONFIG_DATA_INDIRECT_GATHER_POOL_BYTES",
            "CONFIG_DATA_INDIRECT_GATHER_INDEX_STRIDE",
            "CONFIG_SEED",
        )
    )
    out.append(
        MODULES.data_indirect_gather.emit_indirect_gather_function(
            "data_indirect_gather",
            "CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT",
        )
    )
    out.append(
        MODULES.data_hot_stride.emit_stream_init_function(
            "data_hot_stride",
            "CONFIG_DATA_HOT_STRIDE_BUFFER_BYTES",
            "CONFIG_SEED",
        )
    )
    out.append(
        MODULES.data_hot_stride.emit_offset_cycle_function(
            "data_hot_stride",
            "kDataHotStrideOffsets",
            "CONFIG_DATA_HOT_STRIDE_ACCESS_COUNT",
        )
    )
    out.append(
        MODULES.data_cold_stride.emit_stream_init_function(
            "data_cold_stride",
            "CONFIG_DATA_COLD_STRIDE_BUFFER_BYTES",
            "CONFIG_SEED",
        )
    )
    out.append(
        MODULES.data_cold_stride.emit_offset_cycle_function(
            "data_cold_stride",
            "kDataColdStrideOffsets",
            "CONFIG_DATA_COLD_STRIDE_ACCESS_COUNT",
        )
    )
    out.append(
        MODULES.data_tlb_indirect.emit_stream_init_function(
            "data_tlb_indirect",
            "CONFIG_DATA_TLB_INDIRECT_POOL_BYTES",
            "CONFIG_SEED",
        )
    )
    out.append(
        MODULES.data_tlb_indirect.emit_offset_cycle_function(
            "data_tlb_indirect",
            "kDataTlbIndirectOffsets",
            "CONFIG_DATA_TLB_INDIRECT_ACCESS_COUNT",
        )
    )

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
    out.append("static void run_hot_l1_once(void) {\n")
    if hot_l1_size > 0:
        out.append("    hot_l1_blob();\n")
    out.append("}\n\n")

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_hot_l2_once(void) {\n")
    if hot_l2_size > 0:
        out.append("    hot_l2_blob();\n")
    out.append("}\n\n")

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_mixed_region_once(void) {\n")
    if mixed_region_size > 0 and mixed_region_pages > 0:
        out.append("    mixed_region_kernel();\n")
    out.append("}\n\n")
    for slot in mixed_region_slots[1:]:
        out.append("__attribute__((used, noinline))\n")
        out.append(f"static void run_mixed_region_{slot['slot_id']}_once(void) {{\n")
        if slot["size"] > 0 and slot["pages"] > 0:
            out.append(f"    {slot['prefix']}_kernel();\n")
        out.append("}\n\n")

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_fetch_amplifier_once(void) {\n")
    if fetch_total_blocks > 0:
        out.append("    ((bench_func_t)g_fetch_table[0])();\n")
    out.append("}\n\n")

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_data_stream_once(void) {\n")
    if data_stream_size > 0:
        out.append("    data_stream_kernel();\n")
    out.append("}\n\n")

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_data_pointer_chase_once(void) {\n")
    if data_pointer_chase_pages > 0:
        out.append("    data_pointer_chase_kernel();\n")
    out.append("}\n\n")

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_data_page_stride_once(void) {\n")
    if data_page_stride_pages > 0:
        out.append("    data_page_stride_kernel();\n")
    out.append("}\n\n")

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_data_indirect_gather_once(void) {\n")
    if data_indirect_gather_pages > 0:
        out.append("    data_indirect_gather_kernel();\n")
    out.append("}\n\n")

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_data_hot_stride_once(void) {\n")
    if data_hot_stride_access_count > 0:
        out.append("    data_hot_stride_kernel();\n")
    out.append("}\n\n")

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_data_cold_stride_once(void) {\n")
    if data_cold_stride_access_count > 0:
        out.append("    data_cold_stride_kernel();\n")
    out.append("}\n\n")

    out.append("__attribute__((used, noinline))\n")
    out.append("static void run_data_tlb_indirect_once(void) {\n")
    if data_tlb_indirect_pages > 0:
        out.append("    data_tlb_indirect_kernel();\n")
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

    if mixed_region_size > 0 and mixed_region_pages > 0:
        out.append("    init_mixed_region_pool();\n")
    for slot in mixed_region_slots[1:]:
        if slot["size"] > 0 and slot["pages"] > 0:
            out.append(f"    init_{slot['prefix']}_pool();\n")
    if data_stream_size > 0:
        out.append("    init_data_stream_buffer();\n")
    if data_pointer_chase_pages > 0:
        out.append("    init_data_pointer_chase_pool();\n")
    if data_page_stride_pages > 0:
        out.append("    init_data_page_stride_buffer();\n")
    if data_indirect_gather_pages > 0:
        out.append("    init_data_indirect_gather_pool();\n")
    if data_hot_stride_access_count > 0:
        out.append("    init_data_hot_stride_buffer();\n")
    if data_cold_stride_access_count > 0:
        out.append("    init_data_cold_stride_buffer();\n")
    if data_tlb_indirect_pages > 0:
        out.append("    init_data_tlb_indirect_buffer();\n")
    if (
        mixed_region_enabled
        or data_stream_size > 0
        or data_pointer_chase_pages > 0
        or data_page_stride_pages > 0
        or data_indirect_gather_pages > 0
        or data_hot_stride_access_count > 0
        or data_cold_stride_access_count > 0
        or data_tlb_indirect_pages > 0
    ):
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
    mixed_region_extra_slots = [
        {
            "size": int(cfg.get(f"mixed_region_loop_{slot_id}_size", 0)),
            "ldr_count_per_unit": int(cfg.get(f"mixed_region_loop_{slot_id}_ldr_count_per_unit", 0)),
            "data_mode": str(cfg.get(f"mixed_region_loop_{slot_id}_data_mode", "linear")),
            "pages": int(cfg.get(f"mixed_region_loop_{slot_id}_pages", 1)),
            "lines_per_page": int(cfg.get(f"mixed_region_loop_{slot_id}_lines_per_page", 8)),
            "region_reps": int(cfg.get(f"mixed_region_loop_{slot_id}_region_reps", 0)),
            "pos": int(cfg.get(f"mixed_region_loop_{slot_id}_pos", 2 + slot_id)),
        }
        for slot_id in range(1, 7)
    ]
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
        mixed_region_size=int(cfg.get("mixed_region_loop_size", 0)),
        mixed_region_ldr_count_per_unit=int(cfg.get("mixed_region_loop_ldr_count_per_unit", 0)),
        mixed_region_data_mode=str(cfg.get("mixed_region_loop_data_mode", "linear")),
        mixed_region_pages=int(cfg.get("mixed_region_loop_pages", 1)),
        mixed_region_lines_per_page=int(cfg.get("mixed_region_loop_lines_per_page", 8)),
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
