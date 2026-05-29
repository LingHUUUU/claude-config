# Lasers

## 概述

激光通过在 box 一侧施加振荡磁场边界条件实现。支持激光的 BC 为 `"silver-muller"` 和 `"PML"`。Smilei 提供多种激光定义方式。

**方向约定:** 以下定义默认激光从 `xmin`/`xmax` 注入。从 `ymin`/`ymax` 注入时，将 `By` 替换为 `Bx`。从 `zmin`/`zmax` 注入时，`By`→`Bx`，`Bz`→`By`。

---

## 通用公共参数

以下参数出现在多种激光 block 中：

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| box_side | str | `"xmin"` | 注入面: `"xmin"`, `"xmax"`, `"ymin"`, `"ymax"`, `"zmin"`, `"zmax"` |
| omega | float | 必填 | 激光角频率 (\(\omega_r\)) |
| a0 | float | 必填 | 归一化矢势 |
| time_envelope | function / time profile | `tconstant()` | 激光时间包络（场，非强度） |
| chirp_profile | function / time profile | `tconstant()` | 频率随时间变化: \(\omega(t)\) = `omega` × `chirp_profile(t)`。**注意：非标准定义**（见下方 Chirp 说明） |
| polarization_phi | float | 必填 | 偏振椭圆主轴与 X-Y 平面夹角 (rad) |
| ellipticity | float | 必填 | 偏振椭圆率: 0 = 线性, ±1 = 圆形 |
| phase_offset / phase_zero | float | 必填 | 附加相位（同时作用于包络和载波） |

### Chirp 说明

> **Warning:** Smilei 的 `chirp_profile` 不是瞬时频率 \(\omega_{\rm inst}(t)\)。关系为 \(\omega(t) = \omega \times \mathtt{chirp\_profile}(t)\)，其中瞬时频率 \(\omega_{\rm inst}(t) = \frac{d}{dt}[\omega(t) t]\)。

若知 \(C(t) = \omega_{\rm inst}(t)/\omega\)，可由下式转换：
\[\mathtt{chirp\_profile}(t) = \frac{1}{t} \int_0^t C(t') dt'\]

**线性 chirp 示例:** \(\omega_{\rm inst}(t) = \omega[1+\alpha\omega(t-t_0)]\)，\(C(t) = 1+\alpha\omega(t-t_0)\)：
\[\mathtt{chirp\_profile}(t) = 1 - \alpha\omega t_0 + \frac{\alpha}{2}\omega t\]

**指数 chirp 示例:** \(\omega_{\rm inst}(t) = \omega \alpha^{\omega t}\)，\(C(t) = \alpha^{\omega t}\)：
\[\mathtt{chirp\_profile}(t) = \frac{\alpha^{\omega t} - 1}{\omega t \ln \alpha}\]

---

## Block: Laser（通用波）

### 直接定义时空分布
```python
Laser(
    box_side = "xmin",
    space_time_profile = [By_profile, Bz_profile]
)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| space_time_profile | list[2 func] | 注入面的完整波形: `[By_func, Bz_func]`。参数: 1D `(t)`, 2D `(y,t)`, 3D `(y,z,t)`。仅 Cartesian |
| space_time_profile_AM | list[complex func] | 仅 AM 几何。定义各 mode 的 \(B_r\), \(B_\theta\)，顺序: `[Br_mode0, Bt_mode0, Br_mode1, Bt_mode1, ...]`。参数: `(r,t)` |

### 包络形式定义
```python
Laser(
    box_side = "xmin",
    omega = 1.,
    chirp_profile = tconstant(),
    time_envelope = tgaussian(),
    space_envelope = [By_profile, Bz_profile],
    phase = [PhiY_profile, PhiZ_profile],
    delay_phase = [0., 0.]
)
```

生成波形：
\[B_y(\mathbf{x}, t) = S_y(\mathbf{x}) T(t-t_{0y}) \sin(\omega(t) t - \phi_y(\mathbf{x}))\]
\[B_z(\mathbf{x}, t) = S_z(\mathbf{x}) T(t-t_{0z}) \sin(\omega(t) t - \phi_z(\mathbf{x}))\]

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| space_envelope | list[2 func/profile] | `[1., 0.]` | 空间包络 \(S_y\), \(S_z\) |
| phase | list[2 func/profile] | `[0., 0.]` | 空间变化相位 \(\phi_y\), \(\phi_z\) |
| delay_phase | list[2 float] | `[0., 0.]` | \(B_y\), \(B_z\) 时间包络的额外延迟 (\(\omega t\))，仅作用于包络不作用于载波。椭圆偏振且 phase 不匹配时有用 |

---

## Block: LaserPlanar1D（1D 平面波）

```python
LaserPlanar1D(
    box_side = "xmin",
    a0 = 1.,
    omega = 1.,
    polarization_phi = 0.,
    ellipticity = 0.,
    time_envelope = tconstant(),
    phase_offset = 0.,
)
```

所有参数见 [通用公共参数](#通用公共参数)。

---

## Block: LaserGaussian2D（2D 高斯波）

```python
LaserGaussian2D(
    box_side = "xmin",
    a0 = 1.,
    omega = 1.,
    focus = [50., 40.],
    waist = 3.,
    incidence_angle = 0.,
    polarization_phi = 0.,
    ellipticity = 0.,
    time_envelope = tconstant(),
    phase_offset = 0.,
)
```

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| focus | list[2 float] | 必填 | 焦点位置 `[X, Y]` (\(L_r\)) |
| waist | float | 必填 | 束腰 (\(L_r\))。横向坐标处场降至最大值的 1/e |
| incidence_angle | float | 必填 | 激光束与注入面法线夹角 (rad)，在 X-Y 平面内 |

其他参数见 [通用公共参数](#通用公共参数)。

---

## Block: LaserGaussian3D（3D 高斯波）

```python
LaserGaussian3D(
    box_side = "xmin",
    a0 = 1.,
    omega = 1.,
    focus = [50., 40., 40.],
    waist = 3.,
    incidence_angle = [0., 0.1],
    polarization_phi = 0.,
    ellipticity = 0.,
    time_envelope = tconstant(),
    phase_offset = 0.,
)
```

与 LaserGaussian2D 相同，但 `focus` 有 3 个元素 `[X, Y, Z]`，`incidence_angle` 有 2 个角度（分别绕 y 和 z 旋转）。

从 `ymin`/`ymax` 注入时，incidence angles 对应绕 x 和 z 旋转。

---

## Block: LaserGaussianAM（AM 柱坐标高斯波）

```python
LaserGaussianAM(
    box_side = "xmin",
    a0 = 1.,
    omega = 1.,
    focus = [50.],
    waist = 3.,
    polarization_phi = 0.,
    ellipticity = 0.,
    time_envelope = tconstant()
)
```

焦点在 r=0 轴上传播，因此 `focus` 仅需 `[X]` 坐标。

---

## Block: LaserSmoothing2D / LaserSmoothingPeriodic2D（2D 平滑光束）

实现随机相位板产生的空间和相位分布。参考：[Cross-beam energy transfer, Oudin et al.](https://doi.org/10.1063/5.0109511)

LaserSmoothingPeriodic2D 用于周期性 BC，注意 fnumber = \(L_y (k_0/2\pi) / N_y\)。

```python
LaserSmoothing2D(
    box_side = "xmin",
    a0 = 1.,
    omega = 1.,
    focus = None,
    incidence_angle = 0.,
    polarization_phi = 0.,
    ellipticity = 0.,
    phase_zero = 0.,
    Lf = 3.00e6,
    fnumber = 8.00,
    N = 6,
    rpp_random_seed = 10,
    temporal_smoothing = None,
    temporal_smoothing_random_seed = 42,
    omega_m = 0.,
    modulation_depth = 0,
    rpp_per_mode = False,
    rpp_seed_per_mode = [42],
    omega_m_trans = 0.,
    modulation_depth_trans = 0,
    mode2generate_trans = None,
    omega_m_longi = 0.,
    modulation_depth_longi = 0,
    mode2generate_longi = None,
    space_envelope = lambda y,z: 1.,
    time_envelope = tconstant(),
    chirp_profile = tconstant()
)
```

### 平滑光束专用参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| Lf | float | `3.00e6` | 焦距（code units） |
| fnumber | float | 必填 | 焦比 \(L_f/D\)，D = 光学系统有效孔径 |
| N | int (2D) / list[2] (3D) | `6` / `[0,0]` | 每个方向的相位板元素数（2D: 单个 int; 3D: `[Ny, Nz]`） |
| rpp_random_seed | int / None | `10` | RPP 各相位元素种子。`None` = 无随机（所有元素零相位） |
| temporal_smoothing | str | None | 时间平滑类型: `None`, `"Broadband"`, `"TSSD"`, `"LSSD"` |
| temporal_smoothing_random_seed | int | `42` | Broadband 模式各 mode 随机相位种子 |
| omega_m | float | 必填 | Broadband 调制频率（中心频率的分数） |
| modulation_depth | int | `0` | Broadband 调制深度 m，频率带宽 = 2m |
| rpp_per_mode | bool | `False` | Broadband: 每个 mode 使用不同的 RPP |
| rpp_seed_per_mode | list[int] | `[42]` | Broadband: 每个 RPP 的种子列表。len = 2×modulation_depth+1 |
| omega_m_trans | float | 必填 | TSSD 横向调制频率 |
| modulation_depth_trans | int | `0` | TSSD 调制深度 m，带宽 = 2m |
| mode2generate_trans | int | None | TSSD: 仅生成指定 mode（调试用） |
| omega_m_longi | float | 必填 | LSSD 纵向调制频率 |
| modulation_depth_longi | int | `0` | LSSD 调制深度 m，带宽 = 2m |
| mode2generate_longi | int | None | LSSD: 仅生成指定 mode（调试用） |
| space_envelope | func/profile | `lambda y,z: 1.` | 叠加在相位板空间分布上的额外用户空间分布 \(S_y\), \(S_z\) |

---

## Block: LaserSmoothing3D / LaserSmoothingPeriodic3D（3D 平滑光束）

参数与 2D 版本相同，区别：
- `N` 为 `[Ny, Nz]`（两个方向的元素数）
- `focus` 为 `[X, Y, Z]`
- fnumber 为张量: `fnumber_y = L_y (k_0/2\pi) / N_y`, `fnumber_z = L_z (k_0/2\pi) / N_z`
- 3D 版本额外参数 `direction` (str, 默认 `'y'`): TSSD 横向方向 `'y'` 或 `'z'`

---

## Block: LaserOffset（离边界注入）

当激光场不直接在边界已知，而在 box 内某平面已知时，Smilei 使用角谱方法从该平面反推边界波形。仅 2D/3D Cartesian，需 numpy。

参考：[Laser offset 详解](laser_offset.html)

```python
LaserOffset(
    box_side = "xmin",
    space_time_profile = [By_profile, Bz_profile],
    offset = 10.,
    extra_envelope = tconstant(),
    keep_n_strongest_modes = 100,
    angle = 10./180.*3.14159
)
```

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| space_time_profile | list[2 func] | 必填 | 某平面的磁场分布。参数: 2D `(y,t)`, 3D `(y,z,t)` |
| offset | float | 必填 | 从边界到 `space_time_profile` 定义平面的距离 (\(L_r\)) |
| extra_envelope | func/profile | `lambda *z: 1.` | 在边界额外施加的包络。参数: 2D `(y,t)`, 3D `(y,z,t)`。因 FFT 周期性可能导致脉冲重复，用此包络消除虚假重复 |
| keep_n_strongest_modes | int | `100` | 预处理中保留的时间 Fourier 模式数 |
| angle | float | 必填 | 边界与 profile 平面之间的夹角 (rad)（绕 z 旋转） |
| fft_time_window | float | `simulation_time` | `space_time_profile` 采样时长。对整个 simulation_time 做 FFT 代价可能很高 |
| fft_time_step | float | `timestep` | 采样时间步长。增大可减内存但移除高频 |
| number_of_processes | int | 全部可用 | 计算 LaserOffset 的 MPI 进程数。多进程 FFT 更快但太多可能通信代价高 |
| file | str | None | 以往模拟生成的 `LaserOffset*.h5` 文件路径。可减少重复计算 |

### 代码示例
```python
LaserOffset(
    box_side = "xmin",
    space_time_profile = [By_profile, Bz_profile],
    offset = 10.,
    extra_envelope = tconstant(),
    keep_n_strongest_modes = 100,
)
```
