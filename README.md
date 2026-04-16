# icache_hiperf Workspace

这个目录用于生成、运行和拟合一组合成前端 benchmark，目标是用少量可控模块去逼近真实程序的前端 PMU 画像。

当前工程有两条主线：

1. `fit/fitter.py`
   面向“连续权重 + 分阶段 beam 搜索”的主拟合器。
2. `fit/raw_count_sparse_solver.py`
   面向“11 维 raw count 稀疏组合”的求解器。

这两条主线共享同一套单模块参数库，也共享同一套设备侧 `hiperf` 跑数链路。

## 1. 当前工程在做什么

整个工程分成三个步骤：

1. 先把单模块 case 跑成参数库 CSV。
2. 再基于这些 CSV 做组合搜索。
3. 最后把搜索结果落成整数 repeat plan，回放成真实 bench 去真机验证。

这里最重要的原则是：

- 单模块库里保存的是模块“单位贡献”。
- 搜索时优先关注 raw count。
- `mpki` 和 `miss_rate` 更多是由 raw count 反推出来的检查项，不应该过早拿来裁剪搜索空间。

## 2. 目录结构

- [config/runtime.py](/Users/chentao/Desktop/tmp/icache_hiperf/config/runtime.py)
  运行时配置。定义设备编译、`hdc`、`run_hiperf.sh`、默认 PMU 事件列表和基础模块参数。【F:/Users/chentao/Desktop/tmp/icache_hiperf/config/runtime.py†L3-L17】【F:/Users/chentao/Desktop/tmp/icache_hiperf/config/runtime.py†L20-L37】【F:/Users/chentao/Desktop/tmp/icache_hiperf/config/runtime.py†L40-L84】

- [config/transform.py](/Users/chentao/Desktop/tmp/icache_hiperf/config/transform.py)
  配置扁平化、CSV 表头和派生字段工具。

- [test/experiment_config.py](/Users/chentao/Desktop/tmp/icache_hiperf/test/experiment_config.py)
  单模块 case sweep 和随机组合 probe 的配置中心。【F:/Users/chentao/Desktop/tmp/icache_hiperf/test/experiment_config.py†L23-L45】【F:/Users/chentao/Desktop/tmp/icache_hiperf/test/experiment_config.py†L48-L103】

- [test/single.py](/Users/chentao/Desktop/tmp/icache_hiperf/test/single.py)
  跑单模块参数库。

- [fit/module_combos.py](/Users/chentao/Desktop/tmp/icache_hiperf/fit/module_combos.py)
  跑随机组合 probe，用来观察顺序扰动和线性叠加误差。

- [fit/fitter.py](/Users/chentao/Desktop/tmp/icache_hiperf/fit/fitter.py)
  主拟合器。

- [fit/raw_count_sparse_solver.py](/Users/chentao/Desktop/tmp/icache_hiperf/fit/raw_count_sparse_solver.py)
  11 维 raw-count 稀疏组合求解器。【F:/Users/chentao/Desktop/tmp/icache_hiperf/fit/raw_count_sparse_solver.py†L55-L87】

- [fit/validate_fitted_bench.py](/Users/chentao/Desktop/tmp/icache_hiperf/fit/validate_fitted_bench.py)
  从拟合结果/JSON 回放真实 bench，再跑真机验证。

- [pipeline.py](/Users/chentao/Desktop/tmp/icache_hiperf/pipeline.py)
  单实例代码生成器。

- [combo_codegen.py](/Users/chentao/Desktop/tmp/icache_hiperf/combo_codegen.py)
  多模块组合代码生成器。

- [utils.py](/Users/chentao/Desktop/tmp/icache_hiperf/utils.py)
  设备运行、输出解析、派生指标计算和 CSV 写入工具层。

## 3. 模块角色

当前基础模块有 4 类：

### 3.1 `cold_block_sequence`

用途：

- 提供冷取指路径。
- 更擅长塑造 `L2-TLB access`、`L2-Icache access/refill` 一类结构。

常见参数：

- `blocks`
- `direct_run_len`
- `layout`
- `region_reps`

当前 sweep：

- `blocks = 1000 .. 20000`
- `direct_run_len = [1, 2, 4, 8, 16]`
- `layout = linear / in_page_shuffle(bitrev)`【F:/Users/chentao/Desktop/tmp/icache_hiperf/test/experiment_config.py†L23-L29】

### 3.2 `itlb`

用途：

- 提供跨页代码池。
- 更擅长塑造 `L1/L2 ITLB` 相关计数。

常见参数：

- `funcs`
- `lines_per_page`
- `region_reps`
- `mode`
- `direct_run_len`

当前 sweep：

- `funcs = [256, 512, 1024, 2048, 4096, 8192]`
- `lines_per_page = [1, 4, 8]`
- `region_reps = [1]`
- `mode = chain`
- `direct_run_len = 0`【F:/Users/chentao/Desktop/tmp/icache_hiperf/test/experiment_config.py†L36-L40】【F:/Users/chentao/Desktop/tmp/icache_hiperf/test/experiment_config.py†L89-L102】

### 3.3 `fetch_amplifier`

用途：

- 补 `L1 I-cache / L1 ITLB access`。
- 现在也支持像 `hot` 一样注入固定不跳的 branch 对。

常见参数：

- `blocks`
- `direct_run_len`
- `branch_pairs_per_block`
- `block_slots`
- `region_reps`

当前 sweep：

- `blocks = [32, 64, 128]`
- `direct_run_len = [1, 2, 4, 8]`
- `block_slots = [4, 8, 16]`
- `branch_pairs_per_block`:
  - `4 -> [0, 1, 2]`
  - `8 -> [0, 1, 2, 3]`
  - `16 -> [0, 1, 2, 4, 6]`
- `region_reps = [1000]`【F:/Users/chentao/Desktop/tmp/icache_hiperf/test/experiment_config.py†L42-L45】【F:/Users/chentao/Desktop/tmp/icache_hiperf/test/experiment_config.py†L74-L88】

### 3.4 `hot_region_loop`

用途：

- 主要用来补 branch 和热访问。
- 当前在 `fitter.py` 主线里重新启用了。

常见参数：

- `size`
- `branch_pairs_per_unit`
- `region_reps`

当前 sweep：

- `size = [4096, 8192]`
- `branch_pairs_per_unit = [0, 1, 2, 3, 4]`
- `region_reps = [1000]`【F:/Users/chentao/Desktop/tmp/icache_hiperf/test/experiment_config.py†L31-L34】【F:/Users/chentao/Desktop/tmp/icache_hiperf/test/experiment_config.py†L62-L73】

## 4. PMU 指标与当前口径

设备侧原始 PMU 事件在 [config/runtime.py](/Users/chentao/Desktop/tmp/icache_hiperf/config/runtime.py) 中定义：

- `cpu-cycles:u`
- `instructions:u`
- `br_retired:u`
- `br_mis_pred:u`
- `l1i_cache:u`
- `l1i_cache_refill:u`
- `l1i_tlb:u`
- `l1i_tlb_refill:u`
- `l2i_cache:u`
- `l2i_cache_refill:u`
- `l2i_tlb:u`
- `l2i_tlb_refill:u`【F:/Users/chentao/Desktop/tmp/icache_hiperf/config/runtime.py†L3-L17】

注意：

- `itlb_walk:u` 已经从当前主运行链路中摘掉，不再作为主指标处理。
- `raw_count_sparse_solver.py` 只使用 11 维 raw count 向量，不使用 `cpu-cycles:u`，也不允许把 `ipc` 放进线性拟合空间。【F:/Users/chentao/Desktop/tmp/icache_hiperf/fit/raw_count_sparse_solver.py†L55-L71】【F:/Users/chentao/Desktop/tmp/icache_hiperf/fit/raw_count_sparse_solver.py†L147-L187】

当前 11 维 raw count 空间是：

- `instructions:u`
- `br_retired:u`
- `br_mis_pred:u`
- `l1i_cache:u`
- `l1i_cache_refill:u`
- `l1i_tlb:u`
- `l1i_tlb_refill:u`
- `l2i_cache:u`
- `l2i_cache_refill:u`
- `l2i_tlb:u`
- `l2i_tlb_refill:u`【F:/Users/chentao/Desktop/tmp/icache_hiperf/fit/raw_count_sparse_solver.py†L55-L71】

## 5. 单模块库如何生成

入口：

```bash
cd /Users/chentao/Desktop/tmp/icache_hiperf
python3 test/single.py
```

输出文件：

- `/Users/chentao/Desktop/tmp/icache_hiperf/output/cold_block_sequence.csv`
- `/Users/chentao/Desktop/tmp/icache_hiperf/output/fetch_amplifier.csv`
- `/Users/chentao/Desktop/tmp/icache_hiperf/output/hot_region_loop.csv`
- `/Users/chentao/Desktop/tmp/icache_hiperf/output/itlb.csv`

单模块 CSV 的意义：

- 每一行是一个 case。
- raw count 是按 `run.iters = 1000` 跑出来的总量。
- 在拟合时会先除以 `outer_iters=1000`，变成“单次单位贡献”。【F:/Users/chentao/Desktop/tmp/icache_hiperf/config/runtime.py†L79-L83】【F:/Users/chentao/Desktop/tmp/icache_hiperf/fit/fitter_config.py†L20-L27】

## 6. 随机组合 probe

入口：

```bash
cd /Users/chentao/Desktop/tmp/icache_hiperf
python3 fit/module_combos.py
```

用途：

- 检查组合后和单模块线性累加相比差多少。
- 看顺序扰动是否明显。

输出：

- `/Users/chentao/Desktop/tmp/icache_hiperf/output/random_combo_probe.csv`

## 7. `fitter.py` 主线

入口：

```bash
cd /Users/chentao/Desktop/tmp/icache_hiperf
python3 fit/fitter.py
```

### 7.1 当前思路

`fitter.py` 的核心不是单指标穷举，而是：

1. 读取各 family 的单模块库。
2. 先把 raw count 按 `outer_iters=1000` 归一化成“单位贡献”。
3. 在 family 级别做分阶段 beam 搜索。
4. 每个状态先求连续权重，再落成整数 `repeat_count`。
5. 输出 top-k 结果和选择轨迹。

### 7.2 当前配置重点

配置文件在：
- [fit/fitter_config.py](/Users/chentao/Desktop/tmp/icache_hiperf/fit/fitter_config.py)

当前主配置包括：

- family 上限：
  - `cold_block_sequence = 4`
  - `fetch_amplifier = 3`
  - `hot_region_loop = 2`
  - `itlb = 2`【F:/Users/chentao/Desktop/tmp/icache_hiperf/fit/fitter_config.py†L28-L34】

- 并行搜索：
  - `parallel_workers = 128`
  - `parallel_chunk_size = 64`【F:/Users/chentao/Desktop/tmp/icache_hiperf/fit/fitter_config.py†L68-L72】

- 低 MPKI 近似稳定项：
  - `fetch_amplifier`
  - `hot_region_loop`
  的低 MPKI 原始事件默认不再按重复次数线性放大，这主要是为了解决一些很小的 refill / tlb count 在重复很多次后并不会线性增长的问题。【F:/Users/chentao/Desktop/tmp/icache_hiperf/fit/fitter_config.py†L45-L54】

### 7.3 当前阶段划分

当前 `search_stages` 是：

1. `itlb`：先盯 `l2i_tlb_refill`
2. `cold_block_sequence`：再补 `TLB access + I-cache refill`
3. `fetch_amplifier`：补 `L1 access`
4. `hot_region_loop`：最后修 branch【F:/Users/chentao/Desktop/tmp/icache_hiperf/fit/fitter_config.py†L149-L175】

### 7.4 输出

`fitter.py` 输出：

- `/Users/chentao/Desktop/tmp/icache_hiperf/output/fitter_results.csv`
- `/Users/chentao/Desktop/tmp/icache_hiperf/output/fitter_results.json`
- `/Users/chentao/Desktop/tmp/icache_hiperf/output/best_fit.json`

这些结果包含：

- 连续权重
- 整数 repeat plan
- `pmu_counts`
- 派生 `mpki`
- 派生 `miss_rate`
- 搜索轨迹 `history`

## 8. 11 维 raw-count 稀疏求解器

入口：

```bash
cd /Users/chentao/Desktop/tmp/icache_hiperf
python3 fit/raw_count_sparse_solver.py
```

### 8.1 这条求解器在解决什么问题

它把每个单模块 case 看成一个 11 维 raw count 向量，然后求：

- 选不超过 `max_templates` 个模板
- 找一组 `k_i >= 0`
- 使得 11 个 raw count 尽量落进
  `[(1-tol)*target, (1+tol)*target]`

这条线的特点是：

- 线性求解空间只看 raw count。
- 不在线性空间里直接拟合 `miss_rate`。
- `mpki` 和 `miss_rate` 都是从最终 raw count 反推出来的。

### 8.2 当前搜索配置

默认搜索配置在脚本顶部：

- `max_templates = 20`
- `seed_beam = 48`
- `beam_size = 64`
- `expand_per_state = 24`
- `max_nnls_iter = 4000`
- `tolerance = 0.10`
- `top_k = 20`
- `parallel_workers = 128`
- `parallel_batch_size = 16`【F:/Users/chentao/Desktop/tmp/icache_hiperf/fit/raw_count_sparse_solver.py†L74-L87】

### 8.3 当前实现细节

这版求解器已经支持：

- 11 维 raw count 稀疏搜索
- 多进程子集评估
- persistent process pool
- top-k 去重
- 连续系数 `coefficient`
- 整数量化后的 `repeat_plan_integer`
- `integer_prediction`
- `integer_box_violation`【F:/Users/chentao/Desktop/tmp/icache_hiperf/fit/raw_count_sparse_solver.py†L103-L123】【F:/Users/chentao/Desktop/tmp/icache_hiperf/fit/raw_count_sparse_solver.py†L263-L349】【F:/Users/chentao/Desktop/tmp/icache_hiperf/fit/raw_count_sparse_solver.py†L352-L381】【F:/Users/chentao/Desktop/tmp/icache_hiperf/fit/raw_count_sparse_solver.py†L609-L669】

这里要特别注意：

- `coefficient` 是连续系数，不是整数 repeat。
- `repeat_count` 是后处理量化出来的整数版本。
- `max_box_violation` 是 11 维里最坏一维超出容差盒子的幅度，不是余弦距离，也不是方向角。

### 8.4 输出

输出文件：

- `/Users/chentao/Desktop/tmp/icache_hiperf/output/raw_count_sparse_solver.log`
- `/Users/chentao/Desktop/tmp/icache_hiperf/output/raw_count_sparse_solver_results.json`
- `/Users/chentao/Desktop/tmp/icache_hiperf/output/raw_count_sparse_solver_best.json`

日志中每条结果会同时打印：

- `continuous_prediction`
- `integer_prediction`
- 模块 `coefficient`
- 模块 `repeat_count`

JSON 中会保存：

- `coefficients`
- `repeat_plan_integer`
- `integer_prediction`
- `integer_box_violation`
- 反推得到的 `target_metric_prediction`

## 9. 验证链路

如果你要做真机验证，建议走这条链：

1. 先跑 `fit/fitter.py` 或 `fit/raw_count_sparse_solver.py`
2. 取出整数 `repeat plan`
3. 用验证脚本把它翻译成真实组合 bench
4. 推到设备侧跑 `hiperf`

当前更适合直接接验证的是：

- `best_fit.json`
- 或 `raw_count_sparse_solver_best.json` 里的 `repeat_plan_integer`

## 10. 当前经验和边界

### 10.1 当前更可靠的结论

- `fitter.py` 仍然是当前最稳的主拟合器。
- raw-count 稀疏求解器更本质，但还在继续优化搜索效率和去冗余。
- `miss_rate` 不能直接线性拟合，应当由 raw count 反推。
- 一些很小的热模块事件计数，不能简单按重复次数线性放大。

### 10.2 当前仍在优化的点

- raw-count 稀疏求解器的并行调度和 batch 粒度
- 稀疏搜索里非常相似候选的进一步去冗余
- 连续解到整数 repeat plan 的量化质量

## 11. 建议的日常工作流

如果是正常迭代，建议按这个顺序：

1. 修改 [test/experiment_config.py](/Users/chentao/Desktop/tmp/icache_hiperf/test/experiment_config.py) 的 sweep 范围。【F:/Users/chentao/Desktop/tmp/icache_hiperf/test/experiment_config.py†L23-L45】
2. 运行 `python3 test/single.py` 更新单模块参数库。
3. 运行 `python3 fit/fitter.py` 看主线拟合结果。
4. 如果想验证“11 维 raw count 可行域”，再运行 `python3 fit/raw_count_sparse_solver.py`。
5. 如果需要真机验证，再把整数 `repeat plan` 接到验证脚本。

## 12. 常用命令

单模块参数库：

```bash
cd /Users/chentao/Desktop/tmp/icache_hiperf
python3 test/single.py
```

随机组合 probe：

```bash
cd /Users/chentao/Desktop/tmp/icache_hiperf
python3 fit/module_combos.py
```

主拟合器：

```bash
cd /Users/chentao/Desktop/tmp/icache_hiperf
python3 fit/fitter.py
```

11 维 raw-count 求解器：

```bash
cd /Users/chentao/Desktop/tmp/icache_hiperf
python3 fit/raw_count_sparse_solver.py
```

指定并行 worker 和模板上限：

```bash
cd /Users/chentao/Desktop/tmp/icache_hiperf
python3 fit/raw_count_sparse_solver.py --max-templates 5 --parallel-workers 128 --parallel-batch-size 16
```
