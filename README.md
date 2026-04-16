# icache_hiperf

用少量可控的合成模块逼近真实程序的前端 PMU 画像。

## 程序目的

真实程序的前端行为（I-cache miss、ITLB miss、branch 等）往往难以直接复现。本工程的思路是：

1. 把前端行为拆成若干个语义清晰、参数可控的基础模块。
2. 单独测量每个模块在不同参数下的 PMU 计数向量（11 维 raw count）。
3. 验证多模块组合时计数是否近似线性叠加。
4. 用稀疏组合求解器找到一组模块及其权重，使组合后的 PMU 向量逼近目标程序的画像。

最终产物是一个整数 `repeat_plan`，可以直接回放成真实 benchmark 在设备上验证。

---

## 拟合思想

### 线性叠加假设

如果模块 A 单独跑产生计数向量 $\mathbf{v}_A$，模块 B 产生 $\mathbf{v}_B$，那么当两者组合运行时，期望：

$$\mathbf{v}_{A+B} \approx \mathbf{v}_A + \mathbf{v}_B$$

这个假设在模块间耦合较弱时成立。`fit/combo_codegen.py` 专门用来验证这一点。

### 11 维 raw count 空间

求解器只在以下 11 个原始计数维度上做线性拟合：

```
instructions:u        br_retired:u          br_mis_pred:u
l1i_cache:u           l1i_cache_refill:u
l1i_tlb:u             l1i_tlb_refill:u
l2i_cache:u           l2i_cache_refill:u
l2i_tlb:u             l2i_tlb_refill:u
```

`miss_rate`、`mpki` 等比率指标不进入线性空间，而是从最终 raw count 反推得到。这样做的原因是比率不满足线性叠加，直接拟合会引入系统性误差。

### 求解过程

给定目标向量 $\mathbf{t} \in \mathbb{R}^{11}$，从候选模板库中选不超过 `max_templates` 个模板 $\{\mathbf{v}_i\}$，求非负系数 $\{k_i\}$，使得：

$$\left(1 - \epsilon\right) \mathbf{t} \leq \sum_i k_i \mathbf{v}_i \leq \left(1 + \epsilon\right) \mathbf{t}$$

其中 $\epsilon$ 为容差（默认 10%）。连续系数 $k_i$ 最后量化为整数 `repeat_count`。

### 分阶段搜索策略

求解器按以下顺序逐步加入模块家族，每阶段用 beam search 保留最优状态集：

1. `itlb` — 先定住 L2-TLB refill 骨架
2. `cold_block_sequence` — 补 TLB access 和 I-cache refill
3. `fetch_amplifier` — 补 L1 I-cache access
4. `hot_region_loop` — 最后修 branch 计数

---

## 模块介绍

### `cold_block_sequence`

**用途**：构造离散块链，提供冷取指路径，主要塑造 L2 I-cache 和 L2 TLB 相关计数。

**核心参数**：

| 参数 | 说明 | 影响 |
|------|------|------|
| `blocks` | 基本块总数 | 决定代码工作集大小，越大 L2 I-cache/TLB miss 越多 |
| `direct_run_len` | 连续直接跳转次数 | 每隔 N 步插入一次间接调度，控制 BTB/间接分支压力 |
| `layout` | 块物理排列方式 | `linear`：顺序；`in_page_shuffle`：页内位反转，打散页内局部性 |
| `region_reps` | 外层重复次数 | 线性放大所有计数 |

**sweep 范围**：`blocks = 1000..20000`，`direct_run_len = [1,2,4,8,16]`

**生成代码示例**（`blocks=5000, direct_run_len=4, layout=linear`）：

```c
// 生成 5000 个 64 字节对齐的基本块函数
// blocks=5000 → 工作集 = 5000 × 64B = 312KB，远超 L1 I-cache

__attribute__((naked, aligned(64)))
static void block_0(void) {
    asm volatile(
        ".rept 15\n\t"   // 15 条 nop 填满 64B 块（15×4 + 1×4 = 64B）
        "nop\n\t"
        ".endr\n\t"
        "b block_1\n\t"  // 直接跳转到下一块（direct_run_len 控制何时改为间接）
        ::: "x0","x9","x16","x17","cc","memory");
}

// direct_run_len=4：每 4 步直接跳转后，第 4 步改为间接调度
// 即 block_3 不直接 b block_4，而是：
__attribute__((naked, aligned(64)))
static void block_3(void) {
    asm volatile(
        ".rept 15\n\t"
        "nop\n\t"
        ".endr\n\t"
        // (3+1) % 4 == 0 → 间接调度：把下一块 ID 装入 x0，跳 dispatcher
        "movz x0, #4\n\t"          // 下一块逻辑 ID = 4
        "b dispatch_main_indirect\n\t"
        ::: "x0","x9","x16","x17","cc","memory");
}
// direct_run_len 越小 → 间接跳转越密集 → 更多 BTB 压力
// direct_run_len 越大 → 几乎全是直接跳转 → 更纯粹的 I-cache 压力

// layout=in_page_shuffle：块的物理顺序按页内位反转排列
// 例如页内 8 个块的访问顺序：0,4,2,6,1,5,3,7（位反转）
// 打散页内空间局部性，增加 TLB 压力

for (uint32_t rep = 0; rep < region_reps; rep++) {
    block_0();  // 触发整条链：block_0 → block_1 → ... → block_4999 → block_0
                // 每次跨 64B 边界 → L1 I-cache miss → L2 I-cache access
                // 每次跨 4KB 页边界 → ITLB access
}
```

---

### `itlb`

**用途**：构造跨页代码池，专门塑造 L1/L2 ITLB 相关计数。

**核心参数**：

| 参数 | 说明 | 影响 |
|------|------|------|
| `funcs` | 函数总数（每个函数独占一个 4KB 页） | 决定 ITLB 工作集，越大 L2 ITLB miss 越多 |
| `lines_per_page` | 每个函数执行几条 cache line 的指令 | 控制每次访问的取指量，影响 L1 I-cache access |
| `mode` | `chain`：函数间直接跳转链 | chain 模式每步跨页，最大化 ITLB 压力 |
| `direct_run_len` | chain 模式下连续直接跳转次数 | 同 cold_block_sequence，控制间接跳转频率 |
| `region_reps` | 外层重复次数 | 线性放大所有计数 |

**sweep 范围**：`funcs = [256,512,1024,2048,4096,8192]`，`lines_per_page = [1,4,8]`

**生成代码示例**（`funcs=1024, lines_per_page=1, mode=chain`）：

```c
// 每个函数 4096 字节对齐（独占一个 4KB 页）
// funcs=1024 → 工作集 = 1024 个不同页 → ITLB 工作集 = 1024 页

__attribute__((naked, aligned(4096)))
static void itlb_func_0(void) {
    asm volatile(
        "add x9, x9, #1\n\t"    // payload：计数器递增（防止被优化掉）
        "eor x10, x10, x9\n\t"  // payload：数据依赖（防止 CPU 消除死代码）
        ".rept 125\n\t"          // lines_per_page=1 → 执行 1 条 cache line
        "nop\n\t"                // 1 line = 16 条指令，减去 add/eor/b 共 3 条 = 13 条 nop
        ".endr\n\t"              // 实际：(1×16 - 2)×4 - 1 = 125 条 nop
        "b itlb_func_1\n\t"     // chain 模式：直接跳到下一个函数（跨页 → ITLB miss）
        ::: "x9","x10","cc","memory");
}

// lines_per_page=4 时，每个函数执行 4 条 cache line：
// nop 数量 = (4×16 - 2)×4 - 1 = 253 条 nop
// → 每次访问取指量增加 4 倍 → L1 I-cache access 增加

// chain 模式执行流：
// itlb_func_0 → itlb_func_1 → ... → itlb_func_1023 → itlb_func_0
// 每一跳都跨 4KB 页边界 → 每步触发 ITLB lookup
// funcs 超过 ITLB 容量后 → L1 ITLB refill → L2 ITLB access/refill

for (uint32_t rep = 0; rep < region_reps; rep++) {
    itlb_func_0();  // 触发整条 1024 步跨页链
}
```

---

### `fetch_amplifier`

**用途**：补充 L1 I-cache 和 L1 ITLB access 计数，同时可注入固定不跳的 branch 对。

**核心参数**：

| 参数 | 说明 | 影响 |
|------|------|------|
| `blocks` | 块池总大小 | 决定代码工作集上限 |
| `block_slots` | 每轮实际访问的槽位数 | 控制热集大小，决定 L1 I-cache 命中/miss 比例 |
| `direct_run_len` | 连续直接跳转次数 | 同 cold_block_sequence，控制间接跳转频率 |
| `branch_pairs_per_block` | 每块注入的 branch 对数 | 每对 = `cmp x9,x9` + `b.ne label`，永不跳转但增加 br_retired |
| `block_slots` | 每块指令槽位总数 | branch 对 + nop 填满剩余槽位，控制每块取指量 |
| `region_reps` | 外层重复次数 | 线性放大所有计数 |

**sweep 范围**：`blocks = [32,64,128]`，`block_slots = [4,8,16]`，`region_reps = [1000]`

**生成代码示例**（`blocks=64, block_slots=8, direct_run_len=2, branch_pairs_per_block=1`）：

```c
// blocks=64，block_slots=8：块池 64 个，每轮只访问前 8 个
// → 热集 = 8 × 64B = 512B，完全在 L1 I-cache 内
// → 大量 L1 I-cache access，极少 refill

// block_slots=8，branch_pairs_per_block=1：
// 每块 8 个指令槽：1 对 branch（2 条）+ nop 填充（5 条）+ 1 条跳转尾
__attribute__((naked, aligned(64)))
static void fetch_block_0(void) {
    asm volatile(
        // branch_pairs_per_block=1 → 1 对永不跳转的条件分支
        "cmp x9, x9\n\t"    // x9 == x9 永远成立，ZF=1
        "b.ne 1f\n\t"        // b.ne 在 ZF=1 时不跳 → 永不跳转
        "1:\n\t"
        // 剩余槽位填 nop：8 slots - 2(branch pair) - 1(tail b) = 5 nop
        ".rept 5\n\t"
        "nop\n\t"
        ".endr\n\t"
        "b fetch_block_1\n\t"  // direct_run_len=2：每 2 步直接跳，第 2 步改间接
        ::: "x0","x9","x16","x17","cc","memory");
}

// branch_pairs_per_block 越大 → br_retired 越多（但永不 mis-predict）
// block_slots 越大 → 每块指令越多 → 每次取指跨越更多 cache line

// direct_run_len=2：fetch_block_1 改为间接调度
__attribute__((naked, aligned(64)))
static void fetch_block_1(void) {
    asm volatile(
        "cmp x9, x9\n\t"
        "b.ne 1f\n\t"
        "1:\n\t"
        ".rept 3\n\t"
        "nop\n\t"
        ".endr\n\t"
        // (1+1) % 2 == 0 → 间接调度
        "movz x0, #2\n\t"
        "b dispatch_fetch_indirect\n\t"
        ::: "x0","x9","x16","x17","cc","memory");
}

for (uint32_t rep = 0; rep < 1000; rep++) {
    fetch_block_0();  // 触发 8 槽热链，大量 L1 I-cache access
}
```

---

### `hot_region_loop`

**用途**：构造热循环区域，主要用来补 branch 计数和热访问特征。

**核心参数**：

| 参数 | 说明 | 影响 |
|------|------|------|
| `size` | 热区字节数（必须是 64 的倍数） | 决定热代码工作集，`size/64` 个 cache line 单元 |
| `branch_pairs_per_unit` | 每个 64B 单元注入的 branch 对数 | 每对 = `cmp x9,x9` + `b.ne label`，永不跳转，线性增加 br_retired |
| `region_reps` | 外层重复次数 | 线性放大所有计数 |

**sweep 范围**：`size = [4096,8192]`，`branch_pairs_per_unit = [0,1,2,3,4]`，`region_reps = [1000]`

**生成代码示例**（`size=4096, branch_pairs_per_unit=2`）：

```c
// size=4096 → 64 个 64B cache line 单元，全部在同一个函数内
// 整个热区 4096B，通常完全驻留在 L1 I-cache 中

__attribute__((naked, aligned(64)))
static void hot_region_blob(void) {
    asm volatile(
        // === cache line 单元 0 ===
        "add x9, x9, #1\n\t"    // payload：计数器（防止死代码消除）
        "eor x10, x10, x9\n\t"  // payload：数据依赖链
        // branch_pairs_per_unit=2 → 2 对永不跳转的条件分支
        "cmp x9, x9\n\t"        // ZF=1（永远相等）
        "b.ne 1f\n\t"            // 永不跳转
        "1:\n\t"
        "cmp x9, x9\n\t"
        "b.ne 2f\n\t"            // 永不跳转
        "2:\n\t"
        // 剩余槽位填 nop：16 slots - 2(add/eor) - 4(2对branch) = 10 nop
        ".rept 6\n\t"
        "nop\n\t"
        ".endr\n\t"

        // === cache line 单元 1 ===  （结构完全相同，重复 64 次）
        "add x9, x9, #1\n\t"
        "eor x10, x10, x9\n\t"
        "cmp x9, x9\n\t"
        "b.ne 3f\n\t"
        "3:\n\t"
        // ... 共 64 个单元 ...

        "ret\n\t"
        ::: "x9","x10","cc","memory");
}

// branch_pairs_per_unit=0 → 每单元只有 add/eor + nop，br_retired 极少
// branch_pairs_per_unit=4 → 每单元 4 对 branch，br_retired 是 0 时的 4 倍多
// size 翻倍 → 单元数翻倍 → br_retired/L1 I-cache access 同比翻倍

for (uint32_t rep = 0; rep < 1000; rep++) {
    hot_region_blob();  // 热循环：全程命中 L1 I-cache，大量 br_retired
}
```

---

## 工作流

```
test/single.py          →  output/*.csv        单模块参数库
fit/combo_codegen.py    →  验证线性叠加假设
fit/raw_count_sparse_solver.py  →  output/raw_count_sparse_solver_best.json
fit/validate_fitted_bench.py    →  output/fitted_bench_validation.csv  真机验证
```

### 常用命令

```bash
# 1. 生成单模块参数库
python3 test/single.py

# 2. （可选）验证线性叠加
python3 fit/combo_codegen.py

# 3. 运行稀疏求解器
python3 fit/raw_count_sparse_solver.py

# 4. 指定搜索参数
python3 fit/raw_count_sparse_solver.py --max-templates 20 --tolerance 0.10 --parallel-workers 128

# 5. 真机验证
python3 fit/validate_fitted_bench.py --result-json output/raw_count_sparse_solver_best.json
```

---

## 目录结构

```
config/config.py              运行时配置：设备、hdc、PMU 事件列表
test/experiment_config.py     各模块 sweep 参数定义
test/single.py                运行单模块参数库扫描
fit/combo_codegen.py          随机组合 probe，验证线性性
fit/raw_count_sparse_solver.py  11 维 raw count 稀疏求解器
fit/fitter_config.py          求解器配置：目标、阶段权重、家族上限
fit/validate_fitted_bench.py  整数 repeat plan 回放验证
output/                       CSV、JSON、日志输出
```

---

## 注意事项

- `miss_rate` 和 `mpki` 不参与线性求解，由最终 raw count 反推。
- `cpu-cycles:u` 不进入 11 维求解空间，`ipc` 同理。
- 热模块（`fetch_amplifier`、`hot_region_loop`）的低 MPKI 计数（如极小的 refill）在重复多次时不线性增长，求解器对此有特殊处理。
- `coefficient` 是连续系数，`repeat_count` 是量化后的整数版本，两者不同。
