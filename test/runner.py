#!/usr/bin/env python3

import math
import random
from copy import deepcopy
from pathlib import Path

if __package__ in (None, "", "test"):
    from config import zero_all_modules
    from test.csv_layout import join_case_labels, metric_headers, with_metric_separators
    from utils import calc_derived, run_one, write_csv_row
else:
    from ..config import zero_all_modules
    from .csv_layout import join_case_labels, metric_headers, with_metric_separators
    from ..utils import calc_derived, run_one, write_csv_row


CSV_PREFIX = ["suite", "case", "order_tag", "modules"]
HOT_BOOSTER_MODULES = {"hot_region_loop", "fetch_amplifier", "data_hot_stride"}
COUNT_METRICS = [
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
]


def is_hot_booster_case(case):
    module_name = case["module"]
    params = case.get("params", {})
    if module_name in HOT_BOOSTER_MODULES:
        return True
    if module_name == "mixed_region_loop" or module_name.startswith("mixed_region_loop_"):
        return int(params.get("ldr_count_per_unit", 0)) <= 0
    return False


def suite_report_path(output_dir, suite_cfg):
    report_name = suite_cfg.get("report_name")
    if report_name:
        return output_dir / report_name
    return output_dir / f"{Path(suite_cfg['csv_name']).stem}.md"


def init_markdown_report(report_out, suite_name):
    report_out.parent.mkdir(parents=True, exist_ok=True)
    report_out.write_text(f"# {suite_name}\n\n", encoding="utf-8")


def append_markdown(report_out, text):
    with report_out.open("a", encoding="utf-8") as handle:
        handle.write(text)


def format_param_value(value):
    if isinstance(value, float):
        return f"{value:.6g}"
    return str(value)


def format_case_config(case):
    params = case.get("params", {})
    if not params:
        return f"- `{join_case_labels([case])}`: no params\n"
    param_text = ", ".join(f"`{key}={format_param_value(value)}`" for key, value in sorted(params.items()))
    return f"- `{join_case_labels([case])}`: {param_text}\n"


def format_metric_value(value):
    if value in ("", None):
        return ""
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def format_ascii_table(headers, rows, indent="    "):
    if not rows:
        return f"{indent}_none_\n"

    table = [[format_metric_value(cell) for cell in row] for row in rows]
    widths = [
        max(len(str(headers[col])), *(len(row[col]) for row in table))
        for col in range(len(headers))
    ]

    def render_row(row):
        return indent + " | ".join(str(row[col]).ljust(widths[col]) for col in range(len(headers)))

    separator = indent + "-+-".join("-" * width for width in widths)
    lines = [render_row(headers), separator]
    lines.extend(render_row(row) for row in table)
    return "\n".join(lines) + "\n"


def combined_sort_key(row):
    tag = row.get("order_tag", "")
    if tag == "canonical":
        return (0, tag)
    if tag.startswith("shuffle_"):
        return (1, tag)
    if tag == "sum":
        return (2, tag)
    return (3, tag)


def display_order_tags(rows):
    shuffle_count = 0
    shuffle_total = sum(1 for row in rows if row.get("order_tag", "").startswith("shuffle_"))
    labels = {}
    for row in rows:
        tag = row.get("order_tag", "")
        if tag.startswith("shuffle_"):
            shuffle_count += 1
            labels[id(row)] = "shuffle" if shuffle_total == 1 else f"shuffle_{shuffle_count}"
        else:
            labels[id(row)] = tag
    return labels


def format_result_table(rows):
    metrics = [metric for metric in COUNT_METRICS if any(row.get(metric) not in ("", None) for row in rows)]
    if not metrics:
        return "_No metrics captured._\n"

    singles = [row for row in rows if row.get("order_tag") == "single"]
    combined = sorted(
        [
            row
            for row in rows
            if row.get("order_tag") == "canonical"
            or row.get("order_tag") == "sum"
            or row.get("order_tag", "").startswith("shuffle_")
        ],
        key=combined_sort_key,
    )

    parts = []
    if singles:
        single_ids = [f"s{idx}" for idx, _ in enumerate(singles)]
        parts.extend(
            [
                "single_modules:\n",
                format_ascii_table(
                    ["id", "module"],
                    [[single_id, row.get("modules", "")] for single_id, row in zip(single_ids, singles)],
                ),
                "single_counts:\n",
                format_ascii_table(
                    ["metric", *single_ids],
                    [[metric, *[row.get(metric, "") for row in singles]] for metric in metrics],
                ),
            ]
        )

    if combined:
        order_labels = display_order_tags(combined)
        combined_ids = [order_labels[id(row)] for row in combined]
        parts.extend(
            [
                "combined_orders:\n",
                format_ascii_table(
                    ["id", "modules"],
                    [[combined_id, row.get("modules", "")] for combined_id, row in zip(combined_ids, combined)],
                ),
                "combined_counts:\n",
                format_ascii_table(
                    ["metric", *combined_ids],
                    [[metric, *[row.get(metric, "") for row in combined]] for metric in metrics],
                ),
            ]
        )

    return "".join(parts)


def extract_memory_layout_blocks(raw_output):
    blocks = []
    current = []
    capturing = False
    for line in raw_output.splitlines():
        if line.strip() == "===== memory layout =====":
            if current:
                blocks.append(current)
            current = [line]
            capturing = True
            continue
        if not capturing:
            continue
        if line.startswith("iters=") or line.startswith("data_region ") or line.startswith("code_region "):
            current.append(line)
            continue
        blocks.append(current)
        current = []
        capturing = False
    if current:
        blocks.append(current)
    return blocks


def format_memory_layout(raw_output):
    blocks = extract_memory_layout_blocks(raw_output)
    if not blocks:
        return "_No memory layout block captured._\n"
    text = "```text\n" + "\n".join(blocks[0]) + "\n```\n"
    if len(blocks) > 1:
        text += f"\nCaptured `{len(blocks)}` layout snapshots across perf event groups; showing the first one.\n"
    return text


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
    return tagged_row, raw_output


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
    report_out = suite_report_path(output_dir, suite_cfg)
    init_markdown_report(report_out, suite_name)

    for case in suite_cfg["cases"]:
        cfg = build_single_cfg(base_cfg, case)
        row, raw_output = write_tagged_run(
            cfg,
            knobs,
            csv_headers,
            csv_out,
            suite_name=suite_name,
            case_name=join_case_labels([case]),
            order_tag="single",
            modules_tag=join_case_labels([case]),
        )
        append_markdown(
            report_out,
            (
                f"## {join_case_labels([case])}\n\n"
                "### Configuration\n"
                f"{format_case_config(case)}\n"
                "### Result\n"
                f"{format_result_table([row])}\n"
                "### Memory Layout\n"
                f"{format_memory_layout(raw_output)}\n"
            ),
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
        if cases and all(is_hot_booster_case(case) for case in cases):
            continue
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
    report_out = suite_report_path(output_dir, suite_cfg)
    init_markdown_report(report_out, suite_name)
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
            single_reports = []
            combined_reports = []

            for case in selected_cases:
                row, raw_output = write_tagged_run(
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
                single_reports.append((case, row, raw_output))

            ordered_runs = list(distinct_orders(selected_cases, suite_cfg.get("shuffle_rounds", 0), rng))
            for ordered_cases, order_tag in ordered_runs:
                cfg = build_combined_cfg(base_cfg, selected_cases, ordered_cases)
                row, raw_output = write_tagged_run(
                    cfg,
                    knobs,
                    csv_headers,
                    csv_out,
                    suite_name=suite_name,
                    case_name=case_name,
                    order_tag=order_tag,
                    modules_tag=join_case_labels(ordered_cases),
                )
                combined_reports.append((ordered_cases, row, raw_output))

            sum_row = build_sum_row(base_cfg, metric_keys, single_rows, selected_cases, suite_name, case_name, "sum")
            write_csv_row(
                csv_out,
                csv_headers,
                sum_row,
            )
            report_rows = [row for _, row, _ in single_reports]
            report_rows.extend(row for _, row, _ in combined_reports)
            report_rows.append(sum_row)
            report_text = [
                f"## {case_name}\n\n",
                "### Selected Cases\n",
                "".join(format_case_config(case) for case in selected_cases),
                "\n### Combination Rule\n",
                f"- combo size: `{combo_size}`\n",
                "- rejected if every selected case is a hot booster template\n",
                f"- canonical order: `{join_case_labels(selected_cases)}`\n",
                "\n### Results\n",
                format_result_table(report_rows),
                "\n### Combined Memory Layouts\n",
            ]
            for ordered_cases, row, raw_output in combined_reports:
                report_text.append(f"#### {row.get('order_tag', '')}: `{join_case_labels(ordered_cases)}`\n\n")
                report_text.append(format_memory_layout(raw_output))
                report_text.append("\n")
            report_text.append("### Single-Case Memory Layouts\n")
            for case, row, raw_output in single_reports:
                report_text.append(f"#### `{join_case_labels([case])}`\n\n")
                report_text.append(format_memory_layout(raw_output))
                report_text.append("\n")
            append_markdown(report_out, "".join(report_text))

            write_csv_row(csv_out, csv_headers, make_blank_row(csv_headers))
