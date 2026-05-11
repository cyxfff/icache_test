#!/usr/bin/env python3

import argparse
import sys
from collections import defaultdict, deque
from copy import deepcopy
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config import METRIC_KEYS, build_base_cfg, build_knobs
from experiments.experiment_config import MODULE_LIBRARY_SUITE
from experiments.runner import run_case_library_suite


def parse_csv_list(text):
    if not text:
        return []
    return [item.strip() for item in text.split(",") if item.strip()]


def round_robin_limit_cases(cases, limit):
    if limit is None:
        return list(cases)
    limit = max(0, int(limit))
    if limit == 0:
        return []

    buckets = defaultdict(deque)
    order = []
    for case in cases:
        module = case["module"]
        if module not in buckets:
            order.append(module)
        buckets[module].append(case)

    selected = []
    while len(selected) < limit:
        progressed = False
        for module in order:
            if not buckets[module]:
                continue
            selected.append(buckets[module].popleft())
            progressed = True
            if len(selected) >= limit:
                break
        if not progressed:
            break
    return selected


def build_filtered_suite(base_suite, modules, case_contains, max_cases):
    suite = deepcopy(base_suite)
    cases = list(suite["cases"])

    if modules:
        allowed = set(modules)
        cases = [case for case in cases if case["module"] in allowed]

    if case_contains:
        needle = case_contains.strip()
        cases = [case for case in cases if needle in case["label"]]

    cases = round_robin_limit_cases(cases, max_cases)
    suite["cases"] = cases

    suffix_parts = []
    if modules:
        suffix_parts.append("mods" + "-".join(modules))
    if case_contains:
        suffix_parts.append("filt")
    if max_cases is not None:
        suffix_parts.append(f"n{max(0, int(max_cases))}")
    if suffix_parts:
        stem = Path(suite["csv_name"]).stem + "_" + "_".join(suffix_parts)
        suite["csv_name"] = stem + ".csv"
        suite["report_name"] = stem + ".md"
        suite["name"] = suite["name"] + "_" + "_".join(suffix_parts)
    return suite


def parse_args():
    parser = argparse.ArgumentParser(description="Run single-module sweeps for instruction+attached-data cases.")
    parser.add_argument("--output-dir", default="output", help="Directory for CSV and Markdown report output.")
    parser.add_argument(
        "--artifact-stem",
        default="single_module_sweep",
        help="Generated C/binary artifact stem under build/ and remote workdir.",
    )
    parser.add_argument(
        "--modules",
        default="",
        help="Comma-separated module filter, e.g. hot_region_loop,fetch_amplifier,itlb,cold_block_sequence",
    )
    parser.add_argument("--case-contains", default="", help="Only keep cases whose label contains this text.")
    parser.add_argument("--max-cases", type=int, default=None, help="Cap number of single cases to run after filtering (round-robin by module).")
    parser.add_argument("--iters", type=int, default=None, help="Override run.iters for this suite.")
    parser.add_argument("--rounds", type=int, default=None, help="Override run.rounds for this suite.")
    return parser.parse_args()


def main():
    args = parse_args()
    root = PROJECT_ROOT
    output_dir = (root / args.output_dir).resolve() if not Path(args.output_dir).is_absolute() else Path(args.output_dir)
    base_cfg = build_base_cfg()
    knobs = build_knobs(root, artifact_stem=args.artifact_stem)

    suite_cfg = build_filtered_suite(
        MODULE_LIBRARY_SUITE,
        parse_csv_list(args.modules),
        args.case_contains,
        args.max_cases,
    )
    if args.iters is not None or args.rounds is not None:
        run_defaults = dict(suite_cfg.get("run_defaults", {}))
        if args.iters is not None:
            run_defaults["iters"] = max(1, int(args.iters))
        if args.rounds is not None:
            run_defaults["rounds"] = max(1, int(args.rounds))
        suite_cfg["run_defaults"] = run_defaults

    if not suite_cfg["cases"]:
        raise ValueError("no single-module cases matched filters")

    print(f"[single] cases={len(suite_cfg['cases'])} csv={suite_cfg['csv_name']} report={suite_cfg.get('report_name', '')}")
    run_case_library_suite(base_cfg, knobs, METRIC_KEYS, suite_cfg, output_dir)


if __name__ == "__main__":
    main()
