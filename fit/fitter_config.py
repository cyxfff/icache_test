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
        "fetch_amplifier.csv",
        "hot_region_loop.csv",
        "itlb.csv",
    ],
    # test/single.py 默认的外层迭代次数
    # 拟合时先按这个值把 raw counter 和 instructions 除掉，得到“每个模块单次单位贡献”
    "outer_iters": 1000,
    # 最终组合程序允许的最大 instructions
    "max_total_instructions": 100_000_000,
    # 如果 target 中包含 raw event count，则默认按这个 total_instructions 推算
    # 通常直接等于 max_total_instructions
    "fit_total_instructions": 100_000_000,
    # 每个模块家族最多允许出现几个实例
    "family_limits": {
        "cold_block_sequence": 4,
        "fetch_amplifier": 3,
        "hot_region_loop": 2,
        "itlb": 2,
    },
    # 总组件数上限
    "max_components": None,
    # 每个模块家族保留多少个候选 row 进入组合搜索
    # None 表示该家族全部保留
    "candidate_pool_per_family": {
        "cold_block_sequence": None,
        "fetch_amplifier": None,
        "hot_region_loop": None,
        "itlb": None,
    },
    # 低 MPKI 的“非瓶颈”指标在重复很多次时常常很快饱和，
    # 默认把 fetch/hot 这两类热模块的低 MPKI 原始事件视作近似稳定：
    # 一旦 repeat_count > 0，它们的 count 不再按 repeat 线性增长。
    # 这正是前面讨论过的那类情况：比如 hot 中很小的 tlb/refill 计数，
    # 默认不再按 K 次线性放大。
    "stable_low_mpki_modules": [
        "fetch_amplifier",
        "hot_region_loop",
    ],
    "stable_low_mpki_threshold": 1.0,
    # 候选过滤：默认禁用 cold_block_sequence 的 full_shuffle，
    # 避免在做 I-cache 拟合时额外把 TLB 打乱。
    "family_excluded_param_values": {
        "cold_block_sequence": {
            "layout": ["full_shuffle"],
        },
    },
    # 输出前多少个结果
    "top_k": 1,
    # 选择轨迹默认只展开前多少个结果，避免输出过长
    "trace_top_k": 1,
    # projected gradient 的最大迭代数
    "solver_iterations": 250,
    # 并行搜索配置：
    # - parallel_workers <= 0 表示自动按 CPU 核数选择
    # - chunk_size 表示每个进程一次处理多少个组合
    "parallel_workers": 128,
    "parallel_chunk_size": 64,
    # 拟合优先级：
    # 1. 先盯深层 TLB（特别是 l2i_tlb_refill）
    # 2. 再看 TLB access / L1-TLB refill
    # 3. 再看深层 I-cache
    # 4. 用 fetch_amplifier 补 L1 access
    # 5. 最后再用 hot_region_loop 修 branch
    "stage_metrics": {
        "tlb_refill": [
            "l2i_tlb_refill_mpki",
        ],
        "tlb_access": [
            "l2i_tlb_mpki",
            "l1i_tlb_refill_mpki",
        ],
        "icache_refill": [
            "l2i_cache_refill_mpki",
        ],
        "icache_access": [
            "l2i_cache_mpki",
            "l1i_cache_refill_mpki",
        ],
        "fetch_fill": [
            "l1i_cache_mpki",
            "l1i_tlb_mpki",
        ],
        "branch_fill": [
            "br_miss_rate",
            "br_mis_pred_mpki",
            "br_retired_mpki",
        ],
    },
    "stage_weights": {
        "tlb_refill": 160.0,
        "tlb_access": 70.0,
        "icache_refill": 50.0,
        "icache_access": 22.0,
        "fetch_fill": 14.0,
        "branch_fill": 12.0,
    },
    # 单模块候选筛选时，各家族优先关注哪些指标
    "family_focus_metrics": {
        "cold_block_sequence": [
            "l2i_tlb_mpki",
            "l1i_tlb_refill_mpki",
            "l2i_cache_refill_mpki",
            "l2i_cache_mpki",
            "l1i_cache_refill_mpki",
        ],
        "hot_region_loop": [
            "br_retired_mpki",
            "br_mis_pred_mpki",
            "br_miss_rate",
            "l1i_miss_rate",
            "l1i_tlb_miss_rate",
            "l1i_cache_mpki",
            "l1i_tlb_mpki",
        ],
        "fetch_amplifier": [
            "l1i_cache_mpki",
            "l1i_tlb_mpki",
            "br_retired_mpki",
        ],
        "itlb": [
            "l2i_tlb_refill_mpki",
            "l1i_tlb_refill_mpki",
            "l2i_tlb_mpki",
        ],
    },
    # 单模块预筛时，不要默认把单个模块拉到全程序指令预算去比较。
    # 对不同 family，用更符合其“角色”的 raw count 去缩放。
    "family_focus_scale_metric": {
        "itlb": "l2i_tlb_refill:u",
        "cold_block_sequence": "l2i_tlb:u",
        "fetch_amplifier": "l1i_cache:u",
        "hot_region_loop": "br_retired:u",
    },
    # 分阶段搜索顺序，更贴近实际建模思路：
    # 1. 先用 itlb 定住 L2-TLB refill 骨架
    # 2. 再用 cold_block_sequence 去补 TLB/I-cache 的冷访问
    # 3. 再用 fetch_amplifier 补 L1 access
    # 4. 最后用 hot_region_loop 修 branch
    "search_stages": [
        {
            "family": "itlb",
            "metric_groups": ["tlb_refill"],
            "beam_size": 192,
        },
        {
            "family": "cold_block_sequence",
            "metric_groups": ["tlb_refill", "tlb_access", "icache_refill"],
            "beam_size": 384,
        },
        {
            "family": "fetch_amplifier",
            "metric_groups": ["tlb_refill", "tlb_access", "icache_refill", "icache_access", "fetch_fill"],
            "beam_size": 384,
        },
        {
            "family": "hot_region_loop",
            "metric_groups": ["tlb_refill", "tlb_access", "icache_refill", "icache_access", "fetch_fill", "branch_fill"],
            "beam_size": 256,
        },
    ],
    # 如果某个指标需要额外强调，可以在这里加权
    "metric_weight_overrides": {
        # "l2i_tlb_refill_mpki": 2.0,
    },
    "ignored_metrics": [
    ],
    # 在离散 repeat_count 上做一个小范围的局部微调
    "repeat_refine_steps": 200,
    # 把最终 repeat_plan 尽量按比例放大到接近指令预算，
    # 这样最终 raw count 的量级更稳定，更接近真实目标量级。
    "fill_instruction_budget": True,
    # 结果输出
    "result_csv": PROJECT_ROOT / "output" / "fitter_results.csv",
    "result_json": PROJECT_ROOT / "output" / "fitter_results.json",
    # "best_result_json": PROJECT_ROOT / "output" / "best_fit.json",
    "best_result_json": PROJECT_ROOT / "output" / "raw_count_sparse_solver_best.json",
    # 在这里填目标
    # 支持 raw count、MPKI、rate 混合：
    # - raw count 例如: "l1i_cache_refill:u"
    # - MPKI 例如: "l1i_cache_refill_mpki"
    # - rate 例如: "l1i_miss_rate"
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
