# Particle Injector & Merging

## Block: ParticleInjector

### 概述
从边界向模拟域注入宏粒子。未指定的参数默认从关联的 `Species` 继承。

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| name | str | 自动生成 | 注入器名称。可用于使另一注入器复制此注入器的位置 |
| species | str | 必填 | 注入目标物种名 |
| box_side | str | 必填 | 注入边界: `"xmin"`, `"xmax"`, `"ymin"`, `"ymax"`, `"zmin"`, `"zmax"` |
| time_envelope | function / time profile | `tconstant()` | 注入器时间包络 |
| position_initialization | str | 继承 species | 位置初始化方法 |
| momentum_initialization | str | 继承 species | 动量初始化方法 |
| mean_velocity | list[3] / profile | 继承 species | 初始漂移速度 (\(c\))。**无质量粒子时实际为动量 (\(m_e c\))** |
| temperature | list[3] / profile | 继承 species | 初始温度 (\(m_e c^2\)) |
| particles_per_cell | float / profile | 继承 species | 每 cell 注入粒子数 |
| number_density | float / profile | 与 charge_density 二选一 | 数密度绝对值 (\(N_r\)) |
| charge_density | float / profile | 与 number_density 二选一 | 电荷密度绝对值 |
| regular_number | list[int] | 同 Species | `position_initialization="regular"` 时每个方向每 cell 的均匀粒子数: `[Nx, Ny, Nz]` |

### `position_initialization` 选项

| 值 | 说明 |
|----|------|
| `"species"` / `""` | 使用关联 species 的设置 |
| `"regular"` | 均匀分布，由 [`regular_number`](#regular_number) 控制 |
| `"random"` | 随机分布 |
| `"centered"` | 每个 cell 中心 |
| 另一注入器的 `name` | 复制目标注入器的位置（目标须使用上述三种方法之一） |

### `momentum_initialization` 选项

| 值 | 说明 |
|----|------|
| `"species"` / `""` | 使用关联 species 的设置 |
| `"maxwell-juettner"` | 相对论 Maxwellian |
| `"rectangular"` | 矩形分布 |

### 代码示例
```python
ParticleInjector(
    name = "injector1",
    species = "electrons1",
    box_side = "xmin",
    time_envelope = tgaussian(start=0, duration=10., order=4),
    position_initialization = "species",
    momentum_initialization = "rectangular",
    mean_velocity = [0.5, 0., 0.],
    temperature = [1e-30],
    number_density = 1,
    particles_per_cell = 16,
)
```

---

## Particle Merging（在 Species block 中）

### 概述
宏粒子合并方法。需激活向量化或 cell 排序才能使用。在 `Species` block 中配置。

参考：[Particle Merging](../Understand/particle_merging.html)

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| merging_method | str | `"none"` | 合并方法: `"none"` 禁用, `"vranic_cartesian"` 动量笛卡尔分解, `"vranic_spherical"` 动量球分解 |
| merge_every | int / time selection | `0` | 合并事件间隔（timestep） |
| merge_min_particles_per_cell | int | `4` | 触发合并的每 cell 最小粒子数 |
| merge_min_packet_size | int | `4` | 合并包最小粒子数。须 ≥ 4 |
| merge_max_packet_size | int | `4` | 合并包最大粒子数 |
| merge_momentum_cell_size | list[3] | `[16,16,16]` | 动量空间离散化各方向子组数 |
| merge_discretization_scale | str | `"linear"` | 动量离散化尺度: `"linear"` 或 `"log"`（log 仅支持球分解） |
| merge_min_momentum | float | `1e-5` | [专家] log 尺度时的最小动量值（避免 log(0)） |
| merge_min_momentum_cell_length | list[3] | `[1e-10,1e-10,1e-10]` | [专家] 动量空间离散最小子组长度（低于此值子组数设为 1） |
| merge_accumulation_correction | bool | `True` | [专家] 激活累积校正（仅在线性尺度下工作） |

### 代码示例
```python
Species(
    # ... other species params ...
    merging_method = "vranic_spherical",
    merge_every = 5,
    merge_min_particles_per_cell = 16,
    merge_max_packet_size = 4,
    merge_min_packet_size = 4,
    merge_momentum_cell_size = [16, 16, 16],
    merge_discretization_scale = "linear",
)
```
