#!/usr/bin/env python3

import argparse
import json
import sys
from copy import deepcopy
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config import METRIC_KEYS, build_base_cfg, build_knobs, flatten_cfg
from experiments.csv_layout import case_label
from experiments.experiment_config import MODULE_LIBRARY_SUITE, RANDOM_COMBO_SUITE, SAFE_RANDOM_COMBO_SUITE
from experiments.runner import apply_suite_defaults, build_combined_cfg, build_single_cfg
from pipeline import generate_from_flat_cfg
from utils import run_one, write_csv_row


# Edit these defaults for the common "open file, change one string, run script"
# workflow. CLI flags still work and take precedence when provided.
# DEFAULT_LABEL_EXPRESSION = """
# hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l2_sn8
# """
DEFAULT_LABEL_EXPRESSION = """
hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l2_sn8+itlb_f2048_l2_r100_cold_512k_nstr_n65536_p128_np512_l1_sn2048
"""
# +itlb_f2048_l2_r100_cold_512k_nstr_n65536_p128_np512_l1_sn2048

DEFAULT_OUTPUT_C = PROJECT_ROOT / "build_test" / "label_generated.c"
DEFAULT_OUTPUT_JSON = None
DEFAULT_DEFAULTS_PROFILE = "combo"
DEFAULT_RUN_AFTER_GENERATE = True


def parse_args():
    parser = argparse.ArgumentParser(
        description="Parse one or more case labels and generate the corresponding benchmark C source."
    )
    parser.add_argument(
        "labels",
        nargs="*",
        help="Case label expression. Supports a single label or a '+'-joined combo.",
    )
    parser.add_argument(
        "--labels-file",
        help="Read the label expression from a text file.",
    )
    parser.add_argument(
        "--out",
        help="Output C file path.",
    )
    parser.add_argument(
        "--defaults",
        choices=("base", "combo", "safe"),
        default=DEFAULT_DEFAULTS_PROFILE,
        help="Which suite defaults to apply before generating code.",
    )
    parser.add_argument("--allocator", choices=("posix", "arena"), help="Override memory allocator.")
    parser.add_argument(
        "--advice",
        choices=("default", "random", "sequential", "hugepage", "nohugepage"),
        help="Override madvise policy.",
    )
    parser.add_argument("--prefault", type=int, choices=(0, 1), help="Override prefault.")
    parser.add_argument("--warmup-iters", type=int, help="Override warmup iterations.")
    parser.add_argument("--iters", type=int, help="Override measured iterations.")
    parser.add_argument("--rounds", type=int, help="Override rounds.")
    parser.add_argument("--arena-gap-bytes", type=int, help="Override arena gap.")
    parser.add_argument("--arena-hint", type=lambda value: int(value, 0), help="Override arena hint address.")
    parser.add_argument(
        "--dump-json",
        help="Optional path to dump the resolved nested config as JSON.",
    )
    parser.add_argument(
        "--no-run",
        action="store_true",
        help="Only generate C/JSON, do not compile and run the benchmark.",
    )
    parser.add_argument(
        "--result-csv",
        help="Optional path to write one parsed result row as CSV.",
    )
    parser.add_argument(
        "--result-json",
        help="Optional path to write parsed metrics/config as JSON.",
    )
    parser.add_argument(
        "--raw-output",
        help="Optional path to write raw runner output.",
    )
    return parser.parse_args()


def read_expression(args):
    parts = []
    if args.labels:
        parts.append(" ".join(args.labels))
    if args.labels_file:
        parts.append(Path(args.labels_file).read_text(encoding="utf-8"))
    if not parts and DEFAULT_LABEL_EXPRESSION:
        parts.append(DEFAULT_LABEL_EXPRESSION)
    text = "\n".join(parts).strip()
    if not text:
        raise ValueError("no label expression provided")
    return text


def normalize_expression(text):
    compact = "".join(text.split())
    if not compact:
        raise ValueError("label expression became empty after removing whitespace")
    return compact


def flatten_cases():
    return list(MODULE_LIBRARY_SUITE["cases"])


def build_case_index():
    index = {}
    for case in flatten_cases():
        for label in {case["label"], case_label(case)}:
            index.setdefault(label, []).append(case)
    return index


def choose_case(label, matches):
    if len(matches) == 1:
        return deepcopy(matches[0])

    itlb_zero_run = [
        case
        for case in matches
        if case["module"] == "itlb" and int(case["params"].get("direct_run_len", 0) or 0) == 0
    ]
    if len(itlb_zero_run) == 1:
        return deepcopy(itlb_zero_run[0])

    raw_labels = ", ".join(sorted(case["label"] for case in matches))
    raise ValueError(f"ambiguous label {label!r}; candidates: {raw_labels}")


def resolve_cases(expression, case_index):
    labels = [item for item in expression.split("+") if item]
    if not labels:
        raise ValueError("no labels found in expression")

    missing = [label for label in labels if label not in case_index]
    if missing:
        raise KeyError(
            "unknown case label(s): " + ", ".join(missing)
        )
    return [choose_case(label, case_index[label]) for label in labels]


def suite_defaults_from_name(name):
    if name == "base":
        return None
    if name == "combo":
        return RANDOM_COMBO_SUITE
    if name == "safe":
        return SAFE_RANDOM_COMBO_SUITE
    raise ValueError(f"unsupported defaults profile: {name}")


def apply_cli_overrides(cfg, args):
    memory = cfg.setdefault("memory", {})
    run = cfg.setdefault("run", {})

    if args.allocator is not None:
        memory["allocator"] = args.allocator
    if args.advice is not None:
        memory["advice"] = args.advice
    if args.prefault is not None:
        memory["prefault"] = int(args.prefault)
    if args.arena_gap_bytes is not None:
        memory["arena_gap_bytes"] = int(args.arena_gap_bytes)
    if args.arena_hint is not None:
        memory["arena_hint"] = int(args.arena_hint)

    if args.warmup_iters is not None:
        run["warmup_iters"] = max(0, int(args.warmup_iters))
    if args.iters is not None:
        run["iters"] = max(1, int(args.iters))
    if args.rounds is not None:
        run["rounds"] = max(1, int(args.rounds))
    return cfg


def build_cfg(cases, args):
    base_cfg = build_base_cfg()
    suite_cfg = suite_defaults_from_name(args.defaults)
    if len(cases) == 1:
        cfg = build_single_cfg(base_cfg, cases[0], suite_cfg)
    else:
        cfg = build_combined_cfg(base_cfg, cases, cases, suite_cfg)
    return apply_cli_overrides(cfg, args)


def dump_json(path, cfg, labels):
    payload = {
        "labels": labels,
        "config": cfg,
    }
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def ensure_parent(path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def derived_sidecar_path(out_path, suffix):
    out_path = Path(out_path)
    return out_path.with_suffix(suffix)


def dump_result_json(path, labels, row, cfg):
    payload = {
        "labels": labels,
        "config": cfg,
        "metrics": row,
    }
    out_path = ensure_parent(path)
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def print_result_summary(row):
    summary_keys = [
        "cpu-cycles:u",
        "instructions:u",
        "ipc",
        "l1i_cache_refill_mpki",
        "l2i_cache_refill_mpki",
        "l1i_tlb_refill_mpki",
        "l2i_tlb_refill_mpki",
        "l1d_cache_refill_mpki",
        "l2d_cache_refill_mpki",
        "l1d_tlb_refill_mpki",
        "l2d_tlb_refill_mpki",
        "ll_cache_miss_mpki",
    ]
    print("parsed_metrics:")
    for key in summary_keys:
        if key in row:
            print(f"  {key}={row[key]}")


def run_generated_cfg(cfg, out_path, args, labels):
    knobs = build_knobs(PROJECT_ROOT, artifact_stem=Path(out_path).stem)
    knobs["out_c"] = str(Path(out_path).resolve())
    row, raw_output = run_one(cfg, knobs)

    raw_output_path = args.raw_output or derived_sidecar_path(out_path, ".raw.txt")
    ensure_parent(raw_output_path).write_text(raw_output, encoding="utf-8")

    result_json_path = args.result_json or derived_sidecar_path(out_path, ".result.json")
    dump_result_json(result_json_path, labels, row, cfg)

    result_csv_path = args.result_csv or derived_sidecar_path(out_path, ".result.csv")
    csv_path = ensure_parent(result_csv_path)
    write_csv_row(csv_path, list(row.keys()), row)

    print_result_summary(row)
    print(f"raw_output={Path(raw_output_path).resolve()}")
    print(f"result_json={Path(result_json_path).resolve()}")
    print(f"result_csv={Path(result_csv_path).resolve()}")
    return row, raw_output


def main():
    args = parse_args()
    raw_expression = read_expression(args)
    expression = normalize_expression(raw_expression)
    case_index = build_case_index()
    cases = resolve_cases(expression, case_index)
    labels = [case_label(case) for case in cases]
    cfg = build_cfg(cases, args)

    out_path = Path(args.out or DEFAULT_OUTPUT_C).resolve()
    flat_cfg = flatten_cfg(cfg)
    generate_from_flat_cfg(out_path, flat_cfg)

    dump_json_path = args.dump_json if args.dump_json is not None else DEFAULT_OUTPUT_JSON
    if dump_json_path:
        dump_json(dump_json_path, cfg, labels)

    should_run = DEFAULT_RUN_AFTER_GENERATE and not args.no_run
    if should_run:
        run_generated_cfg(cfg, out_path, args, labels)

    print(f"generated={out_path}")
    print(f"labels={'+'.join(labels)}")
    print(f"defaults={args.defaults}")
    print(f"allocator={cfg.get('memory', {}).get('allocator', 'posix')}")


if __name__ == "__main__":
    main()
