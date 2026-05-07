#!/usr/bin/env python3

import sys
from pathlib import Path


if __package__ in (None, "", "test"):
    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    if str(PROJECT_ROOT) not in sys.path:
        sys.path.insert(0, str(PROJECT_ROOT))
    from config import DERIVED_KEYS
else:
    from ..config import DERIVED_KEYS


COUNT_TO_RATE_SEP = " "
RATE_TO_MPKI_SEP = "  "

LAYOUT_TAGS = {
    "linear": "linear",
    "in_page_shuffle": "bitrev",
    "full_shuffle": "shuffle",
}

MIXED_MODE_TAGS = {
    "linear": "lin",
    "line_stride": "lstr",
    "page_stride": "pstr",
    "line_shuffle": "lshuf",
    "random": "rand",
    "page_shuffle": "lshuf",
    "cross_page": "pstr",
    "indirect": "rand",
}


def metric_headers(metric_keys):
    miss_rate_keys = [key for key in DERIVED_KEYS if key.endswith("_miss_rate")]
    mpki_keys = [key for key in DERIVED_KEYS if key.endswith("_mpki")]
    summary_keys = [
        key
        for key in DERIVED_KEYS
        if key not in miss_rate_keys and key not in mpki_keys
    ]
    return [
        *metric_keys,
        *summary_keys,
        COUNT_TO_RATE_SEP,
        *miss_rate_keys,
        RATE_TO_MPKI_SEP,
        *mpki_keys,
    ]


def with_metric_separators(row):
    row[COUNT_TO_RATE_SEP] = ""
    row[RATE_TO_MPKI_SEP] = ""
    return row


def _blocks_from_size(size):
    if isinstance(size, int) and size % 64 == 0:
        return size // 64
    return size


def format_case_label(module_name, params, fallback_label):
    try:
        if module_name == "cold_block_sequence":
            layout = LAYOUT_TAGS.get(params["layout"], params["layout"])
            return f"cold_b{params['blocks']}_d{params['direct_run_len']}_{layout}"
        if module_name == "fetch_amplifier":
            return (
                f"fetch_b{params['blocks']}_d{params['direct_run_len']}"
                f"_bp{params['branch_pairs_per_block']}_s{params['block_slots']}"
                f"_r{params['region_reps']}"
            )
        if module_name == "hot_region_loop":
            return (
                f"hot_b{_blocks_from_size(params['size'])}"
                f"_bp{params['branch_pairs_per_unit']}_r{params['region_reps']}"
            )
        if module_name == "mixed_region_loop" or module_name.startswith("mixed_region_loop_"):
            mode = MIXED_MODE_TAGS.get(params["data_mode"], params["data_mode"])
            nodes_per_page = params.get("nodes_per_page", params.get("lines_per_page", 1))
            label = (
                f"mix_b{_blocks_from_size(params['size'])}"
                f"_ld{params['ldr_count_per_unit']}_{mode}"
                f"_p{params['pages']}_np{nodes_per_page}"
            )
            if params["data_mode"] == "line_stride":
                label += f"_sl{params.get('stride_lines', 1)}"
            if params["data_mode"] == "page_stride":
                label += f"_sp{params.get('stride_pages', 1)}"
            return f"{label}_r{params['region_reps']}"
        if module_name == "data_stream":
            return f"dstream_s{params['size']}_st{params['stride']}_r{params['region_reps']}"
        if module_name == "data_pointer_chase":
            return f"dptr_p{params['pages']}_l{params['lines_per_page']}_r{params['region_reps']}"
        if module_name == "data_page_stride":
            return (
                f"dpage_p{params['pages']}_ps{params['page_stride']}"
                f"_li{params['line_index']}_r{params['region_reps']}"
            )
        if module_name == "data_indirect_gather":
            return (
                f"dgather_p{params['pages']}_l{params['lines_per_page']}"
                f"_is{params['index_stride']}_r{params['region_reps']}"
            )
        if module_name == "data_hot_stride":
            return (
                f"dhot_a{params['access_count']}_st{params['stride']}"
                f"_r{params['region_reps']}"
            )
        if module_name == "data_cold_stride":
            return (
                f"dcold_a{params['access_count']}_st{params['stride']}"
                f"_r{params['region_reps']}"
            )
        if module_name == "data_tlb_indirect":
            return (
                f"dtlb_p{params['pages']}_li{params['line_index']}"
                f"_r{params['region_reps']}"
            )
        if module_name == "itlb":
            return (
                f"itlb_f{params['funcs']}_l{params['lines_per_page']}"
                f"_r{params['region_reps']}"
            )
    except KeyError:
        return fallback_label
    return fallback_label


def case_label(case):
    return format_case_label(case["module"], case["params"], case["label"])


def join_case_labels(cases):
    return "+".join(case_label(case) for case in cases)
