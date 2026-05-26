# Screen & RadiationSpectrum Diagnostics

## Block: DiagScreen

### 概述
当宏粒子穿过指定表面时收集数据，对粒子属性做直方图。与 ParticleBinning 的区别：
- 仅统计穿过表面的粒子
- 数据在所有 timestep 上累积

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| name | str | None | 诊断名称（仅后处理用） |
| shape | str | 必填 | 表面形状: `"plane"`, `"sphere"`, `"cylinder"` |
| point | list[float] | 必填 | 定义表面的点: plane 上一点 / sphere 中心 / cylinder 轴上一点。长度 = 模拟维度 |
| vector | list[float] | 必填 | 定义表面的向量: plane 法向 / sphere 半径 / cylinder 轴（向量模 = 圆柱半径）。长度 = 模拟维度 |
| direction | str | `"both"` | 计数方向: `"both"` 两侧, `"forward"` 向量方向, `"backward"` 反向, `"canceling"` 反向计为负 |
| deposited_quantity | -- | 必填 | 与 [ParticleBinning](12d_particle_binning.md) 的 `deposited_quantity` 相同 |
| every | int / time selection | 必填 | 输出间隔 |
| flush_every | int / time selection | `1` | 文件刷新间隔。刷新过频繁会严重拖慢模拟 |
| species | list[str] | 必填 | 一个或多个物种名。所有物种合并到同一诊断 |
| axes | list | 必填 | 直方图的轴。与 [ParticleBinning](12d_particle_binning.md) 相同，外加: `"a"`/`"b"` (plane: 垂直于 vector 的轴), `"theta"`/`"phi"` (sphere: 相对于 vector 的角度), `"a"`/`"phi"` (cylinder: 轴向和角度) |

### 代码示例
```python
DiagScreen(
    shape = "plane",
    point = [5., 10.],
    vector = [1., 0.],
    direction = "canceling",
    deposited_quantity = "weight",
    species = ["electron"],
    axes = [["a", -10.*l0, 10.*l0, 40], ["px", 0., 3., 30]],
    every = 10
)
```

---

## Block: DiagRadiationSpectrum

### 概述
计算加速电荷非相干高能光子发射的瞬时功率谱。类似 ParticleBinning 但多一个 binning 轴：发射光子能量。其他轴仍然可用。

参考：[High-energy photon emission & radiation reaction](../Understand/radiation_loss.html)

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| name | str | None | 诊断名称（仅后处理用） |
| every | int / time selection | 必填 | 输出间隔 |
| flush_every | int / time selection | `1` | 文件刷新间隔 |
| time_average | int | `1` | 输出前数据平均的 timestep 数 |
| species | list[str] | 必填 | 发射辐射的物种名列表 |
| photon_energy_axis | list | 必填 | 光子能量轴: `[min, max, nsteps, "logscale"]`（单位 \(m_e c^2\)） |
| axes | list | `[]` | 额外 binning 轴，语法同 [ParticleBinning](12d_particle_binning.md) |

### 示例

**全模拟时长积分：**
```python
DiagRadiationSpectrum(
    every = Nt,
    time_average = Nt,
    species = ["electrons"],
    photon_energy_axis = [0., 1000., 100, 'logscale'],
    axes = []
)
```

**角分辨瞬时辐射谱（假设所有电子沿速度方向发射）：**
```python
from numpy import arctan2, pi
def angle(p):
    return arctan2(p.py, p.px)

DiagRadiationSpectrum(
    every = 10,
    species = ["electrons"],
    photon_energy_axis = [0., 1000., 100, 'logscale'],
    axes = [[angle, -pi, pi, 90]]
)
```

### 代码示例
```python
DiagRadiationSpectrum(
    every = 5,
    time_average = 1,
    species = ["electrons1", "electrons2"],
    photon_energy_axis = [0., 1000., 100, 'logscale'],
    axes = []
)
```
