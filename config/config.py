#!/usr/bin/env python3

from copy import deepcopy
from pathlib import Path

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
    "l1d_cache:u",
    "l1d_cache_refill:u",
    "l1d_tlb:u",
    "l1d_tlb_refill:u",
    "l2d_cache:u",
    "l2d_cache_refill:u",
    "l2d_tlb:u",
    "l2d_tlb_refill:u",
    "ll_cache:u",
    "ll_cache_miss:u",
    # "itlb_walk:u",
]

DERIVED_KEYS = [
    "ipc",
    "l1i_miss_rate",
    "l1i_tlb_miss_rate",
    "l2i_miss_rate",
    "l2i_tlb_miss_rate",
    "l1d_miss_rate",
    "l1d_tlb_miss_rate",
    "l2d_miss_rate",
    "l2d_tlb_miss_rate",
    "ll_miss_rate",
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
    "l1d_cache_mpki",
    "l1d_cache_refill_mpki",
    "l1d_tlb_mpki",
    "l1d_tlb_refill_mpki",
    "l2d_cache_mpki",
    "l2d_cache_refill_mpki",
    "l2d_tlb_mpki",
    "l2d_tlb_refill_mpki",
    "ll_cache_mpki",
    "ll_cache_miss_mpki",
    # "itlb_walk_mpki",
]


ACTIVE_PROFILE = "ohos"


# Edit only this value to switch environments.
# - "ohos": OpenHarmony cross-compile + hdc + hiperf
# - "linux": local gcc + local perf
PROFILE_PRESETS = {
    "ohos": {
        "build": {
            "cc": "/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/native/llvm/bin/clang",
            "target": "aarch64-linux-ohos",
            "sysroot": "/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/native/sysroot",
            "extra_cflags": [
                "-march=armv8-a+simd",
            ],
            "extra_ldflags": [],
        },
        "run": {
            "kind": "hdc",
            "script": "run_hiperf.sh",
            "workdir": "/data/local/tmp/synthesis_hiperf",
            "hdc": "/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/toolchains/hdc",
            "env": {
                "CPU_MASK": "800",
            },
        },
        "metrics": {
            "group_marker": "===== perf group =====",
            "normalize_to_event": "raw-instruction-retired:u",
            "event_groups": [
                [
                    "raw-cpu-cycles:u",
                    "raw-instruction-retired:u",
                    "raw-br-mis-pred:u",
                    "raw-br-retired:u",
                ],
                [
                    "raw-instruction-retired:u",
                    "raw-l1-icache:u",
                    "raw-l1-icache-refill:u",
                    "raw-l2-icache:u",
                    "raw-l2-icache-refill:u",
                ],
                [
                    "raw-instruction-retired:u",
                    "raw-l1-itlb:u",
                    "raw-l1-itlb-refill:u",
                    "raw-l2-itlb:u",
                    "raw-l2-itlb-refill:u",
                ],
            ],
            "event_aliases": {
                "raw-cpu-cycles:u": "cpu-cycles:u",
                "raw-instruction-retired:u": "instructions:u",
                "raw-br-retired:u": "br_retired:u",
                "raw-br-mis-pred:u": "br_mis_pred:u",
                "raw-l1-icache:u": "l1i_cache:u",
                "raw-l1-icache-refill:u": "l1i_cache_refill:u",
                "raw-l2-icache:u": "l2i_cache:u",
                "raw-l2-icache-refill:u": "l2i_cache_refill:u",
                "raw-l1-itlb:u": "l1i_tlb:u",
                "raw-l1-itlb-refill:u": "l1i_tlb_refill:u",
                "raw-l2-itlb:u": "l2i_tlb:u",
                "raw-l2-itlb-refill:u": "l2i_tlb_refill:u",
            },
        },
    },
    "linux": {
        "build": {
            "cc": "gcc",
            "target": None,
            "sysroot": None,
            "extra_cflags": [
                "-march=native",
            ],
            "extra_ldflags": [],
        },
        "run": {
            "kind": "local",
            "script": "run_linux.sh",
            "workdir": None,
            "hdc": None,
            "env": {},
        },
        "metrics": {
            # run_linux.sh emits instruction-side counters in group 1 and data-side counters in
            # group 2. Group 2 is normalized back to group 1's instruction count before merging.
            "group_marker": "===== perf group =====",
            "normalize_to_event": "instructions:u",
            "event_groups": [
                [
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
                ],
                [
                    "cpu-cycles:u",
                    "instructions:u",
                    "l1d_cache:u",
                    "l1d_cache_refill:u",
                    "l1d_tlb:u",
                    "l1d_tlb_refill:u",
                    "l2d_cache:u",
                    "l2d_cache_refill:u",
                    "l2d_tlb:u",
                    "l2d_tlb_refill:u",
                    "ll_cache:u",
                    "ll_cache_miss:u",
                ],
            ],
            "event_aliases": {
                "cpu-cycles:u": "cpu-cycles:u",
                "instructions:u": "instructions:u",
                "br_retired:u": "br_retired:u",
                "br_mis_pred:u": "br_mis_pred:u",
                "l1i_cache:u": "l1i_cache:u",
                "l1i_cache_refill:u": "l1i_cache_refill:u",
                "l1i_tlb:u": "l1i_tlb:u",
                "l1i_tlb_refill:u": "l1i_tlb_refill:u",
                "l2i_cache:u": "l2i_cache:u",
                "l2i_cache_refill:u": "l2i_cache_refill:u",
                "l2i_tlb:u": "l2i_tlb:u",
                "l2i_tlb_refill:u": "l2i_tlb_refill:u",
                "l1d_cache:u": "l1d_cache:u",
                "l1d_cache_refill:u": "l1d_cache_refill:u",
                "l1d_tlb:u": "l1d_tlb:u",
                "l1d_tlb_refill:u": "l1d_tlb_refill:u",
                "l2d_cache:u": "l2d_cache:u",
                "l2d_cache_refill:u": "l2d_cache_refill:u",
                "l2d_tlb:u": "l2d_tlb:u",
                "l2d_tlb_refill:u": "l2d_tlb_refill:u",
                "ll_cache:u": "ll_cache:u",
                "ll_cache_miss:u": "ll_cache_miss:u",
            },
        },
    },
}


def _resolve_local_runner_workdir(root, build_dir, configured_workdir, artifact_stem):
    if configured_workdir:
        workdir = Path(configured_workdir)
        if not workdir.is_absolute():
            workdir = root / workdir
        return str(workdir.resolve())
    return str((build_dir / f"{artifact_stem}_run").resolve())


def build_knobs(root, artifact_stem="icache_bench"):
    root = Path(root).resolve()
    build_dir = root / "build"
    if ACTIVE_PROFILE not in PROFILE_PRESETS:
        raise KeyError(f"unknown ACTIVE_PROFILE={ACTIVE_PROFILE!r}, choose from {sorted(PROFILE_PRESETS)}")

    preset = deepcopy(PROFILE_PRESETS[ACTIVE_PROFILE])
    build_cfg = preset["build"]
    run_cfg = preset["run"]
    metrics_cfg = preset["metrics"]

    runner_workdir = run_cfg.get("workdir")
    if run_cfg["kind"] == "local":
        runner_workdir = _resolve_local_runner_workdir(root, build_dir, runner_workdir, artifact_stem)

    return {
        "profile_name": ACTIVE_PROFILE,
        "out_c": str(build_dir / f"{artifact_stem}.c"),
        "out_bin": str(build_dir / artifact_stem),
        "runner_sh": str((root / run_cfg["script"]).resolve()),
        "runner_kind": run_cfg["kind"],
        "runner_workdir": runner_workdir,
        "cc": build_cfg["cc"],
        "target": build_cfg.get("target"),
        "sysroot": build_cfg.get("sysroot"),
        "hdc": run_cfg.get("hdc"),
        "extra_cflags": build_cfg.get("extra_cflags", []),
        "extra_ldflags": build_cfg.get("extra_ldflags", []),
        "runner_env": run_cfg.get("env", {}),
        "group_marker": metrics_cfg.get("group_marker", "===== perf group ====="),
        "metric_groups": metrics_cfg["event_groups"],
        "metric_aliases": metrics_cfg["event_aliases"],
        "normalize_to_event": metrics_cfg.get("normalize_to_event"),
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
            "data_stream": {
                "size": 0,
                "stride": 64,
                "region_reps": 0,
                "pos": 5,
            },
            "data_pointer_chase": {
                "pages": 0,
                "lines_per_page": 1,
                "region_reps": 0,
                "pos": 6,
            },
            "data_page_stride": {
                "pages": 0,
                "page_stride": 1,
                "line_index": 0,
                "region_reps": 0,
                "pos": 7,
            },
            "data_indirect_gather": {
                "pages": 0,
                "lines_per_page": 1,
                "index_stride": 1,
                "region_reps": 0,
                "pos": 8,
            },
            "data_hot_stride": {
                "access_count": 0,
                "stride": 4,
                "region_reps": 0,
                "pos": 9,
            },
            "data_cold_stride": {
                "access_count": 0,
                "stride": 256,
                "region_reps": 0,
                "pos": 10,
            },
            "data_tlb_indirect": {
                "pages": 0,
                "line_index": 0,
                "region_reps": 0,
                "pos": 11,
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
        "data_stream_size": modules["data_stream"]["size"],
        "data_stream_stride": modules["data_stream"]["stride"],
        "data_stream_region_reps": modules["data_stream"]["region_reps"],
        "data_stream_pos": modules["data_stream"]["pos"],
        "data_pointer_chase_pages": modules["data_pointer_chase"]["pages"],
        "data_pointer_chase_lines_per_page": modules["data_pointer_chase"]["lines_per_page"],
        "data_pointer_chase_region_reps": modules["data_pointer_chase"]["region_reps"],
        "data_pointer_chase_pos": modules["data_pointer_chase"]["pos"],
        "data_page_stride_pages": modules["data_page_stride"]["pages"],
        "data_page_stride_page_stride": modules["data_page_stride"]["page_stride"],
        "data_page_stride_line_index": modules["data_page_stride"]["line_index"],
        "data_page_stride_region_reps": modules["data_page_stride"]["region_reps"],
        "data_page_stride_pos": modules["data_page_stride"]["pos"],
        "data_indirect_gather_pages": modules["data_indirect_gather"]["pages"],
        "data_indirect_gather_lines_per_page": modules["data_indirect_gather"]["lines_per_page"],
        "data_indirect_gather_index_stride": modules["data_indirect_gather"]["index_stride"],
        "data_indirect_gather_region_reps": modules["data_indirect_gather"]["region_reps"],
        "data_indirect_gather_pos": modules["data_indirect_gather"]["pos"],
        "data_hot_stride_access_count": modules["data_hot_stride"]["access_count"],
        "data_hot_stride_stride": modules["data_hot_stride"]["stride"],
        "data_hot_stride_region_reps": modules["data_hot_stride"]["region_reps"],
        "data_hot_stride_pos": modules["data_hot_stride"]["pos"],
        "data_cold_stride_access_count": modules["data_cold_stride"]["access_count"],
        "data_cold_stride_stride": modules["data_cold_stride"]["stride"],
        "data_cold_stride_region_reps": modules["data_cold_stride"]["region_reps"],
        "data_cold_stride_pos": modules["data_cold_stride"]["pos"],
        "data_tlb_indirect_pages": modules["data_tlb_indirect"]["pages"],
        "data_tlb_indirect_line_index": modules["data_tlb_indirect"]["line_index"],
        "data_tlb_indirect_region_reps": modules["data_tlb_indirect"]["region_reps"],
        "data_tlb_indirect_pos": modules["data_tlb_indirect"]["pos"],
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

    data_stream = cfg["modules"]["data_stream"]
    data_stream["size"] = 0
    data_stream["stride"] = 64
    data_stream["region_reps"] = 0

    data_pointer_chase = cfg["modules"]["data_pointer_chase"]
    data_pointer_chase["pages"] = 0
    data_pointer_chase["lines_per_page"] = 1
    data_pointer_chase["region_reps"] = 0

    data_page_stride = cfg["modules"]["data_page_stride"]
    data_page_stride["pages"] = 0
    data_page_stride["page_stride"] = 1
    data_page_stride["line_index"] = 0
    data_page_stride["region_reps"] = 0

    data_indirect_gather = cfg["modules"]["data_indirect_gather"]
    data_indirect_gather["pages"] = 0
    data_indirect_gather["lines_per_page"] = 1
    data_indirect_gather["index_stride"] = 1
    data_indirect_gather["region_reps"] = 0

    data_hot_stride = cfg["modules"]["data_hot_stride"]
    data_hot_stride["access_count"] = 0
    data_hot_stride["stride"] = 4
    data_hot_stride["region_reps"] = 0

    data_cold_stride = cfg["modules"]["data_cold_stride"]
    data_cold_stride["access_count"] = 0
    data_cold_stride["stride"] = 256
    data_cold_stride["region_reps"] = 0

    data_tlb_indirect = cfg["modules"]["data_tlb_indirect"]
    data_tlb_indirect["pages"] = 0
    data_tlb_indirect["line_index"] = 0
    data_tlb_indirect["region_reps"] = 0

    itlb["funcs"] = 0
    itlb["lines_per_page"] = 1
    itlb["region_reps"] = 0
    itlb["mode"] = "chain"
    itlb["direct_run_len"] = 0
