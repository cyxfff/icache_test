#!/usr/bin/env python3

import argparse
import sys
from copy import deepcopy
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config import METRIC_KEYS, build_base_cfg, build_knobs
from experiments.experiment_config import RANDOM_COMBO_SUITE
from experiments.runner import run_random_combo_suite


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description=(
            "Run the single-vs-combined linearity experiment: each group records "
            "single modules, canonical combination, shuffled combination, and summed singles."
        )
    )
    parser.add_argument("--groups", type=int, default=100, help="Total random combo groups to run.")
    parser.add_argument("--max-combo-size", type=int, default=7, help="Maximum modules selected per combo.")
    parser.add_argument("--min-combo-size", type=int, default=2, help="Minimum modules selected per combo.")
    parser.add_argument("--shuffle-rounds", type=int, default=1, help="Shuffled order runs per combo group.")
    parser.add_argument("--iters", type=int, help="Override cfg['run']['iters'].")
    parser.add_argument("--rounds", type=int, help="Override cfg['run']['rounds'].")
    parser.add_argument("--cpu-core", type=int, help="Override cfg['run']['cpu_core'].")
    parser.add_argument("--list", action="store_true", help="Print candidate modules and suite settings, then exit.")
    return parser.parse_args(argv)


def build_suite(args):
    suite = deepcopy(RANDOM_COMBO_SUITE)
    module_count = len(suite["module_case_groups"])
    min_combo_size = min(max(1, args.min_combo_size), module_count)
    max_combo_size = min(max(min_combo_size, args.max_combo_size), module_count)
    suite["combo_sizes"] = list(range(min_combo_size, max_combo_size + 1))
    suite["total_groups"] = max(1, args.groups)
    suite["shuffle_rounds"] = max(0, args.shuffle_rounds)
    return suite


def print_suite(suite):
    print(f"suite: {suite['name']}")
    print(f"csv: output/{suite['csv_name']}")
    print(f"combo_sizes: {suite['combo_sizes']}")
    print(f"total_groups: {suite['total_groups']}")
    print(f"shuffle_rounds: {suite['shuffle_rounds']}")
    print("candidate_merge_slots:")
    for module_name, cases in suite["module_case_groups"].items():
        print(f"  {module_name}: {len(cases)} cases")


def main(argv=None):
    args = parse_args(argv)
    suite = build_suite(args)

    if args.list:
        print_suite(suite)
        return 0

    base_cfg = build_base_cfg()
    if args.iters is not None:
        base_cfg["run"]["iters"] = args.iters
    if args.rounds is not None:
        base_cfg["run"]["rounds"] = args.rounds
    if args.cpu_core is not None:
        base_cfg["run"]["cpu_core"] = args.cpu_core

    print_suite(suite)
    knobs = build_knobs(PROJECT_ROOT, artifact_stem=suite["artifact_stem"])
    run_random_combo_suite(base_cfg, knobs, METRIC_KEYS, suite, PROJECT_ROOT / "output")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
