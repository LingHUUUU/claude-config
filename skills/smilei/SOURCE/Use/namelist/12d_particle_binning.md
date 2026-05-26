# ParticleBinning Diagnostics

## Block: DiagParticleBinning

### 概述
从宏粒子收集数据并在运行时处理。不提供单个粒子信息，而是产生平均量（粒子密度、电流等）。原始数据及 happi 后处理说明见 [binning units](binning_units.html)。

数据离散化在用户选择的"网格"中，每个维度称为"轴"（axis）。支持任意维度（含 0-D = 总积分密度）。

参考：[Units: weights](../Understand/units.html#weights)

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| name | str | None | 诊断名称（仅后处理用） |
| deposited_quantity | str / Python function | 必填 | 每个网格单元求和的量（见下方） |
| every | int / time selection | 必填 | 输出间隔（timestep） |
| flush_every | int / time selection | `1` | 文件刷新间隔。刷新过频繁会严重拖慢模拟 |
| time_average | int | `1` | 时间平均的 timestep 数（在选定时间后连续平均 time_average 次） |
| species | list[str] | 必填 | 一个或多个物种名。所有物种合并到同一诊断 |
| axes | list[list] | `[]` | 定义网格的轴列表。可为空（0-D，输出总量） |

### `deposited_quantity` 选项

| 值 | 输出结果 |
|----|----------|
| `"weight"` | 数密度 |
| `"weight_charge"` | 电荷密度 |
| `"weight_charge_vx"` | \(j_x\) 电流密度（同有 vy, vz） |
| `"weight_p"` | 动量密度（同有 px, py, pz） |
| `"weight_ekin"` | 能量密度 |
| `"weight_vx_px"` | xx 压强（同有 yy, zz, xy, yz, xz） |
| `"weight_chi"` | 量子参数密度（仅辐射损失物种） |
| Python function | 自定义量（见下方） |

#### 自定义 `deposited_quantity` 函数

参数为一个对象（通常命名为 `particles`），具有属性 `x`, `y`, `z`, `px`, `py`, `pz`, `charge`, `weight`, `chi`, `id`（以及 `keep_interpolated_fields` 启用的场属性）。每个属性为 numpy array（对应 1 个 patch 中所有粒子）。函数须返回同形状的 numpy array。

```python
# 等价于 "weight_px"
def stuff(particles):
    return particles.weight * particles.px

# 或使用 lambda
deposited_quantity = lambda p: p.weight * p.px
```

### `axes` 参数

每个轴的语法：
```
[type, min, max, nsteps, "logscale", "edge_inclusive"]
```

#### `type` 可用值

| 轴类型 | 说明 |
|--------|------|
| `"x"`, `"y"`, `"z"` | 空间坐标。moving window 时可用 `"moving_x"` |
| `"px"`, `"py"`, `"pz"`, `"p"` | 动量 |
| `"vx"`, `"vy"`, `"vz"`, `"v"` | 速度 |
| `"gamma"`, `"ekin"` | 能量（Lorentz 因子 / 动能） |
| `"chi"` | 量子参数 |
| `"charge"` | 粒子电荷 |
| Python function | 自定义轴（同 `deposited_quantity` 的函数签名） |

#### 轴参数说明

| 参数 | 说明 |
|------|------|
| `min`, `max` | 轴范围。可设为 `"auto"` 自动计算（可能影响性能） |
| `nsteps` | bin 数量 |
| `"logscale"` | 可选，设为对数轴 |
| `"edge_inclusive"` | 可选，将 [min, max] 范围外的粒子纳入边界 bin |

### 示例

**x 方向密度变化：**
```python
DiagParticleBinning(
    deposited_quantity = "weight",
    every = 5, time_average = 1,
    species = ["electron1"],
    axes = [["x", 0., 1., 30]]
)
```

**x-y 密度图：**
```python
axes = [["x", 0., 1., 30], ["y", 0., 1., 30]]
```

**速度分布：**
```python
axes = [["vx", -0.1, 0.1, 100]]
```

**相空间：**
```python
axes = [["x", 0., 1., 30], ["px", -1., 1., 100]]
```

**对数能量分布（输入单位 \(m_e c^2 \approx 0.5\) MeV）：**
```python
axes = [["ekin", 0.02, 2., 100, "logscale"]]
```

**三能段 x-y 密度图（edge_inclusive 使上限到 ∞）：**
```python
axes = [["x", 0., 1., 30], ["y", 0., 1., 30], ["ekin", 0., 6., 3, "edge_inclusive"]]
```

**电荷分布：**
```python
axes = [["charge", -0.5, 10.5, 11]]
```

### 代码示例
```python
DiagParticleBinning(
    deposited_quantity = "weight",
    every = 5,
    time_average = 1,
    species = ["electrons1", "electrons2"],
    axes = [
        ["x", 0., 10, 100],
        ["ekin", 0.1, 100, 1000, "logscale", "edge_inclusive"]
    ]
)
```
