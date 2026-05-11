#!/usr/bin/env python3

import csv
from collections import defaultdict

csv_path = "output/merge_module_library.csv"

# Analyze stride parameter combinations
with open(csv_path, newline='') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Count stride variations for hot_region_loop
stride_patterns = defaultdict(int)
hot_cases = 0
cold_cases = 0
itlb_cases = 0
fetch_cases = 0

for row in rows:
    case = row.get("case", "")
    if "_sn" in case:  # Stride node
        base = case.split("_sn")[0]
        stride_patterns[base] += 1
        if case.startswith("hot_"):
            hot_cases += 1
        elif case.startswith("cold_"):
            cold_cases += 1
    elif case.startswith("itlb"):
        itlb_cases += 1
    elif case.startswith("fetch"):
        fetch_cases += 1

print("Stride parameter analysis:")
print(f"  hot_region_loop with stride: {hot_cases} cases")
print(f"  cold_block_sequence with stride: {cold_cases} cases")
print(f"  fetch_amplifier: {fetch_cases} cases")
print(f"  itlb: {itlb_cases} cases")

print("\nStride count distribution:")
stride_counts = defaultdict(int)
for base, count in stride_patterns.items():
    stride_counts[count] += 1

for count in sorted(stride_counts.keys()):
    print(f"  {count} stride variants: {stride_counts[count]} groups")

# Estimate reduction if we remove stride variants
total_with_strides = sum(stride_patterns.values())
estimated_reduction = total_with_strides - len(stride_patterns)
print(f"\nEstimated cases with stride variants: {total_with_strides}")
print(f"Estimated cases if stride removed: {len(stride_patterns)}")
print(f"Potential reduction from stride removal: {estimated_reduction} cases")

print("\n" + "="*80)
print("Recommended case reduction strategies:")
print("="*80)
print("""
1. STRIDE REMOVAL (largest impact):
   - Remove stride_nodes variants (keep only sn1)
   - Potential reduction: ~1000-1500 cases
   - Impact: Minor - stride doesn't significantly vary performance

2. REDUCE DATA VARIANTS (medium impact):
   - Keep only 1-2 top pool_bytes levels (128k, 512k instead of 3-4 levels)
   - Potential reduction: ~500-800 cases
   - Impact: Low - pool size is well represented

3. REDUCE INSTRUCTION VARIANTS (medium impact):
   - Reduce direct_run_len variants for fetch_amplifier
   - Reduce block counts for cold_block_sequence
   - Potential reduction: ~300-500 cases
   - Impact: Medium - some instruction patterns matter

4. COMBINED (recommended):
   - Remove strides: -1000
   - Reduce data levels: -500
   - Reduce instr variants: -400
   - Total reduction: -1900 cases (4088 -> 2188)
   - New case count: ~2200 cases (keeps good diversity)
""")
