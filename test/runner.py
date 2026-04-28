#!/usr/bin/env python3

import math
import random
from copy import deepcopy

if __package__ in (None, "", "test"):
    from config import zero_all_modules
    from test.csv_layout import join_case_labels, metric_headers, with_metric_separators
    from utils import calc_derived, run_one, write_csv_row
else:
    from ..config import zero_all_modules
    from .csv_layout import join_case_labels, metric_headers, with_metric_separators
    from ..utils import calc_derived, run_one, write_csv_row


CSV_PREFIX = ["suite", "case", "order_tag", "modules"]


def apply_module_config(cfg, module_name, params):
    module = cfg["modules"][module_name]
    for key, value in params.items():
        module[key] = value


def set_module_order(cfg, ordered_module_names):
    base = 1
    assigned = set()
    for offset, module_name in enumerate(ordered_module_names):
        cfg["modules"][module_name]["pos"] = base + offset
        assigned.add(module_name)

    tail_pos = base + len(ordered_module_names)
    for module_name in cfg["modules"]:
        if module_name in assigned:
            continue
        cfg["modules"][module_name]["pos"] = tail_pos
        tail_pos += 1


def build_headers(metric_keys, _base_cfg):
    return [*CSV_PREFIX, *metric_headers(metric_keys)]


def make_blank_row(headers):
    return {key: "" for key in headers}


def tag_row(row, suite_name, case_name, order_tag, modules_tag):
    row["suite"] = suite_name
    row["case"] = case_name
    row["order_tag"] = order_tag
    row["modules"] = modules_tag
    return row


def write_tagged_run(cfg, knobs, csv_headers, csv_out, suite_name, case_name, order_tag, modules_tag):
    row, raw_output = run_one(cfg, knobs)
    tagged_row = with_metric_separators(tag_row(row, suite_name, case_name, order_tag, modules_tag))
    write_csv_row(csv_out, csv_headers, tagged_row)
    print(f"[{suite_name}] {case_name} order={order_tag} modules={modules_tag}")
    print(raw_output)
    return tagged_row


def build_sum_row(base_cfg, metric_keys, rows, selected_cases, suite_name, case_name, order_tag):
    row = tag_row({}, suite_name, case_name, order_tag, join_case_labels(selected_cases))

    for key in metric_keys:
        total = 0
        has_value = False
        for row_item in rows:
            value = row_item.get(key)
            if value not in ("", None):
                total += value
                has_value = True
        row[key] = total if has_value else ""

    row.update(calc_derived(row))
    return with_metric_separators(row)


def build_single_cfg(base_cfg, case):
    cfg = deepcopy(base_cfg)
    zero_all_modules(cfg)
    apply_module_config(cfg, case["module"], case["params"])
    set_module_order(cfg, [case["module"]])
    return cfg


def build_combined_cfg(base_cfg, selected_cases, ordered_cases):
    cfg = deepcopy(base_cfg)
    zero_all_modules(cfg)
    for case in selected_cases:
        apply_module_config(cfg, case["module"], case["params"])
    set_module_order(cfg, [case["module"] for case in ordered_cases])
    return cfg


def run_case_library_suite(base_cfg, knobs, metric_keys, suite_cfg, output_dir):
    csv_headers = build_headers(metric_keys, base_cfg)
    csv_out = output_dir / suite_cfg["csv_name"]
    suite_name = suite_cfg["name"]

    for case in suite_cfg["cases"]:
        cfg = build_single_cfg(base_cfg, case)
        write_tagged_run(
            cfg,
            knobs,
            csv_headers,
            csv_out,
            suite_name=suite_name,
            case_name=join_case_labels([case]),
            order_tag="single",
            modules_tag=join_case_labels([case]),
        )


def distinct_orders(selected_cases, shuffle_rounds, rng):
    canonical = tuple(case["label"] for case in selected_cases)
    yielded = {canonical}

    yield list(selected_cases), "canonical"

    max_unique = math.factorial(len(selected_cases)) - 1
    target = min(max_unique, max(0, shuffle_rounds))
    attempts = 0
    produced = 0

    while produced < target and attempts < max(20, target * 8):
        attempts += 1
        shuffled = list(selected_cases)
        rng.shuffle(shuffled)
        key = tuple(case["label"] for case in shuffled)
        if key in yielded:
            continue
        yielded.add(key)
        produced += 1
        yield shuffled, "shuffle_" + "_".join(key)


def choose_random_case_sets(case_groups, combo_size, sample_count, rng):
    module_names = sorted(case_groups.keys())
    if combo_size > len(module_names):
        return []

    selected = []
    seen = set()
    attempts = 0
    max_attempts = max(32, sample_count * 20)

    while len(selected) < sample_count and attempts < max_attempts:
        attempts += 1
        chosen_modules = rng.sample(module_names, combo_size)
        chosen_modules.sort()
        cases = [rng.choice(case_groups[module_name]) for module_name in chosen_modules]
        key = tuple(case["label"] for case in cases)
        if key in seen:
            continue
        seen.add(key)
        selected.append(cases)

    return selected


def distribute_total_groups(total_groups, combo_sizes):
    if total_groups <= 0 or not combo_sizes:
        return {combo_size: 0 for combo_size in combo_sizes}

    base_count, extra_count = divmod(total_groups, len(combo_sizes))
    return {
        combo_size: base_count + (1 if index < extra_count else 0)
        for index, combo_size in enumerate(combo_sizes)
    }


def run_random_combo_suite(base_cfg, knobs, metric_keys, suite_cfg, output_dir):
    suite_name = suite_cfg["name"]
    csv_headers = build_headers(metric_keys, base_cfg)
    csv_out = output_dir / suite_cfg["csv_name"]
    case_groups = suite_cfg["module_case_groups"]
    combo_sizes = suite_cfg.get("combo_sizes", [])
    if suite_cfg.get("samples_per_size") is None and "total_groups" in suite_cfg:
        samples_by_size = distribute_total_groups(suite_cfg.get("total_groups", 0), combo_sizes)
        use_global_case_index = True
    else:
        sample_count = suite_cfg.get("samples_per_size", 0)
        samples_by_size = {combo_size: sample_count for combo_size in combo_sizes}
        use_global_case_index = False

    rng = random.Random(base_cfg["build"]["seed"])
    global_combo_index = 0
    for combo_size in combo_sizes:
        case_sets = choose_random_case_sets(
            case_groups,
            combo_size,
            samples_by_size.get(combo_size, 0),
            rng,
        )
        for combo_index, selected_cases in enumerate(case_sets):
            if use_global_case_index:
                case_name = f"combo_{global_combo_index:03d}_s{combo_size}"
            else:
                case_name = f"combo_{combo_size}_{combo_index:02d}"
            global_combo_index += 1
            single_rows = []

            for case in selected_cases:
                row = write_tagged_run(
                    build_single_cfg(base_cfg, case),
                    knobs,
                    csv_headers,
                    csv_out,
                    suite_name=suite_name,
                    case_name=case_name,
                    order_tag="single",
                    modules_tag=join_case_labels([case]),
                )
                single_rows.append(row)

            ordered_runs = list(distinct_orders(selected_cases, suite_cfg.get("shuffle_rounds", 0), rng))
            for ordered_cases, order_tag in ordered_runs:
                cfg = build_combined_cfg(base_cfg, selected_cases, ordered_cases)
                write_tagged_run(
                    cfg,
                    knobs,
                    csv_headers,
                    csv_out,
                    suite_name=suite_name,
                    case_name=case_name,
                    order_tag=order_tag,
                    modules_tag=join_case_labels(ordered_cases),
                )

            write_csv_row(
                csv_out,
                csv_headers,
                build_sum_row(base_cfg, metric_keys, single_rows, selected_cases, suite_name, case_name, "sum"),
            )

            write_csv_row(csv_out, csv_headers, make_blank_row(csv_headers))
