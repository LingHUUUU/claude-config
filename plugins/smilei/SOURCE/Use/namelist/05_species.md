# Species

## Block: Species

### 概述
定义粒子物种。每种粒子需一个独立的 `Species` block。支持电子、离子、光子物种，以及丰富的物理模块（电离、辐射、QED 对产生、粒子合并等）。

---

### 属性速查表

#### 基本属性

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| name | str | 必填 | 物种名称。须多于 1 字符，不能以 `"m_"` 开头 |
| mass | float | 必填 | 粒子质量 (\(m_e\))。光子为 0 |
| charge | float / profile | 必填 | 粒子电荷 (\(e\)) |
| atomic_number | int | `0` | 原子序数（≤ 100）。电离和核反应必需。在碰撞中考虑原子屏蔽效应（离子设为 0 则视为完全电离） |
| maximum_charge_state | int | `0` | `ionization_model="from_rate"` 时的最大电荷态 |
| is_test | bool | `False` | 测试粒子标志。`True` 则粒子不参与电荷和电流 |
| pusher | str | `"boris"` | 推进器类型（见下方） |

#### 位置初始化

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| position_initialization | str/array/file | 必填 | `"regular"` / `"random"` / `"centered"` (不支持AM) / 另一物种 `name` (复制位置) / numpy array / HDF5 文件路径 |
| regular_number | list[int] | 自动 | `position_initialization="regular"` 时每方向每 cell 的粒子数: `[Nx, Ny, Nz]`（AM: `[Nx, Nr, Ntheta]`，推荐 Ntheta ≥ 4×(number_of_AM-1)）。未设时 particles_per_cell 须为模拟维度的幂 |

#### 动量初始化

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| momentum_initialization | str/array/file | 必填 | `"maxwell-juettner"` (相对论 Maxwellian) / `"rectangular"` / `"cold"` (零温) / numpy array / HDF5 文件 |
| mean_velocity | list[3] / profile | 必填 | 初始漂移速度 (\(c\))。**无质量粒子时此为动量 (\(m_e c\))** |
| mean_velocity_AM | list[3] / profile | 仅 AM | 纵向/径向/角向的初始漂移速度 (\(c\))。与 `mean_velocity` 二选一。**无质量粒子时为动量。警告：应用于每个粒子可能计算量较大** |
| temperature | list[3] / profile | `1e-10` | 初始温度 (\(m_e c^2\)) |

#### 密度与粒子数

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| particles_per_cell | float / profile | 必填 | 每 cell 粒子数 |
| number_density | float / profile | 与 charge_density 二选一 | 数密度绝对值 (\(N_r\)) |
| charge_density | float / profile | 与 number_density 二选一 | 电荷密度绝对值 |

#### 边界条件

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| boundary_conditions | list[list[str]] | `[["periodic"]]` | `"periodic"`, `"reflective"`, `"remove"` (删除), `"stop"` (动量归零), `"thermalize"`。光子 (mass=0) 不支持后两种。语法同 EM_boundary_conditions |
| thermal_boundary_temperature | list[float] | None | 热边界（BC=`"thermalize"`）的温度。当前仅 x 方向生效 |
| thermal_boundary_velocity | list[float] | `[]` | 热边界后粒子的漂移速度分量 |

#### 冻结

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| time_frozen | float | 必填 | 粒子冻结时间 (\(T_r\))。冻结粒子不动、不产生电流，但产生电荷密度；可被电离。比非冻结粒子计算量小得多 |

#### 场电离

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| ionization_model | str | `"none"` | `"tunnel"` (PPT-ADK), `"tunnel_full_PPT"` (实验性，含磁量子数), `"tunnel_envelope_averaged"` (激光包络), `"from_rate"` (用户定义速率，需 maximum_charge_state)。前三种需 atomic_number |
| bsi_model | str | `"none"` | Barrier Suppression Ionization 修正: `"Tong_Lin"`, `"KAG"`。仅支持 `ionization_model="tunnel"` 或 `"tunnel_full_PPT"` |
| ionization_rate | Python function | 必填（from_rate 模式） | 用户定义的电离速率函数 |
| ionization_electrons | str | 必填（电离启用时） | 接收电离新生电子的电子物种名 |

#### 辐射反应

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| radiation_model | str | `"none"` | `"Landau-Lifshitz"`/`"ll"` (高能近似), `"corrected-Landau-Lifshitz"`/`"cll"` (含量子修正), `"Niel"` (随机辐射模型), `"Monte-Carlo"`/`"mc"` (MC 辐射模型，可生成宏光子)。**光子 (mass=0) 不可用** |
| radiation_photon_species | str | None | Monte-Carlo 模型生成宏光子的目标光子物种名。光子物种 mass=0，须在 namelist 中定义于辐射物种之后。**光子不可用** |
| radiation_photon_sampling | int | `1` | 每次发射事件生成的宏光子数（总权重守恒）。大值可能严重拖慢性能 |
| radiation_max_emissions | int | `10` | 每个宏粒子每 timestep 最多发射 MC 事件数。用于缓冲区分配，高值可能耗尽内存。**光子不可用** |
| radiation_photon_gamma_threshold | float | `2` | 宏光子能量阈值 (\(m_e c^2\))。低于此值不生成宏光子但计入能量平衡。默认值 = 2 倍电子静止能量（衰变成电子-正电子对所需能量）。**光子不可用** |

#### 其他物理

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| relativistic_field_initialization | bool | `False` | 相对论场初始化。`True` 则在 `time_frozen` 时刻将该物种的电磁场加入模拟。推荐将该物种与其他物种远离放置以避免瞬时非物理力 |
| multiphoton_Breit_Wheeler | list[2] | `[None, None]` | 通过多光子 BW 对产生创建的 [电子物种名, 正电子物种名]。**仅光子 (mass=0) 可用** |
| multiphoton_Breit_Wheeler_sampling | list[2] | `[1, 1]` | 每次光子衰变生成的 [电子数, 正电子数]（总权重守恒）。**仅光子可用** |
| keep_interpolated_fields | list[str] | `[]` | 存储在内存中的插值场: `"Ex"`, `"Ey"`, `"Ez"`, `"Bx"`, `"By"`, `"Bz"`。可被 ParticleBinning 和 TrackParticles 诊断访问。磁场来自插值器，相比 Fields 诊断有半个 timestep 偏移。额外: `"Wx"`, `"Wy"`, `"Wz"` (时间累积的各电场分量做功) |

### `pusher` 选项

| 值 | 说明 |
|----|------|
| `"boris"` | 相对论 Boris 推进器（默认） |
| `"borisnr"` | 非相对论 Boris 推进器 |
| `"vay"` | J. L. Vay 相对论推进器 |
| `"higueracary"` | Higuera-Cary 相对论推进器 |
| `"norm"` | 仅光子：匀速直线传播 |
| `"ponderomotive_boris"` | 激光包络模型用的修正 Boris 推进器（需质量非零） |
| `"borisBTIS3"` | Boris + B-TIS3 插值 B 场。须 `use_BTIS3_interpolation=True` |
| `"ponderomotive_borisBTIS3"` | 同上 + 包络模型。须 `use_BTIS3_interpolation=True` |

### `position_initialization` 选项

| 值 | 说明 |
|----|------|
| `"regular"` | 均匀分布，由 `regular_number` 控制 |
| `"random"` | 随机分布 |
| `"centered"` | 每个 cell 中心（不支持 AMcylindrical） |
| 另一物种名 | 复制目标物种的位置（目标须使用上述三种方法之一，且须先定义） |
| numpy array / HDF5 | 详见 [Particle initialization](particle_initialization.html) |

### `momentum_initialization` 选项

| 值 | 说明 |
|----|------|
| `"maxwell-juettner"` | 相对论 Maxwellian 分布（依赖 `temperature`） |
| `"rectangular"` | 矩形分布（依赖 `temperature`） |
| `"cold"` | 零温 |
| numpy array / HDF5 | 详见 [Particle initialization](particle_initialization.html) |

### `ionization_rate` 函数规范

函数接受一个 `particles` 参数，具有属性 `x`, `y`, `z`, `px`, `py`, `pz`, `charge`, `weight`, `id`（均为 numpy array）。须返回同形状的 numpy array。

```python
from numpy import exp, zeros_like

def my_rate(particles):
    rate = zeros_like(particles.x)
    charge_0 = (particles.charge == 0)
    charge_1 = (particles.charge == 1)
    rate[charge_0] = r0 * particles.x[charge_0]
    rate[charge_1] = r1 * particles.x[charge_1]
    return rate

Species(..., ionization_rate=my_rate)
```

### 代码示例
```python
Species(
    name = "electron",
    position_initialization = "random",
    momentum_initialization = "maxwell-juettner",
    particles_per_cell = 64,
    mass = 1.0,
    charge = -1.0,
    number_density = 0.01,
    temperature = [0.001],
    boundary_conditions = [["remove", "remove"], ["remove", "remove"]],
    time_frozen = 0.0,
    pusher = "boris",
)
```
