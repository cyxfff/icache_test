#!/usr/bin/env python3

import argparse
import json
import sys
from pathlib import Path

if __package__ in (None, "", "test", "experiments"):
    THIS_DIR = Path(__file__).resolve().parent
    PARENT = THIS_DIR.parent
    if str(PARENT) not in sys.path:
        sys.path.insert(0, str(PARENT))
    if str(THIS_DIR) not in sys.path:
        sys.path.insert(0, str(THIS_DIR))
    from config import DERIVED_KEYS, METRIC_KEYS, build_base_cfg, build_knobs
    from experiments.csv_layout import case_label, metric_headers, with_metric_separators
    from experiments.experiment_config import ACTIVE_MODULE_CASE_GROUPS
    from experiments.experiment_config import MODULE_CASE_GROUPS
    from experiments.runner import build_single_cfg
    from utils import run_one, write_csv_row
else:
    from ..config import DERIVED_KEYS, METRIC_KEYS, build_base_cfg, build_knobs
    from .csv_layout import case_label, metric_headers, with_metric_separators
    from .experiment_config import ACTIVE_MODULE_CASE_GROUPS
    from .experiment_config import MODULE_CASE_GROUPS
    from .runner import build_single_cfg
    from ..utils import run_one, write_csv_row


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Run selected single-module benchmark cases.")
    parser.add_argument(
        "--modules",
        nargs="+",
        choices=sorted(MODULE_CASE_GROUPS.keys()),
        help="Module names to run. Defaults to ACTIVE_MODULE_CASE_GROUPS.",
    )
    parser.add_argument("--output-dir", help="Directory for per-module CSV output.")
    parser.add_argument("--artifact-prefix", default="single", help="Generated artifact prefix.")
    parser.add_argument("--list", action="store_true", help="Print available module groups and exit.")
    return parser.parse_args(argv)


def build_row(module_name, case, measured_row):
    row = {
        "case": case_label(case),
        "module": module_name,
        "params_json": json.dumps(case["params"], sort_keys=True, separators=(",", ":")),
    }

    for key in METRIC_KEYS:
        row[key] = measured_row.get(key, "")
    for key in DERIVED_KEYS:
        row[key] = measured_row.get(key, "")
    return with_metric_separators(row)


def run_modules(selected_modules, base_cfg=None, output_dir=None, artifact_prefix="single"):
    root = Path(__file__).resolve().parents[1]
    output_dir = Path(output_dir) if output_dir is not None else root / "output"
    base_cfg = build_base_cfg() if base_cfg is None else base_cfg

    for module_name in selected_modules:
        if module_name not in MODULE_CASE_GROUPS:
            raise KeyError(f"unknown module: {module_name}")

        cases = MODULE_CASE_GROUPS[module_name]
        csv_out = output_dir / f"{module_name}.csv"
        headers = ["case", "module", *metric_headers(METRIC_KEYS), "params_json"]
        knobs = build_knobs(root, artifact_stem=f"{artifact_prefix}_{module_name}")

        for case in cases:
            cfg = build_single_cfg(base_cfg, case)
            row, raw_output = run_one(cfg, knobs)
            write_csv_row(csv_out, headers, build_row(module_name, case, row))
            print(f"[single_modules] module={module_name} case={case_label(case)}")
            print(raw_output)


def print_module_groups():
    print("active_modules:")
    for module_name, cases in ACTIVE_MODULE_CASE_GROUPS.items():
        print(f"  {module_name}: {len(cases)} cases")
    print("available_modules:")
    for module_name, cases in MODULE_CASE_GROUPS.items():
        print(f"  {module_name}: {len(cases)} cases")


def main(argv=None):
    args = parse_args(argv)
    if args.list:
        print_module_groups()
        return 0

    selected_modules = args.modules if args.modules is not None else ACTIVE_MODULE_CASE_GROUPS.keys()
    run_modules(selected_modules, output_dir=args.output_dir, artifact_prefix=args.artifact_prefix)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
