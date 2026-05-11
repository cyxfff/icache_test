#!/usr/bin/env python3

import argparse
import sys
from copy import deepcopy
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config import METRIC_KEYS, build_base_cfg, build_knobs
from experiments.experiment_config import RANDOM_COMBO_SUITE, SAFE_RANDOM_COMBO_SUITE
from experiments.runner import run_random_combo_suite
from tools.render_combo_linearity_md import render_combo_linearity_csv


def parse_csv_list(text):
    if not text:
        return []
    return [item.strip() for item in text.split(",") if item.strip()]


def normalize_group_filters(groups, available):
    if not groups:
        return sorted(available)

    selected = set()
    available_set = set(available)
    for group in groups:
        if group in available_set:
            selected.add(group)
    return sorted(selected)


def parse_combo_sizes(text, defaults):
    if not text:
        return list(defaults)
    values = []
    for part in text.split(","):
        token = part.strip()
        if not token:
            continue
        values.append(max(1, int(token)))
    return values


def build_suite_cfg(base_suite, args):
    suite = deepcopy(base_suite)
    available_groups = sorted(suite["module_case_groups"].keys())

    selected_groups = normalize_group_filters(parse_csv_list(args.groups), available_groups)
    suite["module_case_groups"] = {
        name: suite["module_case_groups"][name]
        for name in selected_groups
    }

    if args.max_cases_per_group is not None:
        limit = max(1, int(args.max_cases_per_group))
        suite["module_case_groups"] = {
            name: cases[:limit]
            for name, cases in suite["module_case_groups"].items()
        }

    suite["combo_sizes"] = parse_combo_sizes(args.combo_sizes, suite.get("combo_sizes", []))
    if args.total_groups is not None:
        suite["total_groups"] = max(0, int(args.total_groups))
        suite.pop("samples_per_size", None)
    if args.samples_per_size is not None:
        suite["samples_per_size"] = max(0, int(args.samples_per_size))
        suite.pop("total_groups", None)
    if args.shuffle_rounds is not None:
        suite["shuffle_rounds"] = max(0, int(args.shuffle_rounds))

    suffix = []
    if args.groups:
        suffix.append("grp")
    if args.max_cases_per_group is not None:
        suffix.append(f"g{max(1, int(args.max_cases_per_group))}")
    if args.total_groups is not None:
        suffix.append(f"tg{max(0, int(args.total_groups))}")
    if args.samples_per_size is not None:
        suffix.append(f"sp{max(0, int(args.samples_per_size))}")
    if args.combo_sizes:
        suffix.append("sz")
    if suffix:
        stem = Path(suite["csv_name"]).stem + "_" + "_".join(suffix)
        suite["csv_name"] = stem + ".csv"
        suite["report_name"] = stem + ".md"
        suite["name"] = suite["name"] + "_" + "_".join(suffix)

    run_defaults = dict(suite.get("run_defaults", {}))
    if args.iters is not None:
        run_defaults["iters"] = max(1, int(args.iters))
    if args.rounds is not None:
        run_defaults["rounds"] = max(1, int(args.rounds))
    if run_defaults:
        suite["run_defaults"] = run_defaults

    return suite


def parse_args():
    parser = argparse.ArgumentParser(description="Run multi-module combo linearity tests for instruction+attached-data groups.")
    parser.add_argument("--output-dir", default="output", help="Directory for CSV and Markdown report output.")
    parser.add_argument(
        "--artifact-stem",
        default="combo_linearity_probe",
        help="Generated C/binary artifact stem under build/ and remote workdir.",
    )
    parser.add_argument(
        "--safe-linearity",
        action="store_true",
        help="Use low-risk combo filter and safer memory defaults.",
    )
    parser.add_argument(
        "--groups",
        default="",
        help="Comma-separated group filter, e.g. hot_region_loop,fetch_amplifier,itlb,cold_block_sequence",
    )
    parser.add_argument("--max-cases-per-group", type=int, default=None, help="Cap sampled case pool per group before random selection.")
    parser.add_argument("--combo-sizes", default="", help="Override combo sizes, e.g. 2,3,4")
    parser.add_argument("--total-groups", type=int, default=None, help="Override total random combo groups across all combo sizes.")
    parser.add_argument("--samples-per-size", type=int, default=None, help="Override random groups sampled per combo size.")
    parser.add_argument("--shuffle-rounds", type=int, default=None, help="Override number of shuffled-order runs per selected combo.")
    parser.add_argument("--iters", type=int, default=None, help="Override run.iters for this suite.")
    parser.add_argument("--rounds", type=int, default=None, help="Override run.rounds for this suite.")
    return parser.parse_args()


def main():
    args = parse_args()
    root = PROJECT_ROOT
    output_dir = (root / args.output_dir).resolve() if not Path(args.output_dir).is_absolute() else Path(args.output_dir)
    base_cfg = build_base_cfg()
    knobs = build_knobs(root, artifact_stem=args.artifact_stem)

    base_suite = SAFE_RANDOM_COMBO_SUITE if args.safe_linearity else RANDOM_COMBO_SUITE
    suite_cfg = build_suite_cfg(base_suite, args)

    if not suite_cfg["module_case_groups"]:
        raise ValueError("no combo groups matched filters")

    csv_path = output_dir / suite_cfg["csv_name"]
    if csv_path.exists():
        csv_path.unlink()

    group_count = len(suite_cfg["module_case_groups"])
    print(f"[combo] groups={group_count} sizes={suite_cfg.get('combo_sizes', [])} csv={suite_cfg['csv_name']}")
    run_random_combo_suite(base_cfg, knobs, METRIC_KEYS, suite_cfg, output_dir)

    render_combo_linearity_csv(
        csv_path,
        output_dir / f"{Path(suite_cfg['csv_name']).stem}_counts.md",
    )


if __name__ == "__main__":
    main()
