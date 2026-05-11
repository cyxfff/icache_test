# 组合异常排查笔记

## 本轮做了什么

1. 将 `issue_combos_dcache.md` 改写为中文。
2. 在生成链路里新增了可控的内存实验开关：
   - `memory_allocator`: `posix` / `arena`
   - `memory_advice`: `default` / `random` / `sequential` / `hugepage` / `nohugepage`
   - `memory_arena_gap_bytes`
   - `memory_arena_hint`
   - `memory_prefault`
3. 扩展了 `test/issue_cases/run_issue_cases.py`，结果 CSV/Markdown 会把上述内存配置一起记下来。

## 机器侧观察

- 当前机器：`aarch64`, Linux `5.10.0-216.0.0.115.oe2203sp4.aarch64`
- Transparent Huge Page 状态：
  - `/sys/kernel/mm/transparent_hugepage/enabled` -> `always madvise [never]`
  - `/sys/kernel/mm/transparent_hugepage/defrag` -> `always defer defer+madvise madvise [never]`

这表示默认并不会主动给匿名内存上 THP，只有显式 `madvise(MADV_HUGEPAGE)` 才更可能触发。

## 关于“禁止硬件预取”

这台机器没有找到一个可直接从普通用户态切换的硬件预取开关。  
代码里主要访存也来自显式 `ldr` 指令和指针链，编译器级别的 `-fno-prefetch-loop-arrays` 这类选项基本帮不上忙。

所以这一轮采用的是“代理实验”：

- `memory_advice=random`：更像是在探测“更差的顺序性/更不利的页访问建议”会不会放大异常
- `memory_advice=hugepage/nohugepage`：探测页粒度与页表组织是否影响组合结果

## 代表性结果

### case: combo_013_s2

原始组合：

- `mix_b64_ld1_indir_p128_lp4_r1000`
- `mix_b64_ld1_pshuf_p1_lp1_r1000`

结果摘要：

| 方案 | worst rel_diff | 备注 |
| --- | ---: | --- |
| `posix/default` | `0.2941` | 默认基线 |
| `arena/default` | `0.1051` | 明显变好 |
| `arena/default + gap=2MB` | `0.1584` | 仍然受地址分布影响 |
| `arena/hugepage + prefault` | `0.0782` | 继续变好 |
| `arena/nohugepage + prefault` | `0.0617` | 本轮最稳 |
| `posix/random` | `0.3894` | 明显变差 |
| `arena/default + hint=0x4000000000` | `0.0259` | 仅改 VA 范围也显著变好 |

结论：

- 这个 case 对 **虚拟地址分布** 非常敏感。
- 只改分配方式、地址 hint、页建议，不改模块参数，就能把偏差从 `29%` 压到 `2%~10%`。
- `random` 建议会放大异常，说明它和访存顺序性、预取收益、页局部性高度相关。

补充：使用重复扫描脚本后，`combo_013_s2` 还出现了两个更具体的局部规律：

- 当 `slot0` 的大页链模块 `pages` 从 `1/4/16/64` 提升到 `512` 时，`l2d_cache_refill` 的中位相对偏差会从 `40%~99%` 级别下降到约 `0.6%`。
- 当 `slot1` 的小热页模块保持 `pages=1` 时最稳；把它放大到 `16/64` 这类中间区间时，中位偏差会明显上升。

这说明对这类二模块组合，更像是：

- “冷大工作集模块”要足够大
- “热小工作集模块”要足够小
- 处于中间页数的模块最容易和其他模块产生共享层级干扰

### case: combo_043_s4

原始组合：

- `mix_b64_ld14_xpage_p1_lp1_r1000`
- `mix_b64_ld1_indir_p128_lp1_r1000`
- `mix_b128_ld4_indir_p128_lp4_r1000`
- `mix_b128_ld1_indir_p128_lp4_r1000`

结果摘要：

| 方案 | worst rel_diff | 备注 |
| --- | ---: | --- |
| `posix/default` | `0.1630` | 默认基线 |
| `arena/default` | `0.1852` | 略差 |
| `arena/hugepage + prefault` | `0.4596` | 明显恶化 |
| `arena/nohugepage + prefault` | `0.2671` | 仍然恶化 |
| `arena/default + hint=0x4000000000` | `0.2986` | 也变差 |

结论：

- 这个 case 也受内存布局影响，但方向和 `combo_013_s2` 不同。
- 对它来说，THP 风格的页组织反而可能把多个随机/跨页链路更紧地耦合在一起。
- 说明“不能线性相加”并不是单一原因，而是 **不同 mixed data mode + 工作集 + 页组织** 的共同结果。

补充：重复扫描后，`arena + nohugepage + prefault` 在这个 case 上也能把中位偏差从约 `16.9%` 压到约 `9.1%`，而 `random_advice` 的中位偏差约 `3.1%`。  
也就是说，至少在这两组 case 上，**页组织策略** 仍然是一个可控且有效的主因子。

## 当前最可信的判断

1. 问题不是单纯统计噪声。
   - `combo_013_s2` 只把模块顺序反过来，`l2d_cache_refill` 就会换一个方向偏。
   - 改变地址分布后，偏差幅度也会系统性变化。

2. 问题和共享的数据侧层级强相关。
   - 目前最敏感的是 `l2d_cache_refill:u`。
   - 这和 L2D / TLB / 预取状态共享是吻合的。

3. “单模块可加，组合后不可加”很可能因为单模块运行时拥有独立的地址布局与热状态，而组合运行时：
   - 多个模块共享 L2D/TLB/LLC
   - 指针链之间互相改变预取命中与替换行为
   - 匿名页的实际映射方式、VA 范围、THP 行为会改变这些干扰强度

4. 超大页集本身也是坏因素。
   - `pages=524288` 这类配置不只可能破坏线性，还会让静态 offset 数组非常大，直接拖垮编译时间与实验吞吐。
   - 因此它不适合放进“safe 生成”模式。

## 目前不建议的假设

- 不建议先把锅全甩给“脚本算错”。
  目前已经看到改变内存布局会稳定地改变偏差方向和幅度，这更像真实硬件行为。

- 不建议先假设“只有 LLC 不够大”。
  当前最强信号还是 `l2d_cache_refill`，而且同样大小的工作集，仅仅换地址布局就会变。

## 下一步建议

1. 优先对 `combo_013_s2` 一类小 case 做更细 sweep：
   - `pages`
   - `nodes_per_page`
   - `data_mode`
   - `memory_arena_hint`
   - `memory_arena_gap_bytes`

2. 对 `combo_043_s4` 一类多随机链 case，重点比较：
   - `hugepage` vs `nohugepage`
   - `posix` vs `arena`
   - 顺序 `canonical` vs `reverse`

3. 后续如果你要手动实验，建议从这条命令改起：

```bash
python3 test/issue_cases/run_issue_cases.py \
  --config test/issue_cases/issue_combos_dcache.json \
  --case-ids combo_013_s2 \
  --memory-allocator arena \
  --memory-arena-hint 0x4000000000
```

## 新增工具与生成限制

### 重复扫描工具

新增：

- `test/issue_cases/linearity_factor_scan.py`

用途：

- 对指定 case 做重复跑
- 比较不同内存策略或局部参数 sweep
- 输出每个变体的 `rel_diff_median / min / max`

示例：

```bash
python3 test/issue_cases/linearity_factor_scan.py \
  --case-ids combo_013_s2 \
  --metrics l2d_cache_refill:u \
  --repeats 3 \
  --iters 200 \
  --include-memory-variants \
  --page-sweep 0:1,4,16,64,128,512
```

### safe-linearity 生成模式

目前已经在生成侧加入了一个**试探性的低风险模式**：

- `tools/run_combo_linearity.py --safe-linearity`

它会做几件事：

1. 使用更稳的内存默认值：
   - `allocator=arena`
   - `advice=nohugepage`
   - `prefault=1`
2. 过滤掉明显高风险的 case：
   - `pages > 512`
   - `1 < pages < 128`
   - `nodes_per_page > 4`
   - `pages == 1` 且 `data_mode in {random, page_stride}`
   - 组合中出现完全重复的模块
   - 组合里出现多个 `pages == 1` 的热点模块

这些规则还不是最终版，但已经足够作为“更偏向线性可加”的第一道筛子。
