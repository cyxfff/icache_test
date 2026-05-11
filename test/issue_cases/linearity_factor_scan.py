#!/usr/bin/env python3

import argparse
import json
import statistics
import sys
from copy import deepcopy
from pathlib import Path
from typing import Dict, List

if __package__ in (None, "", "test"):
    PROJECT_ROOT = Path(__file__).resolve().parents[2]
    if str(PROJECT_ROOT) not in sys.path:
        sys.path.insert(0, str(PROJECT_ROOT))
    from config import build_base_cfg, build_knobs, zero_all_modules
    from experiments.runner import apply_module_config, set_module_order
    from utils import run_one, write_csv_row
else:
    from ...config import build_base_cfg, build_knobs, zero_all_modules
    from ...experiments.runner import apply_module_config, set_module_order
    from ...utils import run_one, write_csv_row


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan linearity-sensitive factors for issue combos using repeated runs and aggregate rel-diff stats."
    )
    parser.add_argument(
        "--config",
        default="test/issue_cases/issue_combos_dcache.json",
        help="Issue combo JSON config path.",
    )
    parser.add_argument(
        "--case-ids",
        default="combo_013_s2,combo_043_s4",
        help="Comma-separated case ids to scan.",
    )
    parser.add_argument(
        "--metrics",
        default="l2d_cache_refill:u,l1d_cache_refill:u",
        help="Comma-separated metrics to compare against the single-module sum.",
    )
    parser.add_argument(
        "--repeats",
        type=int,
        default=3,
        help="How many times to rerun each case/variant.",
    )
    parser.add_argument(
        "--iters",
        type=int,
        default=300,
        help="Benchmark iterations per run.",
    )
    parser.add_argument(
        "--rounds",
        type=int,
        default=1,
        help="Runner rounds per run.",
    )
    parser.add_argument(
        "--artifact-stem",
        default="linearity_factor_scan",
        help="Build artifact stem prefix.",
    )
    parser.add_argument(
        "--out-csv",
        default="output/linearity_factor_scan.csv",
        help="CSV output path.",
    )
    parser.add_argument(
        "--out-md",
        default="output/linearity_factor_scan.md",
        help="Markdown output path.",
    )
    parser.add_argument(
        "--include-memory-variants",
        action="store_true",
        help="Include the built-in memory-layout variants.",
    )
    parser.add_argument(
        "--page-sweep",
        action="append",
        default=[],
        help="Repeatable sweep spec, e.g. 0:1,4,16,64,128.",
    )
    parser.add_argument(
        "--nodes-sweep",
        action="append",
        default=[],
        help="Repeatable sweep spec, e.g. 0:1,2,4.",
    )
    parser.add_argument(
        "--mode-sweep",
        action="append",
        default=[],
        help="Repeatable sweep spec, e.g. 0:linear,random,page_stride.",
    )
    return parser.parse_args()


def parse_csv_list(raw: str) -> List[str]:
    return [item.strip() for item in raw.split(",") if item.strip()]


def parse_int_sweep_specs(specs: List[str], field_name: str) -> List[Dict]:
    out = []
    for spec in specs:
        slot_text, values_text = spec.split(":", 1)
        slot = int(slot_text)
        for value_text in parse_csv_list(values_text):
            out.append({"slot": slot, "field": field_name, "value": int(value_text)})
    return out


def parse_mode_sweep_specs(specs: List[str]) -> List[Dict]:
    out = []
    for spec in specs:
        slot_text, values_text = spec.split(":", 1)
        slot = int(slot_text)
        for value_text in parse_csv_list(values_text):
            out.append({"slot": slot, "field": "data_mode", "value": value_text})
    return out


def default_memory_variants() -> List[Dict]:
    return [
        {"name": "base", "order": "canonical", "memory": {}},
        {"name": "reverse", "order": "reverse", "memory": {}},
        {"name": "arena", "order": "canonical", "memory": {"allocator": "arena"}},
        {"name": "arena_hint", "order": "canonical", "memory": {"allocator": "arena", "arena_hint": 0x4000000000}},
        {"name": "arena_gap_2m", "order": "canonical", "memory": {"allocator": "arena", "arena_gap_bytes": 2 * 1024 * 1024}},
        {"name": "arena_huge_prefault", "order": "canonical", "memory": {"allocator": "arena", "advice": "hugepage", "prefault": 1}},
        {"name": "arena_nohuge_prefault", "order": "canonical", "memory": {"allocator": "arena", "advice": "nohugepage", "prefault": 1}},
        {"name": "random_advice", "order": "canonical", "memory": {"advice": "random"}},
    ]


def mutation_variants(args: argparse.Namespace) -> List[Dict]:
    variants = []
    for item in parse_int_sweep_specs(args.page_sweep, "data_pages"):
        variants.append(
            {
                "name": f"pages_s{item['slot']}_{item['value']}",
                "order": "canonical",
                "memory": {},
                "mutations": [item],
            }
        )
    for item in parse_int_sweep_specs(args.nodes_sweep, "data_nodes_per_page"):
        variants.append(
            {
                "name": f"nodes_s{item['slot']}_{item['value']}",
                "order": "canonical",
                "memory": {},
                "mutations": [item],
            }
        )
    for item in parse_mode_sweep_specs(args.mode_sweep):
        variants.append(
            {
                "name": f"mode_s{item['slot']}_{item['value']}",
                "order": "canonical",
                "memory": {},
                "mutations": [item],
            }
        )
    return variants


def build_variants(args: argparse.Namespace) -> List[Dict]:
    variants = []
    if args.include_memory_variants:
        variants.extend(default_memory_variants())
    variants.extend(mutation_variants(args))
    if not variants:
        variants.append({"name": "base", "order": "canonical", "memory": {}})
    return variants


def rel_diff(observed: float, baseline: float) -> float:
    return abs(observed - baseline) / max(1.0, abs(baseline))


def row_metric_value(row: Dict, metric: str):
    value = row.get(metric)
    if value in ("", None):
        return None
    return float(value)


def apply_memory_config(cfg: Dict, memory_overrides: Dict, args: argparse.Namespace) -> None:
    memory_cfg = cfg.setdefault("memory", {})
    memory_cfg["allocator"] = memory_overrides.get("allocator", "posix")
    memory_cfg["advice"] = memory_overrides.get("advice", "default")
    memory_cfg["arena_gap_bytes"] = memory_overrides.get("arena_gap_bytes", 0)
    memory_cfg["arena_hint"] = memory_overrides.get("arena_hint", 0)
    memory_cfg["prefault"] = memory_overrides.get("prefault", 0)
    cfg["run"]["iters"] = args.iters
    cfg["run"]["rounds"] = args.rounds


def mutate_modules(case_obj: Dict, variant: Dict) -> List[Dict]:
    modules = deepcopy(case_obj["modules"])
    for mutation in variant.get("mutations", []):
        target_slot = mutation["slot"]
        field_name = mutation["field"]
        field_value = mutation["value"]
        found = False
        for module_item in modules:
            if int(module_item.get("slot", -1)) == target_slot:
                module_item["params"][field_name] = field_value
                found = True
        if not found:
            raise KeyError(f"slot {target_slot} not found in case {case_obj['case_id']}")
    return modules


def build_cfg(base_cfg: Dict, modules: List[Dict], order: List[str], args: argparse.Namespace, variant: Dict) -> Dict:
    cfg = deepcopy(base_cfg)
    zero_all_modules(cfg)
    apply_memory_config(cfg, variant.get("memory", {}), args)
    for module_item in modules:
        module_name = module_item["module"]
        params = module_item["params"]
        if module_name not in cfg["modules"]:
            raise KeyError(f"unknown module {module_name!r}")
        apply_module_config(cfg, module_name, params)
    set_module_order(cfg, order)
    return cfg


def run_variant_once(case_obj: Dict, variant: Dict, base_cfg: Dict, args: argparse.Namespace, metrics: List[str], repeat_id: int):
    modules = mutate_modules(case_obj, variant)
    order = [module_item["module"] for module_item in modules]
    if variant.get("order") == "reverse":
        order = list(reversed(order))

    artifact_stem = f"{args.artifact_stem}_{case_obj['case_id']}_{variant['name']}_r{repeat_id}"
    knobs = build_knobs(PROJECT_ROOT, artifact_stem=artifact_stem)

    single_rows = []
    for module_item in modules:
        single_cfg = build_cfg(base_cfg, [module_item], [module_item["module"]], args, variant)
        row, _ = run_one(single_cfg, knobs)
        single_rows.append(row)

    combo_cfg = build_cfg(base_cfg, modules, order, args, variant)
    combo_row, _ = run_one(combo_cfg, knobs)

    result_rows = []
    for metric in metrics:
        single_sum = 0.0
        valid = True
        for row in single_rows:
            value = row_metric_value(row, metric)
            if value is None:
                valid = False
                break
            single_sum += value
        if not valid:
            continue
        combo_value = row_metric_value(combo_row, metric)
        if combo_value is None:
            continue
        result_rows.append(
            {
                "case_id": case_obj["case_id"],
                "variant": variant["name"],
                "order_tag": variant.get("order", "canonical"),
                "metric": metric,
                "repeat_id": repeat_id,
                "single_sum": single_sum,
                "observed": combo_value,
                "abs_diff": combo_value - single_sum,
                "rel_diff": rel_diff(combo_value, single_sum),
            }
        )
    return result_rows


def aggregate_rows(rows: List[Dict]) -> List[Dict]:
    grouped = {}
    for row in rows:
        key = (row["case_id"], row["variant"], row["order_tag"], row["metric"])
        grouped.setdefault(key, []).append(row)

    summary_rows = []
    for key, samples in grouped.items():
        rel_samples = [item["rel_diff"] for item in samples]
        abs_samples = [item["abs_diff"] for item in samples]
        observed_samples = [item["observed"] for item in samples]
        sum_samples = [item["single_sum"] for item in samples]
        summary_rows.append(
            {
                "case_id": key[0],
                "variant": key[1],
                "order_tag": key[2],
                "metric": key[3],
                "sample_count": len(samples),
                "single_sum_median": statistics.median(sum_samples),
                "observed_median": statistics.median(observed_samples),
                "abs_diff_median": statistics.median(abs_samples),
                "rel_diff_median": statistics.median(rel_samples),
                "rel_diff_mean": statistics.mean(rel_samples),
                "rel_diff_min": min(rel_samples),
                "rel_diff_max": max(rel_samples),
            }
        )
    return sorted(summary_rows, key=lambda item: (item["case_id"], -item["rel_diff_median"], item["variant"], item["metric"]))


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def write_markdown(out_md: Path, summary_rows: List[Dict], args: argparse.Namespace) -> None:
    ensure_parent(out_md)
    lines = []
    lines.append("# Linearity Factor Scan\n\n")
    lines.append(f"- cases: `{args.case_ids}`\n")
    lines.append(f"- repeats: `{args.repeats}`\n")
    lines.append(f"- iters: `{args.iters}`\n\n")
    lines.append("| case_id | variant | order | metric | rel_diff_median | rel_diff_range |\n")
    lines.append("| --- | --- | --- | --- | ---: | --- |\n")
    for row in sorted(summary_rows, key=lambda item: item["rel_diff_median"], reverse=True):
        lines.append(
            f"| {row['case_id']} | {row['variant']} | {row['order_tag']} | {row['metric']} | "
            f"{row['rel_diff_median']:.6f} | {row['rel_diff_min']:.6f}..{row['rel_diff_max']:.6f} |\n"
        )
    out_md.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    cfg_path = (PROJECT_ROOT / args.config).resolve() if not Path(args.config).is_absolute() else Path(args.config)
    config_obj = json.loads(cfg_path.read_text(encoding="utf-8"))
    selected_case_ids = set(parse_csv_list(args.case_ids))
    metrics = parse_csv_list(args.metrics)
    variants = build_variants(args)
    base_cfg = build_base_cfg()
    cases = [case for case in config_obj.get("cases", []) if case.get("case_id") in selected_case_ids]

    raw_rows = []
    for case_obj in cases:
        for variant in variants:
            variant_rows = []
            for repeat_id in range(1, args.repeats + 1):
                result_rows = run_variant_once(case_obj, variant, base_cfg, args, metrics, repeat_id)
                raw_rows.extend(result_rows)
                variant_rows.extend(result_rows)
            worst = max((row["rel_diff"] for row in variant_rows), default=0.0)
            print(
                f"[scan] case={case_obj['case_id']} variant={variant['name']} "
                f"order={variant.get('order', 'canonical')} repeats={args.repeats} worst_rel={worst:.6f}"
            )

    summary_rows = aggregate_rows(raw_rows)

    out_csv = (PROJECT_ROOT / args.out_csv).resolve() if not Path(args.out_csv).is_absolute() else Path(args.out_csv)
    ensure_parent(out_csv)
    headers = [
        "case_id",
        "variant",
        "order_tag",
        "metric",
        "sample_count",
        "single_sum_median",
        "observed_median",
        "abs_diff_median",
        "rel_diff_median",
        "rel_diff_mean",
        "rel_diff_min",
        "rel_diff_max",
    ]
    for row in summary_rows:
        write_csv_row(out_csv, headers, row)

    out_md = (PROJECT_ROOT / args.out_md).resolve() if not Path(args.out_md).is_absolute() else Path(args.out_md)
    write_markdown(out_md, summary_rows, args)
    print(f"[done] csv={out_csv}")
    print(f"[done] md={out_md}")


if __name__ == "__main__":
    main()
