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


# v2 is merge-only. Each case is a direct instruction+data fused template:
# a code region with evenly spaced pointer-chasing ldr instructions.
MIXED_REGION_LOOP_SIZES = [4096, 8192]
MIXED_REGION_LOOP_LDR_COUNTS = [1, 2, 4, 7, 14]
MIXED_REGION_LOOP_MODES = [
    ("linear", "lin"),
    ("page_shuffle", "pshuf"),
    ("cross_page", "xpage"),
    ("indirect", "indir"),
]
MIXED_REGION_LOOP_MAX_DATA_BYTES = 2 * 1024 * 1024 * 1024
MIXED_REGION_LOOP_MAX_PAGES = MIXED_REGION_LOOP_MAX_DATA_BYTES // 4096
MIXED_REGION_LOOP_PAGES = [1, 128, 512, MIXED_REGION_LOOP_MAX_PAGES]
MIXED_REGION_LOOP_LINES_PER_PAGE = [1, 4]
MIXED_REGION_LOOP_REGION_REPS = [1000]


MERGE_MODULE_CASE_GROUPS = {
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
}


MODULE_CASE_GROUPS = MERGE_MODULE_CASE_GROUPS
ACTIVE_MODULE_CASE_GROUPS = MERGE_MODULE_CASE_GROUPS


COMBO_MODULE_CASE_GROUPS = {
    ("mixed_region_loop" if slot_id == 0 else f"mixed_region_loop_{slot_id}"): alias_cases(
        MERGE_MODULE_CASE_GROUPS["mixed_region_loop"],
        "mixed_region_loop" if slot_id == 0 else f"mixed_region_loop_{slot_id}",
        f"mixslot{slot_id}",
    )
    for slot_id in range(MIXED_REGION_SLOT_COUNT)
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
    "name": "merge_module_library",
    "artifact_stem": "merge_module_library",
    "csv_name": "merge_module_library.csv",
    "cases": flatten_case_groups(MERGE_MODULE_CASE_GROUPS),
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


TEST_RUNS = [
    {
        "kind": "random_combo_suite",
        "config": RANDOM_COMBO_SUITE,
    },
]


ACTIVE_RUNS = TEST_RUNS
