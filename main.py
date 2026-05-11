#!/usr/bin/env python3

from pathlib import Path

if __package__ in (None, ""):
    from config import METRIC_KEYS, build_base_cfg, build_knobs
    from experiments.runner import run_case_library_suite, run_random_combo_suite
    from experiments.experiment_config import ACTIVE_RUNS
else:
    from .config import METRIC_KEYS, build_base_cfg, build_knobs
    from .experiments.runner import run_case_library_suite, run_random_combo_suite
    from .experiments.experiment_config import ACTIVE_RUNS


def main():
    root = Path(__file__).resolve().parent
    output_dir = root / "output"
    base_cfg = build_base_cfg()

    for item in ACTIVE_RUNS:
        kind = item["kind"]
        config = item["config"]
        knobs = build_knobs(root, artifact_stem=config.get("artifact_stem", "icache_bench"))

        if kind == "case_library_suite":
            run_case_library_suite(base_cfg, knobs, METRIC_KEYS, config, output_dir)
        elif kind == "random_combo_suite":
            run_random_combo_suite(base_cfg, knobs, METRIC_KEYS, config, output_dir)
        else:
            raise ValueError(f"unknown run kind: {kind}")


if __name__ == "__main__":
    main()
