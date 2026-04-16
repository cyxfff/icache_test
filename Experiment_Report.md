# Experiment Report

## 1. 目的

当前 `synthesis` 的目标不是直接手工拼一段“大而全”的 benchmark，而是先把前端行为拆成若干个更容易理解、也更容易拟合的模块。每个模块在单独运行时形成一条稳定的性能画像；多个模块组合时，如果它们之间耦合较弱，那么原始计数和 `MPKI` 就可以近似叠加，这样后续才能把目标 benchmark 近似看成这些模块的组合。

换句话说，当前建模思路是：

1. 先构造若干个前端行为明确的基础模块。
2. 单独测量这些模块在不同参数下的计数和 `MPKI` 向量。
3. 再检查多个模块合起来跑时，是否仍然接近“单模块相加”。
4. 如果近似成立，就可以把拟合过程理解为“找一组模块及其权重，使组合后的向量逼近目标 benchmark”。

---

## 2. 当前模块设计

当前对外保留的模块只有 3 个：

1. `cold_block_sequence`
2. `hot_region_loop`
3. `itlb`

之所以先收敛到这 3 个，而不是继续保留更多控制流语义模块，是因为当前阶段更重要的是：

- 模块行为要清楚
- 参数影响要可解释
- 组合后要尽量可加

如果一开始就把 `call/ret`、`plt stub`、`indirect target` 这些更复杂的控制流模块一起放进来，虽然现象会更多，但会明显增加耦合来源，不利于先建立一个稳定的基础模型。

### 2.1 `cold_block_sequence`

实现文件：`modules/block_loop.py`

设计目的：

- 构造一个“冷的基本块序列”模块
- 主要控制前端的 block-to-block 取指路径
- 更偏向 `I-cache`、分支密度和取指工作集，而不是页级 `ITLB`

它的核心形态是：

- 有很多固定大小、固定对齐的基本块
- 基本块之间按某种顺序跳转
- 可以连续直接跳转若干次，也可以周期性插入一次间接调度

之所以需要这个模块，是因为它提供了一个和 `hot_region_loop` 完全不同的方向：

- `hot_region_loop` 更像“连续热区”
- `cold_block_sequence` 更像“离散块链”

因此它更适合控制：

- `br_retired`
- `l1i_cache`
- `l1i_cache_refill`
- 在布局打散较强时，也会间接带动部分 `l1i_tlb`

参数如下：

- `blocks`
  - 基本块总数
  - 决定整体代码工作集大小
  - 值越大，通常越容易提高 `l1i_cache_refill_mpki`

- `block_align`
  - 每个基本块的对齐大小
  - 会影响一页里能放多少块，也会影响页内块分布
  - 当前通常固定为 `64`

- `direct_run_len`
  - 连续多少次直接跳转之后，插入一次间接调度
  - `1` 表示几乎每一步都通过 dispatch 走一次
  - 更大的值会让控制流更接近纯直接链

- `region_reps`
  - 每轮外层循环中重复多少次该模块
  - 主要控制该模块在整次运行中的权重

- `layout`
  - 决定块顺序的生成方式
  - 当前支持 3 种：
    - `linear`
    - `in_page_shuffle`
    - `full_shuffle`

其中：

- `linear`
  - 物理和执行顺序都最规则
  - 局部性最强

- `in_page_shuffle`
  - 先随机排列页面
  - 再在每个页内按 bit-reversal 顺序访问 block slot
  - 这个模式比“纯随机”更稳定，也更容易明确打散页内预取

- `full_shuffle`
  - 对所有块做全局随机打散
  - 最激进，但稳定性也最差

- `pos`
  - 模块在整轮执行中的顺序位置

### 2.2 `hot_region_loop`

实现文件：`modules/hot_region.py`

设计目的：

- 构造一个连续、可重复、可控的小热区
- 作为整个合成 benchmark 里的“热分母模块”
- 主要用来增加热取指活动，而不是制造大量冷 miss

之所以需要这个模块，是因为单独做“冷模块”很容易导致：

- `l1i_cache_refill` 高
- `l2i_cache_refill` 高
- 但整体 `l1i_cache` 分母不够大

此时很多目标点就很难达到。
`hot_region_loop` 的作用就是提供一个稳定热区，让整体程序保持较大的热取指分母，从而更容易构造：

- 低总体 `L1I miss rate`
- 但局部存在较深冷 miss 的组合

参数如下：

- `size`
  - 热区字节数
  - 决定连续热区 footprint
  - 典型档位对应不同热区大小

- `region_reps`
  - 每轮重复多少次热区
  - 是该模块最重要的权重参数
  - 值越大，整体程序中热区占比越高

- `pos`
  - 模块执行顺序
  - 如果多个模块组合，`hot_region_loop` 在前还是在后，会影响后续模块看到的前端状态

这个模块主要影响：

- `l1i_cache_mpki`
- `instructions`
- 对 `l1i_cache_refill_mpki` 有稀释作用

通常它不负责制造强的 `ITLB` 压力，也不主打复杂控制流。

### 2.3 `itlb`

实现文件：`modules/tlb_region.py`

设计目的：

- 构造一个跨页代码池模块
- 主要控制页工作集和页间跳转
- 用来塑造 `ITLB`、`L2 TLB`、`page walk`，以及与之伴随的冷取指行为

这个模块本质上是：

- 一组 `4KB` 对齐的代码页
- 每页对应一个函数
- 按设定顺序在这些页之间跳转
- 每页内部只执行有限个 cache line

当前它已经吸收了旧的 `page_sparse` 思路，所以不再单独保留 `page_sparse`。
统一后的好处是：同一种“代码页池”模块，只通过参数变化就可以衍生出不同对象。

参数如下：

- `funcs`
  - 代码页数量
  - 也是页工作集大小的主要控制量
  - 通常用 `2^k` 档位，例如 `128 ~ 4096`

- `lines_per_page`
  - 每页执行多少个 `64B` cache line
  - `1` 更接近“只触碰这个页就走”
  - 更大的值会让该模块不仅影响 `ITLB`，也越来越明显地影响 `I-cache`

- `region_reps`
  - 每轮重复多少次
  - 控制该模块整体权重

- `mode`
  - 当前主要使用 `chain`
  - 表示当前页函数直接跳到下一个页函数
  - 这种模式更适合连续跨页执行

- `direct_run_len`
  - 当前测试中暂时禁用，通常设为 `0`
  - 启用时表示每隔多少个直接跳转插入一次间接 dispatch

- `pos`
  - 执行顺序

这个模块主要影响：

- `l1i_tlb_mpki`
- `l1i_tlb_refill_mpki`
- `l2i_tlb_mpki`
- `l2i_tlb_refill_mpki`
- `itlb_walk_mpki`

同时，随着 `lines_per_page` 增大，它也会越来越明显地影响：

- `l1i_cache_refill_mpki`
- `l2i_cache_refill_mpki`

---

## 3. 当前实验结果

### 3.1 最近一次验证

- 实验日期：2026-04-16
- 搜索方法：`fit/raw_count_sparse_solver.py`
- 目标类型：raw count + 派生 MPKI / miss_rate 检查
- 组合结果来源：`output/raw_count_sparse_solver_best.json`
- 验证脚本：`fit/validate_fitted_bench.py`

### 3.2 最终执行计划

验证回放的整数计划为：

- `cold_b11000_d2_linear` x 14
- `fetch_b128_d4_bp0_s4_r1000` x 29
- `hot_s8192_b3_r1000` x 35
- `itlb_f512_l1_r1` x 205
- `itlb_f4096_l1_r1` x 8

### 3.3 真机执行结果

- 执行指令数：2,105,033,903
- 运行耗时：
  - `bench_seconds` = 0.762711875
  - `bench_seconds` = 0.755941250
  - `bench_seconds` = 0.760561563
  -（以上为三个 perf group 的实际 bench 时长）

### 3.4 验证对比指标

#### miss_rate

- `br_miss_rate`：目标 2.8141% / 实测 3.0550% / delta 0.2409% / rel_err 8.56%
- `l1i_miss_rate`：目标 5.5394% / 实测 7.5868% / delta 2.0474% / rel_err 36.96%
- `l2i_miss_rate`：目标 62.2989% / 实测 58.5756% / delta -3.7233% / rel_err 5.98%
- `l1i_tlb_miss_rate`：目标 0.4984% / 实测 0.5822% / delta 0.0838% / rel_err 16.81%
- `l2i_tlb_miss_rate`：目标 16.1292% / 实测 20.9795% / delta 4.8503% / rel_err 30.07%

#### mpki_and_raw

- `br_mis_pred_mpki`：目标 5.554000 / 实测 5.826509 / delta 0.272509 / rel_err 4.91%
- `br_retired_mpki`：目标 197.462000 / 实测 190.720153 / delta -6.741847 / rel_err 3.41%
- `l1i_cache_mpki`：目标 344.559000 / 实测 233.548785 / delta -111.010215 / rel_err 32.22%
- `l1i_cache_refill_mpki`：目标 19.088000 / 实测 17.718902 / delta -1.369098 / rel_err 7.17%
- `l2i_cache_mpki`：目标 17.860000 / 实测 17.625797 / delta -0.234203 / rel_err 1.31%
- `l2i_cache_refill_mpki`：目标 11.123000 / 实测 10.324416 / delta -0.798584 / rel_err 7.18%
- `l1i_tlb_mpki`：目标 246.990000 / 实测 228.963625 / delta -18.026375 / rel_err 7.30%
- `l1i_tlb_refill_mpki`：目标 1.231000 / 实测 1.332943 / delta 0.101943 / rel_err 8.28%
- `l2i_tlb_mpki`：目标 1.846000 / 实测 1.360169 / delta -0.485831 / rel_err 26.32%
- `l2i_tlb_refill_mpki`：目标 0.298000 / 实测 0.285356 / delta -0.012644 / rel_err 4.24%
- `l2i_cache_access_proxy_mpki`：目标 17.854248 / 实测 17.625797 / delta -0.228451 / rel_err 1.28%
- `l2i_tlb_access_proxy_mpki`：目标 1.847581 / 实测 1.360169 / delta -0.487412 / rel_err 26.38%

### 3.5 关键结论

- 这次验证结果显示，当前组合在 `l1i_cache_mpki` 和 `l1i_miss_rate` 方向误差最大，说明实际取指冷 miss 与目标不一致。
- `l2i_cache` 相关指标表现较好，说明当前组合在 L2 访问方向上更接近目标。
- `l2i_tlb_mpki` 和 `l2i_tlb_access_proxy_mpki` 差距较大，提示跨页/ITLB 方向的权重需要进一步校准。

---

## 4. 记录格式

每次实验推荐记录以下字段：

| 项目 | 内容 |
|---|---|
| 实验日期 | YYYY-MM-DD |
| 搜索方法 | e.g. raw_count_sparse_solver / MILP / beam search 等 |
| 目标类型 | raw count / mpki / miss_rate / 混合 |
| 目标指令数 | target instructions |
| 组合方案 | 模块+case+repeat_count 列表 |
| 预测 raw 结果 | raw prediction 向量、instructions/u、br_retired/u 等 |
| 预测整数结果 | integer repeat plan、integer prediction |
| 验证实际执行 | 实际 instructions、执行耗时、实际 metrics |
| 真机与 target 比较 | 关键 metric delta 和相对误差 |
| 备注 | 特殊说明、问题、观察 |

---

## 5. 以后每次实验建议填写的标准条目

### 5.1 搜索阶段

1. 说明使用的求解器
   - `fit/raw_count_sparse_solver.py`：11 维 raw count 稀疏组合
   - `--use-milp`：如果启用 MILP 求解
   - `fit/fitter.py`：连续权重 + 分阶段 beam search
2. 说明搜索参数
   - `max_templates`
   - `tolerance`
   - `parallel_workers`
   - `stable_low_mpki_threshold`
3. 记录最终 `output/raw_count_sparse_solver_best.json` 或 `fit` 结果 JSON

### 5.2 组合比较

- 记录 `raw_target` vs `raw_prediction` 每个关键指标的值
- 记录 `integer_prediction` vs `raw_target` 的最大 item 差异
- 对于 `br_retired_mpki / l1i_cache_mpki / l2i_cache_refill_mpki` 等指标，写出实际偏差

### 5.3 真机验证

- 记录 `validate_fitted_bench.py` 的实际执行 plan
- 记录 `actual_instructions`
- 如果可以，从硬件侧日志补充 `elapsed time (s)` 和 `bench_seconds`
- 记录实际 metrics 和 target 的对比

---

## 6. 记录模板示例

```md
### 实验 YYYY-MM-DD

- 方法：`raw_count_sparse_solver.py`
- 参数：`--max-templates 20 --tolerance 0.10 --top-k 1`
- 目标：raw count + MPKI
- raw target instructions：100,000,000

#### 组合方案
- module 1 x N
- module 2 x M

#### 预测结果
- raw instructions：...
- raw br_retired:u：...
- raw l2i_cache_refill:u：...

#### 真机验证
- 实际 instructions：...
- 实际耗时：... s
- actual br_retired_mpki：...
- actual l1i_cache_mpki：...
- actual l2i_cache_refill_mpki：...

#### 对比
- br_retired_mpki delta：actual - target = ...
- l1i_cache_mpki delta：...

#### 结论
- 这次组合的主要偏差在 ...
```

---

## 7. 说明

当前实验报告文档主要用于规范化记录，后续每次搜索完成后可直接补齐：

- `Experiment_Report.md` 中新增一节
- 或者按上述模板追加到 README 末尾

如果你希望，我可以继续把这个模板改成“自动生成实验报告”的 Python 脚本。



base) chentao@ChentaodeMacBook-Air icache_hiperf % python3 fit/validate_fitted_bench.py  
Loading plan from /Users/chentao/Desktop/tmp/icache_hiperf/output/raw_count_sparse_solver_best.json...
[validate_fitted_bench] warning: resolved candidate by module/case/source_csv fallback for ('itlb', 'itlb_f512_l1_r1', 'itlb.csv')
[validate_fitted_bench] warning: resolved candidate by module/case/source_csv fallback for ('itlb', 'itlb_f4096_l1_r1', 'itlb.csv')
plan_json: /Users/chentao/Desktop/tmp/icache_hiperf/output/raw_count_sparse_solver_best.json
== Validation Compare ==
  repeat_plan: cold_b11000_d2_linear x 14 | fetch_b128_d4_bp0_s4_r1000 x 29 | hot_s8192_b3_r1000 x 35 | itlb_f512_l1_r1 x 205 | itlb_f4096_l1_r1 x 8
  exec_instructions: 2105033903
  miss_rate:
    metric            | target   | exec     | delta    | rel_err
    ------------------+----------+----------+----------+--------
    br_miss_rate      | 2.8141%  | 3.0550%  | 0.2409%  | 8.56%  
    l1i_miss_rate     | 5.5394%  | 7.5868%  | 2.0474%  | 36.96% 
    l2i_miss_rate     | 62.2989% | 58.5756% | -3.7233% | 5.98%  
    l1i_tlb_miss_rate | 0.4984%  | 0.5822%  | 0.0838%  | 16.81% 
    l2i_tlb_miss_rate | 16.1292% | 20.9795% | 4.8503%  | 30.07% 
  mpki_and_raw:
    metric                      | target     | exec       | delta       | rel_err
    ----------------------------+------------+------------+-------------+--------
    br_mis_pred_mpki            | 5.554000   | 5.826509   | 0.272509    | 4.91%  
    br_retired_mpki             | 197.462000 | 190.720153 | -6.741847   | 3.41%  
    l1i_cache_mpki              | 344.559000 | 233.548785 | -111.010215 | 32.22% 
    l1i_cache_refill_mpki       | 19.088000  | 17.718902  | -1.369098   | 7.17%  
    l2i_cache_mpki              | 17.860000  | 17.625797  | -0.234203   | 1.31%  
    l2i_cache_refill_mpki       | 11.123000  | 10.324416  | -0.798584   | 7.18%  
    l1i_tlb_mpki                | 246.990000 | 228.963625 | -18.026375  | 7.30%  
    l1i_tlb_refill_mpki         | 1.231000   | 1.332943   | 0.101943    | 8.28%  
    l2i_tlb_mpki                | 1.846000   | 1.360169   | -0.485831   | 26.32% 
    l2i_tlb_refill_mpki         | 0.298000   | 0.285356   | -0.012644   | 4.24%  
    l2i_cache_access_proxy_mpki | 17.854248  | 17.625797  | -0.228451   | 1.28%  
    l2i_tlb_access_proxy_mpki   | 1.847581   | 1.360169   | -0.487412   | 26.38% 
===== round 1/1 =====
===== perf group =====
events=raw-cpu-cycles:u,raw-instruction-retired:u,raw-br-mis-pred:u,raw-br-retired:u
iters=1
cpu_mask=800
PID is 36501
Profiling duration is 10000.000 seconds.
Start Profiling...
tracked processes have exited (total 923 ms)
                    count  name                           | comment                          | coverage
               12,264,999  raw-br-mis-pred:u              |                                  | (100%)
              401,472,387  raw-br-retired:u               |                                  | (100%)
              886,779,760  raw-cpu-cycles:u               |                                  | (100%)
            2,105,033,903  raw-instruction-retired:u      |                                  | (100%)
PROXYBENCH_READY
completed_iters=1
bench_seconds=0.762711875

===== perf group =====
events=raw-instruction-retired:u,raw-l1-icache:u,raw-l1-icache-refill:u,raw-l2-icache:u,raw-l2-icache-refill:u
iters=1
cpu_mask=800
PID is 36526
Profiling duration is 10000.000 seconds.
Start Profiling...
tracked processes have exited (total 948 ms)
                    count  name                           | comment                          | coverage
            2,105,031,684  raw-instruction-retired:u      |                                  | (100%)
               37,298,850  raw-l1-icache-refill:u         |                                  | (100%)
              491,627,593  raw-l1-icache:u                |                                  | (100%)
               21,733,222  raw-l2-icache-refill:u         |                                  | (100%)
               37,102,861  raw-l2-icache:u                |                                  | (100%)
PROXYBENCH_READY
completed_iters=1
bench_seconds=0.755941250

===== perf group =====
events=raw-instruction-retired:u,raw-l1-itlb:u,raw-l1-itlb-refill:u,raw-l2-itlb:u,raw-l2-itlb-refill:u
iters=1
cpu_mask=800
PID is 36548
Profiling duration is 10000.000 seconds.
Start Profiling...
tracked processes have exited (total 958 ms)
                    count  name                           | comment                          | coverage
            2,105,042,814  raw-instruction-retired:u      |                                  | (100%)
                2,805,902  raw-l1-itlb-refill:u           |                                  | (100%)
              481,978,234  raw-l1-itlb:u                  |                                  | (100%)
                  600,687  raw-l2-itlb-refill:u           |                                  | (100%)
                2,863,213  raw-l2-itlb:u                  |                                  | (100%)
PROXYBENCH_READY
completed_iters=1
bench_seconds=0.760561563


validation written to /Users/chentao/Desktop/tmp/icache_hiperf/output/fitted_bench_validation.csv
(base) chentao@ChentaodeMacBook-Air icache_hiperf % 