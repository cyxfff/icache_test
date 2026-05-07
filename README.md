# icache_test

这个目录现在主要用于验证一种 **instruction + data fused** 的合成模板：在固定大小的指令区域里，把一部分 `nop` 替换成 pointer-chasing load，让同一个模块同时产生 I-side 和 D-side 行为。

当前重点不是旧版的纯 instruction 模块库，而是 `mixed_region_loop` 以及它的多 slot 组合线性实验。

## 当前实验模型

`mixed_region_loop` 的核心形态是：

```asm
mov x11, cursor

// 每个 64B code unit:
add x9, x9, #1
eor x10, x10, x9
nop / ldr x11, [x11] / nop ...

mov cursor, x11
```

也就是说，每个 active slot 有自己的：

- instruction kernel，例如 `mixed_region_kernel`、`mixed_region_1_kernel`
- data pool，例如 `g_mixed_region_pool`、`g_mixed_region_1_pool`
- cursor，例如 `g_mixed_region_cursor`、`g_mixed_region_1_cursor`
- `region_reps`

组合实验不是把多个参数硬塞进同一个函数，而是启用多个独立 slot，然后在主循环里按顺序执行：

```c
while (!g_abort && completed_iters < iters) {
    for (rep = 0; rep < CONFIG_MIXED_REGION_4_REPS; ++rep)
        run_mixed_region_4_once();

    for (rep = 0; rep < CONFIG_MIXED_REGION_6_REPS; ++rep)
        run_mixed_region_6_once();

    ++completed_iters;
}
```

这个顺序执行本身不是线性成立的原因；更关键的是每个 slot 的 code/data/cursor 是独立的，且 data pointer 通过 inline asm operand 显式进入 `x11`，不是依赖跨函数调用保留某个寄存器。

## D-stream 的真实含义

当前 D 侧是一个 pointer-chasing 环。

初始化时会生成一组 offset：

```python
offset = page_index * 4096 + line_index * 64
```

然后把每个节点写成指向下一个节点：

```c
*(uintptr_t *)(pool + cur) = (uintptr_t)(pool + nxt);
cursor = (uintptr_t)(pool + offsets[0]);
```

运行时反复执行：

```asm
ldr x11, [x11]
```

所以它确实是“分配一片区域，里面放指针，指向区域内另一个地址，然后把起始地址放进 `x11`，持续 pointer chase”。

## 参数语义

当前 sweep 参数在 `test/experiment_config.py` 里定义。D-side 现在按更正交的维度组织：工作集大小、每页节点密度、访问模式，以及只在规则访问 pattern 内部生效的 stride。

| 参数 | 当前作用 | 注意 |
| --- | --- | --- |
| `size` | I-side code payload 大小，当前 4096 或 8192 | 决定每次 kernel 执行多少个 64B code unit |
| `ldr_count_per_unit` | 每个 64B code unit 插入多少条 `ldr x11, [x11]` | 这是最直接的 I/D 混合密度参数 |
| `pages` | D pool 页数，pool bytes = `pages * 4096` | 控制 D 工作集上限 |
| `nodes_per_page` | 每页选几个 64B line 作为 pointer-chain 节点 | 节点会在 4KB 页内均匀摊开，不再总是取前几个 line |
| `data_mode` | offset 排序方式 | 现在使用 `linear`、`line_stride`、`page_stride`、`random` |
| `stride_lines` | 只属于 `line_stride` 模式 | `linear/random/page_stride` 不扫这个参数 |
| `stride_pages` | 只属于 `page_stride` 模式 | `linear/random/line_stride` 不扫这个参数 |
| `region_reps` | 重复执行 mixed kernel 的次数 | 不是独立 D 参数，而是跟着 fused instruction kernel 一起放大 |

`data_mode` 当前推荐四种：

| mode | 排序方式 | 典型含义 |
| --- | --- | --- |
| `linear` | 按页、按 line 顺序访问 | 顺序 pointer chain |
| `line_stride` | 把所有已选节点展平成一维，再按 `stride_lines` 跳 | 显式控制 line/node stride |
| `page_stride` | 对 page 按 `stride_pages` 跳，每个选中 line index 都跑一遍 | 显式控制跨页/TLB stride |
| `random` | 全部节点全局 shuffle | 最大程度打乱访问顺序 |

旧名字仍兼容：`indirect` 会映射到 `random`，`cross_page` 会映射到 `page_stride`，`page_shuffle` 会映射到 `line_shuffle`。新的随机 combo sweep 不再包含 `pages=1`，也不会生成 `line_stride + nodes_per_page=1` 这种明显退化 case。

也就是说，`stride` 不是全局主轴；它只是 `line_stride/page_stride` 这两个规则访问 pattern 的内部参数，避免把 `access_pattern` 的含义混掉。

## 组合线性判断

`run_combo_linearity.py` 会生成 `output/combo_linearity.csv`，并在 benchmark 结束后用 `render_combo_linearity_md.py` 从 CSV 重新生成 `output/combo_linearity.md`。

每个 combo case 通常包含：

- 多条 `single` 行：每个 slot 单独运行的 raw count
- 一条 `canonical` 行：按原顺序组合运行
- 一条 `shuffle_...` 行：换顺序组合运行
- 一条 `sum` 行：把 single raw count 直接求和得到的预测值

判断线性时应比较：

```text
canonical 或 shuffle 实测值
vs
sum 行预测值
```

当前完整结果的主要观察是：

- `instructions:u` 非常线性。
- `br_retired:u` 非常线性。
- `l1d_cache_refill:u` 和 `l1d_tlb_refill:u` 大体线性。
- `l2d_cache_refill:u` 有一定交互，但多数样本仍可用。
- `cpu-cycles:u` 不稳定，不适合作为线性 raw vector 的核心维度。
- `ll_cache_miss:u` 不稳定。
- I-side refill 类 counter 的相对误差很大，但多数 expected MPKI 极低，不能简单按相对误差判死刑。

推荐线性筛选时加入 MPKI 门槛：

```text
如果 single-sum expected MPKI < 0.1，则该 counter 在该 combo 上忽略。
```

这样可以避免把几百、几千级别的低基数噪声放大成“几倍相对误差”。

## 组合约束

随机组合选择逻辑在 `test/runner.py`。

当前有一个保护：

```python
if cases and all(is_hot_booster_case(case) for case in cases):
    continue
```

也就是组合不会全部由 hot booster 组成。

不过当前 `combo_linearity` suite 实际只使用 `mixed_region_loop` slots，且 `ldr_count_per_unit` 取值是 `1, 2, 4, 7, 14`，因此没有纯 hot/no-ldr mixed case。

## 地址输出

benchmark 启动后会打印 memory layout。注意：CSV 里不保存 layout，因此由 CSV 重新生成的 `combo_linearity.md` 只包含 count 表，不包含地址快照。

现在 layout 里包含两类行：

```text
data_region kind=mixed-data name=mixed_region_loop_4 start=0x... end=0x... bytes=... pages=... nodes=... reps=...
code_region kind=mixed-code name=mixed_region_loop_4 symbol=mixed_region_4_kernel entry=0x... end=0x... bytes=... cache_lines=... ldr_per_unit=... reps=... source=nm+objdump
```

`data_region` 是真实 data pool 虚拟地址范围。只打印 `reps > 0` 的 active data pool；组合实验里未启用 slot 的占位 pool 不会出现在报告中。

`nodes` 是 pointer-chain 里的节点数，也就是本次 data pool 中会被串起来的 cache-line offset 数量。对 `mixed_region_loop` 来说，通常等于 `pages * lines_per_page`。例如 `pages=128, lines_per_page=4` 时，`nodes=512`。

`code_region entry/end/bytes` 是编译完成后从 ELF 符号大小和 `objdump -d` 反汇编结果回填出来的函数边界。C 运行时仍会先打印入口地址，但 Python runner 会在 `run_one()` 返回前用构建产物重写 `code_region` 行，因此 combo 报告、单模块 Markdown 报告、以及直接跑单模块脚本的 stdout 都使用同一套严格边界。

`cache_lines` 是严格函数字节数按 64B 向上取整后的 footprint，`ldr_per_unit` 是每个 64B instruction unit 中注入的 `ldr x11, [x11]` 条数，`reps` 是每个 benchmark outer iteration 内重复调用该 mixed kernel 的次数。

如果需要手工复核函数边界，可以在构建产物上用：

```bash
nm -n build/combo_linearity_probe
objdump -d build/combo_linearity_probe
```

## Markdown 报告生成

CSV 只能重新生成 count-only 版本；它不含运行时地址快照。默认脚本会把 count-only 报告写到 `combo_linearity_counts.md`，避免覆盖带 layout 的 `combo_linearity.md`。

```bash
python3 render_combo_linearity_md.py \
  --csv output/combo_linearity.csv \
  --out output/combo_linearity_counts.md
```

默认使用较短的 core raw-count 指标，方便阅读。如果要展开所有 raw count：

```bash
python3 render_combo_linearity_md.py --metric-set raw
```

## Fit Target

`fit/raw_count_sparse_solver.py` 现在不再固定旧的 11-D I-side raw 向量。`fit/fitter_config.py` 中的 `raw_vector_metrics="auto"` 会根据 `target` 能推导出的 raw count 自动选择维度：如果 target 只有 branch/I-cache/I-TLB 指标，就保持旧 11 维；如果加入 `l1d_*`、`l2d_*`、`ll_*` 这类 D-cache/D-TLB/LLC 指标，solver 会自动把对应 raw events 纳入线性求解空间。

注意不要用占位数字填 D-side target。应先从 app target 实测得到 `l1d_cache_mpki`、`l1d_cache_refill_mpki`、`l1d_tlb_mpki`、`l1d_tlb_refill_mpki` 等指标，再写入 `fit/fitter_config.py` 的 `target`。

## 常用命令

```bash
# 跑当前 fused I+D combo 线性实验
python3 run_combo_linearity.py

# 输出目录默认是 output/
python3 run_combo_linearity.py --output-dir output

# 服务器/设备封装入口
python3 run_server.py
```

## 关键文件

| 文件 | 作用 |
| --- | --- |
| `modules/mixed_region.py` | mixed instruction+data 模板，包含 pointer-chain 初始化和 `ldr x11, [x11]` 注入 |
| `pipeline.py` | 生成最终 C benchmark，包括 slot、主循环、memory/code layout 输出 |
| `test/experiment_config.py` | 当前 sweep 和 combo suite 参数 |
| `test/runner.py` | 单 case、combo、shuffle、sum 行生成逻辑 |
| `run_combo_linearity.py` | 当前 combo 线性实验入口 |
| `render_combo_linearity_md.py` | 从 `combo_linearity.csv` 重新生成可读 Markdown count 报告 |
| `output/combo_linearity.csv` | raw count 结果 |
| `output/combo_linearity.md` | 由 CSV 生成的每个 combo 可读 count 报告 |
