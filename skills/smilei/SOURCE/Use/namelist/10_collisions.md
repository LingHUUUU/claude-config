# Collisions & Reactions

## Block: Collisions

### 概述
二元库仑碰撞与反应：处理短程库仑相互作用（小于 cell 尺寸），包括碰撞电离和核反应。通过一个或多个 `Collisions` block 指定。

参考：[Collisions](../Understand/collisions.html)

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| species1 | list[str] | 必填 | 第一组物种名列表 |
| species2 | list[str] | 必填 | 第二组物种名列表 |
| every | int / time selection | `1` | 碰撞计算间隔（timestep）。仅在碰撞频率相对 timestep 逆较低时设 >1 |
| debug_every | int | `0` | 碰撞信息输出间隔。`0` = 无输出 |
| time_frozen | float | 必填 | 无碰撞/反应的时间段 (\(T_r\)) |
| coulomb_log | float | 必填 | `=0`: 自动计算；`>0`: 固定值；`<0`: 禁用碰撞（其他反应仍可发生） |
| coulomb_log_factor | float | 必填 | 严格正的库仑对数乘数因子（无论自动计算还是固定值），可用于补偿人为降低的离子质量 |
| ionizing | bool/str | `False` | 碰撞电离。`False`: 禁用；已存在电子物种名: 电离电子创建于该物种；`True`: 使用 `species1`/`species2` 中第一个电子物种 |
| nuclear_reaction | list[str] | `None` | 核反应产物物种名列表。`species1` 和 `species2` 各自必须为同种原子（由 `mass` 和 `atomic_number` 自动识别）。当前仅支持 D(d,n)He³ |
| nuclear_reaction_multiplier | float | 自动调整 | 核反应速率乘数（正数）。人为增加反应次数以获得良好统计。产物权重自动调整以保持物理正确数量。`0.` = 自动 |

### 属性详情

#### `species1` / `species2` — 碰撞分组规则
碰撞/反应在 `species1` 组和 `species2` 组之间发生。两组要么完全不相交，要么完全相同（称为 intra-collisions）。若两组各仅含 1 个物种，算法可能更快（尤其支持 SIMD 向量化时）。

> **Warning:** `species1 = ["electrons1", "electrons2"], species2 = ["ions"]` 不会使 `electrons1` 与 `electrons2` 之间碰撞。

#### `ionizing` — 电离条件
一个物种组必须全为电子（`mass = 1`），另一个全为相同 `atomic_number` 的离子。

#### 束缚电子屏蔽
仅在 e-i 碰撞中考虑。需原子物种定义非零 `atomic_number`。

### 代码示例
```python
Collisions(
    species1 = ["electrons1", "electrons2"],
    species2 = ["ions1"],
    debug_every = 1000,
    coulomb_log = 0.,
    coulomb_log_factor = 1.,
    ionizing = False,
)
```
