# TODO

这个清单的目标不是“把事情都记下来”，而是把接下来要做的工作拆成可以执行、可以验收、可以继续细分的任务。

当前主线目标：

1. 统一 mixed 模块参数模型；
2. 找出影响模块线性相加的关键因素；
3. 解释这些因素背后的底层原因；
4. 将高风险因素转化为生成约束；
5. 最终让生成系统支持“更偏向线性可加”的模块与组合。

---

## A. 参数模型与接口统一

### A1. 定义 canonical mixed 配置模型

- [ ] 明确 mixed 模块的三层结构：
  - [ ] `instruction_subtemplate`
  - [ ] `data_subtemplate`
  - [ ] `fusion_controls`
- [ ] 设计 canonical 字段命名规范：
  - [ ] `instr_*`
  - [ ] `data_*`
  - [ ] `fusion_*`
- [ ] 禁止在新接口中继续使用历史缩写作为主命名
- [ ] 明确哪些字段是所有 mixed family 共享的
- [ ] 明确哪些字段只属于特定 instruction family
- [ ] 明确哪些字段只属于特定 data family

### A2. 设计 instruction family 抽象

- [ ] 定义 `instr_family` 的候选集合
  - [ ] `hot_loop`
  - [ ] `block_chain`
  - [ ] `fetch_amplifier`
  - [ ] `itlb_walk`
  - [ ] `call_ret`
  - [ ] `indirect_target`
- [ ] 为每个 family 列出最小必要参数
- [ ] 为每个 family 列出可选扩展参数
- [ ] 统一“instruction footprint”描述方式
  - [ ] 哪些 family 用 `instr_size_bytes`
  - [ ] 哪些 family 用 `instr_blocks`
  - [ ] 哪些 family 用 `instr_funcs`
- [ ] 统一 branch/jump/layout 相关参数命名
  - [ ] `instr_layout`
  - [ ] `instr_direct_run_len`
  - [ ] `instr_branch_pairs_per_unit`
  - [ ] `instr_branch_pairs_per_block`
  - [ ] `instr_block_align`

### A3. 设计 data family 抽象

- [ ] 明确当前 mixed 主线的数据子模板是否统一叫 `pointer_chain`
- [ ] 明确后续是否需要支持多个 data family
  - [ ] `pointer_chain`
  - [ ] `stream`
  - [ ] `page_stride`
  - [ ] `indirect_gather`
- [ ] 统一 data 侧字段：
  - [ ] `data_pages`
  - [ ] `data_nodes_per_page`
  - [ ] `data_mode`
  - [ ] `data_stride_lines`
  - [ ] `data_stride_pages`
- [ ] 明确 `page` 在 mixed 语义中永远指 data page，而不是 code page

### A4. 设计 fusion 控制字段

- [ ] 统一 `fusion_ldr_per_unit`
- [ ] 明确是否还需要：
  - [ ] `fusion_slot_policy`
  - [ ] `fusion_unit_bytes`
  - [ ] `fusion_fixed_instrs`
- [ ] 明确 `region_reps` 是否保留为通用字段
- [ ] 明确 `pos` 是否仍作为组合执行顺序字段保留在模块级

### A5. 统一标签与 CSV 字段

- [ ] 定义新的 canonical label 规则
- [ ] label 中不要再混入历史别名
- [ ] 明确 label 中哪些字段必须出现
- [ ] 明确 label 中哪些字段可以省略
- [ ] 统一 CSV 首行字段命名
- [ ] 评估是否需要对旧 CSV 提供转换脚本

### A6. 验收标准

- [ ] 新 mixed 配置可以不依赖历史字段独立表达
- [ ] README 中所有模块示例都使用 canonical 字段
- [ ] 新增 case 时不需要再手动解释 `b64 / lp4 / pshuf / indir`

---

## B. mixed 模块族重构

### B1. 保留当前 `mixed_region_loop`，但重新定位

- [ ] 明确它只是 `mixed_hot_loop` 的一个简化实现，还是单独 family
- [ ] 给它补 canonical 配置入口
- [ ] 让它不再作为“所有 mixed 模板的总代表”

### B2. 设计 `mixed_hot_loop`

- [ ] instruction 侧复用 `hot_region_loop` 语义
- [ ] 明确保留哪些参数：
  - [ ] `instr_size_bytes`
  - [ ] `instr_branch_pairs_per_unit`
  - [ ] `region_reps`
- [ ] 明确哪些 data family 可以接入
- [ ] 明确 label 该怎么写

### B3. 设计 `mixed_block_chain`

- [ ] instruction 侧复用 `cold_block_sequence` / `fetch_amplifier`
- [ ] 明确保留哪些参数：
  - [ ] `instr_blocks`
  - [ ] `instr_block_align`
  - [ ] `instr_layout`
  - [ ] `instr_direct_run_len`
  - [ ] `instr_branch_pairs_per_block`
- [ ] 明确 direct/indirect 跳转是如何和 data 访问交织的
- [ ] 明确 block family 的 mixed 是否需要多个变体

### B4. 设计 `mixed_itlb_walk`

- [ ] instruction 侧复用 `itlb`
- [ ] 明确保留哪些参数：
  - [ ] `instr_funcs`
  - [ ] `instr_lines_per_page`
  - [ ] `instr_mode`
  - [ ] `instr_direct_run_len`
- [ ] 明确 data 访问如何插入多 page code walk 中
- [ ] 明确这个 family 的主要用途：
  - [ ] 模拟 code-page walk + data walk 共振
  - [ ] 观察 ITLB/DTLB 组合干扰

### B5. 设计 `mixed_call_ret`

- [ ] instruction 侧复用 `call_ret_chain`
- [ ] 明确保留哪些参数：
  - [ ] `instr_funcs`
  - [ ] `instr_lines_per_func`
- [ ] 评估 call/ret 结构和 pointer-chasing load 的耦合方式

### B6. 设计 `mixed_indirect_target`

- [ ] instruction 侧复用 `indirect_target_set`
- [ ] 明确保留哪些参数：
  - [ ] `instr_target_count`
  - [ ] `instr_block_align`
- [ ] 评估它在 branch predictor / I-cache / D-side 交互中的价值

### B7. 验收标准

- [ ] mixed family 至少不再只有一个“size 驱动的统一模板”
- [ ] 每个 family 都能解释“它保留了哪类 instruction 语义”
- [ ] README 中每个 family 都有最小示例

---

## C. 生成管线改造

### C1. 改造 `pipeline.py`

- [ ] 支持从 canonical mixed 配置生成不同 instruction family
- [ ] 将当前 `mixed_region_loop` 的生成逻辑隔离成独立 family builder
- [ ] 为未来 mixed family 预留 dispatch 入口
- [ ] 明确 code/data init 流程是否因 family 不同而变化
- [ ] 明确 memory layout 输出中如何标记不同 family

### C2. 改造 `experiments/experiment_config.py`

- [ ] 使用 canonical mixed 配置定义 case
- [ ] 不再让 case 只靠 `size + ldr_count + pages + nodes` 描述一切
- [ ] 为每个 family 提供单独 case generator
- [ ] 明确哪些 case group 用于单模块库
- [ ] 明确哪些 case group 用于组合库

### C3. 改造 `experiments/runner.py`

- [ ] 让 runner 理解新的 mixed case 结构
- [ ] 让 single/combo 运行逻辑不依赖旧字段
- [ ] 继续支持 memory defaults / combo filter
- [ ] 评估是否需要为不同 mixed family 提供不同 shuffle 策略

### C4. 改造输出与报告

- [ ] CSV 字段适配 canonical mixed 模型
- [ ] Markdown 报告展示新的 mixed family 信息
- [ ] 明确 layout 输出中 family、instruction footprint、data footprint 的显示格式

### C5. 兼容与迁移

- [ ] 决定是否保留旧字段兼容层
- [ ] 若保留，明确兼容层生命周期
- [ ] 若不保留，提供转换脚本或一次性迁移说明

### C6. 验收标准

- [ ] 新 case 可不依赖历史字段独立运行
- [ ] 新旧脚本至少有一条清晰迁移路径
- [ ] mixed family 扩展不需要继续改大量 if/else

---

## D. 线性相加判定方法重构

### D1. 不再只盯 data 指标

- [ ] 将当前分析范围从 D-side 扩展到全套 raw 指标
- [ ] 明确当前 profile 下的完整指标集合
- [ ] 对每个指标分别建立“是否线性”的判定方式

### D2. 建立指标分层

- [ ] 第一层：高基数、稳定指标
  - [ ] `instructions:u`
  - [ ] `br_retired:u`
  - [ ] `l1d_cache_refill:u`
  - [ ] `l2d_cache_refill:u`
- [ ] 第二层：中等稳定性指标
  - [ ] `l1i_*`
  - [ ] `l2i_*`
  - [ ] `l1d_tlb_*`
  - [ ] `l2d_tlb_*`
- [ ] 第三层：低基数或高噪声指标
  - [ ] `ll_cache_miss:u`
  - [ ] 其他低基数 miss 指标

### D3. 定义统一误差标准

- [ ] 定义绝对误差门槛
- [ ] 定义相对误差门槛
- [ ] 定义 MPKI 门槛
- [ ] 规定何时因为 expected 太低而跳过判定
- [ ] 明确是比较 `canonical vs sum`、`shuffle vs sum`，还是两者都看

### D4. 引入重复实验统计

- [ ] 对关键 case 使用 repeated run
- [ ] 使用中位数/均值/区间，而不是只看一次
- [ ] 明确何时把偏差判为噪声
- [ ] 明确何时把偏差判为真实非线性

### D5. 扩展扫描脚本

- [ ] 让 `linearity_factor_scan.py` 支持多指标扫描
- [ ] 支持输出每个指标的：
  - [ ] `rel_diff_median`
  - [ ] `rel_diff_mean`
  - [ ] `rel_diff_min`
  - [ ] `rel_diff_max`
- [ ] 支持按指标汇总“最安全变体”和“最危险变体”

### D6. 验收标准

- [ ] 文档里能明确回答“线性相加是针对哪些指标定义的”
- [ ] safe-linearity 不再只是基于 D-side 经验

---

## E. 影响因素识别与机理分析

### E1. data working set 规模

- [ ] 系统扫描 `data_pages`
- [ ] 区分小/中/大工作集的行为
- [ ] 验证是否存在稳定高风险区间
  - [ ] `pages == 1`
  - [ ] `1 < pages < 128`
  - [ ] `pages >= 128`
  - [ ] `pages > 512`

### E2. 每页节点密度

- [ ] 系统扫描 `data_nodes_per_page`
- [ ] 判断节点密度是否影响：
  - [ ] D-cache refill
  - [ ] DTLB refill
  - [ ] LLC miss
- [ ] 判断是否存在推荐上限

### E3. data mode

- [ ] 比较：
  - [ ] `linear`
  - [ ] `line_stride`
  - [ ] `page_stride`
  - [ ] `random`
- [ ] 分析不同 mode 的干扰路径
- [ ] 判断哪些 mode 更适合 safe 模式

### E4. instruction family

- [ ] 分析不同 instruction family 对线性的影响
- [ ] 判断是否某些 family 更容易和 data 侧耦合
- [ ] 判断 `itlb_walk` 是否天然更难线性
- [ ] 判断 branch-heavy family 是否更难线性

### E5. 组合结构

- [ ] 分析重复模块是否更容易不线性
- [ ] 分析多个热点模块叠加的影响
- [ ] 分析是否必须限制“热模块数量”
- [ ] 分析组合顺序是否系统性影响结果

### E6. 虚拟内存布局

- [ ] 分析 `allocator=posix` vs `allocator=arena`
- [ ] 分析 `memory_arena_gap_bytes`
- [ ] 分析 `memory_arena_hint`
- [ ] 分析地址连续性对 cache/TLB 的影响

### E7. page backing / 内核策略

- [ ] 分析 `memory_advice=default`
- [ ] 分析 `random`
- [ ] 分析 `sequential`
- [ ] 分析 `hugepage`
- [ ] 分析 `nohugepage`
- [ ] 分析 `prefault`

### E8. 机理解释

- [ ] 区分是：
  - [ ] cache set 冲突
  - [ ] prefetch 行为变化
  - [ ] TLB reach 变化
  - [ ] first-touch/fault 干扰
  - [ ] LLC 共享
- [ ] 为主要现象写出“最可能原因”
- [ ] 把“现象 -> 原因 -> 约束”串起来

### E9. 验收标准

- [ ] 每条 safe 约束都能追溯到至少一个实验现象
- [ ] 每个主要现象都有一个可以自洽的底层解释

---

## F. safe-linearity 生成模式正式化

### F1. 审核当前启发式规则

- [ ] 重新评估当前规则是否合理：
  - [ ] `pages > 512` 禁止
  - [ ] `1 < pages < 128` 禁止
  - [ ] `nodes_per_page > 4` 禁止
  - [ ] `pages == 1 && data_mode in {random, page_stride}` 禁止
  - [ ] 组合内重复模块禁止
  - [ ] 多个 `pages == 1` 模块禁止

### F2. 将规则升级为“多指标约束”

- [ ] 不再只以 D-side 经验决定 safe 规则
- [ ] 明确哪些规则是全局通用
- [ ] 明确哪些规则只适用于特定 family

### F3. 支持 family-aware 的 safe 规则

- [ ] `mixed_hot_loop` 的 safe 规则
- [ ] `mixed_block_chain` 的 safe 规则
- [ ] `mixed_itlb_walk` 的 safe 规则
- [ ] `mixed_call_ret` 的 safe 规则

### F4. 形成稳定入口

- [ ] 保留普通生成模式
- [ ] 保留 safe-linearity 生成模式
- [ ] 明确两种模式输出文件命名
- [ ] 明确 safe 模式是不是默认启用某些 memory defaults

### F5. 验收标准

- [ ] safe 模式在代表性测试集上，坏组合比例明显低于普通模式
- [ ] safe 模式的限制规则在 README 中能清楚解释

---

## G. 测试与基准

### G1. 建立回归 case 集

- [ ] 选出一组稳定坏 case
- [ ] 选出一组稳定好 case
- [ ] 选出一组边界 case

### G2. 自动化回归

- [ ] 跑普通模式
- [ ] 跑 safe 模式
- [ ] 比较坏 case 占比
- [ ] 比较全指标误差分布

### G3. 编译与运行成本

- [ ] 监控超大 case 的 C 文件大小
- [ ] 监控编译时间
- [ ] 监控运行时间
- [ ] 将“生成成本不可接受”也纳入 safe 约束

### G4. 验收标准

- [ ] safe 模式不会频繁生成编译失控 case
- [ ] 回归结果可重复

---

## H. 文档与说明

### H1. README 持续完善

- [ ] 保持 README 只讲最新 canonical 模型
- [ ] 增加 mixed family 参数对照表
- [ ] 增加 instruction family 说明
- [ ] 增加 data family 说明
- [ ] 增加 fusion 参数说明
- [ ] 增加 safe-linearity 规则总结表

### H2. 报告文档

- [ ] 继续维护 `investigation_notes.md`
- [ ] 为关键实验结论建立单独小节
- [ ] 记录哪些结论是稳定的，哪些还只是观察

### H3. 使用示例

- [ ] 给每种 mixed family 写最小配置示例
- [ ] 给每种内存策略写调用示例
- [ ] 给 factor scan 写示例

### H4. 验收标准

- [ ] 看 README 就能理解：
  - [ ] 标签在表达什么
  - [ ] `page` 在控制什么
  - [ ] safe 模式在限制什么
  - [ ] memory 策略参数是做什么的

---

## I. 推荐执行顺序

### 第一阶段：先把模型统一

- [ ] 完成 A1 ~ A6
- [ ] 完成 B1
- [ ] 输出 canonical mixed 配置草案

### 第二阶段：先让现有 mixed 不再含糊

- [ ] 完成 C1 ~ C6
- [ ] 让当前 `mixed_region_loop` 接入 canonical 接口
- [ ] 保证旧 case 至少有迁移路径

### 第三阶段：系统扫描影响因素

- [ ] 完成 D1 ~ D6
- [ ] 完成 E1 ~ E9
- [ ] 形成第一版“高风险因素清单”

### 第四阶段：正式化 safe 模式

- [ ] 完成 F1 ~ F5
- [ ] 跑回归对比普通模式和 safe 模式

### 第五阶段：扩 mixed family

- [ ] 完成 B2 ~ B6
- [ ] 按 family 补实验与 safe 规则

---

## J. 当前优先级最高的具体任务

- [ ] 先定义 canonical mixed 配置结构
- [ ] 决定 instruction family 的最小集合
- [ ] 让 `mixed_region_loop` 用 canonical 字段重命名
- [ ] 扩展 `linearity_factor_scan.py` 到全指标
- [ ] 用 repeated scan 验证当前 safe 规则是否真的降低坏组合比例
- [ ] 再决定 safe 规则哪些保留，哪些删除，哪些改成 family-specific
