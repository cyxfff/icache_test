# icache_test 与 merge_bench 线性相加差异分析

## 结论先说

两个目录里的代码表面上都在做一件类似的事：在 instruction 模块的空槽里，把一部分 `nop` 换成 `ldr x11, [x11]`，用 instruction stream 带动 data stream。这个方向是一样的。

但这次对比的两个实验并不是同一个模块、同一种运行语义、同一种内存模型。`icache_test` 里新的 `combo_linearity` 用的是专门的 `mixed_region_loop` slot 模型；`merge_bench` Phase A 用的是 `hot_region_loop`、`fetch_amplifier`、`cold_block_sequence`、`itlb` 等原 instruction module 加 LDR 注入。

所以更准确的判断是：

- `icache_test` 能线性相加，不是因为“跑完一个再跑下一个”这个形式本身；`merge_bench` 也是 segment 顺序执行。更关键的是，`icache_test` 的每个 case slot 有自己的 code、data pool 和 cursor，并且主循环真实执行每个 slot 的 `region_reps=1000`。
- `merge_bench` 当前 Phase A 的“不线性”里有三类问题混在一起：第一类是运行异常，部分 combo 没有正常打印 `completed_iters`；第二类是生成语义差异，`region_reps` 被读出来但最终没有进入主循环执行次数；第三类是更底层的 ABI/register contract 问题，D-stream cursor 通过 `x11` 隐式传入 naked asm function，但实际编译后的二进制并没有稳定地在每次调用前把 pool head 放进 `x11`。
- `icache_test` 也不是所有 raw counter 都线性。它的 `instructions:u`、`l1d_cache_refill:u`、`l1d_tlb_refill:u` 很线性；但 `l1i_cache_refill:u`、`ll_cache_miss:u` 仍然有明显非线性。这说明这里的线性主要成立在“确定性工作量”和部分 D-side 事件上，不是硬件计数器普遍满足线性。

## 使用的证据

主要看了这些文件和结果：

- `/home/tchen/icache_test/test/experiment_config.py`
- `/home/tchen/icache_test/modules/mixed_region.py`
- `/home/tchen/icache_test/pipeline.py`
- `/home/tchen/icache_test/output/combo_linearity.csv`
- `/home/tchen/icache_test/output/combo_linearity.md`
- `/home/tchen/icache_test/build/combo_linearity_probe.c`
- `/home/tchen/merge_bench/src/merge_codegen.py`
- `/home/tchen/merge_bench/src/modules/hot_region.py`
- `/home/tchen/merge_bench/src/modules/block_loop.py`
- `/home/tchen/merge_bench/scripts_homo/run_phase_a_single.py`
- `/home/tchen/merge_bench/data/linux_server_validation/phase_a_combo/phase_a_combo_vectors.csv`
- `/home/tchen/merge_bench/data/linux_server_validation/phase_a_analysis/phase_a_combo_residuals.csv`
- `/home/tchen/merge_bench/data/linux_server_validation/phase_a_combo/*/logs/group_01_run_1.bench.log`

## 1. 两边的 Instruction 模块是否一样？

结论：不一样。思想相似，但本次实验实际跑的模块不是同一个。

### icache_test 跑的是 mixed_region_loop

`icache_test/test/experiment_config.py` 明确写了这次 v2 是 merge-only，每个 case 是直接融合 I+D 的模板：

```text
v2 is merge-only. Each case is a direct instruction+data fused template:
a code region with evenly spaced pointer-chasing ldr instructions.
```

对应代码在 `/home/tchen/icache_test/test/experiment_config.py:34` 到 `:48`。这里的 case 全部来自 `mixed_region_loop`，参数空间只有：

- `size`: 4096 或 8192
- `ldr_count_per_unit`: 1、2、4、7、14
- `data_mode`: `linear`、`page_shuffle`、`cross_page`、`indirect`
- `pages`: 1、128、512、最大页数
- `lines_per_page`: 1 或 4
- `region_reps`: 1000

然后它把同一个 `mixed_region_loop` 复制成多个 slot：

```python
COMBO_MODULE_CASE_GROUPS = {
    ("mixed_region_loop" if slot_id == 0 else f"mixed_region_loop_{slot_id}"): alias_cases(...)
    for slot_id in range(MIXED_REGION_SLOT_COUNT)
}
```

见 `/home/tchen/icache_test/test/experiment_config.py:77` 到 `:84`。这意味着 combo 不是把同一个 module 参数叠在一起，而是启用多个不同 slot。

### merge_bench 跑的是多个旧 instruction module 的 LDR 注入版

`merge_bench` Phase A 里的 atom 来自这些 I-side module：

- `hot_region_loop`
- `fetch_amplifier`
- `cold_block_sequence`
- `itlb`

`merge_bench/src/modules/hot_region.py`、`block_loop.py`、`tlb_region.py` 都是在旧 instruction module 的 filler slot 里加入 `ldr` 支持。比如 `hot_region.py` 的单位实现是：

- 先 `add x9`、`eor x10`
- 再插入 branch pairs
- 再用 `ldr_per_unit` 替换剩余 filler nops

见 `/home/tchen/merge_bench/src/modules/hot_region.py:16` 到 `:47`。

`block_loop.py` 的逻辑又不同，它保留了 direct branch、indirect dispatch、tail branch/ret 的结构，然后只在 filler slot 里注入 LDR。见 `/home/tchen/merge_bench/src/modules/block_loop.py:143` 到 `:210`。

### 核心差别

| 问题 | icache_test combo_linearity | merge_bench Phase A |
| --- | --- | --- |
| 实际使用的 I 模块 | `mixed_region_loop` | `hot_region_loop`、`fetch_amplifier`、`cold_block_sequence`、`itlb` |
| 是否是同一套 instruction module | 不是 | 不是 |
| 是否都有 NOP -> LDR 思想 | 是 | 是 |
| LDR 插入位置 | 固定 64B unit 的 filler slot，均匀分布 | 不同 module 各自插入，受 branch、tail、dispatch 限制 |
| 是否保留原 branch/dispatch 行为 | 基本不保留，mixed region 是直线 kernel | 保留，例如 block/fetch 仍是 block chain |
| 函数形态 | 普通 noinline 函数，内部 asm | 大量 naked noinline asm 函数 |

所以如果只看“把 NOP 换 LDR”，两边像；但如果看完整 instruction 模块，两边并不等价。

## 2. 最终模块的运行方式是否一样？

结论：宏观上相似，都是“跑完一个再跑下一个”；细节上不一样，而且关键差异就在这些细节里。

### icache_test: 每个 slot 按自己的 region_reps 真实执行

`icache_test/pipeline.py` 会为每个 mixed slot 生成一个 loop entry：

```python
(
    slot["pos"],
    slot["label"],
    f"CONFIG_MIXED_REGION_{slot['slot_id']}_REPS",
    f"CONFIG_MIXED_REGION_{slot['slot_id']}_SIZE > 0 && CONFIG_MIXED_REGION_{slot['slot_id']}_PAGE_COUNT > 0",
    f"run_mixed_region_{slot['slot_id']}_once();",
)
```

见 `/home/tchen/icache_test/pipeline.py:967` 到 `:975`。

最终主循环会把所有 active module loop 逐个写进去：

```python
while (!g_abort && completed_iters < iters) {
    for each ordered module:
        for rep < CONFIG_..._REPS:
            run_module_once()
    ++completed_iters;
}
```

代码生成点在 `/home/tchen/icache_test/pipeline.py:1764` 到 `:1769`。

生成后的 C 里能看到具体例子：

```c
#define CONFIG_MIXED_REGION_4_REPS 1000u
#define CONFIG_MIXED_REGION_5_REPS 1000u

while (!g_abort && completed_iters < iters) {
    for (uint32_t rep = 0; rep < CONFIG_MIXED_REGION_5_REPS && !g_abort; ++rep) {
        run_mixed_region_5_once();
    }
    for (uint32_t rep = 0; rep < CONFIG_MIXED_REGION_4_REPS && !g_abort; ++rep) {
        run_mixed_region_4_once();
    }
}
```

这就是为什么 `combo_linearity.csv` 里 `instructions:u` 是十亿级。默认 `iters=1000`，每个 selected slot 又有 `region_reps=1000`。

### merge_bench: 也是 segment 顺序执行，但 region_reps 被读出后没有用于 Phase A 执行次数

先澄清：`merge_bench` 也是“跑完一个再跑下一个”。比如实际生成出来的 combo 代码是：

```c
/* Seg 0: postlude -> hot x1 (dual) */
r_dptr = postlude_head;
for (uint32_t rep = 0; rep < 1u && !g_abort; ++rep) {
    run_inst_0_inst_0_hot_d_once();
}

/* Seg 1: l2_cold -> fetch x1 */
r_dptr = l2cold_head;
for (uint32_t rep = 0; rep < 1u && !g_abort; ++rep) {
    run_inst_1_inst_0_fetch_s_once();
}
```

所以问题不是“它没有顺序执行”。问题是：它顺序执行时，每段只执行 `i_reps=1`，并且通过 `r_dptr = pool_head` 把 data pool 指针塞进 `x11`。

`merge_bench/src/merge_codegen.py` 在生成 I-stream function 时确实读了 `region_reps`：

```python
region_reps = max(1, int(params.get("region_reps", 1)))
...
all_loop_bodies[prefix] = (runner, region_reps)
```

见 `/home/tchen/merge_bench/src/merge_codegen.py:238` 和 `:259`、`:307`。

但主循环真正生成执行次数时，取的是 segment 的 `i_reps`：

```python
reps = seg["i_reps"]
runner, _ = loop_bodies[prefix]
out.append(emit_instance_loop(reps, f"{runner}();"))
```

见 `/home/tchen/merge_bench/src/merge_codegen.py:505`、`:513`、`:524`。这里 `runner, _` 把前面保存的 `region_reps` 丢掉了。

而 Phase A 的 segment 是这样构造的：

```python
segment = {
    "id": 0,
    "d_module": ...,
    "i_module": i_name,
    "i_reps": 1,
    "dual_ldr": dual,
}
```

见 `/home/tchen/merge_bench/scripts_homo/run_phase_a_single.py:209`。所以 Phase A 中即便 `i_params_json` 写了 `region_reps=1000`，最终生成出来的主循环通常也是 `rep < 1u`。

一个实际生成结果是：

```c
/* Seg 0: postlude -> hot x1 (dual) */
r_dptr = postlude_head;
for (uint32_t rep = 0; rep < 1u && !g_abort; ++rep) {
    run_inst_0_inst_0_hot_d_once();
}

/* Seg 1: l2_cold -> fetch x1 */
r_dptr = l2cold_head;
for (uint32_t rep = 0; rep < 1u && !g_abort; ++rep) {
    run_inst_1_inst_0_fetch_s_once();
}
```

见 `/home/tchen/merge_bench/data/linux_server_validation/phase_a_combo/0003_combo_hot_fetch_canonical/merged_bench.c:2738` 到 `:2748`。

### 这个差异会带来什么后果

`icache_test` 的 single 和 combo 都执行大量重复工作，固定开销被冲淡。一个 combo 的指令数自然接近多个 single 的加和。

`merge_bench` Phase A 的 single 和 combo 执行体都很短，且不是按 `region_reps=1000` 重复。这样一来：

- 计数更容易被启动、初始化、信号、perf attach/detach、函数调用等固定开销污染。
- 组合后任何一个 segment 的异常都会让整行结果失真。
- raw count 的“可加性”不再是在测大工作量，而是在测很短代码片段和运行器行为。

## 3. 两边的内存分配策略是否一样？

结论：不一样。

### icache_test: 每个 mixed slot 拥有自己的 pool 和 cursor

`MixedRegionBuilder.emit_storage()` 给每个 prefix 生成独立状态：

```c
static uint8_t *g_prefix_pool = NULL;
static uintptr_t g_prefix_cursor = 0;
static uint64_t g_prefix_sink = 0;
```

见 `/home/tchen/icache_test/modules/mixed_region.py:77` 到 `:83`。

`emit_init_function()` 会在这个 pool 内按 offsets 建 pointer ring，并设置 `g_prefix_cursor`：

```c
*(uintptr_t *)(g_prefix_pool + cur) = (uintptr_t)(g_prefix_pool + nxt);
g_prefix_cursor = (uintptr_t)(g_prefix_pool + offsets[0]);
```

见 `/home/tchen/icache_test/modules/mixed_region.py:86` 到 `:101`。

内存分配使用 `posix_memalign`，每个 slot 分配自己的连续内存：

```c
posix_memalign(ptr, alignment, bytes)
```

见 `/home/tchen/icache_test/pipeline.py:562` 到 `:576`，mixed slot allocation 在 `/home/tchen/icache_test/pipeline.py:627` 到 `:646`。

所以 combo 中两个 active slot 的 data path 是两个独立 pool、两个独立 cursor。它们可能互相污染 cache/TLB，但不会共享同一个 cursor 状态。

### merge_bench: D-stream pool 是全局命名资源，由 segment 切换 x11 指针

`merge_bench` 的 D-stream infrastructure 使用多种 pool 构造方式：

- `map_pool()` 使用 `mmap` 并 `madvise(..., MADV_NOHUGEPAGE)`，见 `/home/tchen/merge_bench/src/merge_codegen.py:72` 到 `:80`。
- `build_shuffled_ring()` 在连续 mmap pool 中构造随机 pointer ring，见 `/home/tchen/merge_bench/src/merge_codegen.py:126` 到 `:143`。
- `build_shuffled_ring_dual()` 构造 `[next][data][pad]` 的 dual-node ring，见 `/home/tchen/merge_bench/src/merge_codegen.py:146` 到 `:165`。
- `build_scatter_ring()` 每页单独 mmap，用于 scatter/stlb/tlb 压力，见 `/home/tchen/merge_bench/src/merge_codegen.py:168` 开始。

主循环里每个 segment 执行前切换 `r_dptr`：

```c
r_dptr = postlude_head;
run_hot_once();

r_dptr = l2cold_head;
run_fetch_once();
```

见 `/home/tchen/merge_bench/data/linux_server_validation/phase_a_combo/0003_combo_hot_fetch_canonical/merged_bench.c:2738` 到 `:2748`。

也就是说，`merge_bench` 的数据状态不是“module 自带 cursor”，而是“外部 segment 给 I-stream function 准备 x11 指针”。这和 `icache_test` 的 per-slot cursor 模型不同。

### 内存策略差异总结

| 项目 | icache_test mixed_region_loop | merge_bench Phase A |
| --- | --- | --- |
| 分配方式 | `posix_memalign` | `mmap`、scatter mmap |
| pool 所属 | 每个 slot 自己拥有 | 全局 D-stream pool，由 segment 选择 |
| cursor 保存 | `g_mixed_region_N_cursor` | C 变量绑定到 `x11`，进入 asm 后更新 |
| combo 内多模块关系 | 多个独立 pool/cursor | 多个 segment 切换不同 D pool head |
| 是否重置 cursor | cursor 跨调用保存 | 每个 outer iteration/segment 重新设为 pool head |

## 4. 模块的核心实现是否一样？

结论：不是同一个核心实现。相似点是 NOP -> LDR；差异点是函数 ABI、cursor 状态、控制流、LDR 分布、重复次数。

### 相似点

两边都使用 64B 左右的 instruction unit，并用 LDR 替换一部分原来的 NOP。

`icache_test` 的 unit body：

```python
add x9, x9, #1
eor x10, x10, x9
... nop 或 ldr x11, [x11] ...
```

见 `/home/tchen/icache_test/modules/mixed_region.py:116` 到 `:146`。

`merge_bench` 的 hot/block 也有类似逻辑：

- hot: `/home/tchen/merge_bench/src/modules/hot_region.py:16` 到 `:47`
- block/fetch: `/home/tchen/merge_bench/src/modules/block_loop.py:87` 到 `:111`

### 差异 1: icache_test 的 cursor 是显式 asm operand

`icache_test` 的 AArch64 kernel 是普通 C 函数，进入 asm 前把 `g_prefix_cursor` 放进局部变量，然后通过 asm operand 显式传给 x11，结束时再从 x11 写回：

```c
uintptr_t cursor = g_prefix_cursor;
asm volatile(
    "mov x11, %[cursor]\n\t"
    ...
    "mov %[cursor], x11\n\t"
    : [cursor] "+r"(cursor)
    :
    : "x9", "x10", "x11", "cc", "memory");
g_prefix_cursor = cursor;
```

见 `/home/tchen/icache_test/modules/mixed_region.py:157` 到 `:172`。

这个模型的好处是：C 编译器知道 asm 的输入输出关系，x11 只是 asm 内部寄存器，状态通过 `cursor` 这个 C 变量安全传递。

### 差异 2: merge_bench 的 cursor 通过 x11 隐式传入 naked function

`merge_bench` 的主循环生成：

```c
register void *r_dptr __asm__("x11");
r_dptr = postlude_head;
run_inst_0_inst_0_hot_d_once();
```

见 `/home/tchen/merge_bench/src/merge_codegen.py:494` 到 `:524`，实际生成代码见 `/home/tchen/merge_bench/data/linux_server_validation/phase_a_combo/0003_combo_hot_fetch_canonical/merged_bench.c:2732` 到 `:2748`。

而 hot/block 的实际 asm 函数是 `naked`，LDR 直接使用 `x11`：

```python
__attribute__((used, naked, noinline, aligned(...)))
...
"ldr x11, [x11]\n\t"
```

见 `/home/tchen/merge_bench/src/modules/hot_region.py:75` 和 `:29` 到 `:36`。

这个模型依赖一个隐式契约：调用 naked function 时，`x11` 必须已经是合法 pointer。这个契约比 `icache_test` 的 asm operand 模型脆弱得多。

### 差异 2.1: objdump 证明 merge_bench 的 x11 契约实际没有成立

这里不能只看生成出来的 C，因为 `register void *r_dptr __asm__("x11")` 不是函数调用 ABI。AArch64 下普通函数参数走 `x0` 到 `x7`，`x9` 到 `x15` 这类寄存器是 caller-saved scratch register。`x11` 不会因为 C 里写了一个局部 register variable，就自动变成“调用 `run_inst_*_once()` 前必须保存的参数寄存器”。

`merge_bench` 生成 C 的意图是：

```c
r_dptr = postlude_head;
run_inst_0_inst_0_hot_d_once();

r_dptr = l2cold_head;
run_inst_1_inst_0_fetch_s_once();
```

但在实际二进制 `/home/tchen/merge_bench/data/linux_server_validation/phase_a_combo/0003_combo_hot_fetch_canonical/merged_bench` 里，主循环附近的 objdump 是：

```asm
4049fc: ldr w0, [x19, #2508]
404a00: cbnz w0, 404a08
404a04: bl 404048 <run_inst_0_inst_0_hot_d_once>
404a08: mov x11, x21
404a0c: ldr w0, [x19, #2508]
404a10: cbnz w0, 404a18
404a14: bl 404080 <run_inst_1_inst_0_fetch_s_once>
```

这个顺序非常关键：第一段 `run_inst_0_inst_0_hot_d_once` 已经被调用了，之后才出现 `mov x11, x21`。也就是说，源码里的 `r_dptr = postlude_head` 没有变成“调用 hot segment 前写 `x11`”。第一段 hot 的 naked asm 里如果第一批 filler slot 已经被替换成 `ldr x11, [x11]`，它读到的就是旧的、未定义的、或被前面 C library call/信号等待路径污染过的 `x11`。

这和 `icache_test` 正好相反。`icache_test/build/combo_linearity_probe` 中 `mixed_region_2_kernel` 的 objdump 是：

```asm
40390c: ldr x0, [x0]
403924: mov x11, x0
403930: ldr x11, [x11]
403934: ldr x11, [x11]
403938: ldr x11, [x11]
```

也就是先从 `g_mixed_region_2_cursor` 取 cursor，再明确 `mov x11, x0`，随后才开始执行 `ldr x11, [x11]`。这里 data pointer 是 kernel 自己建立的局部状态，不依赖跨 C 函数调用保存 `x11`。

所以从底层架构看，`merge_bench` 不是“data 注入方式不同所以略有偏差”，而是当前注入方式在 ABI 层没有被正确表达给编译器。源码看起来像是把 data pool 塞进去了，但机器码里第一段没有真的塞进去。这能直接解释为什么一批 combo log 只有 `PROXYBENCH_READY`、没有 `completed_iters`：benchmark 收到启动信号后进入第一段，裸汇编第一批 `ldr` 很可能解引用非法 `x11`，进程提前异常退出。

### 差异 3: icache_test 是直线 mixed kernel，merge_bench 保留原 I-stream 控制流

`mixed_region_loop` 每个 64B unit 都是固定结构：`add/eor` 加若干均匀分布的 LDR 或 NOP。它没有 block chain、没有 indirect dispatcher、没有 itlb function chain。

`merge_bench` 的 block/fetch module 仍然保留：

- direct branch
- indirect dispatch
- tail branch 或 `ret`
- branch pairs

这些会改变 filler slot 数量，也会让不同 module 的控制流成本不同。见 `/home/tchen/merge_bench/src/modules/block_loop.py:156` 到 `:207`。

### 差异 4: LDR 的分布方式不同

`icache_test` 里，LDR positions 通过 `_ldr_positions()` 在 14 个 filler slot 中均匀铺开：

```python
((slot + 1) * filler_slots) // ldr_count
```

见 `/home/tchen/icache_test/modules/mixed_region.py:104` 到 `:113`。

`merge_bench` 的 hot module 是先放 branch pairs，再用 LDR 替换剩余 filler 的前一段。block/fetch module 还要先给 tail branch/dispatch 留指令槽，再决定 filler。也就是说，同样叫 `ldr_count`，实际落点不一样。

## 5. 结果层面的证据

### icache_test 的哪些事件线性

我按 `canonical` 对 `sum` 的相对误差统计了 `/home/tchen/icache_test/output/combo_linearity.csv`：

| counter | 样本数 | median abs rel err | max abs rel err | 5% 内样本 |
| --- | ---: | ---: | ---: | ---: |
| `instructions:u` | 47 | 0.0000 | 0.0000 | 47/47 |
| `cpu-cycles:u` | 47 | 0.0474 | 0.2934 | 25/47 |
| `l1d_cache_refill:u` | 47 | 0.0043 | 0.1206 | 45/47 |
| `l1d_tlb_refill:u` | 47 | 0.0003 | 0.0295 | 47/47 |
| `l2d_cache_refill:u` | 47 | 0.0151 | 0.2740 | 35/47 |
| `l1i_cache_refill:u` | 47 | 1.5187 | 7.4635 | 0/47 |
| `ll_cache_miss:u` | 47 | 0.1782 | 87.3585 | 19/47 |

所以 `icache_test` 的线性不是全事件线性。它最强的是指令数和 D-side refill/TLB refill；I-cache refill 和 LLC miss 很不稳定。

### merge_bench 的异常结果和 completed_iters

`merge_bench` Phase A combo 一共有 12 个 combo 运行日志。其中 8 个没有 `completed_iters=1`，只有 `PROXYBENCH_READY`；4 个正常完成。

缺 `completed_iters` 的包括：

- `0003_combo_hot_fetch_canonical`
- `0004_combo_hot_fetch_shuffle...`
- `0008_combo_hot_itlb_canonical`
- `0009_combo_hot_itlb_shuffle...`
- `0013_combo_cold_itlb_canonical`
- `0014_combo_cold_itlb_shuffle...`
- `0018_combo_cold_hot_canonical`
- `0019_combo_cold_hot_shuffle...`

正常完成的包括：

- `0023_combo_layout_density_canonical`
- `0024_combo_layout_density_shuffle...`
- `0028_combo_hot_sequence_itlb_canonical`
- `0029_combo_hot_sequence_itlb_shuffle...`

这和 residual 很一致：前面那些缺 `completed_iters` 的组合，`canonical_minus_sum` 基本是 94% 到 99% 的巨大负偏差；正常完成的组合偏差小很多，例如 `combo_layout_density` 平均相对偏差约 7.4%，`combo_hot_sequence_itlb` 平均相对偏差约 19.9%。

因此，之前 `merge_bench` “完全不可加”的结论不能只解释成硬件非线性。至少一部分是运行没有正常完成，导致 measured combo 不是实际 combo 工作量。

## 6. 逐项回答你的四个问题

### 两边的 Instructions 模块是否一样？

不一样。

`icache_test` 新结果用的是 `mixed_region_loop`。这是一个专门的融合 I+D 模块，不是 `hot_region_loop/fetch_amplifier/cold_block_sequence/itlb` 那套模块。它的 unit 更简单，状态更显式。

`merge_bench` 是在旧 instruction module 上加 LDR 注入。它保留了不同 module 原来的控制流结构。

### 最终模块的运行方式是否一样？

不一样。

`icache_test` 中每个 active slot 都按自己的 `CONFIG_MIXED_REGION_N_REPS` 执行，`region_reps=1000` 真实进入主循环。

`merge_bench` Phase A 里 `region_reps` 被读取但被丢弃，最终用 `segment.i_reps`，而 Phase A 的 `i_reps` 固定是 1。

### 两边的内存分配策略是否一样？

不一样。

`icache_test` 是每个 slot 独立 pool、独立 cursor、`posix_memalign` 连续分配。

`merge_bench` 是全局 D-stream pool，按 segment 切换 `x11` 指针，pool 构造包含连续 mmap、scatter mmap、postlude ring 等多种策略。

### 模块的核心实现是否一样？

不一样。

共同点是 NOP -> LDR。不同点包括：

- `icache_test` 是普通 C 函数内联 asm，cursor 用 input/output operand 显式传递。
- `merge_bench` 多数 I-stream 函数是 naked asm，依赖调用前 x11 已经被正确设置。
- `icache_test` mixed region 是直线 kernel。
- `merge_bench` 保留 hot、block、fetch、itlb 各自原本的控制流。
- `icache_test` LDR 均匀分布。
- `merge_bench` LDR 分布受 branch pair、tail branch、indirect dispatch 限制。

## 7. 我现在更确信的判断

之前说“merge_bench 的问题很可能是运行异常和语义差异”，现在可以更具体：

1. `merge_bench` Phase A 的一批 combo 确实没有正常完成，因为日志缺 `completed_iters`。
2. 两边宏观上都是顺序执行，所以“跑完一个再跑下一个”不是线性差异的根因。
3. `merge_bench` Phase A 确实没有把 `region_reps` 按参数语义执行进去。
4. `merge_bench` 的 x11 隐式传参模型不只是“更脆弱”，而是在 `0003_combo_hot_fetch_canonical` 的实际机器码里已经失败：第一段 naked asm 调用前没有设置 `x11`。
5. `icache_test` 的线性主要来自独立状态、显式 cursor、大重复次数和 D-side 工作量主导，不代表任意 instruction module 加 LDR 后都能线性。

## 8. 建议下一步验证

为了把这个问题彻底钉死，我建议做三步：

1. 给 `merge_bench` runner 加硬检查：如果 bench log 没有 `completed_iters=`，该行标记为 failed，不再写成有效 measured vector。
2. 修 `merge_bench` 的执行次数语义：把 instance 的 `region_reps` 乘进 segment 执行次数，或者在主循环中用 `region_reps * i_reps`。
3. 先修 `merge_bench` 的 D pointer 传递：最低限度也要在每次 runner 调用前用 inline asm 明确写 `x11`，并保证写 `x11` 和 naked runner 之间没有普通 C 调用；更稳的方案是改成和 `icache_test` 一样的显式 cursor 模型，每个 segment 或每个 D pool 有自己的 cursor 变量，asm 用 input/output operand 传入/写回，不依赖跨函数调用保留 `x11`。

修完后再重新跑同一组 Phase A combo。到那时如果仍然不线性，剩下的偏差才更有资格归因到 cache/TLB 污染、顺序效应、共享数据池和硬件计数器本身的非线性。
