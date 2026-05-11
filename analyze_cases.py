#!/usr/bin/env python3

import csv
from collections import defaultdict
from pathlib import Path

csv_path = Path("output/merge_module_library.csv")

# Read and analyze the csv
with open(csv_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"Total rows: {len(rows)}")

# Analyze by module
by_module = defaultdict(list)
for row in rows:
    # Extract base module from "modules" column
    modules_str = row.get("modules", "").split("+")[0]
    module_base = modules_str.split("_")[0] if modules_str else ""
    by_module[module_base].append(row)

print("\nCases by module base:")
for module_name in sorted(by_module.keys()):
    count = len(by_module[module_name])
    print(f"  {module_name}: {count} cases")

# Look for cases with very similar or identical metrics
print("\n" + "="*80)
print("Analyzing metric similarity to find redundant cases...")
print("="*80)

key_metrics = ["instructions:u", "l1d_cache_refill:u", "l2d_cache_refill:u", "br_retired:u"]

# Group by exact metric values
metric_groups = defaultdict(list)
for row in rows:
    key = tuple(
        int(float(row.get(m, 0))) // 100 for m in key_metrics  # Group by 100 for tolerance
    )
    metric_groups[key].append(row)

redundant_count = sum(len(v) - 1 for v in metric_groups.values() if len(v) > 1)
print(f"\nFound {redundant_count} cases that could be considered redundant")
print(f"(within 100-count tolerance on key metrics)")

# Show the largest redundant groups
print("\nLargest redundant groups (cases with very similar metrics):")
sorted_groups = sorted(metric_groups.items(), key=lambda x: -len(x[1]))
for i, (key, cases) in enumerate(sorted_groups[:10]):
    if len(cases) > 1:
        print(f"\nGroup {i+1}: {len(cases)} similar cases")
        sample = cases[0]
        print(f"  Sample case: {sample.get('case', 'N/A')}")
        print(f"  Instructions: {sample.get('instructions:u', 'N/A')}")
        print(f"  L1D refill: {sample.get('l1d_cache_refill:u', 'N/A')}")
        print(f"  L2D refill: {sample.get('l2d_cache_refill:u', 'N/A')}")

# Analyze variation by instructon count levels
print("\n" + "="*80)
print("Instruction count distribution:")
print("="*80)

instr_bins = defaultdict(int)
for row in rows:
    try:
        instr = int(float(row.get("instructions:u", 0)))
        if instr < 1000:
            bin_key = "< 1k"
        elif instr < 10000:
            bin_key = "1k - 10k"
        elif instr < 100000:
            bin_key = "10k - 100k"
        elif instr < 1000000:
            bin_key = "100k - 1m"
        else:
            bin_key = "> 1m"
        instr_bins[bin_key] += 1
    except:
        pass

for bin_key in ["< 1k", "1k - 10k", "10k - 100k", "100k - 1m", "> 1m"]:
    if bin_key in instr_bins:
        print(f"  {bin_key}: {instr_bins[bin_key]} cases")

print("\n" + "="*80)
print("Recommendations for case reduction:")
print("="*80)
print(f"""
Based on analysis:
1. Total cases: {len(rows)}
2. Redundant cases (similar metrics): ~{redundant_count}
3. Suggested reduction: Keep only 1 from each redundant group
4. Estimated new case count: ~{len(rows) - redundant_count} cases

For Gromacs fitting, consider:
- Focus on cases with instructions in the 100k-1m range (more representative)
- Remove near-duplicate metric patterns
- Keep diversity in data patterns for better fitting
""")
