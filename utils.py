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


CODE_REGION_RE = re.compile(
    r"^code_region kind=(?P<kind>\S+) name=(?P<name>\S+)"
    r"(?: symbol=(?P<symbol>\S+))?"
    r" entry=0x(?P<entry>[0-9a-fA-F]+)"
    r" approx_payload_end=0x(?P<approx_end>[0-9a-fA-F]+)"
    r" payload_bytes=(?P<payload_bytes>\d+)"
    r" cache_lines=(?P<cache_lines>\d+)"
    r" ldr_per_unit=(?P<ldr_per_unit>\d+)"
    r" reps=(?P<reps>\d+)$"
)
OBJDUMP_FUNC_RE = re.compile(r"^([0-9a-fA-F]+) <([^>]+)>:$")
OBJDUMP_INSN_RE = re.compile(r"^\s*([0-9a-fA-F]+):\s*([0-9a-fA-F ]+)")
NM_SYMBOL_RE = re.compile(r"^([0-9a-fA-F]+)\s+([0-9a-fA-F]+)\s+([A-Za-z])\s+(.+)$")


def code_symbol_from_region_name(name):
    if name == "mixed_region_loop":
        return "mixed_region_kernel"
    match = re.fullmatch(r"mixed_region_loop_(\d+)", name)
    if match:
        return f"mixed_region_{match.group(1)}_kernel"
    return None


def objdump_instruction_width(byte_text):
    width = 0
    for token in byte_text.split():
        if not re.fullmatch(r"[0-9a-fA-F]+", token):
            break
        if len(token) % 2 != 0:
            break
        width += len(token) // 2
    return width


def parse_objdump_function_ranges(text):
    ranges = {}
    current_name = None
    current_start = None
    current_end = None

    def finish_current():
        if current_name is None or current_start is None or current_end is None:
            return
        if current_end > current_start:
            ranges[current_name] = (current_start, current_end)

    for line in text.splitlines():
        header = OBJDUMP_FUNC_RE.match(line.strip())
        if header:
            finish_current()
            current_start = int(header.group(1), 16)
            current_name = header.group(2)
            current_end = current_start
            continue

        if current_name is None:
            continue

        insn = OBJDUMP_INSN_RE.match(line)
        if not insn:
            continue
        width = objdump_instruction_width(insn.group(2))
        if width <= 0:
            continue
        current_end = max(current_end, int(insn.group(1), 16) + width)

    finish_current()
    return ranges


def read_objdump_function_ranges(binary_path):
    binary_path = Path(binary_path)
    if not binary_path.exists():
        return {}

    for tool in ("objdump", "llvm-objdump"):
        try:
            completed = run_cmd([tool, "-d", str(binary_path)], check=True, capture=True)
        except (FileNotFoundError, subprocess.CalledProcessError):
            continue
        return parse_objdump_function_ranges(completed.stdout or "")
    return {}


def parse_nm_function_ranges(text):
    ranges = {}
    for line in text.splitlines():
        match = NM_SYMBOL_RE.match(line.strip())
        if not match:
            continue
        symbol_type = match.group(3).lower()
        if symbol_type not in ("t", "w"):
            continue
        start = int(match.group(1), 16)
        size = int(match.group(2), 16)
        if size <= 0:
            continue
        name = match.group(4).split()[0]
        ranges[name] = (start, start + size)
    return ranges


def read_nm_function_ranges(binary_path):
    binary_path = Path(binary_path)
    if not binary_path.exists():
        return {}

    for tool in ("nm", "llvm-nm"):
        try:
            completed = run_cmd([tool, "-S", "-n", str(binary_path)], check=True, capture=True)
        except (FileNotFoundError, subprocess.CalledProcessError):
            continue
        ranges = parse_nm_function_ranges(completed.stdout or "")
        if ranges:
            return ranges
    return {}


def read_binary_function_ranges(binary_path):
    nm_ranges = read_nm_function_ranges(binary_path)
    objdump_ranges = read_objdump_function_ranges(binary_path)

    if nm_ranges:
        return {
            name: (start, end, "nm+objdump" if name in objdump_ranges else "nm")
            for name, (start, end) in nm_ranges.items()
        }

    return {
        name: (start, end, "objdump")
        for name, (start, end) in objdump_ranges.items()
    }


def exact_code_region_line(match, function_ranges):
    info = match.groupdict()
    name = info["name"]
    symbol = info.get("symbol") or code_symbol_from_region_name(name)
    if not symbol:
        return match.group(0)

    function_range = function_ranges.get(symbol)
    if function_range is None:
        return match.group(0)

    symbol_entry, symbol_end, source = function_range
    runtime_entry = int(info["entry"], 16)
    slide = runtime_entry - symbol_entry
    runtime_end = symbol_end + slide
    byte_count = symbol_end - symbol_entry
    cache_lines = (byte_count + 63) // 64

    return (
        f"code_region kind={info['kind']} name={name} symbol={symbol} "
        f"entry=0x{runtime_entry:x} end=0x{runtime_end:x} bytes={byte_count} "
        f"cache_lines={cache_lines} ldr_per_unit={info['ldr_per_unit']} "
        f"reps={info['reps']} source={source}"
    )


def enrich_code_regions_from_binary(raw_output, binary_path):
    if "code_region " not in raw_output:
        return raw_output

    function_ranges = read_binary_function_ranges(binary_path)
    if not function_ranges:
        return raw_output

    lines = []
    for line in raw_output.splitlines():
        match = CODE_REGION_RE.match(line)
        if match:
            lines.append(exact_code_region_line(match, function_ranges))
        else:
            lines.append(line)
    return "\n".join(lines) + ("\n" if raw_output.endswith("\n") else "")


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
    output = enrich_code_regions_from_binary(output, knobs["out_bin"])
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
