#!/usr/bin/env python3

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = ROOT.parent

_json_path = ROOT / "fitter_config.json"
with _json_path.open(encoding="utf-8") as _f:
    _data = json.load(_f)

FIT_CONFIG = {
    "output_dir": PROJECT_ROOT / "output",
    "csv_files": _data["csv_files"],
    "outer_iters": _data["outer_iters"],
    "fit_total_instructions": _data["fit_total_instructions"],
    "raw_vector_metrics": _data["raw_vector_metrics"],
    "stable_low_mpki_threshold": _data["stable_low_mpki_threshold"],
    "parallel_workers": _data["parallel_workers"],
    "parallel_chunk_size": _data["parallel_chunk_size"],
    "result_csv": PROJECT_ROOT / "output" / "fitter_results.csv",
    "result_json": PROJECT_ROOT / "output" / "fitter_results.json",
    "best_result_json": PROJECT_ROOT / "output" / "best_fit.json",
    "target": _data["target"],
    "count_scale_mpki_threshold": _data["count_scale_mpki_threshold"],
    "search_config": _data["search_config"],
}
