#!/usr/bin/env python3

import sys
from pathlib import Path


if __package__ in (None, "", "test", "experiments"):
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
    "node_stride": "nstr",
    "line_stride": "nstr",
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


def _attached_data_suffix(params):
    template = str(params.get("data_template", "") or "")
    level = str(params.get("data_level", "") or "")
    pool_nodes = int(params.get("data_pool_nodes", 0) or 0)
    pages = int(params.get("data_pages", 0) or 0)
    nodes = int(params.get("data_nodes_per_page", params.get("lines_per_page", 0)) or 0)
    mode = str(params.get("data_mode", "linear"))
    mode_tag = MIXED_MODE_TAGS.get(mode, mode)
    ldr = int(params.get("fusion_ldr_per_unit", 0) or 0)

    if pages <= 0 and pool_nodes <= 0 and ldr <= 0:
        return ""

    prefix = ""
    if template:
        prefix = f"_{template}"
        if level:
            prefix += f"_{level}"

    suffix = f"{prefix}_{mode_tag}_n{pool_nodes}_p{pages}_np{nodes}_l{ldr}"
    if mode in {"node_stride", "line_stride"}:
        suffix += f"_sn{int(params.get('data_stride_nodes', params.get('data_stride_lines', params.get('stride_nodes', params.get('stride_lines', 1)))) or 1)}"
    if mode == "page_stride":
        suffix += f"_sp{int(params.get('data_stride_pages', params.get('stride_pages', 1)) or 1)}"
    return suffix


def format_case_label(module_name, params, fallback_label):
    try:
        if module_name == "cold_block_sequence":
            layout = LAYOUT_TAGS.get(params["layout"], params["layout"])
            return (
                f"cold_b{params['blocks']}_d{params['direct_run_len']}_{layout}"
                f"{_attached_data_suffix(params)}"
            )
        if module_name == "fetch_amplifier":
            return (
                f"fetch_b{params['blocks']}_d{params['direct_run_len']}"
                f"_bp{params['branch_pairs_per_block']}_s{params['block_slots']}"
                f"_r{params['region_reps']}"
                f"{_attached_data_suffix(params)}"
            )
        if module_name == "hot_region_loop":
            return (
                f"hot_b{_blocks_from_size(params['size'])}"
                f"_bp{params['branch_pairs_per_unit']}_r{params['region_reps']}"
                f"{_attached_data_suffix(params)}"
            )
        if module_name == "itlb":
            return (
                f"itlb_f{params['funcs']}_l{params['lines_per_page']}"
                f"_r{params['region_reps']}"
                f"{_attached_data_suffix(params)}"
            )
    except KeyError:
        return fallback_label
    return fallback_label


def case_label(case):
    return format_case_label(case["module"], case["params"], case["label"])


def join_case_labels(cases):
    return "+".join(case_label(case) for case in cases)
