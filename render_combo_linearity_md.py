#!/usr/bin/env python3

import argparse
import csv
from collections import OrderedDict
from pathlib import Path
from typing import Dict, Iterable, List, Sequence


RAW_COUNT_METRICS = [
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


CORE_COUNT_METRICS = [
    "instructions:u",
    "cpu-cycles:u",
    "br_retired:u",
    "br_mis_pred:u",
    "l1i_cache_refill:u",
    "l1i_tlb_refill:u",
    "l1d_cache_refill:u",
    "l1d_tlb_refill:u",
    "l2d_cache_refill:u",
    "ll_cache_miss:u",
]


def parse_args():
    parser = argparse.ArgumentParser(description="Render combo_linearity.csv as a readable Markdown report.")
    parser.add_argument(
        "--csv",
        default="output/combo_linearity.csv",
        help="Input combo_linearity CSV path.",
    )
    parser.add_argument(
        "--out",
        default="output/combo_linearity.md",
        help="Output Markdown path.",
    )
    parser.add_argument(
        "--metric-set",
        choices=("raw", "core"),
        default="core",
        help="Metric set to show. raw includes all raw count counters; core is a shorter subset.",
    )
    parser.add_argument(
        "--metrics",
        default="",
        help="Optional comma-separated metric override.",
    )
    return parser.parse_args()


def read_csv_rows(csv_path: Path) -> List[Dict[str, str]]:
    with csv_path.open(newline="", encoding="utf-8") as handle:
        rows = []
        for row in csv.DictReader(handle):
            if not row.get("case"):
                continue
            rows.append(row)
        return rows


def group_by_case(rows: Iterable[Dict[str, str]]) -> "OrderedDict[str, List[Dict[str, str]]]":
    grouped: "OrderedDict[str, List[Dict[str, str]]]" = OrderedDict()
    for row in rows:
        grouped.setdefault(row["case"], []).append(row)
    return grouped


def choose_metrics(rows: Sequence[Dict[str, str]], metric_set: str, metrics_override: str) -> List[str]:
    if metrics_override.strip():
        candidates = [metric.strip() for metric in metrics_override.split(",") if metric.strip()]
    elif metric_set == "core":
        candidates = CORE_COUNT_METRICS
    else:
        candidates = RAW_COUNT_METRICS

    return [
        metric
        for metric in candidates
        if any(row.get(metric) not in ("", None) for row in rows)
    ]


def cell_text(value) -> str:
    if value in (None, ""):
        return ""
    return str(value)


def format_ascii_table(headers: Sequence[str], rows: Sequence[Sequence[str]], indent: str = "    ") -> str:
    if not rows:
        return f"{indent}_none_\n"

    table = [[cell_text(cell) for cell in row] for row in rows]
    widths = [
        max(len(str(headers[col])), *(len(row[col]) for row in table))
        for col in range(len(headers))
    ]

    def render_row(row: Sequence[str]) -> str:
        return indent + " | ".join(str(row[col]).ljust(widths[col]) for col in range(len(headers)))

    separator = indent + "-+-".join("-" * width for width in widths)
    lines = [render_row(headers), separator]
    lines.extend(render_row(row) for row in table)
    return "\n".join(lines) + "\n"


def combined_sort_key(row: Dict[str, str]):
    tag = row.get("order_tag", "")
    if tag == "canonical":
        return (0, tag)
    if tag.startswith("shuffle_"):
        return (1, tag)
    if tag == "sum":
        return (2, tag)
    return (3, tag)


def display_order_tags(rows: Sequence[Dict[str, str]]) -> Dict[int, str]:
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


def render_case(case_name: str, rows: Sequence[Dict[str, str]], metrics: Sequence[str]) -> str:
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
    order_labels = display_order_tags(combined)

    single_ids = [f"s{idx}" for idx, _ in enumerate(singles)]
    single_legend_rows = [
        [single_id, row.get("modules", "")]
        for single_id, row in zip(single_ids, singles)
    ]
    single_count_rows = [
        [metric, *[row.get(metric, "") for row in singles]]
        for metric in metrics
    ]

    combined_ids = [order_labels[id(row)] for row in combined]
    combined_legend_rows = [
        [combined_id, row.get("modules", "")]
        for combined_id, row in zip(combined_ids, combined)
    ]
    combined_count_rows = [
        [metric, *[row.get(metric, "") for row in combined]]
        for metric in metrics
    ]

    parts = [
        f"== {case_name} ==\n",
        "single_modules:\n",
        format_ascii_table(["id", "module"], single_legend_rows),
        "single_counts:\n",
        format_ascii_table(["metric", *single_ids], single_count_rows),
        "combined_orders:\n",
        format_ascii_table(["id", "modules"], combined_legend_rows),
        "combined_counts:\n",
        format_ascii_table(["metric", *combined_ids], combined_count_rows),
        "\n",
    ]
    return "".join(parts)


def render_combo_linearity_csv(csv_path: Path, out_path: Path, metric_set: str = "raw", metrics_override: str = ""):
    rows = read_csv_rows(csv_path)
    metrics = choose_metrics(rows, metric_set, metrics_override)
    grouped = group_by_case(rows)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    parts = [
        "== combo_linearity ==\n",
        f"source={csv_path}\n",
        "mode=csv_render_only\n",
        "errors=not_computed\n",
        "layout_snapshots=not_available_from_csv\n",
        f"cases={len(grouped)}\n",
        f"rows={len(rows)}\n",
        f"metrics={len(metrics)}\n",
        f"metric_set={metric_set}\n\n",
    ]
    for case_name, case_rows in grouped.items():
        parts.append(render_case(case_name, case_rows, metrics))

    out_path.write_text("".join(parts), encoding="utf-8")


def main():
    args = parse_args()
    render_combo_linearity_csv(
        Path(args.csv),
        Path(args.out),
        metric_set=args.metric_set,
        metrics_override=args.metrics,
    )


if __name__ == "__main__":
    main()
