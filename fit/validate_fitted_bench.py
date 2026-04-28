#!/usr/bin/env python3

import csv
import json
import sys
from pathlib import Path

if __package__ in (None, ""):
    SCRIPT_DIR = Path(__file__).resolve().parent
    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    if str(SCRIPT_DIR) not in sys.path:
        sys.path.insert(0, str(SCRIPT_DIR))
    if str(PROJECT_ROOT) not in sys.path:
        sys.path.insert(0, str(PROJECT_ROOT))
    from fit.combo_codegen import generate_combo_source, write_combo_source
    from config import build_base_cfg, build_knobs
    from fitter_config import FIT_CONFIG
    from fitter import load_candidates
    from utils import calc_derived, compile_bin, parse_runner_metrics, run_benchmark_runner, write_csv_row
else:
    from .combo_codegen import generate_combo_source, write_combo_source
    from ..config import build_base_cfg, build_knobs
    from .fitter_config import FIT_CONFIG
    from .fitter import load_candidates
    from ..utils import calc_derived, compile_bin, parse_runner_metrics, run_benchmark_runner, write_csv_row


VALIDATE_CONFIG = {
    "artifact_stem": "fitted_validate",
    "validation_csv": "fitted_bench_validation.csv",
    "plan_json": FIT_CONFIG["best_result_json"],
    # "plan_json": FIT_CONFIG["raw_count_sparse_solver_best_json"],
}

def load_plan(path):
    print(f"Loading plan from {path}...")
    with Path(path).open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if "best_result" in payload:
        return payload["best_result"]
    if "results" in payload and payload["results"]:
        return payload["results"][0]
    raise ValueError(f"no result record found in {path}")


def build_instances_from_plan(plan_record):
    candidates = load_candidates(FIT_CONFIG)
    candidate_lookup = {
        (
            candidate.module,
            candidate.case,
            Path(candidate.source_csv).name,
            int(candidate.source_row),
        ): candidate
        for candidate in candidates
    }
    candidate_lookup_fallback = {}
    for candidate in candidates:
        key = (candidate.module, candidate.case, Path(candidate.source_csv).name)
        candidate_lookup_fallback.setdefault(key, []).append(candidate)

    def resolve_candidate(item, key):
        candidate = candidate_lookup.get(key)
        if candidate is not None:
            return candidate
        fallback_key = (item["module"], item["case"], item.get("source_csv"))
        fallback = candidate_lookup_fallback.get(fallback_key, [])
        if len(fallback) == 1:
            print(
                f"[validate_fitted_bench] warning: resolved candidate by module/case/source_csv fallback for {fallback_key}",
                file=sys.stderr,
            )
            return fallback[0]
        return None

    if plan_record.get("repeat_plan_integer"):
        instances = []
        for position, item in enumerate(plan_record.get("repeat_plan_integer", []), start=1):
            repeat_count = int(item.get("repeat_count", 0)) * 20
            if repeat_count <= 0:
                continue

            key = (
                item["module"],
                item["case"],
                item.get("source_csv"),
                int(item.get("source_row", -1)),
            )
            candidate = resolve_candidate(item, key)
            if candidate is None:
                raise ValueError(f"unable to resolve candidate params for {key}")

            params = {
                field: value
                for field, value in candidate.row.items()
                if field not in ("case", "module", "params_json", "__source_csv", "__source_row")
                and field not in FIT_CONFIG.get("ignored_metrics", [])
                and not field.endswith(":u")
                and not field.endswith("_mpki")
                and not field.endswith("_rate")
                and field != "ipc"
                and value not in (None, "")
            }

            normalized = {}
            params_json = candidate.row.get("params_json")
            if params_json not in (None, ""):
                normalized.update(json.loads(params_json))
            for field, value in params.items():
                text = str(value).strip()
                if text == "":
                    continue
                try:
                    number = float(text)
                    normalized[field] = int(number) if number.is_integer() else number
                except ValueError:
                    normalized[field] = text

            normalized["region_reps"] = int(normalized.get("region_reps", 1)) * repeat_count
            normalized["pos"] = position
            instances.append(
                {
                    "module": item["module"],
                    "label": item["case"],
                    "params": normalized,
                }
            )

        if not instances:
            raise ValueError("plan json produced no runnable instances")
        return instances

    instances = []
    for position, item in enumerate(plan_record.get("repeat_plan", []), start=1):
        repeat_count = int(item.get("repeat_count", 0)) * 20
        if repeat_count <= 0:
            continue
        params = dict(item.get("params", {}))
        params["region_reps"] = int(params.get("region_reps", 1)) * repeat_count
        params["pos"] = position
        instances.append(
            {
                "module": item["module"],
                "label": item["case"],
                "params": params,
            }
        )
    if not instances:
        raise ValueError("plan json produced no runnable instances")
    return instances


def plan_text_from_record(plan_record):
    if plan_record.get("repeat_plan_text"):
        return plan_record["repeat_plan_text"]
    if plan_record.get("repeat_plan_integer"):
        parts = []
        for item in plan_record.get("repeat_plan_integer", []):
            repeat_count = int(item.get("repeat_count", 0))
            if repeat_count <= 0:
                continue
            parts.append(f"{item['case']} x {repeat_count}")
        return " | ".join(parts)
    if plan_record.get("coefficients"):
        parts = []
        for item in plan_record.get("coefficients", []):
            coeff = float(item.get("coefficient", 0.0))
            if coeff <= 0.0:
                continue
            parts.append(f"{item['case']} @ {coeff:.6f}")
        return " | ".join(parts)
    return ""


def run_combo_instances(instances, knobs, base_cfg):
    source = generate_combo_source(
        instances,
        seed=base_cfg["build"]["seed"],
        default_iters=base_cfg["run"]["iters"],
    )
    write_combo_source(knobs["out_c"], source)
    compile_bin(
        knobs["cc"],
        knobs["out_c"],
        knobs["out_bin"],
        {"opt_level": base_cfg["build"]["opt_level"]},
        target=knobs.get("target"),
        sysroot=knobs.get("sysroot"),
        extra_cflags=knobs.get("extra_cflags"),
        extra_ldflags=knobs.get("extra_ldflags"),
    )
    output = run_benchmark_runner(
        knobs,
        {
            "iters": base_cfg["run"]["iters"],
            "rounds": base_cfg["run"]["rounds"],
            "cpu_core": base_cfg["run"]["cpu_core"],
        },
    )
    metrics = parse_runner_metrics(
        output,
        knobs["events"],
        knobs["metric_groups"],
        knobs["metric_aliases"],
        normalize_to_event=knobs.get("normalize_to_event"),
        group_marker=knobs.get("group_marker", "===== perf group ====="),
        runner_label=Path(knobs["runner_sh"]).name,
    )
    derived = calc_derived(metrics)
    row = {}
    row.update(metrics)
    row.update(derived)
    return row, output


def comparison_headers(target):
    headers = [
        "rank",
        "objective",
        "repeat_plan",
        "exec_instructions",
    ]
    for metric in target:
        headers.extend(
            [
                f"target::{metric}",
                f"exec::{metric}",
                f"delta::{metric}",
                f"rel_err::{metric}",
            ]
        )
    return headers


def build_comparison_row(plan_record, actual_row):
    target = dict(plan_record.get("target_metrics", {}))
    row = {
        "rank": plan_record.get("rank", 1),
        "objective": plan_record["objective"],
        "repeat_plan": plan_text_from_record(plan_record),
        "exec_instructions": actual_row.get("instructions:u", ""),
    }

    for metric, target_value in target.items():
        exec_value = actual_row.get(metric)
        delta_value = None if exec_value in (None, "") else exec_value - target_value
        rel_err_value = None if exec_value in (None, "") else relative_error(target_value, exec_value)

        row[f"target::{metric}"] = target_value
        row[f"exec::{metric}"] = exec_value
        row[f"delta::{metric}"] = delta_value
        row[f"rel_err::{metric}"] = rel_err_value

    return row, target


def is_rate_metric(metric):
    return metric.endswith("_rate")


def format_metric_value(metric, value):
    if value is None:
        return "NA"
    if is_rate_metric(metric):
        return f"{value * 100.0:.4f}%"
    return f"{value:.6f}"


def relative_error(target_value, observed):
    if observed is None:
        return None
    denom = max(abs(target_value), 1e-9)
    return abs(observed - target_value) / denom


def metric_display_order(target):
    rate_metrics = [
        "br_miss_rate",
        "l1i_miss_rate",
        "l2i_miss_rate",
        "l1i_tlb_miss_rate",
        "l2i_tlb_miss_rate",
        "l1d_miss_rate",
        "l2d_miss_rate",
        "l1d_tlb_miss_rate",
        "l2d_tlb_miss_rate",
        "ll_miss_rate",
    ]
    other_metrics = [
        "br_mis_pred_mpki",
        "br_retired_mpki",
        "l1i_cache_mpki",
        "l1i_cache_refill_mpki",
        "l2i_cache_mpki",
        "l2i_cache_refill_mpki",
        "l1i_tlb_mpki",
        "l1i_tlb_refill_mpki",
        "l2i_tlb_mpki",
        "l2i_tlb_refill_mpki",
        "l1d_cache_mpki",
        "l1d_cache_refill_mpki",
        "l2d_cache_mpki",
        "l2d_cache_refill_mpki",
        "l1d_tlb_mpki",
        "l1d_tlb_refill_mpki",
        "l2d_tlb_mpki",
        "l2d_tlb_refill_mpki",
        "ll_cache_mpki",
        "ll_cache_miss_mpki",
        "ipc",
        "instructions:u",
    ]
    ordered = [metric for metric in rate_metrics + other_metrics if metric in target]
    for metric in target:
        if metric not in ordered:
            ordered.append(metric)
    return ordered


def print_table(headers, rows, indent="  "):
    widths = [len(str(header)) for header in headers]
    normalized_rows = []
    for row in rows:
        cells = [str(cell) for cell in row]
        normalized_rows.append(cells)
        for idx, cell in enumerate(cells):
            widths[idx] = max(widths[idx], len(cell))

    def render(cells):
        return indent + "  " + " | ".join(cell.ljust(widths[idx]) for idx, cell in enumerate(cells))

    print(render(headers))
    print(indent + "  " + "-+-".join("-" * width for width in widths))
    for row in normalized_rows:
        print(render(row))


def print_metric_comparison(row, target):
    print("== Validation Compare ==")
    print(f"  repeat_plan: {row['repeat_plan']}")
    print(f"  exec_instructions: {row['exec_instructions']}")

    ordered = metric_display_order(target)
    rate_metrics = [metric for metric in ordered if is_rate_metric(metric)]
    other_metrics = [metric for metric in ordered if not is_rate_metric(metric)]

    if rate_metrics:
        print("  miss_rate:")
        rows = []
        for metric in rate_metrics:
            target_value = row[f"target::{metric}"]
            exec_value = row[f"exec::{metric}"]
            delta_value = row[f"delta::{metric}"]
            rel_err_value = row[f"rel_err::{metric}"]

            rows.append([
                metric,
                format_metric_value(metric, target_value),
                format_metric_value(metric, exec_value),
                format_metric_value(metric, delta_value) if delta_value is not None else "NA",
                "NA" if rel_err_value is None else f"{rel_err_value * 100.0:.2f}%",
            ])

        print_table(
            ["metric", "target", "exec", "delta", "rel_err"],
            rows,
        )

    if other_metrics:
        print("  mpki_and_raw:")
        rows = []
        for metric in other_metrics:
            target_value = row[f"target::{metric}"]
            exec_value = row[f"exec::{metric}"]
            delta_value = row[f"delta::{metric}"]
            rel_err_value = row[f"rel_err::{metric}"]

            rows.append([
                metric,
                format_metric_value(metric, target_value),
                format_metric_value(metric, exec_value),
                format_metric_value(metric, delta_value) if delta_value is not None else "NA",
                "NA" if rel_err_value is None else f"{rel_err_value * 100.0:.2f}%",
            ])

        print_table(
            ["metric", "target", "exec", "delta", "rel_err"],
            rows,
        )


def main():
    root = Path(__file__).resolve().parents[1]
    base_cfg = build_base_cfg()
    base_cfg["run"]["iters"] = 1
    knobs = build_knobs(root, artifact_stem=VALIDATE_CONFIG["artifact_stem"])

    plan_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(VALIDATE_CONFIG["plan_json"])
    # print(plan_path)
    plan_record = load_plan(plan_path)
    instances = build_instances_from_plan(plan_record)
    actual_row, raw_output = run_combo_instances(instances, knobs, base_cfg)

    comparison_row, target = build_comparison_row(plan_record, actual_row)
    csv_out = root / "output" / VALIDATE_CONFIG["validation_csv"]
    write_csv_row(csv_out, comparison_headers(target), comparison_row)

    print(f"plan_json: {plan_path}")
    print_metric_comparison(comparison_row, target)
    print(raw_output)
    print(f"validation written to {csv_out}")


if __name__ == "__main__":
    main()
