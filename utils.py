#!/usr/bin/env python3

import csv
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path

if __package__ in (None, ""):
    from config import flatten_cfg
    from pipeline import MAIN_LAYOUT_CHOICES, generate_from_flat_cfg
else:
    from .config import flatten_cfg
    from .pipeline import MAIN_LAYOUT_CHOICES, generate_from_flat_cfg


def run_cmd(cmd, check=True, capture=True, cwd=None, env=None):
    return subprocess.run(
        [str(item) for item in cmd],
        cwd=str(cwd) if cwd else None,
        env=env,
        text=True,
        capture_output=capture,
        check=check,
    )


def ensure_parent_dir(path):
    Path(path).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)


def write_csv_row(csv_path, headers, row):
    def csv_value(value):
        if value is None:
            return ""
        if isinstance(value, float):
            return f"{value:.4f}"
        return value

    csv_path = Path(csv_path)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    exists = csv_path.exists()
    with csv_path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        if not exists:
            writer.writeheader()
        writer.writerow({key: csv_value(row.get(key, "")) for key in headers})


def parse_perf_stat(text, events):
    result = {event: None for event in events}
    line_re = re.compile(
        r"^\s*(?P<value><not counted>|<not supported>|[0-9][0-9,]*)\s+"
        r"(?P<event>[A-Za-z0-9_\-.:/]+)\b"
    )

    for line in text.splitlines():
        match = line_re.match(line)
        if not match:
            continue
        event = match.group("event")
        if event not in result:
            continue
        raw_value = match.group("value")
        result[event] = None if raw_value.startswith("<") else int(raw_value.replace(",", ""))

    return result


def split_perf_groups(text, marker="===== perf group ====="):
    return [part for part in text.split(marker)[1:]]


def normalize_metrics_to_ref_event(metrics, ref_value, ref_event):
    current_value = metrics.get(ref_event)
    if current_value in (None, 0) or ref_value in (None, 0):
        return metrics.copy()

    scale = ref_value / current_value
    normalized = {}
    for key, value in metrics.items():
        if value is None:
            normalized[key] = None
        elif key == ref_event:
            normalized[key] = ref_value
        else:
            normalized[key] = int(round(value * scale))
    return normalized


def merge_metric_dicts(metric_dicts):
    merged = {}
    for metric_dict in metric_dicts:
        for key, value in metric_dict.items():
            if value is not None and merged.get(key) is None:
                merged[key] = value
    return merged


def calc_derived(metrics):
    def div(lhs, rhs):
        if lhs in (None, "") or rhs in (None, "", 0):
            return None
        return lhs / rhs

    def safe_div(lhs, rhs):
        if lhs is None or rhs is None or rhs == 0:
            return None
        return lhs / rhs

    def mpki(counter_key):
        value = div(metrics.get(counter_key), metrics.get("instructions:u"))
        if value is None:
            return None
        return value * 1000.0

    return {
        "ipc": div(metrics.get("instructions:u"), metrics.get("cpu-cycles:u")),
        "br_miss_rate": div(metrics.get("br_mis_pred:u"), metrics.get("br_retired:u")),
        "l1i_miss_rate": div(metrics.get("l1i_cache_refill:u"), metrics.get("l1i_cache:u")),
        "l1i_tlb_miss_rate": div(metrics.get("l1i_tlb_refill:u"), metrics.get("l1i_tlb:u")),
        "l2i_miss_rate": div(metrics.get("l2i_cache_refill:u"), metrics.get("l2i_cache:u")),
        "l2i_tlb_miss_rate": div(metrics.get("l2i_tlb_refill:u"), metrics.get("l2i_tlb:u")),
        "l1d_miss_rate": div(metrics.get("l1d_cache_refill:u"), metrics.get("l1d_cache:u")),
        "l1d_tlb_miss_rate": div(metrics.get("l1d_tlb_refill:u"), metrics.get("l1d_tlb:u")),
        "l2d_miss_rate": div(metrics.get("l2d_cache_refill:u"), metrics.get("l2d_cache:u")),
        "l2d_tlb_miss_rate": div(metrics.get("l2d_tlb_refill:u"), metrics.get("l2d_tlb:u")),
        "ll_miss_rate": div(metrics.get("ll_cache_miss:u"), metrics.get("ll_cache:u")),
        "br_retired_mpki": mpki("br_retired:u"),
        "br_mis_pred_mpki": mpki("br_mis_pred:u"),
        "l1i_cache_mpki": mpki("l1i_cache:u"),
        "l1i_cache_refill_mpki": mpki("l1i_cache_refill:u"),
        "l1i_tlb_mpki": mpki("l1i_tlb:u"),
        "l1i_tlb_refill_mpki": mpki("l1i_tlb_refill:u"),
        "l2i_cache_mpki": mpki("l2i_cache:u"),
        "l2i_cache_refill_mpki": mpki("l2i_cache_refill:u"),
        "l2i_tlb_mpki": mpki("l2i_tlb:u"),
        "l2i_tlb_refill_mpki": mpki("l2i_tlb_refill:u"),
        "l1d_cache_mpki": mpki("l1d_cache:u"),
        "l1d_cache_refill_mpki": mpki("l1d_cache_refill:u"),
        "l1d_tlb_mpki": mpki("l1d_tlb:u"),
        "l1d_tlb_refill_mpki": mpki("l1d_tlb_refill:u"),
        "l2d_cache_mpki": mpki("l2d_cache:u"),
        "l2d_cache_refill_mpki": mpki("l2d_cache_refill:u"),
        "l2d_tlb_mpki": mpki("l2d_tlb:u"),
        "l2d_tlb_refill_mpki": mpki("l2d_tlb_refill:u"),
        "ll_cache_mpki": mpki("ll_cache:u"),
        "ll_cache_miss_mpki": mpki("ll_cache_miss:u"),
        "l2i_cache_access_proxy_mpki": safe_div(
            mpki("l2i_cache_refill:u"),
            div(metrics.get("l2i_cache_refill:u"), metrics.get("l2i_cache:u")),
        ),
        "l2i_tlb_access_proxy_mpki": safe_div(
            mpki("l2i_tlb_refill:u"),
            div(metrics.get("l2i_tlb_refill:u"), metrics.get("l2i_tlb:u")),
        ),
    }


def flatten_if_needed(cfg):
    if "modules" in cfg:
        return flatten_cfg(cfg)
    return dict(cfg)


def normalize_single_choice(value, field_name, allowed_values):
    if value in allowed_values:
        return value

    if isinstance(value, str):
        parts = [item.strip() for item in value.split(",") if item.strip()]
        if len(parts) > 1:
            raise ValueError(
                f"{field_name} must be a single value, got {value!r}. "
                f"Choose one of {sorted(allowed_values)} or loop over them in main.py."
            )

    raise ValueError(
        f"invalid {field_name}={value!r}, expected one of {sorted(allowed_values)}"
    )


def format_value(value, digits=6):
    if value is None:
        return "NA"
    if isinstance(value, int):
        return str(value)
    return f"{value:.{digits}f}"


def format_derived_summary(derived):
    lines = [
        "",
        "===== derived =====",
        f"ipc={format_value(derived.get('ipc'), 4)}",
        f"br_retired_mpki={format_value(derived.get('br_retired_mpki'), 4)}",
        f"br_mis_pred_mpki={format_value(derived.get('br_mis_pred_mpki'), 4)}",
        f"l1i_cache_mpki={format_value(derived.get('l1i_cache_mpki'), 4)}",
        f"l1i_cache_refill_mpki={format_value(derived.get('l1i_cache_refill_mpki'), 4)}",
        f"l1i_tlb_mpki={format_value(derived.get('l1i_tlb_mpki'), 4)}",
        f"l1i_tlb_refill_mpki={format_value(derived.get('l1i_tlb_refill_mpki'), 4)}",
        f"l2i_cache_mpki={format_value(derived.get('l2i_cache_mpki'), 4)}",
        f"l2i_cache_refill_mpki={format_value(derived.get('l2i_cache_refill_mpki'), 4)}",
        f"l2i_cache_access_proxy_mpki={format_value(derived.get('l2i_cache_access_proxy_mpki'), 4)}",
        f"l2i_tlb_mpki={format_value(derived.get('l2i_tlb_mpki'), 4)}",
        f"l2i_tlb_refill_mpki={format_value(derived.get('l2i_tlb_refill_mpki'), 4)}",
        f"l2i_tlb_access_proxy_mpki={format_value(derived.get('l2i_tlb_access_proxy_mpki'), 4)}",
        f"l1i_miss_rate={format_value(derived.get('l1i_miss_rate'), 6)}",
        f"l2i_miss_rate={format_value(derived.get('l2i_miss_rate'), 6)}",
        f"l1i_tlb_miss_rate={format_value(derived.get('l1i_tlb_miss_rate'), 6)}",
        f"l2i_tlb_miss_rate={format_value(derived.get('l2i_tlb_miss_rate'), 6)}",
        f"l1d_cache_mpki={format_value(derived.get('l1d_cache_mpki'), 4)}",
        f"l1d_cache_refill_mpki={format_value(derived.get('l1d_cache_refill_mpki'), 4)}",
        f"l1d_tlb_mpki={format_value(derived.get('l1d_tlb_mpki'), 4)}",
        f"l1d_tlb_refill_mpki={format_value(derived.get('l1d_tlb_refill_mpki'), 4)}",
        f"l2d_cache_mpki={format_value(derived.get('l2d_cache_mpki'), 4)}",
        f"l2d_cache_refill_mpki={format_value(derived.get('l2d_cache_refill_mpki'), 4)}",
        f"l2d_tlb_mpki={format_value(derived.get('l2d_tlb_mpki'), 4)}",
        f"l2d_tlb_refill_mpki={format_value(derived.get('l2d_tlb_refill_mpki'), 4)}",
        f"ll_cache_mpki={format_value(derived.get('ll_cache_mpki'), 4)}",
        f"ll_cache_miss_mpki={format_value(derived.get('ll_cache_miss_mpki'), 4)}",
        f"l1d_miss_rate={format_value(derived.get('l1d_miss_rate'), 6)}",
        f"l2d_miss_rate={format_value(derived.get('l2d_miss_rate'), 6)}",
        f"l1d_tlb_miss_rate={format_value(derived.get('l1d_tlb_miss_rate'), 6)}",
        f"l2d_tlb_miss_rate={format_value(derived.get('l2d_tlb_miss_rate'), 6)}",
        f"ll_miss_rate={format_value(derived.get('ll_miss_rate'), 6)}",
    ]
    return "\n".join(lines) + "\n"


def generate_c(out_c, cfg):
    cfg = flatten_if_needed(cfg)
    cfg["cold_block_sequence_layout"] = normalize_single_choice(
        cfg["cold_block_sequence_layout"],
        "cold_block_sequence_layout",
        set(MAIN_LAYOUT_CHOICES),
    )
    cfg["fetch_amplifier_layout"] = normalize_single_choice(
        cfg["fetch_amplifier_layout"],
        "fetch_amplifier_layout",
        set(MAIN_LAYOUT_CHOICES),
    )
    ensure_parent_dir(out_c)
    generate_from_flat_cfg(out_c, cfg)


def compile_bin(
    cc,
    out_c,
    out_bin,
    cfg,
    target=None,
    sysroot=None,
    extra_cflags=None,
    extra_ldflags=None,
):
    ensure_parent_dir(out_bin)
    extra_cflags = list(extra_cflags or [])
    extra_ldflags = list(extra_ldflags or [])
    cmd = [cc]
    if target:
        cmd.extend(["-target", target])
    if sysroot:
        cmd.extend(["--sysroot", sysroot])
    cmd.extend(
        [
            "-o",
            out_bin,
            f"-O{cfg['opt_level']}",
            "-std=gnu11",
            "-w",
            *extra_cflags,
            out_c,
            *extra_ldflags,
        ]
    )
    completed = run_cmd(cmd)
    if completed.stdout:
        print(completed.stdout, end="")
    if completed.stderr:
        print(completed.stderr, end="", file=sys.stderr)


def hdc_shell(hdc, command):
    return run_cmd([hdc, "shell", command])


def hdc_send(hdc, src, dst):
    return run_cmd([hdc, "file", "send", src, dst])


def format_event_groups(event_groups):
    return "\n".join(",".join(group) for group in event_groups)


def build_runner_env(cfg, runner_workdir, bin_path, runner_env=None, event_groups=None):
    env_pairs = {
        "BIN": bin_path,
        "ITERS": cfg["iters"],
        "ROUNDS": cfg["rounds"],
        "CPU_CORE": cfg["cpu_core"],
    }
    if runner_workdir:
        env_pairs["WORKDIR"] = runner_workdir
    if event_groups:
        env_pairs["EVENT_GROUPS"] = format_event_groups(event_groups)
    if runner_env:
        env_pairs.update({key: str(value) for key, value in runner_env.items()})
    return {key: str(value) for key, value in env_pairs.items() if value is not None}


def shell_env_text(env_pairs):
    return " ".join(f"{key}={shlex.quote(value)}" for key, value in env_pairs.items())


def run_remote_runner(hdc, remote_workdir, remote_runner, remote_bin, cfg, runner_env=None, event_groups=None):
    remote_workdir = remote_workdir.rstrip("/")
    remote_bin_name = Path(remote_bin).name
    remote_runner_name = Path(remote_runner).name
    remote_bin_path = f"{remote_workdir}/{remote_bin_name}"
    remote_runner_path = f"{remote_workdir}/{remote_runner_name}"

    hdc_shell(hdc, f"mkdir -p {remote_workdir}")
    hdc_send(hdc, remote_bin, remote_bin_path)
    hdc_send(hdc, remote_runner, remote_runner_path)
    hdc_shell(hdc, f"chmod +x {remote_bin_path} {remote_runner_path}")

    env_pairs = build_runner_env(cfg, remote_workdir, remote_bin_path, runner_env, event_groups)
    env_text = shell_env_text(env_pairs)
    remote_cmd = f"cd {shlex.quote(remote_workdir)} && {env_text} sh {shlex.quote(remote_runner_path)}"
    completed = hdc_shell(hdc, remote_cmd)
    output = (completed.stdout or "") + ("\n" + completed.stderr if completed.stderr else "")
    failure_hints = [
        "need connect-key",
        "confirm a device",
        "[empty]",
        "device not found",
        "more than one target",
    ]
    lowered = output.lower()
    if any(hint in lowered for hint in failure_hints):
        raise RuntimeError(
            "hdc did not execute the remote runner successfully. "
            "Please confirm the device/target selection first. "
            f"Raw hdc output:\n{output.strip()}"
        )
    return output


def run_local_runner(local_workdir, runner_script, local_bin, cfg, runner_env=None, event_groups=None):
    env = os.environ.copy()
    env.update(build_runner_env(cfg, local_workdir, local_bin, runner_env, event_groups))
    completed = run_cmd(["sh", runner_script], cwd=Path(runner_script).resolve().parent, env=env)
    return (completed.stdout or "") + ("\n" + completed.stderr if completed.stderr else "")


def run_benchmark_runner(knobs, cfg):
    runner_kind = knobs["runner_kind"]
    if runner_kind == "hdc":
        return run_remote_runner(
            knobs["hdc"],
            knobs["runner_workdir"],
            knobs["runner_sh"],
            knobs["out_bin"],
            cfg,
            knobs.get("runner_env", {}),
            knobs.get("metric_groups", []),
        )
    if runner_kind == "local":
        return run_local_runner(
            knobs["runner_workdir"],
            knobs["runner_sh"],
            knobs["out_bin"],
            cfg,
            knobs.get("runner_env", {}),
            knobs.get("metric_groups", []),
        )
    raise ValueError(f"unknown runner_kind={runner_kind!r}")


def canonicalize_metrics(raw_metrics, canonical_events, event_aliases):
    canonical = {event: None for event in canonical_events}
    for raw_key, value in raw_metrics.items():
        canonical_key = event_aliases.get(raw_key)
        if canonical_key:
            canonical[canonical_key] = value
    return canonical


def parse_runner_metrics(
    output,
    canonical_events,
    metric_groups,
    event_aliases,
    normalize_to_event=None,
    group_marker="===== perf group =====",
    runner_label="runner",
):
    perf_groups = split_perf_groups(output, group_marker)
    if not perf_groups:
        raise RuntimeError(
            "No perf groups found in runner output. "
            f"Either {runner_label} did not start correctly or the returned text format changed. "
            f"Raw output:\n{output.strip()}"
        )

    if len(perf_groups) < len(metric_groups):
        raise RuntimeError(f"Expected {len(metric_groups)} perf groups, got {len(perf_groups)}")

    parsed_groups = []
    for index, group_text in enumerate(perf_groups[: len(metric_groups)]):
        parsed_groups.append(parse_perf_stat(group_text, metric_groups[index]))

    normalized_groups = parsed_groups
    if normalize_to_event:
        ref_value = parsed_groups[0].get(normalize_to_event)
        if ref_value in (None, 0):
            raise RuntimeError(f"Failed to get reference event {normalize_to_event!r} from perf group 1")

        normalized_groups = [parsed_groups[0]]
        for group_metrics in parsed_groups[1:]:
            normalized_groups.append(normalize_metrics_to_ref_event(group_metrics, ref_value, normalize_to_event))

    merged_raw = merge_metric_dicts(normalized_groups)
    metrics = canonicalize_metrics(merged_raw, canonical_events, event_aliases)
    return metrics


def run_one(cfg, knobs):
    flat_cfg = flatten_if_needed(cfg)
    generate_c(knobs["out_c"], cfg)
    compile_bin(
        knobs["cc"],
        knobs["out_c"],
        knobs["out_bin"],
        flat_cfg,
        target=knobs.get("target"),
        sysroot=knobs.get("sysroot"),
        extra_cflags=knobs.get("extra_cflags"),
        extra_ldflags=knobs.get("extra_ldflags"),
    )

    output = run_benchmark_runner(
        knobs,
        flat_cfg,
    )
    metrics = parse_runner_metrics(
        output,
        knobs["events"],
        knobs["metric_groups"],
        knobs["metric_aliases"],
        normalize_to_event=knobs.get("normalize_to_event"),
        group_marker=knobs.get("group_marker", "===== perf group ====="),
        runner_label=Path(knobs["runner_sh"]).name,
    )
    derived = calc_derived(metrics)

    row = {}
    row.update(flat_cfg)
    row.update(metrics)
    row.update(derived)
    return row, output + format_derived_summary(derived)
