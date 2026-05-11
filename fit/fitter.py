#!/usr/bin/env python3

import csv
import math
import re
from dataclasses import dataclass
from pathlib import Path

if __package__ in (None, "", "fit"):
    from config import DERIVED_KEYS, METRIC_KEYS
else:
    from ..config import DERIVED_KEYS, METRIC_KEYS


EPS = 1e-12
RAW_METRIC_SET = set(METRIC_KEYS)

MISS_RATE_SPECS = {
    "br_miss_rate": ("br_mis_pred:u", "br_retired:u"),
    "br_mis_pred_rate": ("br_mis_pred:u", "br_retired:u"),
    "branch_miss_rate": ("br_mis_pred:u", "br_retired:u"),
    "l1i_miss_rate": ("l1i_cache_refill:u", "l1i_cache:u"),
    "l2i_miss_rate": ("l2i_cache_refill:u", "l2i_cache:u"),
    "l1i_tlb_miss_rate": ("l1i_tlb_refill:u", "l1i_tlb:u"),
    "l2i_tlb_miss_rate": ("l2i_tlb_refill:u", "l2i_tlb:u"),
    "l1d_miss_rate": ("l1d_cache_refill:u", "l1d_cache:u"),
    "l2d_miss_rate": ("l2d_cache_refill:u", "l2d_cache:u"),
    "l1d_tlb_miss_rate": ("l1d_tlb_refill:u", "l1d_tlb:u"),
    "l2d_tlb_miss_rate": ("l2d_tlb_refill:u", "l2d_tlb:u"),
    "ll_miss_rate": ("ll_cache_miss:u", "ll_cache:u"),
}

ACCESS_PROXY_SPECS = {
    "l2i_cache_access_proxy_mpki": ("l2i_cache:u", "l2i_cache_refill_mpki", "l2i_miss_rate"),
    "l2i_tlb_access_proxy_mpki": ("l2i_tlb:u", "l2i_tlb_refill_mpki", "l2i_tlb_miss_rate"),
    "l2d_cache_access_proxy_mpki": ("l2d_cache:u", "l2d_cache_refill_mpki", "l2d_miss_rate"),
    "l2d_tlb_access_proxy_mpki": ("l2d_tlb:u", "l2d_tlb_refill_mpki", "l2d_tlb_miss_rate"),
}

TARGET_KEY_ALIASES = {
    "branch_miss_mpki": "br_mis_pred_mpki",
    "br_miss_mpki": "br_mis_pred_mpki",
    "branch_miss_rate": "br_miss_rate",
    "br_mis_pred_rate": "br_miss_rate",
}

INTERNAL_TARGET_METRICS = set(ACCESS_PROXY_SPECS)
NON_PARAM_COLUMNS = set(METRIC_KEYS) | set(DERIVED_KEYS) | {
    "suite",
    "case",
    "order_tag",
    "module",
    "modules",
    "params_json",
    "__source_csv",
    "__source_row",
}

# D-side metrics that get the ldr linear multiplier (large-count only).
_LDR_SCALED_METRICS = frozenset({
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
})

_LDR_RE = re.compile(r"(?:^|_)l(\d+)(?:_|$)")


def ldr_count_from_module(module_name):
    """Return ldr_count_per_unit encoded in the module name as _l{N}_, or 0."""
    match = _LDR_RE.search(module_name)
    return int(match.group(1)) if match else 0


@dataclass(frozen=True)
class Candidate:
    module: str
    case: str
    source_csv: str
    source_row: int
    row: dict
    unit_instructions: float
    unit_counts: dict
    per_instruction: dict


def parse_number(text):
    if text is None:
        return None
    if isinstance(text, (int, float)):
        return float(text)
    stripped = str(text).strip()
    if stripped == "":
        return None
    try:
        return float(stripped)
    except ValueError:
        return None


def read_csv_rows(path):
    rows = []
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for index, row in enumerate(reader):
            parsed = dict(row)
            parsed["__source_csv"] = str(path)
            parsed["__source_row"] = index
            rows.append(parsed)
    return rows


def safe_div(lhs, rhs):
    if lhs is None or rhs is None or abs(rhs) <= EPS:
        return None
    return lhs / rhs


def normalized_metric_name_set(metrics):
    return {TARGET_KEY_ALIASES.get(metric, metric) for metric in metrics}


def mpki_metric_to_raw(metric):
    if not metric.endswith("_mpki"):
        return None
    return metric[: -len("_mpki")] + ":u"


def ensure_target(config):
    ignored_metrics = normalized_metric_name_set(config.get("ignored_metrics", []))
    target = {}
    for key, value in dict(config.get("target", {})).items():
        canonical_key = TARGET_KEY_ALIASES.get(key, key)
        if canonical_key in ignored_metrics:
            continue
        if canonical_key in target:
            raise ValueError(f"duplicate target metric after alias normalization: {key!r} -> {canonical_key!r}")
        target[canonical_key] = value

    if not target:
        raise ValueError("FIT_CONFIG['target'] is empty; fill at least one raw, MPKI, or miss-rate target.")

    supported = set(RAW_METRIC_SET) | set(DERIVED_KEYS) | set(MISS_RATE_SPECS) | INTERNAL_TARGET_METRICS | {"instructions:u"}
    for key in target:
        if key not in supported:
            raise KeyError(f"unsupported target metric: {key!r}. Supported metrics: {sorted(supported)}")

    for proxy_metric, (_raw_key, refill_key, rate_key) in ACCESS_PROXY_SPECS.items():
        if refill_key in target and rate_key in target and proxy_metric not in target:
            target[proxy_metric] = safe_div(float(target[refill_key]), float(target[rate_key]))

    return target


def is_rate_metric(metric):
    return metric in MISS_RATE_SPECS


def format_metric_value(metric, value):
    if value is None:
        return "NA"
    if is_rate_metric(metric):
        return f"{value * 100.0:.4f}%"
    return f"{value:.6f}"


def normalize_metric_prediction(metric, mixed_rates, total_instructions):
    if metric == "instructions:u":
        return total_instructions
    if metric in ACCESS_PROXY_SPECS:
        raw_key, _refill_key, _rate_key = ACCESS_PROXY_SPECS[metric]
        return 1000.0 * mixed_rates.get(raw_key, 0.0)
    if metric in RAW_METRIC_SET:
        return mixed_rates.get(metric, 0.0) * total_instructions
    if metric == "ipc":
        return safe_div(1.0, mixed_rates.get("cpu-cycles:u", 0.0))
    if metric in MISS_RATE_SPECS:
        numerator_key, denominator_key = MISS_RATE_SPECS[metric]
        return safe_div(mixed_rates.get(numerator_key, 0.0), mixed_rates.get(denominator_key, 0.0))

    raw_key = mpki_metric_to_raw(metric)
    if raw_key in RAW_METRIC_SET:
        return 1000.0 * mixed_rates.get(raw_key, 0.0)

    raise KeyError(f"unsupported metric: {metric}")


def is_blank_row(row):
    for key, value in row.items():
        if key.startswith("__"):
            continue
        if str(value).strip():
            return False
    return True


def module_name_from_row(row):
    module = str(row.get("module", "")).strip()
    if module:
        return module
    modules = str(row.get("modules", "")).strip()
    if not modules:
        return ""
    first = modules.split("+", 1)[0].strip()
    return first.split(":", 1)[0].strip()


def build_candidate(row, outer_iters):
    module = module_name_from_row(row)
    case = str(row.get("case", "")).strip()
    if not module or not case:
        return None

    raw_counts = {}
    for key in METRIC_KEYS:
        value = parse_number(row.get(key))
        if value is None:
            if key == "instructions:u":
                return None
            value = 0.0
        raw_counts[key] = value / outer_iters

    unit_instructions = raw_counts["instructions:u"]
    if unit_instructions <= EPS:
        return None

    per_instruction = {}
    for key in METRIC_KEYS:
        per_instruction[key] = 1.0 if key == "instructions:u" else raw_counts[key] / unit_instructions

    return Candidate(
        module=module,
        case=case,
        source_csv=row["__source_csv"],
        source_row=int(row["__source_row"]),
        row=row,
        unit_instructions=unit_instructions,
        unit_counts=raw_counts,
        per_instruction=per_instruction,
    )


def load_candidates(config):
    output_dir = Path(config["output_dir"])
    if not output_dir.exists():
        raise FileNotFoundError(f"output directory does not exist: {output_dir}")

    candidates = []
    for name in config["csv_files"]:
        csv_path = output_dir / name
        if not csv_path.exists():
            raise FileNotFoundError(f"missing CSV file: {csv_path}")
        for row in read_csv_rows(csv_path):
            if is_blank_row(row):
                continue
            candidate = build_candidate(row, float(config["outer_iters"]))
            if candidate is not None:
                candidates.append(candidate)

    if not candidates:
        raise ValueError("no usable candidate rows found in the configured CSV files")
    return candidates


def effective_repeat_amount(candidate, metric, amount, config=None):
    threshold = float((config or {}).get("count_scale_mpki_threshold", 0.5))
    # MPKI = per_instruction * 1000; large count if MPKI >= threshold
    mpki = candidate.per_instruction.get(metric, 0.0) * 1000.0
    is_large = mpki >= threshold

    if not is_large:
        # Small count: don't scale by reps
        return 1.0

    # Large count: scale by reps, then apply ldr multiplier for D-side metrics
    effective = float(amount)
    if metric in _LDR_SCALED_METRICS:
        ldr = ldr_count_from_module(candidate.module)
        if ldr > 0:
            effective *= ldr
    return effective


def totals_from_repeat_amounts(candidates, repeat_amounts, config=None):
    totals = {key: 0.0 for key in METRIC_KEYS}
    for amount, candidate in zip(repeat_amounts, candidates):
        if amount <= 0:
            continue
        for key in METRIC_KEYS:
            totals[key] += effective_repeat_amount(candidate, key, amount, config) * candidate.unit_counts[key]
    return totals


def predictions_from_totals(totals, target):
    total_instructions = totals.get("instructions:u", 0.0)
    if total_instructions <= EPS:
        return {metric: None for metric in target}, 0.0

    mixed_rates = {}
    for key in METRIC_KEYS:
        mixed_rates[key] = 1.0 if key == "instructions:u" else totals.get(key, 0.0) / total_instructions

    predictions = {
        metric: normalize_metric_prediction(metric, mixed_rates, total_instructions)
        for metric in target
    }
    return predictions, total_instructions


def relative_error(target_value, predicted):
    if predicted is None:
        return None
    return abs(predicted - target_value) / max(abs(target_value), 1e-9)


def metric_display_order(target):
    preferred = [
        "br_miss_rate",
        "l1i_miss_rate",
        "l2i_miss_rate",
        "l1i_tlb_miss_rate",
        "l2i_tlb_miss_rate",
        "l1d_miss_rate",
        "l2d_miss_rate",
        "l1d_tlb_miss_rate",
        "l2d_tlb_miss_rate",
        "ll_miss_rate",
        "br_mis_pred_mpki",
        "br_retired_mpki",
        "l1i_cache_mpki",
        "l1i_cache_refill_mpki",
        "l2i_cache_mpki",
        "l2i_cache_refill_mpki",
        "l1i_tlb_mpki",
        "l1i_tlb_refill_mpki",
        "l2i_tlb_mpki",
        "l2i_tlb_refill_mpki",
        "l1d_cache_mpki",
        "l1d_cache_refill_mpki",
        "l2d_cache_mpki",
        "l2d_cache_refill_mpki",
        "l1d_tlb_mpki",
        "l1d_tlb_refill_mpki",
        "l2d_tlb_mpki",
        "l2d_tlb_refill_mpki",
        "ll_cache_mpki",
        "ll_cache_miss_mpki",
        "ipc",
        "instructions:u",
    ]
    ordered = [metric for metric in preferred if metric in target and metric not in INTERNAL_TARGET_METRICS]
    for metric in target:
        if metric not in ordered and metric not in INTERNAL_TARGET_METRICS:
            ordered.append(metric)
    return ordered


def display_source_ref(candidate):
    return f"{Path(candidate.source_csv).name}#{candidate.source_row}"
