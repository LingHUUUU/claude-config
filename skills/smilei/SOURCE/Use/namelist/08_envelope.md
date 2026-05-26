# Laser Envelope Model

## 概述

在 `x` 方向传播的激光脉冲可用包络模型建模。激光的快振荡被忽略，所有物理量（场、源项、粒子位置和动量）为多个光学周期内的平均值。涉及与激光中心波长可比的特征长度效应（如陡峭等离子体密度分布）**不能**用此选项建模。

参考：[Laser envelope model](../Understand/laser_envelope.html)

### 限制
- AMcylindrical 仅支持柱对称（`number_of_AM = 1`）
- 仅支持 order 2 插值和投影
- 当前仅 1 个激光脉冲（给定频率、正 x 方向）。多脉冲可通过包络分布实现（如两个相邻 Gaussian），但共享相同载波频率和传播方向
- 若包络时空变化尺度接近激光波长，结果不准确

---

## Block: LaserEnvelope（通用）

```python
LaserEnvelope(
    omega = 1.,
    envelope_solver = 'explicit',
    box_side = "inside",
    envelope_profile = envelope_profile,
    Envelope_boundary_conditions = [["reflective"]],
    polarization_phi = 0.,
    ellipticity = 0.
)
```

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| omega | float | `1.` | 激光角频率 (\(\omega_r\)) |
| envelope_solver | str | `"explicit"` | 包络方程求解器. `"explicit"`: 中心有限差分. `"explicit_reduced_dispersion"`: 优化 x 向导数以降低数值色散（推荐远距离传输，CFL 限制更严格） |
| box_side | str | `"inside"` | 激光包络注入方式. `"inside"`: 仅在模拟开始时添加（profile 时间坐标 = x 坐标）. `"xmin"`: 从左侧边界逐步注入（profile 时间坐标同普通 Laser block） |
| envelope_profile | function / profile | 必填 | 复激光包络分布。`"inside"`: 参数为所有空间坐标+时间. `"xmin"`: 参数为 x=0 平面的横向坐标+时间。**推荐在真空中（与等离子体分离）初始化** |
| Envelope_boundary_conditions | list[list[str]] | `[["reflective"]]` | 包络边界条件: `"reflective"` 或 `"PML"`（PML 需在 Main 中定义 `number_of_pml_cells`） |
| polarization_phi | float | 必填 | 偏振椭圆主轴与 X-Y 平面夹角 (rad)。仅在电离中需要 |
| ellipticity | float | 必填 | 偏振椭圆率: `0` = 线性, `1` = 圆形。当前仅支持这两种 |

> **Note:** `"xmin"` 模式下使用傍轴假设，`envelope_profile` 须满足此假设。

---

## 简化 block

以下简化 block 的参数含义与对应普通 Laser block 相同（见 [Lasers](07_lasers.md)），差异说明如下：

### Block: LaserEnvelopePlanar1D（1D）
```python
LaserEnvelopePlanar1D(
    a0 = 1.,
    time_envelope = tgaussian(center=150., fwhm=40.),
    envelope_solver = 'explicit',
    Envelope_boundary_conditions = [["reflective"]],
    polarization_phi = 0.,
    ellipticity = 0.
)
```

### Block: LaserEnvelopeGaussian2D（2D）
```python
LaserEnvelopeGaussian2D(
    a0 = 1.,
    focus = [150., 40.],
    waist = 30.,
    time_envelope = tgaussian(center=150., fwhm=40.),
    envelope_solver = 'explicit',
    Envelope_boundary_conditions = [["reflective"]],
    polarization_phi = 0.,
    ellipticity = 0.
)
```

### Block: LaserEnvelopeGaussian3D（3D）
```python
LaserEnvelopeGaussian3D(
    a0 = 1.,
    focus = [150., 40., 40.],
    waist = 30.,
    time_envelope = tgaussian(center=150., fwhm=40.),
    envelope_solver = 'explicit',
    Envelope_boundary_conditions = [["reflective"]],
    polarization_phi = 0.,
    ellipticity = 0.
)
```

### Block: LaserEnvelopeGaussianAM（柱坐标）
仅当 `number_of_AM = 1` 时可用。

```python
LaserEnvelopeGaussianAM(
    a0 = 1.,
    focus = [150.],
    waist = 30.,
    time_envelope = tgaussian(center=150., fwhm=40.),
    envelope_solver = 'explicit',
    Envelope_boundary_conditions = [["reflective"]],
    polarization_phi = 0.,
    ellipticity = 0.
)
```

### 简化 block 属性说明

| 属性 | 说明 |
|------|------|
| time_envelope | 激光脉冲时间包络。根据 `box_side` 含义不同（见 LaserEnvelope）。变化尺度不可接近激光波长 |
| waist | 束腰。**小于或接近激光波长的 waist 不满足包络模型假设** |
| a0, focus 等 | 与普通 Laser block 相同 |

> **Note:** 简化 block 定义的分布对应激光矢势分量 \(\tilde{A}\) 在偏振方向的复包络。对应电场分量复包络的计算见 [Laser envelope model](../Understand/laser_envelope.html)。

`polarization_phi` 和 `ellipticity` 在包络模型中仅用于计算电离率和电离新生电子的初始动量。对于其他用途（运动方程、有质动力、激光演化），偏振角不起作用。
