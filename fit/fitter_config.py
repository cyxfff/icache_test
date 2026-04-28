#!/usr/bin/env python3

from pathlib import Path
import os


ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = ROOT.parent


FIT_CONFIG = {
    # 单模块参数库输出目录
    "output_dir": PROJECT_ROOT / "output",
    "csv_files": [
        "cold_block_sequence.csv",
        "data_hot_stride.csv",
        "data_cold_stride.csv",
        "data_tlb_indirect.csv",
        "fetch_amplifier.csv",
        "hot_region_loop.csv",
        "mixed_region_loop.csv",
        "itlb.csv",
    ],
    "outer_iters": 1000,
    "fit_total_instructions": 100_000_000,
 
    "stable_low_mpki_threshold": 1.0,

    "parallel_workers": 128,
    "parallel_chunk_size": 64,
    # 结果输出
    "result_csv": PROJECT_ROOT / "output" / "fitter_results.csv",
    "result_json": PROJECT_ROOT / "output" / "fitter_results.json",
    "best_result_json": PROJECT_ROOT / "output" / "best_fit.json",
    "target": {
        "br_miss_rate": 0.028141,
        "br_mis_pred_mpki": 5.5540,
        "br_retired_mpki": 197.4620,

        "l1i_miss_rate": 0.055394,
        "l1i_cache_mpki": 344.5590,
        "l1i_cache_refill_mpki": 19.0880,

        "l1i_tlb_miss_rate": 0.004984,
        "l1i_tlb_mpki": 246.9900,
        "l1i_tlb_refill_mpki": 1.2310,

        "l2i_miss_rate": 0.622989,
        "l2i_cache_mpki": 17.8600,
        "l2i_cache_refill_mpki": 11.1230,

        "l2i_tlb_miss_rate": 0.161292,
        "l2i_tlb_mpki": 1.8460,
        "l2i_tlb_refill_mpki": 0.2980,
    },
}
