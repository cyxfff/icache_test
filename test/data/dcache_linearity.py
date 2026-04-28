#!/usr/bin/env python3

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config import METRIC_KEYS, build_base_cfg, build_knobs
from test.experiment_config import DCACHE_LIBRARY_SUITE, DCACHE_LINEARITY_SUITE
from test.runner import run_case_library_suite, run_random_combo_suite


def main():
    root = PROJECT_ROOT
    output_dir = root / "output"
    base_cfg = build_base_cfg()

    library_knobs = build_knobs(root, artifact_stem=DCACHE_LIBRARY_SUITE["artifact_stem"])
    run_case_library_suite(base_cfg, library_knobs, METRIC_KEYS, DCACHE_LIBRARY_SUITE, output_dir)

    combo_knobs = build_knobs(root, artifact_stem=DCACHE_LINEARITY_SUITE["artifact_stem"])
    run_random_combo_suite(base_cfg, combo_knobs, METRIC_KEYS, DCACHE_LINEARITY_SUITE, output_dir)


if __name__ == "__main__":
    main()
