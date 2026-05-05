#!/usr/bin/env python3

import argparse
from pathlib import Path

from config import METRIC_KEYS, build_base_cfg, build_knobs
from test.experiment_config import RANDOM_COMBO_SUITE
from test.runner import run_random_combo_suite


def parse_args():
    parser = argparse.ArgumentParser(description="Run fused instruction+data combo linearity probes.")
    parser.add_argument("--output-dir", default="output", help="Directory for CSV and Markdown report output.")
    parser.add_argument(
        "--artifact-stem",
        default="combo_linearity_probe",
        help="Generated C/binary artifact stem under build/ and remote workdir.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    root = Path(__file__).resolve().parent
    output_dir = (root / args.output_dir).resolve() if not Path(args.output_dir).is_absolute() else Path(args.output_dir)
    base_cfg = build_base_cfg()
    knobs = build_knobs(root, artifact_stem=args.artifact_stem)
    run_random_combo_suite(base_cfg, knobs, METRIC_KEYS, RANDOM_COMBO_SUITE, output_dir)


if __name__ == "__main__":
    main()
