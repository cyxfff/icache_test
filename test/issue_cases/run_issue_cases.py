#!/usr/bin/env python3

import argparse
import json
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
        description="Run manual combo experiments from JSON and compare combo counters against single-module sums."
    )
    parser.add_argument(
        "--config",
        default="test/issue_cases/issue_combos_dcache.json",
        help="Issue combo JSON config path.",
    )
    parser.add_argument(
        "--artifact-stem",
        default="issue_cases_probe",
        help="Build artifact stem.",
    )
    parser.add_argument(
        "--out-csv",
        default="output/issue_cases_results.csv",
        help="CSV output path.",
    )
    parser.add_argument(
        "--out-md",
        default="output/issue_cases_results.md",
        help="Markdown summary output path.",
    )
    parser.add_argument(
        "--with-reverse-order",
        action="store_true",
        help="Also run reversed module order to probe order sensitivity.",
    )
    parser.add_argument(
        "--metrics",
        default="",
        help="Override metrics list by comma, e.g. l1d_cache_refill:u,l2d_cache_refill:u,ll_cache_miss:u",
    )
    parser.add_argument(
        "--case-ids",
        default="",
        help="Optional comma-separated case ids to run only a subset.",
    )
    parser.add_argument(
        "--max-cases",
        type=int,
        default=0,
        help="Optional cap for number of cases to run (0 means all).",
    )
    parser.add_argument(
        "--memory-allocator",
        default="",
        help="Override memory allocator, e.g. posix or arena.",
    )
    parser.add_argument(
        "--memory-advice",
        default="",
        help="Override memory advice, e.g. default, random, sequential, hugepage, nohugepage.",
    )
    parser.add_argument(
        "--memory-arena-gap-bytes",
        type=int,
        default=-1,
        help="Override arena gap bytes. Negative keeps the base config value.",
    )
    parser.add_argument(
        "--memory-arena-hint",
        type=lambda value: int(value, 0),
        default=-1,
        help="Override arena hint virtual address, e.g. 0x4000000000. Negative keeps the base config value.",
    )
    parser.add_argument(
        "--memory-prefault",
        type=int,
        choices=[-1, 0, 1],
        default=-1,
        help="Override prefault policy. -1 keeps the base config value.",
    )
    return parser.parse_args()


def parse_metrics(args: argparse.Namespace, config_obj: Dict) -> List[str]:
    if args.metrics.strip():
        return [item.strip() for item in args.metrics.split(",") if item.strip()]
    metrics = config_obj.get("focus_metrics", [])
    if metrics:
        return metrics
    return ["l1d_cache_refill:u", "l2d_cache_refill:u", "ll_cache_miss:u"]


def apply_memory_overrides(cfg: Dict, args: argparse.Namespace) -> None:
    memory_cfg = cfg.setdefault("memory", {})
    if args.memory_allocator.strip():
        memory_cfg["allocator"] = args.memory_allocator.strip()
    if args.memory_advice.strip():
        memory_cfg["advice"] = args.memory_advice.strip()
    if args.memory_arena_gap_bytes >= 0:
        memory_cfg["arena_gap_bytes"] = args.memory_arena_gap_bytes
    if args.memory_arena_hint >= 0:
        memory_cfg["arena_hint"] = args.memory_arena_hint
    if args.memory_prefault >= 0:
        memory_cfg["prefault"] = args.memory_prefault


def build_cfg(base_cfg: Dict, modules: List[Dict], order: List[str], args: argparse.Namespace) -> Dict:
    cfg = deepcopy(base_cfg)
    zero_all_modules(cfg)
    apply_memory_overrides(cfg, args)
    for module_item in modules:
        module_name = module_item["module"]
        params = module_item["params"]
        if module_name not in cfg["modules"]:
            raise KeyError(f"unknown module {module_name!r} in input config")
        apply_module_config(cfg, module_name, params)
    set_module_order(cfg, order)
    return cfg


def rel_diff(observed: float, baseline: float) -> float:
    return abs(observed - baseline) / max(1.0, abs(baseline))


def row_metric_value(row: Dict, metric: str):
    value = row.get(metric)
    if value in ("", None):
        return None
    return float(value)


def run_case(
    case_obj: Dict,
    base_cfg: Dict,
    knobs: Dict,
    metrics: List[str],
    with_reverse: bool,
    args: argparse.Namespace,
):
    modules = case_obj["modules"]
    case_id = case_obj["case_id"]

    single_rows = []
    for module_item in modules:
        single_cfg = build_cfg(base_cfg, [module_item], [module_item["module"]], args)
        row, _ = run_one(single_cfg, knobs)
        single_rows.append(row)

    default_order = [module_item["module"] for module_item in modules]
    combo_cfg = build_cfg(base_cfg, modules, default_order, args)
    combo_row, _ = run_one(combo_cfg, knobs)

    reverse_row = None
    reverse_order = list(reversed(default_order))
    if with_reverse and reverse_order != default_order:
        rev_cfg = build_cfg(base_cfg, modules, reverse_order, args)
        reverse_row, _ = run_one(rev_cfg, knobs)

    memory_cfg = combo_cfg.get("memory", {})
    memory_tag = (
        f"{memory_cfg.get('allocator', 'posix')}/"
        f"{memory_cfg.get('advice', 'default')}/"
        f"gap={memory_cfg.get('arena_gap_bytes', 0)}/"
        f"hint=0x{int(memory_cfg.get('arena_hint', 0)):x}/"
        f"prefault={int(memory_cfg.get('prefault', 0))}"
    )

    comparisons = []
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

        comparisons.append(
            {
                "case_id": case_id,
                "order_tag": "canonical",
                "metric": metric,
                "single_sum": single_sum,
                "observed": combo_value,
                "abs_diff": combo_value - single_sum,
                "rel_diff": rel_diff(combo_value, single_sum),
                "memory_tag": memory_tag,
                "memory_allocator": memory_cfg.get("allocator", "posix"),
                "memory_advice": memory_cfg.get("advice", "default"),
                "memory_arena_gap_bytes": memory_cfg.get("arena_gap_bytes", 0),
                "memory_arena_hint": int(memory_cfg.get("arena_hint", 0)),
                "memory_prefault": int(memory_cfg.get("prefault", 0)),
            }
        )

        if reverse_row is not None:
            reverse_value = row_metric_value(reverse_row, metric)
            if reverse_value is not None:
                comparisons.append(
                    {
                        "case_id": case_id,
                        "order_tag": "reverse",
                        "metric": metric,
                        "single_sum": single_sum,
                        "observed": reverse_value,
                        "abs_diff": reverse_value - single_sum,
                        "rel_diff": rel_diff(reverse_value, single_sum),
                        "memory_tag": memory_tag,
                        "memory_allocator": memory_cfg.get("allocator", "posix"),
                        "memory_advice": memory_cfg.get("advice", "default"),
                        "memory_arena_gap_bytes": memory_cfg.get("arena_gap_bytes", 0),
                        "memory_arena_hint": int(memory_cfg.get("arena_hint", 0)),
                        "memory_prefault": int(memory_cfg.get("prefault", 0)),
                    }
                )

    return comparisons


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def write_markdown_summary(out_md: Path, rows: List[Dict], source_config: str) -> None:
    ensure_parent(out_md)
    by_case: Dict[str, List[Dict]] = {}
    for row in rows:
        by_case.setdefault(row["case_id"], []).append(row)

    lines = []
    lines.append("# Issue Case Results\n\n")
    lines.append(f"- config: `{source_config}`\n")
    lines.append(f"- cases: `{len(by_case)}`\n")
    lines.append(f"- rows: `{len(rows)}`\n\n")
    lines.append("| case_id | order | metric | memory | single_sum | observed | rel_diff |\n")
    lines.append("| --- | --- | --- | --- | ---: | ---: | ---: |\n")
    for row in sorted(rows, key=lambda item: item["rel_diff"], reverse=True):
        lines.append(
            f"| {row['case_id']} | {row['order_tag']} | {row['metric']} | {row['memory_tag']} | "
            f"{row['single_sum']:.0f} | {row['observed']:.0f} | {row['rel_diff']:.6f} |\n"
        )
    out_md.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    root = Path(__file__).resolve().parents[2]
    cfg_path = (root / args.config).resolve() if not Path(args.config).is_absolute() else Path(args.config)
    config_obj = json.loads(cfg_path.read_text(encoding="utf-8"))

    base_cfg = build_base_cfg()
    knobs = build_knobs(root, artifact_stem=args.artifact_stem)
    metrics = parse_metrics(args, config_obj)

    selected_case_ids = {item.strip() for item in args.case_ids.split(",") if item.strip()}
    all_cases = config_obj.get("cases", [])
    if selected_case_ids:
        all_cases = [case for case in all_cases if case.get("case_id") in selected_case_ids]
    if args.max_cases > 0:
        all_cases = all_cases[: args.max_cases]

    all_rows = []
    for case_obj in all_cases:
        result_rows = run_case(case_obj, base_cfg, knobs, metrics, args.with_reverse_order, args)
        all_rows.extend(result_rows)
        worst = max((row["rel_diff"] for row in result_rows), default=0.0)
        print(f"[case] {case_obj['case_id']} rows={len(result_rows)} worst_rel_diff={worst:.6f}")

    out_csv = (root / args.out_csv).resolve() if not Path(args.out_csv).is_absolute() else Path(args.out_csv)
    ensure_parent(out_csv)
    headers = [
        "case_id",
        "order_tag",
        "metric",
        "memory_tag",
        "memory_allocator",
        "memory_advice",
        "memory_arena_gap_bytes",
        "memory_arena_hint",
        "memory_prefault",
        "single_sum",
        "observed",
        "abs_diff",
        "rel_diff",
    ]
    for row in all_rows:
        write_csv_row(out_csv, headers, row)

    out_md = (root / args.out_md).resolve() if not Path(args.out_md).is_absolute() else Path(args.out_md)
    write_markdown_summary(out_md, all_rows, str(cfg_path))

    print(f"[done] csv={out_csv}")
    print(f"[done] md={out_md}")


if __name__ == "__main__":
    main()
