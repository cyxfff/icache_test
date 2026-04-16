#!/usr/bin/env python3

import csv
import json
import math
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path

if __package__ in (None, ""):
    SCRIPT_DIR = Path(__file__).resolve().parent
    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    if str(SCRIPT_DIR) not in sys.path:
        sys.path.insert(0, str(SCRIPT_DIR))
    if str(PROJECT_ROOT) not in sys.path:
        sys.path.insert(0, str(PROJECT_ROOT))
    from config import DERIVED_KEYS, METRIC_KEYS
    from fitter_config import FIT_CONFIG
else:
    from ..config import DERIVED_KEYS, METRIC_KEYS
    from .fitter_config import FIT_CONFIG


RAW_METRIC_SET = set(METRIC_KEYS)
EPS = 1e-12

MISS_RATE_SPECS = {
    "l1i_miss_rate": ("l1i_cache_refill:u", "l1i_cache:u"),
    "l1i_tlb_miss_rate": ("l1i_tlb_refill:u", "l1i_tlb:u"),
    "l2i_miss_rate": ("l2i_cache_refill:u", "l2i_cache:u"),
    "l2i_tlb_miss_rate": ("l2i_tlb_refill:u", "l2i_tlb:u"),
    "br_miss_rate": ("br_mis_pred:u", "br_retired:u"),
    "br_mis_pred_rate": ("br_mis_pred:u", "br_retired:u"),
    "branch_miss_rate": ("br_mis_pred:u", "br_retired:u"),
}

NON_PARAM_COLUMNS = set(METRIC_KEYS) | set(DERIVED_KEYS) | {
    "module",
    "case",
    "__source_csv",
    "__source_row",
}

TARGET_KEY_ALIASES = {
    "branch_miss_mpki": "br_mis_pred_mpki",
    "br_miss_mpki": "br_mis_pred_mpki",
    "branch_miss_rate": "br_miss_rate",
    "br_mis_pred_rate": "br_miss_rate",
}

INTERNAL_TARGET_METRICS = {
    "l2i_cache_access_proxy_mpki",
    "l2i_tlb_access_proxy_mpki",
}


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


@dataclass
class FitResult:
    objective: float
    stage_errors: dict
    candidates: list
    weights: list
    repeat_counts: list
    total_instructions: float
    predictions: dict
    history: list = field(default_factory=list)


@dataclass
class StageCandidate:
    candidates: list
    weights: list
    objective: float
    history: list = field(default_factory=list)


@dataclass
class TraceStep:
    stage_name: str
    family: str
    added_case: str
    candidates: list
    weights: list
    objective: float
    predictions: dict
    total_instructions: float


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


def ensure_target(config):
    raw_target = dict(config.get("target", {}))
    ignored_metrics = normalized_metric_name_set(config.get("ignored_metrics", []))
    target = {}
    for key, value in raw_target.items():
        canonical_key = TARGET_KEY_ALIASES.get(key, key)
        if canonical_key in ignored_metrics:
            continue
        if canonical_key in target:
            raise ValueError(
                f"duplicate target metric after alias normalization: {key!r} -> {canonical_key!r}"
            )
        target[canonical_key] = value

    if not target:
        raise ValueError(
            "FIT_CONFIG['target'] is empty. "
            "Please fill the target metrics in icache_hiperf/fit/fitter_config.py, "
            "for example l1i_miss_rate / l2i_miss_rate / l2i_tlb_refill_mpki."
        )

    for key in target:
        if (
            key not in RAW_METRIC_SET
            and key not in DERIVED_KEYS
            and key not in MISS_RATE_SPECS
            and key not in INTERNAL_TARGET_METRICS
            and key != "instructions:u"
        ):
            supported = sorted(
                set(RAW_METRIC_SET)
                | set(DERIVED_KEYS)
                | set(MISS_RATE_SPECS)
                | set(INTERNAL_TARGET_METRICS)
                | {"instructions:u"}
            )
            raise KeyError(
                f"unsupported target metric: {key!r}. "
                f"Known examples include 'br_mis_pred_mpki', 'br_miss_rate', "
                f"'l1i_cache_refill_mpki', 'l2i_tlb_refill_mpki'. "
                f"Supported metrics: {supported}"
            )
    l2i_cache_refill = target.get("l2i_cache_refill_mpki")
    l2i_miss_rate = target.get("l2i_miss_rate")
    if l2i_cache_refill is not None and l2i_miss_rate is not None and "l2i_cache_access_proxy_mpki" not in target:
        target["l2i_cache_access_proxy_mpki"] = safe_div(l2i_cache_refill, l2i_miss_rate)

    l2i_tlb_refill = target.get("l2i_tlb_refill_mpki")
    l2i_tlb_miss_rate = target.get("l2i_tlb_miss_rate")
    if l2i_tlb_refill is not None and l2i_tlb_miss_rate is not None and "l2i_tlb_access_proxy_mpki" not in target:
        target["l2i_tlb_access_proxy_mpki"] = safe_div(l2i_tlb_refill, l2i_tlb_miss_rate)

    return target


def normalized_metric_name_set(metrics):
    normalized = set()
    for metric in metrics:
        canonical = TARGET_KEY_ALIASES.get(metric, metric)
        normalized.add(canonical)
    return normalized


def safe_div(lhs, rhs):
    if lhs is None or rhs is None or abs(rhs) <= EPS:
        return None
    return lhs / rhs


def mpki_metric_to_raw(metric):
    if not metric.endswith("_mpki"):
        return None
    return metric[: -len("_mpki")] + ":u"


def normalize_metric_prediction(metric, mixed_rates, total_instructions):
    if metric == "instructions:u":
        return total_instructions

    if metric == "l2i_cache_access_proxy_mpki":
        return 1000.0 * mixed_rates.get("l1i_cache_refill:u", 0.0)

    if metric == "l2i_tlb_access_proxy_mpki":
        return 1000.0 * mixed_rates.get("l1i_tlb_refill:u", 0.0)

    if metric in RAW_METRIC_SET:
        return mixed_rates.get(metric, 0.0) * total_instructions

    if metric == "ipc":
        cycles_per_instruction = mixed_rates.get("cpu-cycles:u", 0.0)
        return safe_div(1.0, cycles_per_instruction)

    if metric in MISS_RATE_SPECS:
        numerator_key, denominator_key = MISS_RATE_SPECS[metric]
        return safe_div(mixed_rates.get(numerator_key, 0.0), mixed_rates.get(denominator_key, 0.0))

    raw_key = mpki_metric_to_raw(metric)
    if raw_key in RAW_METRIC_SET:
        return 1000.0 * mixed_rates.get(raw_key, 0.0)

    raise KeyError(f"unsupported metric: {metric}")


def metric_derivative(metric, mixed_rates, candidate, total_instructions):
    rates = candidate.per_instruction

    if metric == "instructions:u":
        return 0.0

    if metric == "l2i_cache_access_proxy_mpki":
        return 1000.0 * rates.get("l1i_cache_refill:u", 0.0)

    if metric == "l2i_tlb_access_proxy_mpki":
        return 1000.0 * rates.get("l1i_tlb_refill:u", 0.0)

    if metric in RAW_METRIC_SET:
        return total_instructions * rates.get(metric, 0.0)

    if metric == "ipc":
        cycles_per_instruction = mixed_rates.get("cpu-cycles:u", 0.0)
        if cycles_per_instruction <= EPS:
            return 0.0
        return -rates.get("cpu-cycles:u", 0.0) / (cycles_per_instruction * cycles_per_instruction)

    if metric in MISS_RATE_SPECS:
        numerator_key, denominator_key = MISS_RATE_SPECS[metric]
        numerator = mixed_rates.get(numerator_key, 0.0)
        denominator = mixed_rates.get(denominator_key, 0.0)
        if denominator <= EPS:
            return 0.0
        return (
            rates.get(numerator_key, 0.0) * denominator
            - numerator * rates.get(denominator_key, 0.0)
        ) / (denominator * denominator)

    raw_key = mpki_metric_to_raw(metric)
    if raw_key in RAW_METRIC_SET:
        return 1000.0 * rates.get(raw_key, 0.0)

    raise KeyError(f"unsupported metric: {metric}")


def is_blank_row(row):
    for key, value in row.items():
        if key.startswith("__"):
            continue
        if str(value).strip():
            return False
    return True


def build_candidate(row, outer_iters):
    module = str(row.get("module", "")).strip()
    case = str(row.get("case", "")).strip()
    if not module or not case:
        return None

    raw_counts = {}
    for key in METRIC_KEYS:
        value = parse_number(row.get(key))
        if value is None:
            return None
        raw_counts[key] = value / outer_iters

    unit_instructions = raw_counts["instructions:u"]
    if unit_instructions <= EPS:
        return None

    per_instruction = {}
    for key in METRIC_KEYS:
        if key == "instructions:u":
            per_instruction[key] = 1.0
        else:
            per_instruction[key] = raw_counts[key] / unit_instructions

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
            candidate = build_candidate(row, config["outer_iters"])
            if candidate is not None:
                candidates.append(candidate)

    if not candidates:
        raise ValueError("no usable candidate rows found in the configured CSV files")
    return candidates


def mix_rates(candidates, weights):
    mixed = {key: 0.0 for key in METRIC_KEYS}
    for weight, candidate in zip(weights, candidates):
        if weight <= 0.0:
            continue
        for key in METRIC_KEYS:
            mixed[key] += weight * candidate.per_instruction[key]
    mixed["instructions:u"] = 1.0
    return mixed


def raw_metric_to_mpki(raw_key):
    if raw_key in {"instructions:u", "cpu-cycles:u"}:
        return None
    if not raw_key.endswith(":u"):
        return None
    return raw_key[: -len(":u")] + "_mpki"


def candidate_metric_mpki(candidate, raw_key):
    mpki_key = raw_metric_to_mpki(raw_key)
    if mpki_key is None:
        return None
    value = parse_number(candidate.row.get(mpki_key))
    if value is not None:
        return value
    per_instruction = candidate.per_instruction.get(raw_key)
    if per_instruction is None:
        return None
    return per_instruction * 1000.0


def effective_repeat_amount(candidate, raw_key, repeat_amount, config=None):
    if repeat_amount <= 0.0:
        return 0.0
    if raw_key == "instructions:u":
        return repeat_amount

    cfg = FIT_CONFIG if config is None else config
    stable_modules = {
        str(name).strip()
        for name in cfg.get("stable_low_mpki_modules", [])
        if str(name).strip()
    }
    if stable_modules and candidate.module not in stable_modules:
        return repeat_amount

    threshold = float(cfg.get("stable_low_mpki_threshold", 0.0) or 0.0)
    if threshold <= 0.0:
        return repeat_amount

    mpki_value = candidate_metric_mpki(candidate, raw_key)
    if mpki_value is None:
        return repeat_amount
    if mpki_value < threshold:
        return 1.0
    return repeat_amount


def totals_from_repeat_amounts(candidates, repeat_amounts, config=None):
    totals = {key: 0.0 for key in METRIC_KEYS}
    for repeat_amount, candidate in zip(repeat_amounts, candidates):
        if repeat_amount <= 0.0:
            continue
        totals["instructions:u"] += repeat_amount * candidate.unit_counts["instructions:u"]
        for key in METRIC_KEYS:
            if key == "instructions:u":
                continue
            effective_repeat = effective_repeat_amount(candidate, key, repeat_amount, config)
            totals[key] += effective_repeat * candidate.unit_counts[key]
    return totals


def continuous_exec_instructions(candidates, weights):
    total = 0.0
    for candidate, weight in zip(candidates, weights):
        if weight <= 0.0:
            continue
        total += weight * candidate.unit_instructions
    return total


def predictions_from_weights(candidates, weights, target, total_instructions=None):
    if total_instructions is None:
        total_instructions = continuous_exec_instructions(candidates, weights)
    repeat_amounts = []
    for candidate, weight in zip(candidates, weights):
        if weight <= 0.0:
            repeat_amounts.append(0.0)
            continue
        repeat_amounts.append(weight * total_instructions / max(candidate.unit_instructions, EPS))
    totals = totals_from_repeat_amounts(candidates, repeat_amounts)
    predictions, exec_instructions = predictions_from_totals(totals, target)
    return predictions, exec_instructions


def make_scales(target):
    scales = {}
    for metric, value in target.items():
        if metric in MISS_RATE_SPECS:
            scales[metric] = max(abs(value), 1e-4)
        elif metric.endswith("_mpki") or metric == "ipc":
            scales[metric] = max(abs(value), 1e-3)
        else:
            scales[metric] = max(abs(value), 1.0)
    return scales


def active_stage_metrics(config, target):
    active = {}
    for stage_name, metrics in config["stage_metrics"].items():
        usable = [metric for metric in metrics if metric in target]
        if usable:
            active[stage_name] = usable
    return active


def metric_weights(config, target):
    weights = {metric: 1.0 for metric in target}
    for stage_name, metrics in active_stage_metrics(config, target).items():
        stage_weight = float(config["stage_weights"].get(stage_name, 1.0))
        for metric in metrics:
            weights[metric] = stage_weight

    for metric, value in config.get("metric_weight_overrides", {}).items():
        if metric in weights:
            weights[metric] *= float(value)
    return weights


def parallel_workers(config):
    workers = int(config.get("parallel_workers", 0) or 0)
    if workers > 0:
        return workers
    return min(8, max(1, os.cpu_count() or 1))


def chunked(items, size):
    size = max(1, int(size))
    for index in range(0, len(items), size):
        yield items[index : index + size]


def subset_dict(mapping, keys):
    return {key: mapping[key] for key in keys if key in mapping}


def stage_metric_list(config, target, stage_definition):
    metrics = []
    active = active_stage_metrics(config, target)
    for group_name in stage_definition["metric_groups"]:
        metrics.extend(active.get(group_name, []))
    deduped = []
    seen = set()
    for metric in metrics:
        if metric in seen:
            continue
        seen.add(metric)
        deduped.append(metric)
    return deduped


def objective_and_gradient(candidates, weights, target, scales, metric_weight_map, total_instructions):
    mixed_rates = mix_rates(candidates, weights)
    objective = 0.0
    gradient = [0.0] * len(candidates)

    for metric, target_value in target.items():
        prediction = normalize_metric_prediction(metric, mixed_rates, total_instructions)
        if prediction is None or not math.isfinite(prediction):
            return 1e30, [0.0] * len(candidates)

        scale = scales[metric]
        metric_weight = metric_weight_map[metric]
        delta = (prediction - target_value) / scale
        objective += metric_weight * delta * delta

        for index, candidate in enumerate(candidates):
            derivative = metric_derivative(metric, mixed_rates, candidate, total_instructions)
            gradient[index] += 2.0 * metric_weight * delta * (derivative / scale)

    return objective, gradient


def project_to_simplex(values):
    if not values:
        return []
    sorted_values = sorted(values, reverse=True)
    prefix_sum = 0.0
    rho = -1
    theta = 0.0
    for index, value in enumerate(sorted_values):
        prefix_sum += value
        candidate = (prefix_sum - 1.0) / (index + 1)
        if value - candidate > 0.0:
            rho = index
            theta = candidate
    if rho == -1:
        return [1.0 / len(values)] * len(values)
    theta = (sum(sorted_values[: rho + 1]) - 1.0) / (rho + 1)
    return [max(value - theta, 0.0) for value in values]


def solve_simplex_weights(candidates, target, scales, metric_weight_map, total_instructions, iterations):
    if len(candidates) == 1:
        return [1.0]

    weights = [1.0 / len(candidates)] * len(candidates)
    best = weights[:]
    best_objective, _ = objective_and_gradient(
        candidates,
        weights,
        target,
        scales,
        metric_weight_map,
        total_instructions,
    )
    step = 0.4

    for _ in range(iterations):
        current_objective, gradient = objective_and_gradient(
            candidates,
            weights,
            target,
            scales,
            metric_weight_map,
            total_instructions,
        )
        trial = project_to_simplex(
            [value - step * delta for value, delta in zip(weights, gradient)]
        )
        trial_objective, _ = objective_and_gradient(
            candidates,
            trial,
            target,
            scales,
            metric_weight_map,
            total_instructions,
        )

        if trial_objective + 1e-12 < current_objective:
            weights = trial
            if trial_objective < best_objective:
                best = trial[:]
                best_objective = trial_objective
            step = min(step * 1.1, 1.0)
        else:
            step *= 0.5
            if step < 1e-8:
                break

    return best


def target_count_for_metric(metric, target, total_instructions):
    if metric == "instructions:u":
        return total_instructions
    target_counts = count_view_from_metrics(target, total_instructions)
    return target_counts.get(metric)


def row_prediction(candidate, target, total_instructions, scale_metric=None, config=None):
    repeat_amount = None
    if scale_metric:
        target_value = target_count_for_metric(scale_metric, target, total_instructions)
        unit_value = candidate.unit_counts.get(scale_metric)
        if target_value is not None and unit_value is not None and abs(unit_value) > EPS:
            repeat_amount = target_value / unit_value
    if repeat_amount is None:
        repeat_amount = total_instructions / max(candidate.unit_instructions, EPS)
    totals = totals_from_repeat_amounts([candidate], [repeat_amount], config=config)
    predictions, _ = predictions_from_totals(totals, target)
    return predictions


def single_row_error(candidate, target, scales, metrics, total_instructions, scale_metric=None, config=None):
    prediction = row_prediction(candidate, target, total_instructions, scale_metric=scale_metric, config=config)
    total = 0.0
    for metric in metrics:
        if metric not in target:
            continue
        predicted = prediction[metric]
        target_value = target[metric]
        scale = scales[metric]
        delta = (predicted - target_value) / scale
        total += delta * delta
    return total


def candidate_allowed(candidate, config):
    excluded = config.get("family_excluded_param_values", {}).get(candidate.module, {})
    for key, blocked_values in excluded.items():
        actual = str(candidate.row.get(key, "")).strip()
        blocked = {str(value).strip() for value in blocked_values}
        if actual in blocked:
            return False
    return True


def family_candidate_pool(candidates, config, target, scales):
    by_family = {}
    for candidate in candidates:
        if not candidate_allowed(candidate, config):
            continue
        by_family.setdefault(candidate.module, []).append(candidate)

    result = {}
    family_focus = config.get("family_focus_metrics", {})
    family_scale_metric = config.get("family_focus_scale_metric", {})
    keep_per_family = config.get("candidate_pool_per_family", {})
    total_instructions = float(config["fit_total_instructions"])

    for family, family_rows in by_family.items():
        wanted = keep_per_family.get(family, len(family_rows))
        metrics = [metric for metric in family_focus.get(family, []) if metric in target]
        if not metrics:
            metrics = list(target.keys())
        scale_metric = family_scale_metric.get(family)

        ranked = sorted(
            family_rows,
            key=lambda candidate: (
                single_row_error(
                    candidate,
                    target,
                    scales,
                    metrics,
                    total_instructions,
                    scale_metric=scale_metric,
                    config=config,
                ),
                candidate.case,
            ),
        )
        if wanted in (None, "all"):
            result[family] = ranked
        else:
            wanted = int(wanted)
            if wanted <= 0 or wanted >= len(ranked):
                result[family] = ranked
            else:
                result[family] = ranked[:wanted]
    return result


def totals_from_repeat_counts(candidates, repeat_counts):
    return totals_from_repeat_amounts(candidates, repeat_counts)


def predictions_from_totals(totals, target):
    total_instructions = totals.get("instructions:u", 0.0)
    if total_instructions <= EPS:
        return {metric: None for metric in target}, 0.0

    mixed_rates = {}
    for key in METRIC_KEYS:
        if key == "instructions:u":
            mixed_rates[key] = 1.0
        else:
            mixed_rates[key] = totals[key] / total_instructions

    predictions = {
        metric: normalize_metric_prediction(metric, mixed_rates, total_instructions)
        for metric in target
    }
    return predictions, total_instructions


def score_predictions(predictions, target, scales, metric_weight_map):
    total = 0.0
    for metric, target_value in target.items():
        predicted = predictions.get(metric)
        if predicted is None or not math.isfinite(predicted):
            return 1e30
        delta = (predicted - target_value) / scales[metric]
        total += metric_weight_map[metric] * delta * delta
    return total


def repeat_counts_from_weights(candidates, weights, instruction_budget):
    if not candidates or not weights:
        return []

    counts = []
    for weight, candidate in zip(weights, candidates):
        if weight <= 1e-9:
            counts.append(0)
            continue
        nominal = weight * instruction_budget / candidate.unit_instructions
        count = int(round(nominal))
        if count == 0:
            count = 1
        counts.append(count)

    if all(count == 0 for count in counts):
        best_index = max(range(len(weights)), key=lambda index: weights[index])
        counts[best_index] = 1

    while True:
        totals = totals_from_repeat_counts(candidates, counts)
        if totals["instructions:u"] <= instruction_budget + EPS:
            break
        index = max(
            range(len(counts)),
            key=lambda idx: counts[idx] * candidates[idx].unit_instructions,
        )
        if counts[index] <= 0:
            break
        counts[index] -= 1

    return counts


def scale_repeat_counts_to_budget(candidates, repeat_counts, instruction_budget):
    if not candidates or not repeat_counts:
        return repeat_counts[:]

    totals = totals_from_repeat_counts(candidates, repeat_counts)
    current_instructions = totals.get("instructions:u", 0.0)
    if current_instructions <= EPS:
        return repeat_counts[:]

    scale = instruction_budget / current_instructions
    if scale <= 1.0 + 1e-6:
        return repeat_counts[:]

    scaled = []
    for repeat_count in repeat_counts:
        if repeat_count <= 0:
            scaled.append(0)
            continue
        scaled.append(max(1, int(round(repeat_count * scale))))

    while True:
        totals = totals_from_repeat_counts(candidates, scaled)
        if totals["instructions:u"] <= instruction_budget + EPS:
            break
        index = max(
            range(len(scaled)),
            key=lambda idx: scaled[idx] * candidates[idx].unit_instructions,
        )
        if scaled[index] <= 0:
            break
        scaled[index] -= 1

    return scaled


def refine_repeat_counts(
    candidates,
    repeat_counts,
    instruction_budget,
    target,
    scales,
    metric_weight_map,
    steps,
):
    best = repeat_counts[:]
    best_predictions, best_instructions = predictions_from_totals(
        totals_from_repeat_counts(candidates, best),
        target,
    )
    best_objective = score_predictions(best_predictions, target, scales, metric_weight_map)

    for _ in range(steps):
        improved = False
        for index in range(len(best)):
            for delta in (-1, 1):
                trial = best[:]
                trial[index] += delta
                if trial[index] < 0:
                    continue

                totals = totals_from_repeat_counts(candidates, trial)
                if totals["instructions:u"] > instruction_budget + EPS:
                    continue

                predictions, total_instructions = predictions_from_totals(totals, target)
                objective = score_predictions(predictions, target, scales, metric_weight_map)
                if objective + 1e-12 < best_objective:
                    best = trial
                    best_predictions = predictions
                    best_instructions = total_instructions
                    best_objective = objective
                    improved = True
        if not improved:
            break

    return best, best_predictions, best_instructions, best_objective


def compute_stage_errors(predictions, target, scales, config):
    errors = {}
    for stage_name, metrics in active_stage_metrics(config, target).items():
        total = 0.0
        count = 0
        for metric in metrics:
            predicted = predictions.get(metric)
            if predicted is None or not math.isfinite(predicted):
                total += 1e6
                count += 1
                continue
            delta = (predicted - target[metric]) / scales[metric]
            total += delta * delta
            count += 1
        errors[stage_name] = total / max(count, 1)
    return errors


def component_string(candidates, repeat_counts):
    pieces = []
    for candidate, repeat_count in zip(candidates, repeat_counts):
        if repeat_count <= 0:
            continue
        pieces.append(f"{candidate.case} x {repeat_count}")
    return " | ".join(pieces) if pieces else "(empty)"


def result_signature(candidates, repeat_counts):
    items = []
    for candidate, repeat_count in zip(candidates, repeat_counts):
        if repeat_count <= 0:
            continue
        items.append((candidate.module, candidate.case, int(repeat_count)))
    return tuple(sorted(items))


def continuous_signature(candidates, weights, precision=6):
    items = []
    for candidate, weight in zip(candidates, weights):
        if weight <= 1e-9:
            continue
        items.append((candidate.module, candidate.case, round(float(weight), precision)))
    return tuple(sorted(items))


def weight_string(candidates, weights):
    pieces = []
    for candidate, weight in zip(candidates, weights):
        if weight <= 1e-9:
            continue
        pieces.append(f"{candidate.case}@{weight * 100.0:.2f}%")
    return " | ".join(pieces) if pieces else "(empty)"


def display_source_ref(candidate):
    return f"{Path(candidate.source_csv).name}#{candidate.source_row}"


def candidate_param_summary(candidate):
    pieces = []
    for key in sorted(candidate.row.keys()):
        if key in NON_PARAM_COLUMNS or key.startswith("__"):
            continue
        value = str(candidate.row[key]).strip()
        if value in ("", "0", "0.0"):
            continue
        pieces.append(f"{key}={value}")
    return ", ".join(pieces)


def result_sort_key(result, config):
    stage_order = list(active_stage_metrics(config, config["target"]).keys())
    return tuple(result.stage_errors.get(stage_name, 0.0) for stage_name in stage_order) + (
        result.objective,
        -result.total_instructions,
    )


def solve_stage_combo(combo, metrics, target, scales, metric_weight_map, fit_total_instructions, iterations):
    if not combo:
        target_subset = subset_dict(target, metrics)
        scales_subset = subset_dict(scales, metrics)
        weight_subset = subset_dict(metric_weight_map, metrics)
        zero_predictions = {metric: 0.0 for metric in target_subset}
        objective = score_predictions(zero_predictions, target_subset, scales_subset, weight_subset)
        return StageCandidate(candidates=[], weights=[], objective=objective, history=[])
    target_subset = subset_dict(target, metrics)
    scales_subset = subset_dict(scales, metrics)
    weight_subset = subset_dict(metric_weight_map, metrics)
    weights = solve_simplex_weights(
        combo,
        target_subset,
        scales_subset,
        weight_subset,
        fit_total_instructions,
        iterations,
    )
    objective, _ = objective_and_gradient(
        combo,
        weights,
        target_subset,
        scales_subset,
        weight_subset,
        fit_total_instructions,
    )
    return StageCandidate(candidates=list(combo), weights=weights, objective=objective, history=[])


def _solve_stage_combo_batch(worker_args):
    (
        combo_batch,
        metrics,
        target,
        scales,
        metric_weight_map,
        fit_total_instructions,
        iterations,
    ) = worker_args
    return [
        solve_stage_combo(
            combo,
            metrics,
            target,
            scales,
            metric_weight_map,
            fit_total_instructions,
            iterations,
        )
        for combo in combo_batch
    ]


def with_trace_step(partial, solved, stage_name, family, added_candidate, target, fit_total_instructions):
    del fit_total_instructions
    predictions, total_instructions = predictions_from_weights(
        solved.candidates,
        solved.weights,
        target,
    )
    step = TraceStep(
        stage_name=stage_name,
        family=family,
        added_case=added_candidate.case,
        candidates=list(solved.candidates),
        weights=list(solved.weights),
        objective=solved.objective,
        predictions=predictions,
        total_instructions=total_instructions,
    )
    return StageCandidate(
        candidates=list(solved.candidates),
        weights=list(solved.weights),
        objective=solved.objective,
        history=list(partial.history) + [step],
    )


def merge_stage_candidate(store, candidate):
    signature = continuous_signature(candidate.candidates, candidate.weights)
    previous = store.get(signature)
    if previous is None or candidate.objective < previous.objective:
        store[signature] = candidate


def expand_family_stage(
    partials,
    stage_name,
    family_rows,
    family_limit,
    metrics,
    target,
    scales,
    metric_weight_map,
    fit_total_instructions,
    iterations,
    beam_size,
    max_components,
    executor=None,
    parallel_chunk_size=64,
):
    accumulated = {}

    frontier = list(partials)
    for _ in range(max(0, family_limit)):
        expanded = {}
        combo_specs = []
        for partial in frontier:
            carried = solve_stage_combo(
                partial.candidates,
                metrics,
                target,
                scales,
                metric_weight_map,
                fit_total_instructions,
                iterations,
            )
            carried.history = list(partial.history)
            merge_stage_candidate(accumulated, carried)
            merge_stage_candidate(expanded, carried)

            used_keys = {
                (candidate.module, candidate.case)
                for candidate in partial.candidates
                if candidate.module == family_rows[0].module
            } if family_rows else set()

            for candidate in family_rows:
                if (candidate.module, candidate.case) in used_keys:
                    continue
                combo = list(partial.candidates) + [candidate]
                if len(combo) > max_components:
                    continue
                combo_specs.append((partial, candidate, combo))

        if executor is not None and len(combo_specs) > max(64, parallel_chunk_size):
            worker_args = [
                (
                    [spec[2] for spec in combo_batch],
                    metrics,
                    target,
                    scales,
                    metric_weight_map,
                    fit_total_instructions,
                    iterations,
                )
                for combo_batch in chunked(combo_specs, parallel_chunk_size)
            ]
            for combo_batch, solved_batch in zip(chunked(combo_specs, parallel_chunk_size), executor.map(_solve_stage_combo_batch, worker_args)):
                for (partial, candidate, _combo), solved in zip(combo_batch, solved_batch):
                    traced = with_trace_step(
                        partial,
                        solved,
                        stage_name,
                        family_rows[0].module if family_rows else "",
                        candidate,
                        target,
                        fit_total_instructions,
                    )
                    merge_stage_candidate(expanded, traced)
        else:
            for partial, candidate, combo in combo_specs:
                solved = solve_stage_combo(
                    combo,
                    metrics,
                    target,
                    scales,
                    metric_weight_map,
                    fit_total_instructions,
                    iterations,
                )
                traced = with_trace_step(
                    partial,
                    solved,
                    stage_name,
                    family_rows[0].module if family_rows else "",
                    candidate,
                    target,
                    fit_total_instructions,
                )
                merge_stage_candidate(expanded, traced)

        if not expanded:
            break

        frontier = sorted(expanded.values(), key=lambda item: item.objective)[:beam_size]
        for item in frontier:
            merge_stage_candidate(accumulated, item)

    return sorted(accumulated.values(), key=lambda item: item.objective)[:beam_size]


def stagewise_candidates(candidates_by_family, config, target, scales, metric_weight_map):
    fit_total_instructions = float(config["fit_total_instructions"])
    iterations = int(config["solver_iterations"])
    configured_max = config.get("max_components")
    if configured_max in (None, "", 0):
        max_components = sum(
            max(0, int(config["family_limits"].get(stage_definition["family"], 0)))
            for stage_definition in config["search_stages"]
        )
    else:
        max_components = int(configured_max)
    workers = parallel_workers(config)
    parallel_chunk_size = int(config.get("parallel_chunk_size", 64))

    partials = [StageCandidate(candidates=[], weights=[], objective=0.0)]
    if workers <= 1:
        for stage_definition in config["search_stages"]:
            family = stage_definition["family"]
            metrics = stage_metric_list(config, target, stage_definition)
            beam_size = int(stage_definition["beam_size"])
            family_rows = candidates_by_family.get(family, [])
            family_limit = int(config["family_limits"].get(family, 0))
            partials = expand_family_stage(
                partials,
                family,
                family_rows,
                family_limit,
                metrics,
                target,
                scales,
                metric_weight_map,
                fit_total_instructions,
                iterations,
                beam_size,
                max_components,
                executor=None,
                parallel_chunk_size=parallel_chunk_size,
            )
        return partials

    try:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            for stage_definition in config["search_stages"]:
                family = stage_definition["family"]
                metrics = stage_metric_list(config, target, stage_definition)
                beam_size = int(stage_definition["beam_size"])
                family_rows = candidates_by_family.get(family, [])
                family_limit = int(config["family_limits"].get(family, 0))
                partials = expand_family_stage(
                    partials,
                    family,
                    family_rows,
                    family_limit,
                    metrics,
                    target,
                    scales,
                    metric_weight_map,
                    fit_total_instructions,
                    iterations,
                    beam_size,
                    max_components,
                    executor=executor,
                    parallel_chunk_size=parallel_chunk_size,
                )
        return partials
    except (OSError, PermissionError):
        for stage_definition in config["search_stages"]:
            family = stage_definition["family"]
            metrics = stage_metric_list(config, target, stage_definition)
            beam_size = int(stage_definition["beam_size"])
            family_rows = candidates_by_family.get(family, [])
            family_limit = int(config["family_limits"].get(family, 0))
            partials = expand_family_stage(
                partials,
                family,
                family_rows,
                family_limit,
                metrics,
                target,
                scales,
                metric_weight_map,
                fit_total_instructions,
                iterations,
                beam_size,
                max_components,
                executor=None,
                parallel_chunk_size=parallel_chunk_size,
            )

    return partials


def search_results(candidates_by_family, config, target, scales, metric_weight_map):
    family_limits = config["family_limits"]
    fit_total_instructions = float(config["fit_total_instructions"])
    max_total_instructions = float(config["max_total_instructions"])
    refine_steps = int(config["repeat_refine_steps"])

    stage_keys = list(active_stage_metrics(config, target).keys())
    results = []
    best_by_signature = {}

    for stage_candidate in stagewise_candidates(candidates_by_family, config, target, scales, metric_weight_map):
        combo = stage_candidate.candidates
        weights = stage_candidate.weights
        if not combo or not weights:
            continue
        repeat_counts = repeat_counts_from_weights(combo, weights, max_total_instructions)
        if not repeat_counts:
            continue
        if config.get("fill_instruction_budget", True):
            repeat_counts = scale_repeat_counts_to_budget(combo, repeat_counts, max_total_instructions)
        repeat_counts, predictions, total_instructions, objective = refine_repeat_counts(
            combo,
            repeat_counts,
            max_total_instructions,
            target,
            scales,
            metric_weight_map,
            refine_steps,
        )
        stage_errors = compute_stage_errors(predictions, target, scales, config)

        result = FitResult(
            objective=objective,
            stage_errors=stage_errors,
            candidates=combo,
            weights=weights,
            repeat_counts=repeat_counts,
            total_instructions=total_instructions,
            predictions=predictions,
            history=list(stage_candidate.history),
        )
        signature = result_signature(combo, repeat_counts)
        previous = best_by_signature.get(signature)
        if previous is None or result.objective < previous.objective:
            best_by_signature[signature] = result

    results = list(best_by_signature.values())
    results.sort(
        key=lambda result: tuple(result.stage_errors.get(stage_name, 0.0) for stage_name in stage_keys)
        + (result.objective, -result.total_instructions)
    )
    return results[: config["top_k"]]


def print_target(target):
    print("== Target ==")
    for key, value in target.items():
        if key in INTERNAL_TARGET_METRICS:
            continue
        print(f"  {key} = {format_metric_value(key, value)}")
    print()


def print_ignored_metrics(config):
    ignored_metrics = sorted(normalized_metric_name_set(config.get("ignored_metrics", [])))
    if not ignored_metrics:
        return
    print("== Ignored Metrics ==")
    for metric in ignored_metrics:
        print(f"  {metric}")
    print()


def is_rate_metric(metric):
    return metric in MISS_RATE_SPECS


def format_metric_value(metric, value):
    if value is None:
        return "NA"
    if is_rate_metric(metric):
        return f"{value * 100.0:.4f}%"
    return f"{value:.6f}"


def count_from_mpki(mpki_value, total_instructions):
    if mpki_value is None or total_instructions is None:
        return None
    return mpki_value * total_instructions / 1000.0


def access_from_refill_and_rate(refill_count, miss_rate):
    if refill_count is None or miss_rate is None or abs(miss_rate) <= EPS:
        return None
    return refill_count / miss_rate


def count_view_from_metrics(metrics, total_instructions):
    if total_instructions is None or total_instructions <= EPS:
        return {}

    l1i_cache_refill = count_from_mpki(metrics.get("l1i_cache_refill_mpki"), total_instructions)
    l2i_cache_refill = count_from_mpki(metrics.get("l2i_cache_refill_mpki"), total_instructions)
    l1i_tlb_refill = count_from_mpki(metrics.get("l1i_tlb_refill_mpki"), total_instructions)
    l2i_tlb_refill = count_from_mpki(metrics.get("l2i_tlb_refill_mpki"), total_instructions)

    return {
        "instructions:u": total_instructions,
        "l1i_cache_refill:u": l1i_cache_refill,
        "l1i_cache:u": access_from_refill_and_rate(l1i_cache_refill, metrics.get("l1i_miss_rate")),
        "l2i_cache_refill:u": l2i_cache_refill,
        "l2i_cache:u": access_from_refill_and_rate(l2i_cache_refill, metrics.get("l2i_miss_rate")),
        "l1i_tlb_refill:u": l1i_tlb_refill,
        "l1i_tlb:u": access_from_refill_and_rate(l1i_tlb_refill, metrics.get("l1i_tlb_miss_rate")),
        "l2i_tlb_refill:u": l2i_tlb_refill,
        "l2i_tlb:u": access_from_refill_and_rate(l2i_tlb_refill, metrics.get("l2i_tlb_miss_rate")),
    }


def format_count_value(value):
    if value is None or not math.isfinite(value):
        return "NA"
    abs_value = abs(value)
    if abs_value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f}G"
    if abs_value >= 1_000_000:
        return f"{value / 1_000_000:.2f}M"
    if abs_value >= 1_000:
        return f"{value / 1_000:.2f}K"
    return f"{value:.2f}"


def print_table(headers, rows, indent="    "):
    widths = [len(str(header)) for header in headers]
    normalized_rows = []
    for row in rows:
        normalized = [str(cell) for cell in row]
        normalized_rows.append(normalized)
        for index, cell in enumerate(normalized):
            widths[index] = max(widths[index], len(cell))

    def fmt_row(values):
        return indent + "  " + " | ".join(value.ljust(widths[index]) for index, value in enumerate(values))

    print(fmt_row(headers))
    print(indent + "  " + "-+-".join("-" * width for width in widths))
    for row in normalized_rows:
        print(fmt_row(row))


def print_count_view(target_metrics, predicted_metrics, target_total_instructions, exec_total_instructions, indent="    "):
    target_counts = count_view_from_metrics(target_metrics, target_total_instructions)
    predicted_counts = count_view_from_metrics(predicted_metrics, exec_total_instructions)
    ordered = [
        "instructions:u",
        "l1i_cache:u",
        "l1i_cache_refill:u",
        "l2i_cache:u",
        "l2i_cache_refill:u",
        "l1i_tlb:u",
        "l1i_tlb_refill:u",
        "l2i_tlb:u",
        "l2i_tlb_refill:u",
    ]
    print(f"{indent}pmu_counts:")
    rows = []
    for key in ordered:
        target_value = target_counts.get(key)
        predicted_value = predicted_counts.get(key)
        delta = None if target_value is None or predicted_value is None else predicted_value - target_value
        rows.append([
            key,
            format_count_value(target_value),
            format_count_value(predicted_value),
            format_count_value(delta),
        ])
    print_table(["event", "target", "exec", "delta"], rows, indent=indent)


def project_trace_execution(step, target, config):
    instruction_budget = float(config.get("max_total_instructions", config.get("fit_total_instructions", 0.0)))
    if instruction_budget <= EPS:
        return [], step.predictions, step.total_instructions, step.objective

    repeat_counts = repeat_counts_from_weights(step.candidates, step.weights, instruction_budget)
    if not repeat_counts:
        return [], step.predictions, step.total_instructions, step.objective
    if config.get("fill_instruction_budget", True):
        repeat_counts = scale_repeat_counts_to_budget(step.candidates, repeat_counts, instruction_budget)

    scales = make_scales(target)
    metric_weight_map = metric_weights(config, target)
    refine_steps = int(config.get("trace_repeat_refine_steps", min(32, int(config.get("repeat_refine_steps", 0)))))
    repeat_counts, predictions, total_instructions, objective = refine_repeat_counts(
        step.candidates,
        repeat_counts,
        instruction_budget,
        target,
        scales,
        metric_weight_map,
        refine_steps,
    )
    return repeat_counts, predictions, total_instructions, objective


def relative_error(target_value, predicted):
    if predicted is None:
        return None
    denom = max(abs(target_value), 1e-9)
    return abs(predicted - target_value) / denom


def metric_display_order(target):
    rate_metrics = [
        "br_miss_rate",
        "l1i_miss_rate",
        "l2i_miss_rate",
        "l1i_tlb_miss_rate",
        "l2i_tlb_miss_rate",
    ]
    mpki_and_raw_metrics = [
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
        "ipc",
        "instructions:u",
    ]
    preferred = rate_metrics + mpki_and_raw_metrics
    ordered = [metric for metric in preferred if metric in target and metric not in INTERNAL_TARGET_METRICS]
    for metric in target:
        if metric not in ordered and metric not in INTERNAL_TARGET_METRICS:
            ordered.append(metric)
    return ordered


def print_metric_blocks(target, predictions, indent="    "):
    ordered_metrics = metric_display_order(target)
    rate_metrics = [metric for metric in ordered_metrics if is_rate_metric(metric)]
    other_metrics = [metric for metric in ordered_metrics if not is_rate_metric(metric)]

    if rate_metrics:
        print(f"{indent}miss_rate:")
        rows = []
        for metric in rate_metrics:
            target_value = target[metric]
            predicted = predictions.get(metric)
            delta = None if predicted is None else predicted - target_value
            rel = relative_error(target_value, predicted)
            rel_text = "NA" if rel is None else f"{rel * 100.0:.2f}%"
            rows.append([
                metric,
                format_metric_value(metric, target_value),
                format_metric_value(metric, predicted),
                format_metric_value(metric, delta) if delta is not None else "NA",
                rel_text,
            ])
        print_table(["metric", "target", "exec", "delta", "rel_err"], rows, indent=indent)

    if other_metrics:
        print(f"{indent}mpki_and_raw:")
        rows = []
        for metric in other_metrics:
            target_value = target[metric]
            predicted = predictions.get(metric)
            delta = None if predicted is None else predicted - target_value
            rel = relative_error(target_value, predicted)
            rel_text = "NA" if rel is None else f"{rel * 100.0:.2f}%"
            rows.append([
                metric,
                format_metric_value(metric, target_value),
                format_metric_value(metric, predicted),
                format_metric_value(metric, delta) if delta is not None else "NA",
                rel_text,
            ])
        print_table(["metric", "target", "exec", "delta", "rel_err"], rows, indent=indent)


def print_selection_trace(result, target, config):
    if not result.history:
        return
    target_total_instructions = float(config.get("fit_total_instructions", 0.0))
    print("    selection_trace:")
    for index, step in enumerate(result.history, start=1):
        added_weight = 0.0
        for candidate, weight in zip(step.candidates, step.weights):
            if candidate.case == step.added_case:
                added_weight = max(added_weight, float(weight))
        if added_weight <= 1e-6:
            continue
        stage_repeat_counts, stage_predictions, stage_exec_instructions, stage_exec_objective = project_trace_execution(
            step,
            target,
            config,
        )
        print(
            f"      step {index}: add {step.family}:{step.added_case} "
            f"(search_obj={step.objective:.8f}, exec_obj={stage_exec_objective:.8f}, "
            f"native_instructions={format_count_value(step.total_instructions)}, "
            f"exec_instructions={format_count_value(stage_exec_instructions)})"
        )
        print(f"        instruction_mix_continuous: {weight_string(step.candidates, step.weights)}")
        if stage_repeat_counts:
            print(f"        repeat_plan_integer: {component_string(step.candidates, stage_repeat_counts)}")
        print_count_view(target, stage_predictions, target_total_instructions, stage_exec_instructions, indent="        ")


def print_result(rank, result, target, config):
    stage_order = list(active_stage_metrics(config, target).keys())
    print(f"[{rank}] objective={result.objective:.8f} total_instructions={result.total_instructions:.4f}")
    for stage_name in stage_order:
        print(f"    {stage_name}_error={result.stage_errors.get(stage_name, 0.0):.8f}")
    print(f"    instruction_mix_continuous: {weight_string(result.candidates, result.weights)}")
    print(f"    repeat_plan_integer: {component_string(result.candidates, result.repeat_counts)}")
    for candidate, repeat_count in zip(result.candidates, result.repeat_counts):
        if repeat_count <= 0:
            continue
        print(
            f"      - {candidate.module}:{candidate.case} "
            f"(unit_instructions={candidate.unit_instructions:.4f}, source={display_source_ref(candidate)})"
        )
        summary = candidate_param_summary(candidate)
        if summary:
            print(f"        {summary}")

    trace_top_k = int(config.get("trace_top_k", 1))
    if rank <= trace_top_k:
        print_selection_trace(result, target, config)

    print_metric_blocks(target, result.predictions, indent="    ")
    print()


def write_results_csv(path, results, target, config):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    stage_order = list(active_stage_metrics(config, target).keys())
    headers = [
        "rank",
        "objective",
        *[f"stage::{stage_name}" for stage_name in stage_order],
        "total_instructions",
        "continuous_weights",
        "repeat_plan",
    ]
    for metric in metric_display_order(target):
        headers.extend([f"target::{metric}", f"exec::{metric}", f"delta::{metric}", f"rel_err::{metric}"])

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        for rank, result in enumerate(results, start=1):
            row = {
                "rank": rank,
                "objective": f"{result.objective:.8f}",
                "total_instructions": f"{result.total_instructions:.4f}",
                "continuous_weights": weight_string(result.candidates, result.weights),
                "repeat_plan": component_string(result.candidates, result.repeat_counts),
            }
            for stage_name in stage_order:
                row[f"stage::{stage_name}"] = f"{result.stage_errors.get(stage_name, 0.0):.8f}"
            for metric in metric_display_order(target):
                target_value = target[metric]
                predicted = result.predictions.get(metric)
                delta = None if predicted is None else predicted - target_value
                rel = relative_error(target_value, predicted)
                row[f"target::{metric}"] = f"{target_value:.6f}"
                row[f"exec::{metric}"] = "" if predicted is None else f"{predicted:.6f}"
                row[f"delta::{metric}"] = "" if delta is None else f"{delta:.6f}"
                row[f"rel_err::{metric}"] = "" if rel is None else f"{rel:.6f}"
            writer.writerow(row)


def result_json_record(rank, result, target, config):
    stage_order = list(active_stage_metrics(config, target).keys())
    metric_order = metric_display_order(target)

    def metric_block(metric_names):
        block = {}
        for metric in metric_names:
            predicted = result.predictions.get(metric)
            delta = None if predicted is None else predicted - target[metric]
            rel = relative_error(target[metric], predicted)
            block[metric] = {
                "target": target[metric],
                "exec": predicted,
                "delta": delta,
                "rel_err": rel,
            }
        return block

    components = []
    repeat_plan = []
    for candidate, weight, repeat_count in zip(result.candidates, result.weights, result.repeat_counts):
        if weight <= 1e-9 and repeat_count <= 0:
            continue
        param_map = {}
        for key in sorted(candidate.row.keys()):
            if key in NON_PARAM_COLUMNS or key.startswith("__"):
                continue
            value = candidate.row[key]
            text = str(value).strip()
            if text == "":
                continue
            parsed = parse_number(value)
            if parsed is not None and abs(parsed - round(parsed)) <= 1e-9:
                param_map[key] = int(round(parsed))
            elif parsed is not None:
                param_map[key] = parsed
            else:
                param_map[key] = text

        record = {
            "module": candidate.module,
            "case": candidate.case,
            "source_csv": Path(candidate.source_csv).name,
            "source_row": candidate.source_row,
            "unit_instructions": candidate.unit_instructions,
            "instruction_share": float(weight),
            "repeat_count": int(repeat_count),
            "params": param_map,
        }
        components.append(record)
        if repeat_count > 0:
            repeat_plan.append(record)

    trace = []
    for step in result.history:
        trace.append(
            {
                "stage_name": step.stage_name,
                "family": step.family,
                "added_case": step.added_case,
                "objective": step.objective,
                "native_instructions": step.total_instructions,
                "instruction_mix_continuous": [
                    {
                        "module": candidate.module,
                        "case": candidate.case,
                        "instruction_share": float(weight),
                    }
                    for candidate, weight in zip(step.candidates, step.weights)
                    if weight > 1e-9
                ],
            }
        )

    return {
        "rank": rank,
        "objective": result.objective,
        "stage_errors": {stage_name: result.stage_errors.get(stage_name, 0.0) for stage_name in stage_order},
        "total_instructions": result.total_instructions,
        "continuous_weights_text": weight_string(result.candidates, result.weights),
        "repeat_plan_text": component_string(result.candidates, result.repeat_counts),
        "components": components,
        "repeat_plan": repeat_plan,
        "target_metrics": {metric: target[metric] for metric in metric_order},
        "fit_metrics": {metric: result.predictions.get(metric) for metric in metric_order},
        "metric_compare": metric_block(metric_order),
        "selection_trace": trace,
    }


def write_results_json(path, results, target, config):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    records = [result_json_record(rank, result, target, config) for rank, result in enumerate(results, start=1)]
    payload = {
        "config": {
            "max_total_instructions": config.get("max_total_instructions"),
            "fit_total_instructions": config.get("fit_total_instructions"),
            "outer_iters": config.get("outer_iters"),
            "family_limits": config.get("family_limits"),
            "search_stages": config.get("search_stages"),
        },
        "results": records,
    }
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def write_best_result_json(path, results, target, config):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    best = result_json_record(1, results[0], target, config)
    payload = {
        "config": {
            "max_total_instructions": config.get("max_total_instructions"),
            "fit_total_instructions": config.get("fit_total_instructions"),
            "outer_iters": config.get("outer_iters"),
            "family_limits": config.get("family_limits"),
            "search_stages": config.get("search_stages"),
        },
        "best_result": best,
    }
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def main():
    config = dict(FIT_CONFIG)
    target = ensure_target(config)
    config["target"] = target
    scales = make_scales(target)
    metric_weight_map = metric_weights(config, target)

    candidates = load_candidates(config)
    candidates_by_family = family_candidate_pool(candidates, config, target, scales)

    print_ignored_metrics(config)
    print_target(target)
    print("== Candidate Pool ==")
    for family, family_rows in candidates_by_family.items():
        labels = ", ".join(candidate.case for candidate in family_rows[:8])
        tail = "" if len(family_rows) <= 8 else ", ..."
        print(f"{family}: {len(family_rows)} rows kept -> {labels}{tail}")
    print()

    results = search_results(candidates_by_family, config, target, scales, metric_weight_map)
    if not results:
        raise ValueError("no fit result found; check target metrics and candidate pools")

    print("== Best Fits ==")
    for rank, result in enumerate(results, start=1):
        print_result(rank, result, target, config)

    write_results_csv(config["result_csv"], results, target, config)
    write_results_json(config["result_json"], results, target, config)
    write_best_result_json(config["best_result_json"], results, target, config)
    print(f"results written to {config['result_csv']}")
    print(f"json written to {config['result_json']}")
    print(f"best fit json written to {config['best_result_json']}")


if __name__ == "__main__":
    main()
