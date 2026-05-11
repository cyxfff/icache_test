#!/usr/bin/env python3

import argparse
import json
import math
import multiprocessing as mp
import sys
from concurrent.futures import ProcessPoolExecutor
from contextlib import nullcontext
from dataclasses import dataclass
from pathlib import Path

import numpy as np
try:
    from scipy.optimize import Bounds, LinearConstraint, milp
    HAS_SCIPY = True
except ImportError:
    Bounds = LinearConstraint = milp = None
    HAS_SCIPY = False

if __package__ in (None, "", "fit"):
    SCRIPT_DIR = Path(__file__).resolve().parent
    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    if str(SCRIPT_DIR) not in sys.path:
        sys.path.insert(0, str(SCRIPT_DIR))
    if str(PROJECT_ROOT) not in sys.path:
        sys.path.insert(0, str(PROJECT_ROOT))
    from config import METRIC_KEYS
    from fitter import (
        MISS_RATE_SPECS,
        RAW_METRIC_SET,
        TARGET_KEY_ALIASES,
        display_source_ref,
        effective_repeat_amount,
        ensure_target,
        format_metric_value,
        load_candidates,
        metric_display_order,
        normalized_metric_name_set,
        predictions_from_totals,
        relative_error,
        totals_from_repeat_amounts,
    )
    from fitter_config import FIT_CONFIG
else:
    from ..config import METRIC_KEYS
    from .fitter import (
        MISS_RATE_SPECS,
        RAW_METRIC_SET,
        TARGET_KEY_ALIASES,
        display_source_ref,
        effective_repeat_amount,
        ensure_target,
        format_metric_value,
        load_candidates,
        metric_display_order,
        normalized_metric_name_set,
        predictions_from_totals,
        relative_error,
        totals_from_repeat_amounts,
    )
    from .fitter_config import FIT_CONFIG


EPS = 1e-12
# Candidate raw-count dimensions. The active solve vector is selected from
# this list by the target: old I-side-only targets stay 11-D, while targets
# that include D-cache / D-TLB / LLC metrics automatically become wider.
DEFAULT_RAW_VECTOR_METRICS = [
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
]
RAW_VECTOR_METRICS = list(DEFAULT_RAW_VECTOR_METRICS)


# Loaded from fitter_config.json; populated in main() before use.
SEARCH_CONFIG = dict(FIT_CONFIG.get("search_config", {
    "max_templates": 100,
    "seed_beam": 96,
    "beam_size": 128,
    "expand_per_state": 48,
    "max_nnls_iter": 8000,
    "tolerance": 0.01,
    "top_k": 50,
    "parallel_workers": 128,
    "parallel_batch_size": 16,
    "log_path": "output/raw_count_sparse_solver.log",
    "result_json": "output/raw_count_sparse_solver_results.json",
    "best_result_json": "output/raw_count_sparse_solver_best.json",
}))


def parse_args():
    parser = argparse.ArgumentParser(description="Sparse search in target-selected raw count space.")
    parser.add_argument("--max-templates", type=int, default=SEARCH_CONFIG["max_templates"])
    parser.add_argument("--seed-beam", type=int, default=SEARCH_CONFIG["seed_beam"])
    parser.add_argument("--beam-size", type=int, default=SEARCH_CONFIG["beam_size"])
    parser.add_argument("--expand-per-state", type=int, default=SEARCH_CONFIG["expand_per_state"])
    parser.add_argument("--max-nnls-iter", type=int, default=SEARCH_CONFIG["max_nnls_iter"])
    parser.add_argument("--tolerance", type=float, default=SEARCH_CONFIG["tolerance"])
    parser.add_argument("--top-k", type=int, default=SEARCH_CONFIG["top_k"])
    parser.add_argument("--parallel-workers", type=int, default=SEARCH_CONFIG["parallel_workers"])
    parser.add_argument("--parallel-batch-size", type=int, default=SEARCH_CONFIG["parallel_batch_size"])
    parser.add_argument("--use-milp", action="store_true", help="Use MILP to solve raw-count selection instead of beam search.")
    parser.add_argument("--use-c", action="store_true", help="Use compiled C sparse_solver binary (faster).")
    parser.add_argument(
        "--stable-low-mpki-threshold",
        type=float,
        default=None,
        help="Override FIT_CONFIG['stable_low_mpki_threshold'] for repeat count stability behavior.",
    )
    return parser.parse_args()


@dataclass
class SparseResult:
    indices: tuple
    candidates: list
    coefficients: np.ndarray
    totals: dict
    raw_prediction: dict
    raw_rel_errors: dict
    raw_box_violations: dict
    target_metrics_prediction: dict
    feasible: bool
    max_box_violation: float
    mean_rel_error: float
    objective: float
    integer_repeats: np.ndarray
    integer_prediction: dict
    integer_rel_errors: dict
    integer_box_violations: dict
    integer_target_metrics_prediction: dict
    integer_feasible: bool
    integer_max_box_violation: float


_WORKER_CANDIDATES = None
_WORKER_TARGET_RAW = None
_WORKER_TARGET = None
_WORKER_CONFIG = None


def _init_worker(candidates, target_raw, target, config=None):
    global _WORKER_CANDIDATES, _WORKER_TARGET_RAW, _WORKER_TARGET, _WORKER_CONFIG
    _WORKER_CANDIDATES = candidates
    _WORKER_TARGET_RAW = target_raw
    _WORKER_TARGET = target
    _WORKER_CONFIG = config


def raw_metric_to_mpki(raw_key):
    if raw_key == "instructions:u":
        return None
    if not raw_key.endswith(":u"):
        return None
    return raw_key[: -len(":u")] + "_mpki"


def derive_target_raw_counts(target, fit_total_instructions):
    if "ipc" in target:
        raise ValueError(
            "raw_count_sparse_solver only supports raw-count dimensions; "
            "remove 'ipc' from FIT_CONFIG['target'] for this solver."
        )

    counts = {"instructions:u": float(target.get("instructions:u", fit_total_instructions))}

    for metric, value in target.items():
        canonical = TARGET_KEY_ALIASES.get(metric, metric)
        if canonical in RAW_METRIC_SET:
            counts[canonical] = float(value)
            continue
        if canonical.endswith("_mpki"):
            raw_key = canonical[: -len("_mpki")] + ":u"
            if raw_key in RAW_METRIC_SET and raw_key != "instructions:u":
                counts[raw_key] = float(value) * counts["instructions:u"] / 1000.0

    changed = True
    while changed:
        changed = False
        for rate_metric, (numerator_key, denominator_key) in MISS_RATE_SPECS.items():
            if rate_metric not in target:
                continue
            rate_value = float(target[rate_metric])
            numerator = counts.get(numerator_key)
            denominator = counts.get(denominator_key)
            if numerator is None and denominator is not None:
                counts[numerator_key] = denominator * rate_value
                changed = True
            elif denominator is None and numerator is not None and rate_value > EPS:
                counts[denominator_key] = numerator / rate_value
                changed = True

    return counts


def resolve_raw_vector_metrics(config, target_counts):
    configured = config.get("raw_vector_metrics", "auto")
    if configured in (None, "", "auto"):
        metrics = [metric for metric in DEFAULT_RAW_VECTOR_METRICS if metric in target_counts]
    elif configured == "all":
        metrics = list(DEFAULT_RAW_VECTOR_METRICS)
    else:
        metrics = [TARGET_KEY_ALIASES.get(metric, metric) for metric in configured]

    if "instructions:u" not in metrics:
        metrics.insert(0, "instructions:u")

    unknown = [metric for metric in metrics if metric not in RAW_METRIC_SET and metric != "instructions:u"]
    if unknown:
        raise ValueError(f"raw_vector_metrics contains unsupported raw events: {unknown}")
    return metrics


def build_target_raw_counts(target, fit_total_instructions, config=None):
    counts = derive_target_raw_counts(target, fit_total_instructions)
    raw_vector_metrics = resolve_raw_vector_metrics(config or {}, counts)

    missing = [metric for metric in raw_vector_metrics if metric not in counts]
    if missing:
        raise ValueError(
            "unable to derive all raw target counts from FIT_CONFIG['target']; "
            f"missing={missing}"
        )
    return {metric: counts[metric] for metric in raw_vector_metrics}


def weighted_nnls(A, y, max_iter, warm_start=None):
    if A.size == 0:
        return np.zeros(0, dtype=float)

    n = A.shape[1]
    if warm_start is None or len(warm_start) != n:
        x = np.zeros(n, dtype=float)
    else:
        x = np.maximum(np.asarray(warm_start, dtype=float), 0.0)

    gram = A.T @ A
    rhs = A.T @ y
    step_denom = np.linalg.norm(gram, ord=2)
    if not np.isfinite(step_denom) or step_denom <= EPS:
        step_denom = 1.0
    step = 1.0 / step_denom

    for _ in range(max_iter):
        grad = gram @ x - rhs
        next_x = np.maximum(x - step * grad, 0.0)
        if np.linalg.norm(next_x - x) <= 1e-9 * max(1.0, np.linalg.norm(x)):
            x = next_x
            break
        x = next_x

    x[x < 1e-10] = 0.0
    active = np.flatnonzero(x > 0.0)
    if 0 < len(active) < n:
        reduced = weighted_nnls(A[:, active], y, max_iter=max_iter // 2, warm_start=x[active])
        full = np.zeros(n, dtype=float)
        full[active] = reduced
        full[full < 1e-10] = 0.0
        return full
    return x


def raw_prediction_from_coefficients(candidates, coefficients, config=None):
    return {
        metric: float(
            sum(
                effective_repeat_amount(candidate, metric, coeff, config)
                * candidate.unit_counts[metric]
                for coeff, candidate in zip(coefficients, candidates)
            )
        )
        for metric in RAW_VECTOR_METRICS
    }


def integer_prediction_from_repeats(candidates, repeat_amounts, config=None):
    return totals_from_repeat_amounts(candidates, repeat_amounts, config=config)


def solve_combination_milp(candidates, target_raw, n_max=19, tolerance=0.10, k_positive=True, big_M=None):
    num_samples = len(candidates)
    if not HAS_SCIPY:
        raise ModuleNotFoundError(
            "SciPy is required for --use-milp mode. Install scipy and retry."
        )
    if num_samples == 0:
        return None

    X_all = np.vstack(
        [
            [candidate.unit_counts[metric] for metric in RAW_VECTOR_METRICS]
            for candidate in candidates
        ]
    ).astype(float)
    y_target = np.array([target_raw[metric] for metric in RAW_VECTOR_METRICS], dtype=float)
    dim = len(RAW_VECTOR_METRICS)

    if big_M is None:
        min_inst = min((candidate.unit_instructions for candidate in candidates if candidate.unit_instructions > 0.0), default=1.0)
        big_M = int(max(1000, np.ceil(max(1.0, y_target[0]) / min_inst) * 2))

    c = np.concatenate([np.zeros(num_samples, dtype=float), np.ones(num_samples, dtype=float)])

    if k_positive:
        k_lb = np.zeros(num_samples, dtype=float)
        k_ub = np.full(num_samples, big_M, dtype=float)
    else:
        k_lb = np.full(num_samples, -big_M, dtype=float)
        k_ub = np.zeros(num_samples, dtype=float)

    z_lb = np.zeros(num_samples, dtype=float)
    z_ub = np.ones(num_samples, dtype=float)

    bounds = Bounds(np.concatenate([k_lb, z_lb]), np.concatenate([k_ub, z_ub]))
    integrality = np.concatenate([np.zeros(num_samples, dtype=int), np.ones(num_samples, dtype=int)])

    A_y = np.hstack([X_all.T, np.zeros((dim, num_samples), dtype=float)])
    y_lower = (1.0 - tolerance) * y_target
    y_upper = (1.0 + tolerance) * y_target
    constraints = [LinearConstraint(A_y, y_lower, y_upper)]

    A_n = np.hstack([np.zeros((1, num_samples), dtype=float), np.ones((1, num_samples), dtype=float)])
    constraints.append(LinearConstraint(A_n, 1.0, n_max))

    if k_positive:
        A_kz = np.hstack([np.eye(num_samples, dtype=float), -big_M * np.eye(num_samples, dtype=float)])
        constraints.append(LinearConstraint(A_kz, -np.inf, np.zeros(num_samples, dtype=float)))
    else:
        A_kz = np.hstack([np.eye(num_samples, dtype=float), big_M * np.eye(num_samples, dtype=float)])
        constraints.append(LinearConstraint(A_kz, np.zeros(num_samples, dtype=float), np.inf))

    res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)
    if not res.success:
        return None

    k_opt = res.x[:num_samples]
    z_opt = np.round(res.x[num_samples:]).astype(int)
    indices = np.where(z_opt > 0)[0]
    return {
        "indices": indices,
        "k_opt": k_opt,
        "z_opt": z_opt,
        "objective": res.fun,
        "status": res.status,
        "message": res.message,
    }


def evaluate_raw_prediction(raw_prediction, target_raw, target_metric_view):
    raw_rel_errors = {}
    raw_box_violations = {}
    tolerance = float(SEARCH_CONFIG["tolerance"])
    max_box_violation = 0.0
    rel_values = []

    for metric in RAW_VECTOR_METRICS:
        target_value = target_raw[metric]
        predicted = raw_prediction[metric]
        rel = (predicted - target_value) / max(abs(target_value), 1.0)
        lower = (1.0 - tolerance) * target_value
        upper = (1.0 + tolerance) * target_value
        under = max(0.0, lower - predicted) / max(abs(target_value), 1.0)
        over = max(0.0, predicted - upper) / max(abs(target_value), 1.0)
        box_violation = max(under, over)
        raw_rel_errors[metric] = rel
        raw_box_violations[metric] = box_violation
        rel_values.append(rel * rel)
        if box_violation > max_box_violation:
            max_box_violation = box_violation

    totals = {metric: 0.0 for metric in METRIC_KEYS}
    totals.update(raw_prediction)
    predictions, _ = predictions_from_totals(totals, target_metric_view)
    mean_rel_error = math.sqrt(sum(rel_values) / len(rel_values))
    return (
        totals,
        predictions,
        raw_rel_errors,
        raw_box_violations,
        max_box_violation,
        mean_rel_error,
    )


def quantize_coefficients(coeffs):
    coeffs = np.asarray(coeffs, dtype=float)
    integer_repeats = np.rint(coeffs).astype(int)
    positive_mask = coeffs > 0.0
    integer_repeats[positive_mask] = np.maximum(integer_repeats[positive_mask], 1)
    if positive_mask.any() and not np.any(integer_repeats > 0):
        integer_repeats[int(np.argmax(coeffs))] = 1
    return integer_repeats


def evaluate_subset(candidates, indices, target_raw, target_metric_view, config=None):
    full_subset = [candidates[index] for index in indices]
    threshold = float((config or {}).get("count_scale_mpki_threshold", 0.5))

    # Determine per-metric whether it's "large count" (MPKI >= threshold).
    # For NNLS: large-count columns are divided by 10000 (and target divided by 10000).
    # Small-count columns are used as-is.
    large_mask = np.array([
        (target_raw[metric] / max(target_raw.get("instructions:u", 1e9), 1.0) * 1000.0) >= threshold
        for metric in RAW_VECTOR_METRICS
    ], dtype=float)  # 1.0 = large, 0.0 = small
    scale = np.where(large_mask, 1.0 / 10000.0, 1.0)

    matrix = np.column_stack(
        [
            np.array([candidate.unit_counts[metric] for metric in RAW_VECTOR_METRICS], dtype=float)
            for candidate in full_subset
        ]
    )
    target_vec = np.array([target_raw[metric] for metric in RAW_VECTOR_METRICS], dtype=float)

    # Apply large/small scaling to both matrix and target before NNLS
    matrix_scaled = matrix * scale[:, None]
    target_scaled = target_vec * scale

    scales = np.maximum(np.abs(target_scaled), 1.0)
    A = matrix_scaled / scales[:, None]
    y = target_scaled / scales
    coeffs = weighted_nnls(A, y, max_iter=int(SEARCH_CONFIG["max_nnls_iter"]))

    active = np.flatnonzero(coeffs > 0.0)
    if len(active) == 0:
        subset = []
        indices = tuple()
        coeffs = np.zeros(0, dtype=float)
        totals = {metric: 0.0 for metric in METRIC_KEYS}
        raw_prediction = {metric: 0.0 for metric in RAW_VECTOR_METRICS}
    else:
        subset = [full_subset[index] for index in active]
        indices = tuple(int(indices[index]) for index in active)
        coeffs = coeffs[active]
        raw_prediction = raw_prediction_from_coefficients(subset, coeffs, config=config)
        totals = {metric: 0.0 for metric in METRIC_KEYS}
        totals.update(raw_prediction)
    (
        totals,
        predictions,
        raw_rel_errors,
        raw_box_violations,
        max_box_violation,
        mean_rel_error,
    ) = evaluate_raw_prediction(raw_prediction, target_raw, target_metric_view)

    integer_repeats = quantize_coefficients(coeffs)
    integer_prediction = integer_prediction_from_repeats(subset, integer_repeats, config=config)
    (
        _integer_totals,
        integer_target_metrics_prediction,
        integer_rel_errors,
        integer_box_violations,
        integer_max_box_violation,
        _integer_mean_rel_error,
    ) = evaluate_raw_prediction(integer_prediction, target_raw, target_metric_view)

    objective = max_box_violation * 1000.0 + mean_rel_error

    return SparseResult(
        indices=tuple(indices),
        candidates=subset,
        coefficients=coeffs,
        totals=totals,
        raw_prediction=raw_prediction,
        raw_rel_errors=raw_rel_errors,
        raw_box_violations=raw_box_violations,
        target_metrics_prediction=predictions,
        feasible=max_box_violation <= EPS,
        max_box_violation=max_box_violation,
        mean_rel_error=mean_rel_error,
        objective=objective,
        integer_repeats=integer_repeats,
        integer_prediction=integer_prediction,
        integer_rel_errors=integer_rel_errors,
        integer_box_violations=integer_box_violations,
        integer_target_metrics_prediction=integer_target_metrics_prediction,
        integer_feasible=integer_max_box_violation <= EPS,
        integer_max_box_violation=integer_max_box_violation,
    )


def result_sort_key(result):
    active_templates = sum(1 for value in result.coefficients if value > 0.0)
    return (
        0 if result.feasible else 1,
        result.max_box_violation,
        result.mean_rel_error,
        active_templates,
        result.objective,
    )


def result_signature(result):
    return tuple(
        (
            candidate.module,
            candidate.case,
            Path(candidate.source_csv).name,
            int(candidate.source_row),
        )
        for candidate, coefficient in zip(result.candidates, result.coefficients)
        if coefficient > 0.0
    )


def append_top(results, candidate, top_k):
    candidate_signature = result_signature(candidate)
    for index, existing in enumerate(results):
        if result_signature(existing) == candidate_signature:
            if result_sort_key(candidate) < result_sort_key(existing):
                results[index] = candidate
            results.sort(key=result_sort_key)
            del results[top_k:]
            return
    results.append(candidate)
    results.sort(key=result_sort_key)
    del results[top_k:]


def subset_signature(indices):
    return tuple(sorted(int(index) for index in indices))


def chunked(items, size):
    size = max(1, int(size))
    for start in range(0, len(items), size):
        yield items[start : start + size]


def _evaluate_subset_batch(subset_batch):
    return [
        evaluate_subset(_WORKER_CANDIDATES, indices, _WORKER_TARGET_RAW, _WORKER_TARGET, config=_WORKER_CONFIG)
        for indices in subset_batch
    ]


def evaluate_subsets_parallel(candidates, subset_list, target_raw, target, max_workers, batch_size, executor=None, config=None):
    if not subset_list:
        return []

    max_workers = int(max_workers)
    if max_workers <= 1:
        return [evaluate_subset(candidates, indices, target_raw, target, config=config) for indices in subset_list]

    batches = list(chunked(subset_list, batch_size))
    results = []
    try:
        if executor is not None:
            for partial in executor.map(_evaluate_subset_batch, batches):
                results.extend(partial)
        else:
            executor_kwargs = {
                "max_workers": max_workers,
                "initializer": _init_worker,
                "initargs": (candidates, target_raw, target, config),
            }
            if "fork" in mp.get_all_start_methods():
                executor_kwargs["mp_context"] = mp.get_context("fork")
            with ProcessPoolExecutor(**executor_kwargs) as local_executor:
                for partial in local_executor.map(_evaluate_subset_batch, batches):
                    results.extend(partial)
    except Exception as exc:
        print(
            f"[raw_count_sparse_solver] parallel evaluation failed, falling back to serial: {exc}",
            file=sys.stderr,
        )
        return [evaluate_subset(candidates, indices, target_raw, target, config=config) for indices in subset_list]
    return results


def expand_scores(candidates, result, target_raw):
    scores = []
    deficits = {
        metric: max(0.0, target_raw[metric] - result.raw_prediction[metric]) / max(abs(target_raw[metric]), 1.0)
        for metric in RAW_VECTOR_METRICS
    }
    overs = {
        metric: max(0.0, result.raw_prediction[metric] - target_raw[metric]) / max(abs(target_raw[metric]), 1.0)
        for metric in RAW_VECTOR_METRICS
    }

    current = set(result.indices)
    for index, candidate in enumerate(candidates):
        if index in current:
            continue
        gain = 0.0
        penalty = 0.0
        for metric in RAW_VECTOR_METRICS:
            value = candidate.unit_counts[metric] / max(abs(target_raw[metric]), 1.0)
            gain += deficits[metric] * value
            penalty += overs[metric] * value
        scores.append((gain - 1.5 * penalty, index))
    scores.sort(reverse=True)
    return [index for _, index in scores]


def render_table(headers, rows, indent="  "):
    widths = [len(str(header)) for header in headers]
    normalized = []
    for row in rows:
        text_row = [str(cell) for cell in row]
        normalized.append(text_row)
        for index, cell in enumerate(text_row):
            widths[index] = max(widths[index], len(cell))

    lines = [indent + "  " + " | ".join(text.ljust(widths[index]) for index, text in enumerate(headers))]
    lines.append(indent + "  " + "-+-".join("-" * width for width in widths))
    for row in normalized:
        lines.append(indent + "  " + " | ".join(text.ljust(widths[index]) for index, text in enumerate(row)))
    return "\n".join(lines)


def raw_rows(result, target_raw):
    rows = []
    for metric in RAW_VECTOR_METRICS:
        target_value = target_raw[metric]
        predicted = result.raw_prediction[metric]
        delta = predicted - target_value
        rel = result.raw_rel_errors[metric]
        rows.append(
            [
                metric,
                format_metric_value(metric, target_value),
                format_metric_value(metric, predicted),
                format_metric_value(metric, delta),
                f"{rel * 100.0:.2f}%",
                f"{result.raw_box_violations[metric] * 100.0:.2f}%",
            ]
        )
    return rows


def derived_rows(result, target):
    rows = []
    for metric in metric_display_order(target):
        target_value = target[metric]
        predicted = result.target_metrics_prediction.get(metric)
        delta = None if predicted is None else predicted - target_value
        rel = relative_error(target_value, predicted)
        rows.append(
            [
                metric,
                format_metric_value(metric, target_value),
                format_metric_value(metric, predicted),
                "NA" if delta is None else format_metric_value(metric, delta),
                "NA" if rel is None else f"{rel * 100.0:.2f}%",
            ]
        )
    return rows


def contribution_rows(result):
    rows = []
    for candidate, coefficient, integer_repeat in zip(result.candidates, result.coefficients, result.integer_repeats):
        if coefficient <= 0.0:
            continue
        rows.append(
            [
                f"{candidate.module}:{candidate.case}",
                f"{coefficient:.6f}",
                str(int(integer_repeat)),
                f"{candidate.unit_instructions:.4f}",
                display_source_ref(candidate),
            ]
        )
    return rows


def result_json_record(rank, result, target_raw, target):
    return {
        "rank": rank,
        "feasible": bool(result.feasible),
        "max_box_violation": float(result.max_box_violation),
        "mean_rel_error": float(result.mean_rel_error),
        "objective": float(result.objective),
        "selected_templates": sum(1 for value in result.coefficients if value > 0.0),
        "coefficients": [
            {
                "module": candidate.module,
                "case": candidate.case,
                "coefficient": float(coefficient),
                "repeat_count": int(integer_repeat),
                "unit_instructions": candidate.unit_instructions,
                "source_csv": Path(candidate.source_csv).name,
                "source_row": candidate.source_row,
            }
            for candidate, coefficient, integer_repeat in zip(
                result.candidates, result.coefficients, result.integer_repeats
            )
            if coefficient > 0.0
        ],
        "raw_target": target_raw,
        "raw_prediction": result.raw_prediction,
        "raw_rel_errors": result.raw_rel_errors,
        "repeat_plan_integer": [
            {
                "module": candidate.module,
                "case": candidate.case,
                "repeat_count": int(integer_repeat),
                "unit_instructions": candidate.unit_instructions,
                "source_csv": Path(candidate.source_csv).name,
                "source_row": candidate.source_row,
            }
            for candidate, integer_repeat in zip(result.candidates, result.integer_repeats)
            if integer_repeat > 0
        ],
        "integer_prediction": result.integer_prediction,
        "integer_rel_errors": result.integer_rel_errors,
        "integer_box_violation": result.integer_box_violations,
        "integer_target_metric_prediction": result.integer_target_metrics_prediction,
        "integer_feasible": bool(result.integer_feasible),
        "integer_max_box_violation": float(result.integer_max_box_violation),
        "target_metric_prediction": result.target_metrics_prediction,
        "target_metrics": target,
    }



def run_c_solver(args, config, target_raw, result_json_path, best_json_path):
    """Invoke the compiled C sparse_solver binary and return (best_results, best)."""
    import subprocess, shutil

    binary = Path(__file__).resolve().parent / "sparse_solver"
    if not binary.exists():
        raise FileNotFoundError(f"C solver binary not found: {binary}. Run: gcc -O3 -fopenmp -std=c11 fit/sparse_solver.c -o fit/sparse_solver -lm")

    cfg_json = Path(__file__).resolve().parent / "fitter_config.json"
    csv_path = Path(config["output_dir"]) / config["csv_files"][0]

    cmd = [
        str(binary),
        str(cfg_json),
        str(csv_path),
        str(result_json_path),
        str(best_json_path),
        "--max-templates",    str(SEARCH_CONFIG["max_templates"]),
        "--seed-beam",        str(SEARCH_CONFIG["seed_beam"]),
        "--beam-size",        str(SEARCH_CONFIG["beam_size"]),
        "--expand-per-state", str(SEARCH_CONFIG["expand_per_state"]),
        "--max-nnls-iter",    str(SEARCH_CONFIG["max_nnls_iter"]),
        "--tolerance",        str(SEARCH_CONFIG["tolerance"]),
        "--top-k",            str(SEARCH_CONFIG["top_k"]),
        "--threads",          str(SEARCH_CONFIG["parallel_workers"]),
    ]
    print(f"[raw_count_sparse_solver] running C solver: {' '.join(cmd)}", file=sys.stderr)
    subprocess.run(cmd, check=True)

    # read back results and reconstruct Python SparseResult objects
    candidates = load_candidates(config)
    candidate_lookup = {
        (Path(c.source_csv).name, c.source_row): c for c in candidates
    }

    def _c_record_to_result(rec):
        plan = rec.get("repeat_plan_integer", [])
        cands_out, coeffs_out, int_repeats_out = [], [], []
        for item in plan:
            key = (item["source_csv"], int(item["source_row"]))
            cand = candidate_lookup.get(key)
            if cand is None:
                # fallback: match by module+case
                for c in candidates:
                    if c.module == item["module"] and c.case == item["case"]:
                        cand = c; break
            if cand is None:
                continue
            cands_out.append(cand)
            coeffs_out.append(float(item["repeat_count"]))
            int_repeats_out.append(int(item["repeat_count"]))

        raw_pred = rec.get("raw_prediction", {})
        int_pred = rec.get("integer_prediction", {})
        raw_rel  = rec.get("raw_rel_errors", {})
        int_rel  = rec.get("integer_rel_errors", {})
        raw_box  = {}
        int_box  = rec.get("integer_box_violation", {})
        tol = SEARCH_CONFIG["tolerance"]
        for m, tv in target_raw.items():
            pred = raw_pred.get(m, 0.0)
            lo, hi = (1-tol)*tv, (1+tol)*tv
            denom = max(abs(tv), 1.0)
            raw_box[m] = max(max(0.0, lo-pred)/denom, max(0.0, pred-hi)/denom)

        totals = {m: 0.0 for m in METRIC_KEYS}
        totals.update(raw_pred)
        predictions, _ = predictions_from_totals(totals, _WORKER_TARGET or {})

        max_bv = rec.get("max_box_violation", 1.0)
        int_max_bv = rec.get("integer_max_box_violation", 1.0)
        mean_re = rec.get("mean_rel_error", 1.0)

        return SparseResult(
            indices=tuple(item["source_row"] for item in plan),
            candidates=cands_out,
            coefficients=np.array(coeffs_out, dtype=float),
            totals=totals,
            raw_prediction=raw_pred,
            raw_rel_errors=raw_rel,
            raw_box_violations=raw_box,
            target_metrics_prediction=predictions,
            feasible=bool(rec.get("feasible", False)),
            max_box_violation=max_bv,
            mean_rel_error=mean_re,
            objective=max_bv * 1000.0 + mean_re,
            integer_repeats=np.array(int_repeats_out, dtype=int),
            integer_prediction=int_pred,
            integer_rel_errors=int_rel,
            integer_box_violations=int_box,
            integer_target_metrics_prediction=predictions,
            integer_feasible=bool(rec.get("integer_feasible", False)),
            integer_max_box_violation=int_max_bv,
        )

    with open(result_json_path, encoding="utf-8") as f:
        payload = json.load(f)
    best_results = [_c_record_to_result(r) for r in payload.get("results", [])]
    best_results.sort(key=result_sort_key)

    best_feasible = next((r for r in best_results if r.feasible), None)
    best = best_feasible or (best_results[0] if best_results else None)
    return best_results, best


def main():
    global RAW_VECTOR_METRICS, SEARCH_CONFIG

    # Load SEARCH_CONFIG from fitter_config.json (already in FIT_CONFIG)
    SEARCH_CONFIG = dict(FIT_CONFIG.get("search_config", SEARCH_CONFIG))

    args = parse_args()
    SEARCH_CONFIG["max_templates"] = int(args.max_templates)
    SEARCH_CONFIG["seed_beam"] = int(args.seed_beam)
    SEARCH_CONFIG["beam_size"] = int(args.beam_size)
    SEARCH_CONFIG["expand_per_state"] = int(args.expand_per_state)
    SEARCH_CONFIG["max_nnls_iter"] = int(args.max_nnls_iter)
    SEARCH_CONFIG["tolerance"] = float(args.tolerance)
    SEARCH_CONFIG["top_k"] = int(args.top_k)
    SEARCH_CONFIG["parallel_workers"] = int(args.parallel_workers)
    SEARCH_CONFIG["parallel_batch_size"] = int(args.parallel_batch_size)

    config = dict(FIT_CONFIG)
    if args.stable_low_mpki_threshold is not None:
        FIT_CONFIG["stable_low_mpki_threshold"] = float(args.stable_low_mpki_threshold)
        config["stable_low_mpki_threshold"] = float(args.stable_low_mpki_threshold)

    target = ensure_target(config)
    ignored = normalized_metric_name_set(config.get("ignored_metrics", []))
    if ignored:
        target = {metric: value for metric, value in target.items() if metric not in ignored}

    target_raw = build_target_raw_counts(target, float(config["fit_total_instructions"]), config=config)
    RAW_VECTOR_METRICS = list(target_raw.keys())
    candidates = load_candidates(config)

    log_path = PROJECT_ROOT / SEARCH_CONFIG["log_path"]
    result_json_path = PROJECT_ROOT / SEARCH_CONFIG["result_json"]
    best_json_path = PROJECT_ROOT / SEARCH_CONFIG["best_result_json"]
    log_path.parent.mkdir(parents=True, exist_ok=True)

    if args.use_c:
        _init_worker(candidates, target_raw, target, config)
        best_results, best = run_c_solver(args, config, target_raw, result_json_path, best_json_path)
    elif args.use_milp:
        milp_solution = solve_combination_milp(
            candidates,
            target_raw,
            n_max=int(SEARCH_CONFIG["max_templates"]),
            tolerance=SEARCH_CONFIG["tolerance"],
        )
        if milp_solution is None:
            print("[raw_count_sparse_solver] MILP cannot find a feasible solution", file=sys.stderr)
            sys.exit(1)

        indices = milp_solution["indices"]
        selected = [candidates[index] for index in indices]
        coefficients = milp_solution["k_opt"][indices]

        raw_prediction = raw_prediction_from_coefficients(selected, coefficients)
        totals = {metric: 0.0 for metric in METRIC_KEYS}
        totals.update(raw_prediction)

        _, target_metrics_prediction, raw_rel_errors, raw_box_violations, max_box_violation, mean_rel_error = evaluate_raw_prediction(
            raw_prediction,
            target_raw,
            target,
        )

        integer_repeats = np.rint(coefficients).astype(int)
        integer_prediction = integer_prediction_from_repeats(selected, integer_repeats)
        _, integer_target_metrics_prediction, integer_rel_errors, integer_box_violations, integer_max_box_violation, _ = evaluate_raw_prediction(
            integer_prediction,
            target_raw,
            target,
        )

        best_result = SparseResult(
            indices=tuple(int(index) for index in indices),
            candidates=selected,
            coefficients=coefficients,
            totals=totals,
            raw_prediction=raw_prediction,
            raw_rel_errors=raw_rel_errors,
            raw_box_violations=raw_box_violations,
            target_metrics_prediction=target_metrics_prediction,
            feasible=max_box_violation <= EPS,
            max_box_violation=max_box_violation,
            mean_rel_error=mean_rel_error,
            objective=float(len(indices)),
            integer_repeats=integer_repeats,
            integer_prediction=integer_prediction,
            integer_rel_errors=integer_rel_errors,
            integer_box_violations=integer_box_violations,
            integer_target_metrics_prediction=integer_target_metrics_prediction,
            integer_feasible=integer_max_box_violation <= EPS,
            integer_max_box_violation=integer_max_box_violation,
        )

        best_results = [best_result]
        best_feasible = best_result if best_result.feasible else None
        beam = best_results
    else:
        executor = None
        try:
            if int(SEARCH_CONFIG["parallel_workers"]) > 1:
                executor_kwargs = {
                    "max_workers": int(SEARCH_CONFIG["parallel_workers"]),
                    "initializer": _init_worker,
                    "initargs": (candidates, target_raw, target, config),
                }
                if "fork" in mp.get_all_start_methods():
                    executor_kwargs["mp_context"] = mp.get_context("fork")
                executor = ProcessPoolExecutor(**executor_kwargs)
        except Exception as exc:
            print(
                f"[raw_count_sparse_solver] failed to create persistent process pool, using serial: {exc}",
                file=sys.stderr,
            )
            executor = None

        try:
            seed_scores = evaluate_subsets_parallel(
                candidates,
                [(index,) for index in range(len(candidates))],
                target_raw,
                target,
                SEARCH_CONFIG["parallel_workers"],
                SEARCH_CONFIG["parallel_batch_size"],
                executor=executor,
                config=config,
            )
            seed_scores.sort(key=result_sort_key)
            beam = seed_scores[: int(SEARCH_CONFIG["seed_beam"])]
            best_results = beam[: int(SEARCH_CONFIG["top_k"])]

            seen = {subset_signature(result.indices) for result in beam}
            best_feasible = next((result for result in beam if result.feasible), None)

            for depth in range(2, int(SEARCH_CONFIG["max_templates"]) + 1):
                next_seen = set()
                subset_list = []
                for state in beam:
                    ranked_indices = expand_scores(candidates, state, target_raw)
                    for candidate_index in ranked_indices[: int(SEARCH_CONFIG["expand_per_state"])]:
                        new_indices = subset_signature(state.indices + (candidate_index,))
                        if new_indices in seen or new_indices in next_seen:
                            continue
                        next_seen.add(new_indices)
                        subset_list.append(new_indices)

                batch_results = evaluate_subsets_parallel(
                    candidates,
                    subset_list,
                    target_raw,
                    target,
                    SEARCH_CONFIG["parallel_workers"],
                    SEARCH_CONFIG["parallel_batch_size"],
                    executor=executor,
                    config=config,
                )

                next_beam = []
                for result in batch_results:
                    append_top(next_beam, result, int(SEARCH_CONFIG["beam_size"]))
                    append_top(best_results, result, int(SEARCH_CONFIG["top_k"]))
                    if result.feasible:
                        if best_feasible is None or result_sort_key(result) < result_sort_key(best_feasible):
                            best_feasible = result
                if not next_beam:
                    break
                beam = next_beam
                seen.update(next_seen)
                if best_feasible is not None:
                    break
        finally:
            if executor is not None:
                executor.shutdown(wait=True)

        best_results.sort(key=result_sort_key)
        best = best_feasible or best_results[0]

    if args.use_milp:
        best = best_results[0]

    with log_path.open("w", encoding="utf-8") as handle:
        handle.write("== Raw Count Sparse Solver ==\n")
        handle.write(f"candidate_pool_size={len(candidates)}\n")
        handle.write(f"max_templates={SEARCH_CONFIG['max_templates']}\n")
        handle.write(f"tolerance={SEARCH_CONFIG['tolerance']:.2%}\n\n")

        handle.write("== Raw Target Counts ==\n")
        handle.write(render_table(["metric", "target"], [[metric, format_metric_value(metric, value)] for metric, value in target_raw.items()]))
        handle.write("\n\n")

        handle.write("== Best Results ==\n")
        for rank, result in enumerate(best_results, start=1):
            handle.write(
                f"[{rank}] feasible={result.feasible} max_box_violation={result.max_box_violation:.6f} "
                f"mean_rel_error={result.mean_rel_error:.6f} objective={result.objective:.6f}\n"
            )
            handle.write(
                render_table(
                    ["module", "coefficient", "repeat_count", "unit_instructions", "source"],
                    contribution_rows(result),
                )
            )
            handle.write("\n")
            handle.write("continuous_prediction:\n")
            handle.write(render_table(["metric", "target", "pred", "delta", "rel_err", "box_violation"], raw_rows(result, target_raw)))
            handle.write("\n")
            handle.write("integer_prediction:\n")
            handle.write(
                render_table(
                    ["metric", "target", "pred", "delta", "rel_err", "box_violation"],
                    raw_rows(
                        SparseResult(
                            indices=result.indices,
                            candidates=result.candidates,
                            coefficients=result.coefficients,
                            totals=result.totals,
                            raw_prediction=result.integer_prediction,
                            raw_rel_errors=result.integer_rel_errors,
                            raw_box_violations=result.integer_box_violations,
                            target_metrics_prediction=result.integer_target_metrics_prediction,
                            feasible=result.integer_feasible,
                            max_box_violation=result.integer_max_box_violation,
                            mean_rel_error=result.mean_rel_error,
                            objective=result.objective,
                            integer_repeats=result.integer_repeats,
                            integer_prediction=result.integer_prediction,
                            integer_rel_errors=result.integer_rel_errors,
                            integer_box_violations=result.integer_box_violations,
                            integer_target_metrics_prediction=result.integer_target_metrics_prediction,
                            integer_feasible=result.integer_feasible,
                            integer_max_box_violation=result.integer_max_box_violation,
                        ),
                        target_raw,
                    ),
                )
            )
            handle.write("\n")
            handle.write(render_table(["metric", "target", "pred", "delta", "rel_err"], derived_rows(result, target)))
            handle.write("\n\n")

    payload = {
        "config": {
            "candidate_pool_size": len(candidates),
            "max_templates": SEARCH_CONFIG["max_templates"],
            "tolerance": SEARCH_CONFIG["tolerance"],
        },
        "results": [result_json_record(rank, result, target_raw, target) for rank, result in enumerate(best_results, start=1)],
    }
    result_json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    best_json_path.write_text(json.dumps({"best_result": result_json_record(1, best, target_raw, target), "config": payload["config"]}, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"raw count sparse solver log written to {log_path}")
    print(f"raw count sparse solver results written to {result_json_path}")
    print(f"raw count sparse solver best result written to {best_json_path}")


if __name__ == "__main__":
    main()
