# Fields Diagnostics

## Block: DiagFields

### 概述
收集 PIC 网格位置的场数据（电磁场、电流和密度），支持瞬时值和平均值。

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| name | str | None | 诊断名称（仅后处理用） |
| every | int / time selection | 必填 | 输出间隔（timestep） |
| flush_every | int / time selection | `1` | 文件刷新间隔。与 `every` 重合时实际写入。刷新过频繁会严重拖慢模拟 |
| time_average | int | `1`（无平均） | 时间平均的 timestep 数 |
| fields | list[str] | `[]`（输出全部） | 保存的场名列表 |
| subgrid | list[slice] | `None`（全网格） | 子网格选择（见下方） |
| datatype | str | `"double"` | 数据类型: `"double"` (8 bytes) 或 `"float"` (4 bytes) |

### 可用场列表

**Cartesian 几何:**

| 场 | 说明 |
|----|------|
| `Ex`, `Ey`, `Ez` | 电场分量 |
| `Bx`, `By`, `Bz` | 磁场分量 |
| `Bx_m`, `By_m`, `Bz_m` | 磁场分量（时间中心） |
| `Jx`, `Jy`, `Jz` | 总电流分量 |
| `Jx_abc`, `Jy_abc`, `Jz_abc` | 物种 "abc" 的电流分量 |
| `Rho` | 总电荷密度 |
| `Rho_abc` | 物种 "abc" 的电荷密度 |

**AMcylindrical 几何:** `x/y/z` 替换为 `l/r/t`（纵向/径向/角向），Fourier 模式用后缀 `_mode_i`（`i` = mode number）。如 `El_mode_0`, `Br_mode_1` 等。不指定 mode number 则包含所有可用模式。`Jl`, `Jr`, `Jt`, `Rho` 同理。

**Envelope 模型附加场:**

| 场 | 说明 |
|----|------|
| `Env_A_abs` | 激光矢势复包络模 \(\|\tilde{A}\|\)（横向分量） |
| `Env_Chi` | 总极化率 \(\chi\) |
| `Env_E_abs` | 激光电场复包络模 \(\|\tilde{E}\|\)（横向分量） |
| `Env_Ex_abs` | 激光电场复包络模 \(\|\tilde{E}_x\|\)（传播方向分量） |

> **Note:** 单个 DiagFields 中所有场必须为同一类型（实或复）。AMcylindrical 中 Env 实场需单独 DiagFields block。

**B-TIS3 插值附加场:** `By_mBTIS3`, `Bz_mBTIS3`（Cartesian）；`Br_mBTIS3_mode_i`, `Bt_mBTIS3_mode_i`（AM）。

### `subgrid` 参数

用 numpy `s_[]` 表达式选择网格子区域输出：

```python
from numpy import s_
# 只输出每隔一个 cell
DiagFields(subgrid = s_[::2, ::2, ::2])
# 输出一个长方体范围
DiagFields(subgrid = s_[100:300, 300:500, 300:600])
```

每个维度的元素可为: `None`（全维度）、整数（单个 cell 索引）、slice 对象。

### 代码示例
```python
DiagFields(
    every = 10,
    time_average = 2,
    fields = ["Ex", "Ey", "Ez"],
)
```
