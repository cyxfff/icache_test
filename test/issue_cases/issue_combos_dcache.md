# Dcache Refill 异常组合清单

- 来源 CSV：`output_0506/combo_linearity.csv`
- 筛选规则：关注 `l1d_cache_refill:u` 与 `l2d_cache_refill:u`，只要 `canonical` 或 `shuffle` 相对单模块求和 `sum` 的最大相对偏差 `max_rel_diff >= 0.20`，就记为问题组合。
- 当前收录问题组合数：`8`

## 异常最明显的组合

| case_id | 组合模块数 | 最大相对偏差 | 最差指标 | 出问题的执行顺序 |
| --- | ---: | ---: | --- | --- |
| combo_048_s4 | 4 | 0.4952 | l2d_cache_refill:u | shuffle |
| combo_046_s4 | 4 | 0.4716 | l2d_cache_refill:u | shuffle |
| combo_034_s4 | 4 | 0.3009 | l2d_cache_refill:u | shuffle |
| combo_060_s5 | 5 | 0.2901 | l2d_cache_refill:u | shuffle |
| combo_043_s4 | 4 | 0.2740 | l2d_cache_refill:u | canonical |
| combo_035_s4 | 4 | 0.2433 | l2d_cache_refill:u | shuffle |
| combo_013_s2 | 2 | 0.2164 | l2d_cache_refill:u | canonical |
| combo_015_s2 | 2 | 0.2015 | l2d_cache_refill:u | canonical |

## Case 详情

### combo_048_s4

- 最大相对偏差：`0.495180`
- 最严重的偏差：`shuffle` 顺序下的 `l2d_cache_refill:u`，其中 `sum=555094933`，`obs=829966657`
- 模块组成：
  - `mixed_region_loop` / `mix_b64_ld1_xpage_p1_lp1_r1000`：`size=4096`，`ldr=1`，`mode=cross_page`，`pages=1`，`lp=1`，`reps=1000`
  - `mixed_region_loop_1` / `mix_b64_ld4_pshuf_p128_lp1_r1000`：`size=4096`，`ldr=4`，`mode=page_shuffle`，`pages=128`，`lp=1`，`reps=1000`
  - `mixed_region_loop_2` / `mix_b64_ld4_pshuf_p128_lp1_r1000`：`size=4096`，`ldr=4`，`mode=page_shuffle`，`pages=128`，`lp=1`，`reps=1000`
  - `mixed_region_loop_3` / `mix_b64_ld2_xpage_p524288_lp4_r1000`：`size=4096`，`ldr=2`，`mode=cross_page`，`pages=524288`，`lp=4`，`reps=1000`

### combo_046_s4

- 最大相对偏差：`0.471559`
- 最严重的偏差：`shuffle` 顺序下的 `l2d_cache_refill:u`，其中 `sum=2005538585`，`obs=2951269254`
- 模块组成：
  - `mixed_region_loop` / `mix_b128_ld14_indir_p128_lp1_r1000`：`size=8192`，`ldr=14`，`mode=indirect`，`pages=128`，`lp=1`，`reps=1000`
  - `mixed_region_loop_1` / `mix_b128_ld2_indir_p524288_lp1_r1000`：`size=8192`，`ldr=2`，`mode=indirect`，`pages=524288`，`lp=1`，`reps=1000`
  - `mixed_region_loop_2` / `mix_b128_ld4_pshuf_p1_lp4_r1000`：`size=8192`，`ldr=4`，`mode=page_shuffle`，`pages=1`，`lp=4`，`reps=1000`
  - `mixed_region_loop_3` / `mix_b64_ld2_pshuf_p128_lp1_r1000`：`size=4096`，`ldr=2`，`mode=page_shuffle`，`pages=128`，`lp=1`，`reps=1000`

### combo_034_s4

- 最大相对偏差：`0.300897`
- 最严重的偏差：`shuffle` 顺序下的 `l2d_cache_refill:u`，其中 `sum=749508897`，`obs=975033522`
- 模块组成：
  - `mixed_region_loop` / `mix_b64_ld7_lin_p128_lp4_r1000`：`size=4096`，`ldr=7`，`mode=linear`，`pages=128`，`lp=4`，`reps=1000`
  - `mixed_region_loop_1` / `mix_b64_ld2_lin_p512_lp4_r1000`：`size=4096`，`ldr=2`，`mode=linear`，`pages=512`，`lp=4`，`reps=1000`
  - `mixed_region_loop_2` / `mix_b64_ld2_lin_p512_lp4_r1000`：`size=4096`，`ldr=2`，`mode=linear`，`pages=512`，`lp=4`，`reps=1000`
  - `mixed_region_loop_3` / `mix_b64_ld2_lin_p128_lp1_r1000`：`size=4096`，`ldr=2`，`mode=linear`，`pages=128`，`lp=1`，`reps=1000`

### combo_060_s5

- 最大相对偏差：`0.290133`
- 最严重的偏差：`shuffle` 顺序下的 `l2d_cache_refill:u`，其中 `sum=461377804`，`obs=595238596`
- 模块组成：
  - `mixed_region_loop` / `mix_b128_ld14_indir_p1_lp1_r1000`：`size=8192`，`ldr=14`，`mode=indirect`，`pages=1`，`lp=1`，`reps=1000`
  - `mixed_region_loop_1` / `mix_b128_ld2_pshuf_p128_lp1_r1000`：`size=8192`，`ldr=2`，`mode=page_shuffle`，`pages=128`，`lp=1`，`reps=1000`
  - `mixed_region_loop_2` / `mix_b128_ld1_pshuf_p512_lp4_r1000`：`size=8192`，`ldr=1`，`mode=page_shuffle`，`pages=512`，`lp=4`，`reps=1000`
  - `mixed_region_loop_3` / `mix_b64_ld4_indir_p128_lp4_r1000`：`size=4096`，`ldr=4`，`mode=indirect`，`pages=128`，`lp=4`，`reps=1000`
  - `mixed_region_loop_4` / `mix_b64_ld1_xpage_p1_lp1_r1000`：`size=4096`，`ldr=1`，`mode=cross_page`，`pages=1`，`lp=1`，`reps=1000`

### combo_043_s4

- 最大相对偏差：`0.273997`
- 最严重的偏差：`canonical` 顺序下的 `l2d_cache_refill:u`，其中 `sum=328522153`，`obs=418536136`
- 模块组成：
  - `mixed_region_loop` / `mix_b64_ld14_xpage_p1_lp1_r1000`：`size=4096`，`ldr=14`，`mode=cross_page`，`pages=1`，`lp=1`，`reps=1000`
  - `mixed_region_loop_1` / `mix_b64_ld1_indir_p128_lp1_r1000`：`size=4096`，`ldr=1`，`mode=indirect`，`pages=128`，`lp=1`，`reps=1000`
  - `mixed_region_loop_2` / `mix_b128_ld4_indir_p128_lp4_r1000`：`size=8192`，`ldr=4`，`mode=indirect`，`pages=128`，`lp=4`，`reps=1000`
  - `mixed_region_loop_3` / `mix_b128_ld1_indir_p128_lp4_r1000`：`size=8192`，`ldr=1`，`mode=indirect`，`pages=128`，`lp=4`，`reps=1000`

### combo_035_s4

- 最大相对偏差：`0.243348`
- 最严重的偏差：`shuffle` 顺序下的 `l2d_cache_refill:u`，其中 `sum=444071482`，`obs=552135476`
- 模块组成：
  - `mixed_region_loop` / `mix_b64_ld14_pshuf_p128_lp4_r1000`：`size=4096`，`ldr=14`，`mode=page_shuffle`，`pages=128`，`lp=4`，`reps=1000`
  - `mixed_region_loop_1` / `mix_b128_ld14_pshuf_p1_lp4_r1000`：`size=8192`，`ldr=14`，`mode=page_shuffle`，`pages=1`，`lp=4`，`reps=1000`
  - `mixed_region_loop_2` / `mix_b128_ld2_lin_p1_lp4_r1000`：`size=8192`，`ldr=2`，`mode=linear`，`pages=1`，`lp=4`，`reps=1000`
  - `mixed_region_loop_3` / `mix_b64_ld1_pshuf_p524288_lp1_r1000`：`size=4096`，`ldr=1`，`mode=page_shuffle`，`pages=524288`，`lp=1`，`reps=1000`

### combo_013_s2

- 最大相对偏差：`0.216400`
- 最严重的偏差：`canonical` 顺序下的 `l2d_cache_refill:u`，其中 `sum=30673379`，`obs=24035666`
- 模块组成：
  - `mixed_region_loop` / `mix_b64_ld1_indir_p128_lp4_r1000`：`size=4096`，`ldr=1`，`mode=indirect`，`pages=128`，`lp=4`，`reps=1000`
  - `mixed_region_loop_1` / `mix_b64_ld1_pshuf_p1_lp1_r1000`：`size=4096`，`ldr=1`，`mode=page_shuffle`，`pages=1`，`lp=1`，`reps=1000`

### combo_015_s2

- 最大相对偏差：`0.201539`
- 最严重的偏差：`canonical` 顺序下的 `l2d_cache_refill:u`，其中 `sum=2001044186`，`obs=2404333334`
- 模块组成：
  - `mixed_region_loop` / `mix_b128_ld4_lin_p524288_lp4_r1000`：`size=8192`，`ldr=4`，`mode=linear`，`pages=524288`，`lp=4`，`reps=1000`
  - `mixed_region_loop_1` / `mix_b128_ld14_lin_p128_lp4_r1000`：`size=8192`，`ldr=14`，`mode=linear`，`pages=128`，`lp=4`，`reps=1000`

## 复现方式

使用 `test/issue_cases/run_issue_cases.py` 配合这份 JSON 配置即可：

```bash
python3 test/issue_cases/run_issue_cases.py \
  --config test/issue_cases/issue_combos_dcache.json
```

如果要顺便比较不同的内存布局策略，也可以直接加：

```bash
python3 test/issue_cases/run_issue_cases.py \
  --config test/issue_cases/issue_combos_dcache.json \
  --case-ids combo_013_s2,combo_043_s4 \
  --memory-allocator arena \
  --memory-arena-gap-bytes 2097152 \
  --memory-advice hugepage \
  --memory-prefault 1
```
