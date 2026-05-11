# icache_test

这个仓库现在只保留一条主路径：

- 4 个 instruction 模块
- 每个 instruction 模块都挂载一份 attached-data
- 用单模块 sweep 和多模块组合实验检查硬件计数是否近似线性相加

旧的 standalone data 模块和旧的 `mixed_region_loop` 组合入口已经不再作为当前工作流的一部分。

**当前模块**

- `hot_region_loop`
- `fetch_amplifier`
- `cold_block_sequence`
- `itlb`

## 目录

- [experiments/experiment_config.py](/home/tchen/icache_test/experiments/experiment_config.py:1)
  负责定义 instruction 参数扫法、data 模板、single/combo suite
- [tools/run_single_mixed.py](/home/tchen/icache_test/tools/run_single_mixed.py:1)
  跑单模块 sweep
- [tools/run_combo_linearity.py](/home/tchen/icache_test/tools/run_combo_linearity.py:1)
  跑随机组合线性实验
- [pipeline.py](/home/tchen/icache_test/pipeline.py:1)
  把配置展开成 C 源码
- [modules/mixed_region.py](/home/tchen/icache_test/modules/mixed_region.py:1)
  负责 attached-data 的 node ring、stride、page traversal、ldr 注入底座

## 运行

单模块 sweep：

```bash
python3 tools/run_single_mixed.py
```

只跑一部分模块：

```bash
python3 tools/run_single_mixed.py --modules hot_region_loop fetch_amplifier
```

组合线性实验：

```bash
python3 tools/run_combo_linearity.py
```

先跑一个小样本 smoke：

```bash
python3 tools/run_combo_linearity.py --total-groups 4 --shuffle-rounds 1
```

## instruction 参数

### `hot_region_loop`

- `size`
  指令 footprint，单位 B，内部按 64B 对齐
- `branch_pairs_per_unit`
  每个 64B 指令单元里插入多少对 always-not-taken 条件分支
- `region_reps`
  每轮外层迭代执行多少次

当前 sweep 在 [experiment_config.py](/home/tchen/icache_test/experiments/experiment_config.py:259)：

- `size`: `4096, 8192`
- `branch_pairs_per_unit`: `2, 3, 4`

### `fetch_amplifier`

- `blocks`
  basic block 数量
- `direct_run_len`
  连续直接跳转长度
- `branch_pairs_per_block`
  每个 block 里插入多少对 always-not-taken 条件分支
- `block_slots`
  每个 block 的指令 slot 数
- `layout`
  block 物理布局
- `region_reps`

当前 sweep 在 [experiment_config.py](/home/tchen/icache_test/experiments/experiment_config.py:268)：

- `blocks`: `64, 128`
- `direct_run_len`: `1, 2, 4, 8`
- `branch_pairs_per_block`: `0, 1, 2, 4`
- `block_slots`: 固定 `16`
- `layout`: 固定 `linear`

### `cold_block_sequence`

- `blocks`
- `direct_run_len`
- `layout`
- `region_reps`

当前 sweep 在 [experiment_config.py](/home/tchen/icache_test/experiments/experiment_config.py:281)：

- `blocks`: `1000, 2000, ..., 20000`
- `direct_run_len`: `1, 2, 4, 8, 16`
- `layout`: `in_page_shuffle`, `linear`

### `itlb`

- `funcs`
  函数数量，主要控制代码页数量和 ITLB 压力
- `lines_per_page`
  每页放几条代码行
- `mode`
  当前固定 `chain`
- `direct_run_len`
- `region_reps`

当前 sweep 在 [experiment_config.py](/home/tchen/icache_test/experiments/experiment_config.py:290)：

- `funcs`: `256, 512, 1024, 2048, 4096`
- `lines_per_page`: `1, 2`
- `direct_run_len`: `0, 4`

## attached-data 参数

attached-data 不再按旧的“64B cache line 个数”描述，而是按 `8B node` 建模。

### 核心语义

- `data_pool_nodes`
  pool 中参与 pointer ring 的节点总数
- `data_nodes_per_page`
  每页放多少个 node
- `data_pages`
  派生出的页数，`ceil(data_pool_nodes / data_nodes_per_page)`
- `data_mode`
  ring 的访问顺序
- `data_stride_nodes`
  `node_stride` 模式下的步长
- `data_stride_pages`
  `page_stride` 模式下的步长
- `fusion_ldr_per_unit`
  每个 64B instruction unit 中插入多少条 `ldr x11, [x11]`
- `region_reps`

### 访问模式

- `linear`
  按页序、页内 node 序顺次连成 ring
- `node_stride`
  在所有 node 的平铺序列上按步长循环
- `page_stride`
  页顺序按 stride 循环，页内 node 顺序固定
- `line_shuffle`
  当前保留在 runtime 底座里，但默认 sweep 不再使用
- `random`
  全局随机打乱

实现见 [mixed_region.py](/home/tchen/icache_test/modules/mixed_region.py:20) 和 [mixed_region.py](/home/tchen/icache_test/modules/mixed_region.py:102)

## data 模板

data 现在分 3 个模板族，每个模板族内部继续做参数遍历。

定义见 [experiment_config.py](/home/tchen/icache_test/experiments/experiment_config.py:135)

### `hot`

目标：小 data pool，尽量留在小 cache 层级里，观察高命中、预取、短 stride 的影响

- pool 大小：`2k, 4k, 8k, 16k`
- mode：`node_stride`, `random`
- `data_nodes_per_page`：固定 dense，等于 `512`
- `data_stride_nodes`：`1, 2, 4, 8, 16, 32, 64, 128`

### `cold`

目标：让工作集逐渐跨出 L1D、L2、LLC，重点看 D-cache 容量效应，不主动制造 DTLB 压力

- pool 大小：`64k, 128k, 256k, 512k, 1m, 2m, 4m`
- mode：`node_stride`, `random`
- `data_nodes_per_page`：固定 dense，等于 `512`
- `data_stride_nodes`：`1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048`

### `dtlb`

目标：显式制造跨页访问，主要打 DTLB，不再追求 cache 层级拟合

- pool 大小：`16m, 32m, 64m, 128m, 256m, 512m, 1g`
- mode：`page_stride`, `random`
- `data_nodes_per_page`：`1, 2, 4, 8`
- `data_stride_pages`：`1, 2, 3, 4, 5, 7, 9, 17, 33, 65, 129, 257`

## case label

case label 由 instruction 前缀和 attached-data 后缀组成。

例子：

```text
hot_b64_bp2_r100_hot_2k_nstr_n256_p1_np512_l1_sn1
```

拆开看：

- `hot_b64_bp2_r100`
  `hot_region_loop`
  `b64` 表示 64 个 64B unit，也就是 `4096B`
  `bp2` 表示 `branch_pairs_per_unit=2`
  `r100` 表示 `region_reps=100`
- `hot_2k_nstr_n256_p1_np512_l1_sn1`
  `data_template=hot`
  `data_level=2k`
  `nstr` 表示 `node_stride`
  `n256` 表示 `data_pool_nodes=256`
  `p1` 表示 `data_pages=1`
  `np512` 表示 `data_nodes_per_page=512`
  `l1` 表示 `fusion_ldr_per_unit=1`
  `sn1` 表示 `data_stride_nodes=1`

label 格式实现见 [csv_layout.py](/home/tchen/icache_test/experiments/csv_layout.py:68)

## 内存策略

组合实验默认使用：

- `allocator=arena`
- `prefault=1`
- `warmup_iters=1`

含义：

- `arena`
  所有 attached-data region 从同一个大 `mmap` arena 中切出来，虚拟地址更可控
- `prefault=1`
  测量前逐页 touch，排除首次缺页噪声
- `warmup_iters=1`
  在 perf 统计前先跑一轮完整工作负载

内存布局会在运行输出里打印：

- `arena_span`
- 每个 `data_region`
- 每个 `code_region`

## 输出

### `output/*.csv`

原始结果表。主组合实验默认写：

- `output/combo_linearity.csv`

### `output/*.md`

把 CSV 转成更适合人工看的摘要表。

### CSV 主要字段

当前 CSV 首列只保留当前主路径所需字段：

- `suite, case, order_tag, modules`
- `hot_region_loop_*`
- `fetch_amplifier_*`
- `cold_block_sequence_*`
- `itlb_*`
- `seed, opt_level, iters, warmup_iters, rounds, cpu_core`
- `memory_allocator, memory_advice, memory_arena_gap_bytes, memory_arena_hint, memory_prefault`
- 原始 perf counters
- 派生指标：miss rate、MPKI、IPC

这些字段来自 [config.py](/home/tchen/icache_test/config/config.py:398)

## 当前约定

- 默认研究对象只有 4 个 instruction 模块
- data 一律通过 attached-data 注入
- 不再维护旧 standalone data 路径
- 不再维护旧 `mixed_region_loop` 组合入口
