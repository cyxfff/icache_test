#!/usr/bin/env python3

import json
import sys
from pathlib import Path


if __package__ in (None, "", "test"):
    PARENT = Path(__file__).resolve().parents[1]
    if str(PARENT) not in sys.path:
        sys.path.insert(0, str(PARENT))
    from config import DERIVED_KEYS, METRIC_KEYS, build_base_cfg, build_knobs
    from test.csv_layout import case_label, metric_headers, with_metric_separators
    from test.runner import build_single_cfg
    from test.experiment_config import MODULE_CASE_GROUPS
    from utils import run_one, write_csv_row
else:
    from ..config import DERIVED_KEYS, METRIC_KEYS, build_base_cfg, build_knobs
    from .csv_layout import case_label, metric_headers, with_metric_separators
    from .runner import build_single_cfg
    from .experiment_config import MODULE_CASE_GROUPS
    from ..utils import run_one, write_csv_row


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
