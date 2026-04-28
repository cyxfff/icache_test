#!/usr/bin/env python3

import sys
from pathlib import Path

if __package__ in (None, "", "test"):
    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    if str(PROJECT_ROOT) not in sys.path:
        sys.path.insert(0, str(PROJECT_ROOT))
    from config import MIXED_REGION_SLOT_COUNT, build_base_cfg, build_knobs, METRIC_KEYS
else:
    from ..config import MIXED_REGION_SLOT_COUNT, build_base_cfg, build_knobs, METRIC_KEYS


def make_case(label, module, **params):
    return {
        "label": label,
        "module": module,
        "params": params,
    }


def alias_cases(cases, module_name, label_prefix):
    return [
        {
            "label": f"{label_prefix}_{case['label']}",
            "module": module_name,
            "params": dict(case["params"]),
        }
        for case in cases
    ]


COLD_BLOCK_SEQUENCE_BLOCKS = list(range(1000, 20001, 1000))
COLD_BLOCK_SEQUENCE_DIRECT_RUN_LENS = [1, 2, 4, 8, 16]
COLD_BLOCK_SEQUENCE_LAYOUTS = [
    ("linear", "linear"),
    ("in_page_shuffle", "bitrev"),
    # ("full_shuffle", "shuffle"),
]

HOT_REGION_LOOP_SIZES = [4096, 8192]
# HOT_REGION_LOOP_REPS = [128, 256, 512, 1024, 2048, 4096, 8192]
HOT_REGION_LOOP_REPS = [1000]
HOT_REGION_LOOP_BRANCH_PAIRS = [0, 1, 2, 3, 4]

MIXED_REGION_LOOP_SIZES = [4096, 8192]
MIXED_REGION_LOOP_LDR_COUNTS = [1, 2, 4, 7, 14]
MIXED_REGION_LOOP_MODES = [
    ("linear", "lin"),
    ("page_shuffle", "pshuf"),
    ("cross_page", "xpage"),
    ("indirect", "indir"),
]
MIXED_REGION_LOOP_PAGES = [1, 128, 512]
MIXED_REGION_LOOP_LINES_PER_PAGE = [1, 4]
MIXED_REGION_LOOP_REGION_REPS = [1000]

DATA_STREAM_SIZES = [8 * 1024, 64 * 1024, 512 * 1024, 4 * 1024 * 1024]
DATA_STREAM_STRIDES = [64, 256, 4096]
DATA_STREAM_REGION_REPS = [16]

DATA_POINTER_CHASE_PAGES = [32, 128, 512, 2048]
DATA_POINTER_CHASE_LINES_PER_PAGE = [1, 4]
DATA_POINTER_CHASE_REGION_REPS = [16]

DATA_PAGE_STRIDE_PAGES = [32, 128, 512, 2048]
DATA_PAGE_STRIDE_PAGE_STRIDES = [1, 17]
DATA_PAGE_STRIDE_LINE_INDICES = [0, 7]
DATA_PAGE_STRIDE_REGION_REPS = [16]

DATA_INDIRECT_GATHER_PAGES = [32, 128, 512, 2048]
DATA_INDIRECT_GATHER_LINES_PER_PAGE = [1, 4]
DATA_INDIRECT_GATHER_INDEX_STRIDES = [1, 5]
DATA_INDIRECT_GATHER_REGION_REPS = [16]

DATA_HOT_STRIDE_ACCESS_COUNTS = [64, 128]
DATA_HOT_STRIDE_STRIDES = [4, 8, 16]
DATA_HOT_STRIDE_REGION_REPS = [16]

DATA_COLD_STRIDE_ACCESS_COUNTS = [1024, 4096]
DATA_COLD_STRIDE_STRIDES = [256, 4096]
DATA_COLD_STRIDE_REGION_REPS = [16]

DATA_TLB_INDIRECT_PAGES = [64, 128, 256, 512]
DATA_TLB_INDIRECT_LINE_INDICES = [0, 7]
DATA_TLB_INDIRECT_REGION_REPS = [16]

# ITLB_FUNCS = [128, 256, 512, 1024, 2048, 4096]
ITLB_FUNCS = [256, 512, 1024, 2048, 4096, 8192]
# ITLB_REGION_REPS = [1, 2, 4, 8]
ITLB_REGION_REPS = [1]
ITLB_LINES_PER_PAGE = [1, 4, 8]

FETCH_AMPLIFIER_BLOCKS = [32, 64, 128]
FETCH_AMPLIFIER_DIRECT_RUN_LENS = [1, 2, 4, 8]
FETCH_AMPLIFIER_BRANCH_PAIRS_PER_BLOCK = [0, 1, 2, 4, 6]
FETCH_AMPLIFIER_BLOCK_SLOTS = [4, 8, 16]
FETCH_AMPLIFIER_BLOCK_SLOTS_BRANCH_PAIRS = {
    4: [0, 1, 2],
    8: [0, 1, 2, 3],
    12: [0, 1, 2, 4, 6],
    16: [0, 1, 2, 4, 6],
}
FETCH_AMPLIFIER_REGION_REPS = [1000]


MODULE_CASE_GROUPS = {
    "cold_block_sequence": [
        make_case(
            f"cold_b{blocks}_d{direct_run_len}_{layout_tag}",
            "cold_block_sequence",
            blocks=blocks,
            direct_run_len=direct_run_len,
            region_reps=1,
            layout=layout_name,
        )
        for blocks in COLD_BLOCK_SEQUENCE_BLOCKS
        for direct_run_len in COLD_BLOCK_SEQUENCE_DIRECT_RUN_LENS
        for layout_name, layout_tag in COLD_BLOCK_SEQUENCE_LAYOUTS
    ],
    "hot_region_loop": [
        make_case(
            f"hot_s{size}_b{branch_pairs_per_unit}_r{region_reps}",
            "hot_region_loop",
            size=size,
            branch_pairs_per_unit=branch_pairs_per_unit,
            region_reps=region_reps,
        )
        for size in HOT_REGION_LOOP_SIZES
        for branch_pairs_per_unit in HOT_REGION_LOOP_BRANCH_PAIRS
        for region_reps in HOT_REGION_LOOP_REPS
    ],
    "mixed_region_loop": [
        make_case(
            f"mix_s{size}_l{ldr_count}_m{mode_tag}_p{pages}_lp{lines_per_page}_r{region_reps}",
            "mixed_region_loop",
            size=size,
            ldr_count_per_unit=ldr_count,
            data_mode=mode_name,
            pages=pages,
            lines_per_page=lines_per_page,
            region_reps=region_reps,
        )
        for size in MIXED_REGION_LOOP_SIZES
        for ldr_count in MIXED_REGION_LOOP_LDR_COUNTS
        for mode_name, mode_tag in MIXED_REGION_LOOP_MODES
        for pages in MIXED_REGION_LOOP_PAGES
        for lines_per_page in MIXED_REGION_LOOP_LINES_PER_PAGE
        for region_reps in MIXED_REGION_LOOP_REGION_REPS
    ],
    "data_stream": [
        make_case(
            f"dstream_s{size}_st{stride}_r{region_reps}",
            "data_stream",
            size=size,
            stride=stride,
            region_reps=region_reps,
        )
        for size in DATA_STREAM_SIZES
        for stride in DATA_STREAM_STRIDES
        for region_reps in DATA_STREAM_REGION_REPS
    ],
    "data_pointer_chase": [
        make_case(
            f"dptr_p{pages}_l{lines_per_page}_r{region_reps}",
            "data_pointer_chase",
            pages=pages,
            lines_per_page=lines_per_page,
            region_reps=region_reps,
        )
        for pages in DATA_POINTER_CHASE_PAGES
        for lines_per_page in DATA_POINTER_CHASE_LINES_PER_PAGE
        for region_reps in DATA_POINTER_CHASE_REGION_REPS
    ],
    "data_page_stride": [
        make_case(
            f"dpage_p{pages}_ps{page_stride}_li{line_index}_r{region_reps}",
            "data_page_stride",
            pages=pages,
            page_stride=page_stride,
            line_index=line_index,
            region_reps=region_reps,
        )
        for pages in DATA_PAGE_STRIDE_PAGES
        for page_stride in DATA_PAGE_STRIDE_PAGE_STRIDES
        for line_index in DATA_PAGE_STRIDE_LINE_INDICES
        for region_reps in DATA_PAGE_STRIDE_REGION_REPS
    ],
    "data_indirect_gather": [
        make_case(
            f"dgather_p{pages}_l{lines_per_page}_is{index_stride}_r{region_reps}",
            "data_indirect_gather",
            pages=pages,
            lines_per_page=lines_per_page,
            index_stride=index_stride,
            region_reps=region_reps,
        )
        for pages in DATA_INDIRECT_GATHER_PAGES
        for lines_per_page in DATA_INDIRECT_GATHER_LINES_PER_PAGE
        for index_stride in DATA_INDIRECT_GATHER_INDEX_STRIDES
        for region_reps in DATA_INDIRECT_GATHER_REGION_REPS
    ],
    "data_hot_stride": [
        make_case(
            f"dhot_a{access_count}_st{stride}_r{region_reps}",
            "data_hot_stride",
            access_count=access_count,
            stride=stride,
            region_reps=region_reps,
        )
        for access_count in DATA_HOT_STRIDE_ACCESS_COUNTS
        for stride in DATA_HOT_STRIDE_STRIDES
        for region_reps in DATA_HOT_STRIDE_REGION_REPS
    ],
    "data_cold_stride": [
        make_case(
            f"dcold_a{access_count}_st{stride}_r{region_reps}",
            "data_cold_stride",
            access_count=access_count,
            stride=stride,
            region_reps=region_reps,
        )
        for access_count in DATA_COLD_STRIDE_ACCESS_COUNTS
        for stride in DATA_COLD_STRIDE_STRIDES
        for region_reps in DATA_COLD_STRIDE_REGION_REPS
    ],
    "data_tlb_indirect": [
        make_case(
            f"dtlb_p{pages}_li{line_index}_r{region_reps}",
            "data_tlb_indirect",
            pages=pages,
            line_index=line_index,
            region_reps=region_reps,
        )
        for pages in DATA_TLB_INDIRECT_PAGES
        for line_index in DATA_TLB_INDIRECT_LINE_INDICES
        for region_reps in DATA_TLB_INDIRECT_REGION_REPS
    ],
    "fetch_amplifier": [
        make_case(
            f"fetch_b{blocks}_d{direct_run_len}_bp{branch_pairs_per_block}_s{block_slots}_r{region_reps}",
            "fetch_amplifier",
            blocks=blocks,
            direct_run_len=direct_run_len,
            branch_pairs_per_block=branch_pairs_per_block,
            block_slots=block_slots,
            region_reps=region_reps,
            layout="linear",
        )
        for blocks in FETCH_AMPLIFIER_BLOCKS
        for direct_run_len in FETCH_AMPLIFIER_DIRECT_RUN_LENS
        for block_slots in FETCH_AMPLIFIER_BLOCK_SLOTS
        for branch_pairs_per_block in FETCH_AMPLIFIER_BLOCK_SLOTS_BRANCH_PAIRS[block_slots]
        for region_reps in FETCH_AMPLIFIER_REGION_REPS
    ],
    "itlb": [
        make_case(
            f"itlb_f{funcs}_l{lines_per_page}_r{region_reps}",
            "itlb",
            funcs=funcs,
            lines_per_page=lines_per_page,
            region_reps=region_reps,
            mode="chain",
            direct_run_len=0,
        )
        for funcs in ITLB_FUNCS
        for region_reps in ITLB_REGION_REPS
        for lines_per_page in ITLB_LINES_PER_PAGE
    ],
}


INSTRUCTION_MODULE_CASE_GROUPS = {
    "cold_block_sequence": MODULE_CASE_GROUPS["cold_block_sequence"],
    "hot_region_loop": MODULE_CASE_GROUPS["hot_region_loop"],
    "fetch_amplifier": MODULE_CASE_GROUPS["fetch_amplifier"],
    "itlb": MODULE_CASE_GROUPS["itlb"],
}

# 主线 data 模块：和 icache 侧一样，强调 hot / cold / tlb 三类行为。
ACTIVE_DATA_MODULE_CASE_GROUPS = {
    "data_hot_stride": MODULE_CASE_GROUPS["data_hot_stride"],
    "data_cold_stride": MODULE_CASE_GROUPS["data_cold_stride"],
    "data_tlb_indirect": MODULE_CASE_GROUPS["data_tlb_indirect"],
}

# 旧 data 模块保留做历史对照和单独实验，不再作为默认主线命名。
LEGACY_DATA_MODULE_CASE_GROUPS = {
    "data_stream": MODULE_CASE_GROUPS["data_stream"],
    "data_pointer_chase": MODULE_CASE_GROUPS["data_pointer_chase"],
    "data_page_stride": MODULE_CASE_GROUPS["data_page_stride"],
    "data_indirect_gather": MODULE_CASE_GROUPS["data_indirect_gather"],
}

MERGE_MODULE_CASE_GROUPS = {
    "mixed_region_loop": MODULE_CASE_GROUPS["mixed_region_loop"],
}

ACTIVE_MODULE_CASE_GROUPS = {
    **INSTRUCTION_MODULE_CASE_GROUPS,
    **ACTIVE_DATA_MODULE_CASE_GROUPS,
    **MERGE_MODULE_CASE_GROUPS,
}

COMBO_MODULE_CASE_GROUPS = {
    ("mixed_region_loop" if slot_id == 0 else f"mixed_region_loop_{slot_id}"): alias_cases(
        MODULE_CASE_GROUPS["mixed_region_loop"],
        "mixed_region_loop" if slot_id == 0 else f"mixed_region_loop_{slot_id}",
        f"mixslot{slot_id}",
    )
    for slot_id in range(MIXED_REGION_SLOT_COUNT)
}

DCACHE_MODULE_CASE_GROUPS = ACTIVE_DATA_MODULE_CASE_GROUPS


def flatten_case_groups(case_groups):
    cases = []
    for module_name, module_cases in case_groups.items():
        for case in module_cases:
            if case["module"] != module_name:
                raise ValueError(f"case {case['label']} declared under {module_name} but targets {case['module']}")
            cases.append(case)
    return cases


MODULE_LIBRARY_SUITE = {
    "name": "module_library",
    "artifact_stem": "module_library",
    "csv_name": "module_library.csv",
    "cases": flatten_case_groups(MODULE_CASE_GROUPS),
}


RANDOM_COMBO_SUITE = {
    "name": "combo_linearity",
    "artifact_stem": "combo_linearity_probe",
    "csv_name": "combo_linearity.csv",
    "module_case_groups": COMBO_MODULE_CASE_GROUPS,
    "combo_sizes": [2, 3, 4, 5, 6, 7],
    "total_groups": 100,
    "shuffle_rounds": 1,
}


DCACHE_LIBRARY_SUITE = {
    "name": "dcache_library",
    "artifact_stem": "dcache_library",
    "csv_name": "dcache_library.csv",
    "cases": flatten_case_groups(DCACHE_MODULE_CASE_GROUPS),
}


DCACHE_LINEARITY_SUITE = {
    "name": "dcache_linearity",
    "artifact_stem": "dcache_linearity_probe",
    "csv_name": "dcache_linearity.csv",
    "module_case_groups": DCACHE_MODULE_CASE_GROUPS,
    "combo_sizes": [2, 3],
    "samples_per_size": 12,
    "shuffle_rounds": 1,
}


TEST_RUNS = [
    {
        "kind": "random_combo_suite",
        "config": RANDOM_COMBO_SUITE,
    },
]


ACTIVE_RUNS = TEST_RUNS
