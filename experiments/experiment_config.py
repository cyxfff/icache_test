#!/usr/bin/env python3

import sys
from pathlib import Path

if __package__ in (None, "", "test", "experiments"):
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


def alias_cases(cases, module_name, label_prefix):
    return [
        {
            "label": f"{label_prefix}_{case['label']}",
            "module": module_name,
            "params": dict(case["params"]),
        }
        for case in cases
    ]


def case_signature(case):
    params = case.get("params", {})
    return (
        case.get("module"),
        tuple(sorted(params.items())),
    )


ATTACHED_NODE_BYTES = 8
ATTACHED_PAGE_BYTES = 4096
ATTACHED_MAX_NODES_PER_PAGE = ATTACHED_PAGE_BYTES // ATTACHED_NODE_BYTES


def attached_pages_from_pool_nodes(pool_nodes, nodes_per_page):
    pool_nodes = max(0, int(pool_nodes))
    if pool_nodes == 0:
        return 0
    nodes_per_page = max(1, min(ATTACHED_MAX_NODES_PER_PAGE, int(nodes_per_page)))
    return (pool_nodes + nodes_per_page - 1) // nodes_per_page


def bytes_to_nodes(size_bytes):
    return max(0, int(size_bytes) // ATTACHED_NODE_BYTES)


def bytes_to_pages(size_bytes):
    return max(0, (int(size_bytes) + ATTACHED_PAGE_BYTES - 1) // ATTACHED_PAGE_BYTES)


def attached_pool_nodes(case_or_params):
    params = case_or_params.get("params", case_or_params)
    pool_nodes = int(params.get("data_pool_nodes", 0) or 0)
    if pool_nodes > 0:
        return pool_nodes
    pages = int(params.get("data_pages", params.get("pages", 0)) or 0)
    nodes_per_page = int(params.get("data_nodes_per_page", params.get("nodes_per_page", params.get("lines_per_page", 0))) or 0)
    return pages * nodes_per_page


def attached_pages(case_or_params):
    params = case_or_params.get("params", case_or_params)
    pages = int(params.get("data_pages", params.get("pages", 0)) or 0)
    if pages > 0:
        return pages
    return attached_pages_from_pool_nodes(
        attached_pool_nodes(params),
        params.get("data_nodes_per_page", params.get("nodes_per_page", params.get("lines_per_page", 1))),
    )


def is_low_risk_linearity_case(case):
    params = case.get("params", {})
    pages = attached_pages(params)
    nodes_per_page = int(params.get("data_nodes_per_page", params.get("nodes_per_page", params.get("lines_per_page", 0))) or 0)
    data_mode = str(params.get("data_mode", ""))

    if pages > 512:
        return False
    # Allow a small set of page footprints that map to the dense hot/L2 and DTLB families.
    if pages not in (0, 1, 8, 16, 32) and 1 < pages < 128:
        return False
    # For pages=512 np>4 creates a 128 KB+ per-module working set; the combo
    # ws cap handles pages=128 with np=8 (64 KB/module) safely.
    if pages >= 512 and nodes_per_page > 4:
        return False
    if pages == 1 and data_mode in {"random", "page_stride"}:
        return False
    return True


def is_low_risk_linearity_combo(cases):
    signatures = [case_signature(case) for case in cases]
    if len(set(signatures)) != len(signatures):
        return False

    hot_page_cases = 0
    total_pool_nodes = 0
    for case in cases:
        if not is_low_risk_linearity_case(case):
            return False
        params = case.get("params", {})
        pages = attached_pages(params)
        total_pool_nodes += attached_pool_nodes(params)
        if pages == 1:
            hot_page_cases += 1

    if hot_page_cases > 1:
        return False
    # Keep the unique node working set within ~256 KB for the "safe" pool.
    if total_pool_nodes * ATTACHED_NODE_BYTES > 256 * 1024:
        return False
    return True


def is_safe_itlb_case(case):
    if case.get("module") != "itlb":
        return True
    params = case.get("params", {})
    return int(params.get("funcs", 0) or 0) in {256, 512, 1024, 2048, 4096}


ATTACHED_LDR_PER_UNIT = [0,1,2,3,4]
# ATTACHED_LDR_PER_UNIT = [1]
ATTACHED_REGION_REPS = [1000]
ATTACHED_HOT_NODE_STRIDES = [1]
ATTACHED_COLD_NODE_STRIDES = [1, 4, 8, 16]
ATTACHED_DTLB_PAGE_STRIDES = [1]
ATTACHED_DENSE_NODES_PER_PAGE = ATTACHED_MAX_NODES_PER_PAGE
ATTACHED_DTLB_NODES_PER_PAGE = [1]

ATTACHED_HOT_POOL_BYTES = [
    # ("2k", 2 * 1024),
    ("4k", 4 * 1024),
    ("16k", 8 * 1024),
]
ATTACHED_COLD_POOL_BYTES = [
    ("128k", 128 * 1024),
    ("512k", 512 * 1024),
    ("1m", 1 * 1024 * 1024),
]
ATTACHED_DTLB_POOL_BYTES = [
    ("128m", 128 * 1024 * 1024),
    # ("512m", 512 * 1024 * 1024),
]

ATTACHED_DATA_TEMPLATE_FAMILIES = [
    {
        "name": "hot",
        "tag": "hot",
        "pool_byte_levels": ATTACHED_HOT_POOL_BYTES,
        "modes": [("node_stride", "ns"), ("random", "rnd")],
        "nodes_per_page": [ATTACHED_DENSE_NODES_PER_PAGE],
        "stride_nodes": ATTACHED_HOT_NODE_STRIDES,
    },
    {
        "name": "cold",
        "tag": "cold",
        "pool_byte_levels": ATTACHED_COLD_POOL_BYTES,
        "modes": [("node_stride", "ns"), ("random", "rnd")],
        "nodes_per_page": [ATTACHED_DENSE_NODES_PER_PAGE],
        "stride_nodes": ATTACHED_COLD_NODE_STRIDES,
    },
    {
        "name": "dtlb",
        "tag": "dtlb",
        "pool_byte_levels": ATTACHED_DTLB_POOL_BYTES,
        "modes": [("page_stride", "ps"), ("random", "rnd")],
        "nodes_per_page": ATTACHED_DTLB_NODES_PER_PAGE,
        "stride_pages": ATTACHED_DTLB_PAGE_STRIDES,
    },
]


def _attached_base_params(template_name, level_tag, mode_name, pool_nodes, pages, nodes_per_page, ldr_per_unit, region_reps):
    return {
        "data_template": template_name,
        "data_level": level_tag,
        "data_pool_nodes": int(pool_nodes),
        "data_pages": int(pages),
        "data_nodes_per_page": int(nodes_per_page),
        "data_mode": mode_name,
        "fusion_ldr_per_unit": int(ldr_per_unit),
        "region_reps": int(region_reps),
    }


def _iter_cache_data_variants(family):
    for level_tag, pool_bytes in family["pool_byte_levels"]:
        pool_nodes = bytes_to_nodes(pool_bytes)
        for mode_name, mode_tag in family["modes"]:
            for nodes_per_page in family["nodes_per_page"]:
                pages = attached_pages_from_pool_nodes(pool_nodes, nodes_per_page)
                for ldr_per_unit in ATTACHED_LDR_PER_UNIT:
                    for region_reps in ATTACHED_REGION_REPS:
                        base_suffix = (
                            f"{family['tag']}_{level_tag}_{mode_tag}"
                            f"_n{pool_nodes}_p{pages}_np{nodes_per_page}"
                            f"_l{ldr_per_unit}_r{region_reps}"
                        )
                        base_params = _attached_base_params(
                            family["name"],
                            level_tag,
                            mode_name,
                            pool_nodes,
                            pages,
                            nodes_per_page,
                            ldr_per_unit,
                            region_reps,
                        )
                        if mode_name == "node_stride":
                            for stride in family["stride_nodes"]:
                                params = dict(base_params)
                                params["data_stride_nodes"] = int(stride)
                                params["data_stride_lines"] = int(stride)
                                yield f"{base_suffix}_sn{stride}", params
                        else:
                            yield base_suffix, dict(base_params)


def _iter_dtlb_data_variants(family):
    for level_tag, pool_bytes in family["pool_byte_levels"]:
        page_count = bytes_to_pages(pool_bytes)
        for mode_name, mode_tag in family["modes"]:
            for nodes_per_page in family["nodes_per_page"]:
                pool_nodes = int(page_count) * int(nodes_per_page)
                for ldr_per_unit in ATTACHED_LDR_PER_UNIT:
                    for region_reps in ATTACHED_REGION_REPS:
                        base_suffix = (
                            f"{family['tag']}_{level_tag}_{mode_tag}"
                            f"_n{pool_nodes}_p{page_count}_np{nodes_per_page}"
                            f"_l{ldr_per_unit}_r{region_reps}"
                        )
                        base_params = _attached_base_params(
                            family["name"],
                            level_tag,
                            mode_name,
                            pool_nodes,
                            page_count,
                            nodes_per_page,
                            ldr_per_unit,
                            region_reps,
                        )
                        if mode_name == "page_stride":
                            for stride in family["stride_pages"]:
                                params = dict(base_params)
                                params["data_stride_pages"] = int(stride)
                                yield f"{base_suffix}_sp{stride}", params
                        else:
                            yield base_suffix, dict(base_params)


def make_hot_data_variants():
    return list(_iter_cache_data_variants(ATTACHED_DATA_TEMPLATE_FAMILIES[0]))


def make_cold_data_variants():
    return list(_iter_cache_data_variants(ATTACHED_DATA_TEMPLATE_FAMILIES[1]))


def make_dtlb_data_variants():
    return list(_iter_dtlb_data_variants(ATTACHED_DATA_TEMPLATE_FAMILIES[2]))


def iter_attached_param_variants():
    for item in make_hot_data_variants():
        yield item
    for item in make_cold_data_variants():
        yield item
    for item in make_dtlb_data_variants():
        yield item


def iter_hot_instr_variants():
    for size in [4096]:
        for bp in [2, 3, 4]:
            yield f"hot_s{size}_bp{bp}", {
                "size": size,
                "branch_pairs_per_unit": bp,
            }


def iter_fetch_instr_variants():
    for blocks in [64, 128]:
        for direct_run_len in [1, 2, 4]:
            for branch_pairs_per_block in [1, 2, 4]:
                yield f"fetch_b{blocks}_d{direct_run_len}_bp{branch_pairs_per_block}_s16", {
                    "blocks": blocks,
                    "direct_run_len": direct_run_len,
                    "branch_pairs_per_block": branch_pairs_per_block,
                    "block_slots": 16,
                    "layout": "linear",
                }


def iter_main_instr_variants():
    for blocks in list(range(1000, 16001, 1500)):
        for direct_run_len in [1, 2, 4, 8]:
            # for layout in ["in_page_shuffle", "linear"]:
            for layout in ["linear"]:
                layout_tag = "bitrev" if layout == "in_page_shuffle" else "lin"
                yield f"main_b{blocks}_d{direct_run_len}_{layout_tag}", {
                    "blocks": blocks,
                    "direct_run_len": direct_run_len,
                    "layout": layout,
                }


def iter_itlb_instr_variants():
    for funcs in [512, 1024, 2048, 4096]:
        for lines_per_page in [1, 2]:
            yield f"itlb_f{funcs}_l{lines_per_page}_d0", {
                "funcs": funcs,
                "lines_per_page": lines_per_page,
                "mode": "chain",
                "direct_run_len": 0,
            }


def make_instruction_data_cases(module_name, instr_variants):
    cases = []
    data_variants = list(iter_attached_param_variants())
    for instr_label, instr_params in instr_variants:
        for data_suffix, data_params in data_variants:
            merged = dict(instr_params)
            merged.update(data_params)
            cases.append(
                make_case(
                    f"{instr_label}_{data_suffix}",
                    module_name,
                    **merged,
                )
            )
    return cases


def make_hot_region_attached_cases():
    return make_instruction_data_cases("hot_region_loop", iter_hot_instr_variants())


def make_fetch_attached_cases():
    return make_instruction_data_cases("fetch_amplifier", iter_fetch_instr_variants())


def make_main_block_attached_cases():
    return make_instruction_data_cases("cold_block_sequence", iter_main_instr_variants())


def make_itlb_attached_cases():
    return make_instruction_data_cases("itlb", iter_itlb_instr_variants())


MERGE_MODULE_CASE_GROUPS = {
    "hot_region_loop": make_hot_region_attached_cases(),
    "fetch_amplifier": make_fetch_attached_cases(),
    "cold_block_sequence": make_main_block_attached_cases(),
    "itlb": make_itlb_attached_cases(),
}


MODULE_CASE_GROUPS = MERGE_MODULE_CASE_GROUPS
ACTIVE_MODULE_CASE_GROUPS = MERGE_MODULE_CASE_GROUPS


COMBO_MODULE_CASE_GROUPS = dict(MERGE_MODULE_CASE_GROUPS)


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
    "combo_sizes": [2, 3, 4],
    "total_groups": 100,
    "shuffle_rounds": 1,
    "memory_defaults": {
        "allocator": "arena",
        "prefault": 1,
    },
}


SAFE_RANDOM_COMBO_SUITE = {
    "name": "combo_linearity_safe",
    "artifact_stem": "combo_linearity_safe_probe",
    "csv_name": "combo_linearity_safe.csv",
    "module_case_groups": {
        module_name: [
            case
            for case in module_cases
            if is_low_risk_linearity_case(case) and is_safe_itlb_case(case)
        ]
        for module_name, module_cases in COMBO_MODULE_CASE_GROUPS.items()
    },
    "combo_sizes": [2, 3, 4, 5, 6, 7],
    "total_groups": 100,
    "shuffle_rounds": 1,
    "combo_filter": is_low_risk_linearity_combo,
    "memory_defaults": {
        "allocator": "arena",
        "advice": "nohugepage",
        "prefault": 1,
    },
}


TEST_RUNS = [
    {
        "kind": "random_combo_suite",
        "config": RANDOM_COMBO_SUITE,
    },
]


ACTIVE_RUNS = TEST_RUNS
