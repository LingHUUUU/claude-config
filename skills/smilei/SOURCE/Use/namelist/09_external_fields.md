# External Fields, Antennas & Walls

## Block: ExternalField

### 概述
在模拟开始时对整个 box 施加初始场。

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| field | str | 必填 | 场名称（见下方列表） |
| profile | float / profile | 必填 | 初始空间分布 |

### 可用场名称

**Cartesian 几何:** `"Ex"`, `"Ey"`, `"Ez"`, `"Bx"`, `"By"`, `"Bz"`, `"Bx_m"`, `"By_m"`, `"Bz_m"`

**AM 几何:** `"El_mode_i"`, `"Er_mode_i"`, `"Et_mode_i"`, `"Bl_mode_i"`, `"Br_mode_i"`, `"Bt_mode_i"`, `"Bl_m_mode_i"`, `"Br_m_mode_i"`, `"Bt_m_mode_i"`, `"A_mode_1"`, `"A0_mode_1"`（`i` 为 mode number）

### 属性详情

#### `field` — B 场时间偏移
使用标准 FDTD 格式时，`B` 场定义在 \(t=0.5\Delta t\)，`B_m` 场定义在 \(t=0\)（与 `E` 场相同）。若模拟开始时域内有粒子，必须用 `B_m` 初始化 \(t=0\) 的 B 场。若省略 `B_m`，假定磁场恒定且 \(B_m = B\)。

#### `field` — AM 几何
所有场名必须包含 mode number `"_mode_i"`（如 `"Er_mode_1"`）。外部 envelope 场需在 `"A_mode_1"`（\(t=0\)）和 `"A0_mode_1"`（\(t=-\Delta t\)）初始化。

### 代码示例
```python
ExternalField(
    field = "Ex",
    profile = constant(0.01, xvacuum=0.1)
)
```

---

## Block: PrescribedField

### 概述
在整个模拟过程中叠加用户定义的含时空依赖的电磁场。这些场推动粒子但**不参与 Maxwell 求解**（非自洽）。适用于描述给定外场中的带电粒子动力学。

`PrescribedField` **不在 Field 诊断中可见**，但可通过 Probe 和 TrackParticles 的场属性观测（因为它们采样作用于宏粒子的总场）。

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| field | str | 必填 | 场名称（见下方列表） |
| profile | Python function | 必填 | 时空分布函数：参数为 `(x, t)` 或 `(x, y, t)` 等 |

### 可用场名称

**Cartesian:** `"Ex"`, `"Ey"`, `"Ez"`, `"Bx_m"`, `"By_m"`, `"Bz_m"`

**AM:** `"El_mode_m"`, `"Er_mode_m"`, `"Et_mode_m"`, `"Bl_m_mode_m"`, `"Br_m_mode_m"`, `"Bt_m_mode_m"`

> **Warning:** 施加磁场时必须使用时间中心场 `"Bx_m"`, `"By_m"`, `"Bz_m"`（定义在整数时间步，是粒子推进器使用的场）。

> **Warning:** AM 几何中 mode "m" 必须在场名中显式指定，profile 必须返回复数值。

### 代码示例
```python
from numpy import cos, sin
def myPrescribedProfile(x, t):
    return cos(x) * sin(t)

PrescribedField(
    field = "Ex",
    profile = myPrescribedProfile
)
```

---

## Block: Antenna

### 概述
在整个模拟过程中施加额外电流（天线）。

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| field | str | 必填 | 电流方向: `"Jx"`, `"Jy"`, `"Jz"` |
| space_profile | float / profile | 必填（与 `space_time_profile` 互斥） | 天线空间分布 |
| time_profile | float / profile | 必填（与 `space_time_profile` 互斥） | 天线时间分布，与 `space_profile` 相乘 |
| space_time_profile | float / profile | 必填（与上述两者互斥） | 时空联合分布函数，参数为 N+1 维：如 1D `(x,t)`, 2D `(x,y,t)` |

#### `space_time_profile` 函数签名
函数须接受 `x`, `y`, `z` 为 float 或 numpy array。若接受 float，返回 float；若接受 numpy array（对应 1 个 patch 的坐标），返回同尺寸的 numpy array。

### 代码示例
```python
Antenna(
    field = "Jz",
    space_profile = gaussian(0.01),
    time_profile = tcosine(base=0., duration=1., freq=0.1)
)
```

---

## Block: PartWall

### 概述
引入墙壁以反射、停止、热化或移除到达的粒子。

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| kind | str | 必填 | 墙壁类型: `"reflective"`, `"stop"`, `"thermalize"`, `"remove"` |
| x | float | 三选一 | 墙壁在 x 方向的位置 |
| y | float | 三选一 | 墙壁在 y 方向的位置 |
| z | float | 三选一 | 墙壁在 z 方向的位置 |

### 代码示例
```python
PartWall(
    kind = "reflective",
    x = 20.
)
```
