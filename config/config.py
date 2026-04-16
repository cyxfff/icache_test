#!/usr/bin/env python3

METRIC_KEYS = [
    "cpu-cycles:u",
    "instructions:u",
    "br_retired:u",
    "br_mis_pred:u",
    "l1i_cache:u",
    "l1i_cache_refill:u",
    "l1i_tlb:u",
    "l1i_tlb_refill:u",
    "l2i_cache:u",
    "l2i_cache_refill:u",
    "l2i_tlb:u",
    "l2i_tlb_refill:u",
    # "itlb_walk:u",
]

DERIVED_KEYS = [
    "ipc",
    "l1i_miss_rate",
    "l1i_tlb_miss_rate",
    "l2i_miss_rate",
    "l2i_tlb_miss_rate",
    "br_retired_mpki",
    "br_mis_pred_mpki",
    "l1i_cache_mpki",
    "l1i_cache_refill_mpki",
    "l1i_tlb_mpki",
    "l1i_tlb_refill_mpki",
    "l2i_cache_mpki",
    "l2i_cache_refill_mpki",
    "l2i_tlb_mpki",
    "l2i_tlb_refill_mpki",
    # "itlb_walk_mpki",
]


def build_knobs(root, artifact_stem="icache_bench"):
    build_dir = root / "build"
    return {
        "out_c": str(build_dir / f"{artifact_stem}.c"),
        "out_bin": str(build_dir / artifact_stem),
        "runner_sh": str(root / "run_hiperf.sh"),
        "cc": "/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/native/llvm/bin/clang",
        "sysroot": "/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/native/sysroot",
        "hdc": "/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/toolchains/hdc",
        "remote_workdir": "/data/local/tmp/synthesis_hiperf",
        "extra_cflags": [
            "-march=armv8-a+simd",
        ],
        "runner_env": {
            "CPU_MASK": "800",
        },
        "events": METRIC_KEYS,
    }


def build_base_cfg():
    return {
        "modules": {
            "cold_block_sequence": {
                "blocks": 0,
                "block_align": 64,
                "direct_run_len": 0,
                "region_reps": 1,
                "layout": "in_page_shuffle",
                "pos": 3,
            },
            "fetch_amplifier": {
                "blocks": 0,
                "block_align": 64,
                "direct_run_len": 1,
                "branch_pairs_per_block": 0,
                "block_slots": 16,
                "region_reps": 0,
                "layout": "linear",
                "pos": 4,
            },
            "hot_region_loop": {
                "size": 8192,
                "branch_pairs_per_unit": 3,
                "region_reps": 0,
                "pos": 1,
            },
            "itlb": {
                "funcs": 0,
                "lines_per_page": 1,
                "region_reps": 1,
                "mode": "chain",
                "direct_run_len": 0,
                "pos": 2,
            },
        },
        "build": {
            "seed": 1337,
            "opt_level": 0,
        },
        "run": {
            "iters": 1000,
            "rounds": 1,
            "cpu_core": 0,
        },
    }


def flatten_cfg(cfg):
    modules = cfg["modules"]
    build = cfg["build"]
    run = cfg["run"]

    return {
        "cold_block_sequence_blocks": modules["cold_block_sequence"]["blocks"],
        "cold_block_sequence_block_align": modules["cold_block_sequence"]["block_align"],
        "cold_block_sequence_direct_run_len": modules["cold_block_sequence"]["direct_run_len"],
        "cold_block_sequence_region_reps": modules["cold_block_sequence"]["region_reps"],
        "cold_block_sequence_layout": modules["cold_block_sequence"]["layout"],
        "cold_block_sequence_pos": modules["cold_block_sequence"]["pos"],
        "fetch_amplifier_blocks": modules["fetch_amplifier"]["blocks"],
        "fetch_amplifier_block_align": modules["fetch_amplifier"]["block_align"],
        "fetch_amplifier_direct_run_len": modules["fetch_amplifier"]["direct_run_len"],
        "fetch_amplifier_branch_pairs_per_block": modules["fetch_amplifier"]["branch_pairs_per_block"],
        "fetch_amplifier_block_slots": modules["fetch_amplifier"]["block_slots"],
        "fetch_amplifier_region_reps": modules["fetch_amplifier"]["region_reps"],
        "fetch_amplifier_layout": modules["fetch_amplifier"]["layout"],
        "fetch_amplifier_pos": modules["fetch_amplifier"]["pos"],
        "hot_region_loop_size": modules["hot_region_loop"]["size"],
        "hot_region_loop_branch_pairs_per_unit": modules["hot_region_loop"]["branch_pairs_per_unit"],
        "hot_region_loop_region_reps": modules["hot_region_loop"]["region_reps"],
        "hot_region_loop_pos": modules["hot_region_loop"]["pos"],
        "itlb_funcs": modules["itlb"]["funcs"],
        "itlb_lines_per_page": modules["itlb"]["lines_per_page"],
        "itlb_region_reps": modules["itlb"]["region_reps"],
        "itlb_mode": modules["itlb"]["mode"],
        "itlb_direct_run_len": modules["itlb"]["direct_run_len"],
        "itlb_pos": modules["itlb"]["pos"],
        "seed": build["seed"],
        "opt_level": build["opt_level"],
        "iters": run["iters"],
        "rounds": run["rounds"],
        "cpu_core": run["cpu_core"],
    }


def build_csv_headers(metric_keys, cfg):
    return [*flatten_cfg(cfg).keys(), *metric_keys, *DERIVED_KEYS]


def zero_all_modules(cfg):
    cold_block_sequence = cfg["modules"]["cold_block_sequence"]
    fetch_amplifier = cfg["modules"]["fetch_amplifier"]
    hot_region_loop = cfg["modules"]["hot_region_loop"]
    itlb = cfg["modules"]["itlb"]

    cold_block_sequence["blocks"] = 0
    cold_block_sequence["direct_run_len"] = 4
    cold_block_sequence["region_reps"] = 0

    fetch_amplifier["blocks"] = 0
    fetch_amplifier["direct_run_len"] = 1
    fetch_amplifier["branch_pairs_per_block"] = 0
    fetch_amplifier["block_slots"] = 16
    fetch_amplifier["region_reps"] = 0
    fetch_amplifier["layout"] = "linear"

    hot_region_loop["size"] = 0
    hot_region_loop["branch_pairs_per_unit"] = 3
    hot_region_loop["region_reps"] = 0

    itlb["funcs"] = 0
    itlb["lines_per_page"] = 1
    itlb["region_reps"] = 0
    itlb["mode"] = "chain"
    itlb["direct_run_len"] = 0
