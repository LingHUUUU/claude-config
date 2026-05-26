# Scalar Diagnostics

## Block: DiagScalar

### 概述
收集标量数据：总粒子能量、总场能量等。大多数标量无论如何都会被计算。

> **Warning:** 标量诊断的 min/max cell 在 AMcylindrical 几何中尚未支持。

> **Warning:** 部分量在空间和/或时间上积分，其单位取决于模拟维度。详见 [Units: integrated quantities](../Understand/units.html#integrated-quantities)。

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| every | int / time selection | 必填 | 输出间隔（timestep） |
| vars | list[str] | `[]`（输出全部） | 需要输出的标量列表 |
| precision | int | `10` | 输出数值的位数 |

### 代码示例
```python
DiagScalar(
    every = 10,
    vars = ["Utot", "Ukin", "Uelm"],
    precision = 10
)
```

---

## 可用标量列表

### 空间积分能量密度

| 标量 | 说明 |
|------|------|
| `Utot` | 总能量 |
| `Ukin` | 总动能（粒子中） |
| `Uelm` | 总电磁能（场中） |
| `Uexp` | 期望值（初始 − 损失 + 获得） |
| `Ubal` | 平衡（Utot − Uexp） |
| `Ubal_norm` | 归一化平衡（Ubal / Utot） |
| `Uelm_Ex` | Ex 场贡献 (\(\int E_x^2 dV /2\)) |
| `Uelm_Ey` | Ey 场贡献 |
| `Uelm_Ez` | Ez 场贡献 |
| `Uelm_Bx_m` | Bx_m 场贡献 |
| `Uelm_By_m` | By_m 场贡献 |
| `Uelm_Bz_m` | Bz_m 场贡献 |
| `Urad` | 总辐射能量 |
| `UmBWpairs` | 转化为电子-正电子对的总能量 |

### 空间+时间积分 — 边界能量交换

| 标量 | 说明 |
|------|------|
| `Ukin_bnd` | 时间累积的边界动能交换 |
| `Uelm_bnd` | 时间累积的边界电磁能交换 |
| `PoyXminInst` | 当前 timestep xmin 边界 Poynting 贡献 |
| `PoyXmin` | 时间累积 xmin 边界 Poynting 贡献 |
| `PoyXmaxInst`, `PoyXmax` | xmax 边界（同上） |
| `PoyYminInst`, `PoyYmin` | ymin 边界（同上） |
| `PoyYmaxInst`, `PoyYmax` | ymax 边界（同上） |
| `PoyZminInst`, `PoyZmin` | zmin 边界（同上） |
| `PoyZmaxInst`, `PoyZmax` | zmax 边界（同上） |

### 空间+时间积分 — 其他

| 标量 | 说明 |
|------|------|
| `Ukin_new` | 新粒子（注入器）的时间累积动能 |
| `Ukin_out_mvw` | 移动窗口损失的时间累积动能 |
| `Ukin_inj_mvw` | 移动窗口获得的时间累积动能 |
| `Uelm_out_mvw` | 移动窗口损失的时间累积电磁能 |
| `Uelm_inj_mvw` | 移动窗口获得的时间累积电磁能 |

### 粒子信息（每个物种）

`abc` = 物种名。

| 标量 | 说明 |
|------|------|
| `Zavg_abc` | 物种 "abc" 的平均电荷（无粒子时为 nan） |
| `Dens_abc` | 积分密度 |
| `Ukin_abc` | 积分动能密度 |
| `Urad_abc` | 积分辐射能量密度 |
| `Ntot_abc` | 宏粒子数量 |

### 场信息

| 标量 | 说明 |
|------|------|
| `ExMin` | \(E_x\) 最小值 |
| `ExMinCell` | Ex 最小值所在 cell 索引 |
| `ExMax` | \(E_x\) 最大值 |
| `ExMaxCell` | Ex 最大值所在 cell 索引 |
| 同上有 `Ey`, `Ez`, `Bx_m`, `By_m`, `Bz_m`, `Jx`, `Jy`, `Jz`, `Rho` | 各自的最值和 cell 位置 |
