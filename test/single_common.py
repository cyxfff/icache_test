#!/usr/bin/env python3

import sys
from pathlib import Path


if __package__ in (None, ""):
    PARENT = Path(__file__).resolve().parents[1]
    if str(PARENT) not in sys.path:
        sys.path.insert(0, str(PARENT))
    from config import DERIVED_KEYS, METRIC_KEYS, build_base_cfg, build_knobs
    from test.runner import build_single_cfg
    from test.experiment_config import MODULE_CASE_GROUPS
    from utils import run_one, write_csv_row
else:
    from ..config import DERIVED_KEYS, METRIC_KEYS, build_base_cfg, build_knobs
    from .runner import build_single_cfg
    from .experiment_config import MODULE_CASE_GROUPS
    from ..utils import run_one, write_csv_row


MODULE_PARAM_KEYS = {
    "cold_block_sequence": [
        "blocks",
        "block_align",
        "direct_run_len",
        "region_reps",
        "layout",
        "pos",
    ],
    "fetch_amplifier": [
        "blocks",
        "block_align",
        "direct_run_len",
        "branch_pairs_per_block",
        "block_slots",
        "region_reps",
        "layout",
        "pos",
    ],
    "hot_region_loop": [
        "size",
        "branch_pairs_per_unit",
        "region_reps",
        "pos",
    ],
    "data_stream": [
        "size",
        "stride",
        "region_reps",
        "pos",
    ],
    "data_pointer_chase": [
        "pages",
        "lines_per_page",
        "region_reps",
        "pos",
    ],
    "data_page_stride": [
        "pages",
        "page_stride",
        "line_index",
        "region_reps",
        "pos",
    ],
    "data_indirect_gather": [
        "pages",
        "lines_per_page",
        "index_stride",
        "region_reps",
        "pos",
    ],
    "data_hot_stride": [
        "access_count",
        "stride",
        "region_reps",
        "pos",
    ],
    "data_cold_stride": [
        "access_count",
        "stride",
        "region_reps",
        "pos",
    ],
    "data_tlb_indirect": [
        "pages",
        "line_index",
        "region_reps",
        "pos",
    ],
    "itlb": [
        "funcs",
        "lines_per_page",
        "region_reps",
        "mode",
        "direct_run_len",
        "pos",
    ],
}


MODULE_PARAM_FIELD_MAP = {
    "cold_block_sequence": {
        "blocks": "cold_block_sequence_blocks",
        "block_align": "cold_block_sequence_block_align",
        "direct_run_len": "cold_block_sequence_direct_run_len",
        "region_reps": "cold_block_sequence_region_reps",
        "layout": "cold_block_sequence_layout",
        "pos": "cold_block_sequence_pos",
    },
    "fetch_amplifier": {
        "blocks": "fetch_amplifier_blocks",
        "block_align": "fetch_amplifier_block_align",
        "direct_run_len": "fetch_amplifier_direct_run_len",
        "branch_pairs_per_block": "fetch_amplifier_branch_pairs_per_block",
        "block_slots": "fetch_amplifier_block_slots",
        "region_reps": "fetch_amplifier_region_reps",
        "layout": "fetch_amplifier_layout",
        "pos": "fetch_amplifier_pos",
    },
    "hot_region_loop": {
        "size": "hot_region_loop_size",
        "branch_pairs_per_unit": "hot_region_loop_branch_pairs_per_unit",
        "region_reps": "hot_region_loop_region_reps",
        "pos": "hot_region_loop_pos",
    },
    "data_stream": {
        "size": "data_stream_size",
        "stride": "data_stream_stride",
        "region_reps": "data_stream_region_reps",
        "pos": "data_stream_pos",
    },
    "data_pointer_chase": {
        "pages": "data_pointer_chase_pages",
        "lines_per_page": "data_pointer_chase_lines_per_page",
        "region_reps": "data_pointer_chase_region_reps",
        "pos": "data_pointer_chase_pos",
    },
    "data_page_stride": {
        "pages": "data_page_stride_pages",
        "page_stride": "data_page_stride_page_stride",
        "line_index": "data_page_stride_line_index",
        "region_reps": "data_page_stride_region_reps",
        "pos": "data_page_stride_pos",
    },
    "data_indirect_gather": {
        "pages": "data_indirect_gather_pages",
        "lines_per_page": "data_indirect_gather_lines_per_page",
        "index_stride": "data_indirect_gather_index_stride",
        "region_reps": "data_indirect_gather_region_reps",
        "pos": "data_indirect_gather_pos",
    },
    "data_hot_stride": {
        "access_count": "data_hot_stride_access_count",
        "stride": "data_hot_stride_stride",
        "region_reps": "data_hot_stride_region_reps",
        "pos": "data_hot_stride_pos",
    },
    "data_cold_stride": {
        "access_count": "data_cold_stride_access_count",
        "stride": "data_cold_stride_stride",
        "region_reps": "data_cold_stride_region_reps",
        "pos": "data_cold_stride_pos",
    },
    "data_tlb_indirect": {
        "pages": "data_tlb_indirect_pages",
        "line_index": "data_tlb_indirect_line_index",
        "region_reps": "data_tlb_indirect_region_reps",
        "pos": "data_tlb_indirect_pos",
    },
    "itlb": {
        "funcs": "itlb_funcs",
        "lines_per_page": "itlb_lines_per_page",
        "region_reps": "itlb_region_reps",
        "mode": "itlb_mode",
        "direct_run_len": "itlb_direct_run_len",
        "pos": "itlb_pos",
    },
}


def build_row(module_name, case, measured_row):
    params = dict(case["params"])

    row = {
        "module": module_name,
        "case": case["label"],
    }
    for key in MODULE_PARAM_KEYS[module_name]:
        row[key] = params.get(key, measured_row.get(MODULE_PARAM_FIELD_MAP[module_name][key], ""))

    for key in METRIC_KEYS:
        row[key] = measured_row.get(key, "")
    for key in DERIVED_KEYS:
        row[key] = measured_row.get(key, "")
    return row


def run_modules(selected_modules):
    root = Path(__file__).resolve().parents[1]
    output_dir = root / "output"
    base_cfg = build_base_cfg()

    for module_name in selected_modules:
        if module_name not in MODULE_CASE_GROUPS:
            raise KeyError(f"unknown module: {module_name}")

        cases = MODULE_CASE_GROUPS[module_name]
        csv_out = output_dir / f"{module_name}.csv"
        headers = ["module", "case", *MODULE_PARAM_KEYS[module_name], *METRIC_KEYS, *DERIVED_KEYS]
        knobs = build_knobs(root, artifact_stem=f"single_{module_name}")

        for case in cases:
            cfg = build_single_cfg(base_cfg, case)
            row, raw_output = run_one(cfg, knobs)
            write_csv_row(csv_out, headers, build_row(module_name, case, row))
            print(f"[single_modules] module={module_name} case={case['label']}")
            print(raw_output)
