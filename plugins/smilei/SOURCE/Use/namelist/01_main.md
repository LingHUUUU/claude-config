# Main Variables

## Block: Main

### 概述
`Main` block 是**必填**的，定义模拟的基本参数：几何、网格、时间步长、边界条件等。

参考：[Units](../Understand/units.html), [Parallelization](../Understand/parallelization.html)

---

### 属性速查表

#### 几何与插值

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| geometry | str | `"2Dcartesian"` | 几何类型: `"1Dcartesian"`, `"2Dcartesian"`, `"3Dcartesian"`, `"AMcylindrical"` |
| interpolation_order | int | `2` | 粒子形状函数阶数: `1` (仅AM，含 Ruyten 校正), `2` (全配置), `4` (不支持向量化2D) |
| interpolator | str | `"momentum-conserving"` | 场插值方式: `"momentum-conserving"` 或 `"wt"`（时间步相关插值） |
| use_BTIS3_interpolation | bool | `False` | 启用 B-TIS3 插值（减少数值 Cherenkov 辐射） |
| custom_oversize | int | `2`（根据 interpolation_order 自动设置） | 每个 patch 的 ghost cell 数 |

#### 网格

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| grid_length | list[float] | 与 `number_of_cells` 二选一 | 各维度模拟长度 (\(L_r\)) |
| number_of_cells | list[int] | 与 `grid_length` 二选一 | 各维度 cell 数量 |
| cell_length | list[float] | 由 grid_length 和 number_of_cells 推导 | 各维度 cell 尺寸 (\(L_r\)) |

#### 时间

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| simulation_time | float | 与 `number_of_timesteps` 二选一 | 模拟时长 (\(T_r\)) |
| number_of_timesteps | int | 与 `simulation_time` 二选一 | 总 timestep 数 |
| timestep | float | 与 `timestep_over_CFL` 二选一 | 单步时长 (\(T_r\)) |
| timestep_over_CFL | float | 与 `timestep` 二选一 | 单步时长（CFL 比例），推荐 0.95 |
| time_fields_frozen | float | 必填 | 模拟开始时场冻结的时间 (\(T_r\)) |

#### 并行与性能

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| number_of_patches | list[int] | 必填 | 各方向 patch 数。必须为 2 的幂，总数 ≥ MPI 进程数。强烈建议多于 OpenMP 线程数。GPU 加速时建议每 MPI rank 1 个 patch |
| patch_arrangement | str | `"hilbertian"` | patch 排序方式: `"hilbertian"` (Hilbert 曲线), `"linearized_XY"`/`"linearized_XYZ"` (行优先), `"linearized_YX"`/`"linearized_ZYX"` (列优先，不支持 Field 诊断) |
| cluster_width | int | 自动（最小化内存） | X 方向 cluster 宽度（cell 数）。用于在 patch 内按 cell 排序粒子以改善缓存。须整除 patch 在 X 方向的 cell 数 |
| gpu_computing | bool | `False` | 启用 GPU 加速 |

#### Maxwell 求解器

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| maxwell_solver | str | `"Yee"` | Maxwell 求解器: `"Yee"` (全几何), `"M4"` (全几何), `"Cowan"`/`"Grassi"`/`"Lehe"`/`"Bouchard"` (2D), `"Lehe"`/`"Bouchard"` (3D), `"Lehe"`/`"Terzani"` (AM) |

#### 边界条件

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| EM_boundary_conditions | list[list[str]] | `[["periodic"]]` | EM 边界条件: `"periodic"`, `"silver-muller"` (开放/注入), `"reflective"`, `"ramp??"` (AM 谱求解器基础开放BC, ??=cell数), `"PML"` |
| EM_boundary_conditions_k | list[list[float]] | 见详情 | Silver-Muller 边界的入射波矢 \(k_{inc}\) |
| number_of_pml_cells | list[list[int]] | `[[10,10],[10,10],[10,10]]` | PML 层 cell 数。非 PML 边界须设为 0 |
| pml_sigma | list[profile] | `[lambda x: 20 * x**2]` | PML sigma 分布（每个维度 1 个 profile，定义在 [0,1] 区间） |
| pml_kappa | list[profile] | `[lambda x: 1 + 79 * x**4]` | PML kappa 分布（同上） |

#### Poisson 求解器

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| solve_poisson | bool | `True` | 初始化时是否求解 Poisson 方程 |
| poisson_max_iteration | int | `50000` | Poisson 求解器最大迭代次数 |
| poisson_max_error | float | `1e-14` | Poisson 求解器最大误差 |
| solve_relativistic_poisson | bool | `False` | 是否求解相对论 Poisson 问题 |
| relativistic_poisson_max_iteration | int | `50000` | 相对论 Poisson 最大迭代次数 |
| relativistic_poisson_max_error | float | `1e-22` | 相对论 Poisson 最大误差 |

#### AMcylindrical 专用

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| number_of_AM | int | `2` | Azimuthal Fourier 分解模式数（模式从 0 到 number_of_AM-1） |
| number_of_AM_classical_Poisson_solver | int | `1` | 非相对论 Poisson 使用的模式数（须 ≤ number_of_AM） |
| number_of_AM_relativistic_field_initialization | int | `1` | 相对论场初始化使用的模式数（须 ≤ number_of_AM） |

#### 其他

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| reference_angular_frequency_SI | float | 必填 | 参考角频率 \(\omega_r\) 的 SI 值。碰撞/电离/辐射/QED 时必需 |
| print_every | int | 自动（约 10 次/模拟） | 屏幕信息输出间隔（timestep） |
| print_expected_disk_usage | bool | `True` | 是否打印预计磁盘用量（代价高时可禁用） |
| random_seed | int | `0` | 随机种子。每个 patch 的 seed = random_seed + patch 索引 |

---

### 属性详情

#### `geometry` — AMcylindrical 限制

> **Warning:** AMcylindrical 中粒子 BC 必须 `"remove"`，EM 纵向 BC `"silver-muller"`，横向 BC `"buneman"`（或全部 `"PML"`）。不支持碰撞和 order-4 插值。

AMcylindrical 中 grid 坐标为 2D \((x,r)\)，粒子坐标为 3D Cartesian \((x,y,z)\)。

#### `EM_boundary_conditions` — 语法

三种语法:
1. `[[bc_all]]` — 所有边界相同
2. `[[bc_X], [bc_Y], ...]` — 按维度
3. `[[bc_Xmin, bc_Xmax], ...]` — 按每个面

- **`"silver-muller"`**: 开放/注入 BC。用 `EM_boundary_conditions_k` 定义入射波矢。注入时确保 \(k_{inc}\) 与被注入波对齐；吸收时最优吸收方向为 \(k_{inc}\) 的镜面反射方向
- **`"ramp??"`**: AM 谱求解器专用。前半 ghost cell 场不变，后半逐渐降至零
- **`"PML"`**: 需配合 `number_of_pml_cells`，支持激光注入

#### `EM_boundary_conditions_k` — 默认值
- 2D: `[[1.,0.],[-1.,0.],[0.,1.],[0.,-1.]]`
- 3D: `[[1.,0.,0.],[-1.,0.,0.],[0.,1.,0.],[0.,-1.,0.],[0.,0.,1.],[0.,0.,-1.]]`
- AM: Xmin/Xmax/Rmax 面受影响，k 坐标在 xr 框架中

#### `pml_sigma` / `pml_kappa` — Profile 规范
Profile 为单变量函数，定义在 [0,1]: 0 = PML 内边界，1 = PML 外边界。单个 profile 应用于所有维度；每个维度的两个面使用相同 profile。

参考：[PML in AM geometry](../Understand/PML.html)

#### `maxwell_solver` — 求解器参考

| Solver | 可用几何 | 参考 |
|--------|----------|------|
| Yee | 全部 | 标准 FDTD |
| M4 | 全部 | [paper](https://doi.org/10.1016/j.jcp.2020.109388) |
| Lehe | 2D, 3D, AM | [paper](https://journals.aps.org/prab/abstract/10.1103/PhysRevSTAB.16.021301) |
| Bouchard | 2D, 3D | [thesis p.109](https://tel.archives-ouvertes.fr/tel-02967252) |
| Terzani | AM | [paper](https://doi.org/10.1016/j.cpc.2019.04.007) |
| Cowan, Grassi | 2D | |

### 代码示例
```python
Main(
    geometry = "2Dcartesian",
    interpolation_order = 2,
    grid_length = [80.0 * Lr, 60.0 * Lr],
    cell_length = [0.05 * Lr, 0.05 * Lr],
    number_of_patches = [16, 16],
    timestep = 0.95 / math.sqrt(2) * 0.05 * Lr / c,
    simulation_time = 100.0 * Tr,
    maxwell_solver = 'Yee',
    EM_boundary_conditions = [["silver-muller", "silver-muller"]],
    reference_angular_frequency_SI = omega0,
    print_every = 100,
    random_seed = 0,
)
```
