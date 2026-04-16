#!/usr/bin/env python3

import sys
from pathlib import Path

if __package__ in (None, "", "test"):
    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    if str(PROJECT_ROOT) not in sys.path:
        sys.path.insert(0, str(PROJECT_ROOT))
    from config import build_base_cfg, build_knobs, METRIC_KEYS
else:
    from ..config import build_base_cfg, build_knobs, METRIC_KEYS


def make_case(label, module, **params):
    return {
        "label": label,
        "module": module,
        "params": params,
    }


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
    "name": "random_combo",
    "artifact_stem": "random_combo_probe",
    "csv_name": "random_combo_probe.csv",
    "module_case_groups": MODULE_CASE_GROUPS,
    "combo_sizes": [2, 3, 4, 5],
    "total_groups": 10,
    "shuffle_rounds": 1,
}


TEST_RUNS = [
    {
        "kind": "case_library_suite",
        "config": MODULE_LIBRARY_SUITE,
    },
    {
        "kind": "random_combo_suite",
        "config": RANDOM_COMBO_SUITE,
    },
]


ACTIVE_RUNS = TEST_RUNS
