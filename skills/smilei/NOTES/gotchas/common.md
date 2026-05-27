# Common Gotchas

## Python Interpreter Overhead

- Smilei starts one Python interpreter per MPI rank
- Large namelist imports can be expensive — avoid unnecessary `import` statements
- Use `cleanup()` to delete large variables and free memory after initialization

## Test Mode (`smilei_test`)

- Only initializes, does NOT run the PIC loop — checks namelist consistency
- Must run on 1 MPI process
- Can specify expected MPI/OpenMP config: `./smilei_test 1024 12 namelist.py`

## preprocess() / cleanup() Hooks

- `preprocess()`: runs before main loop, good for copying shared data
- `cleanup()`: runs after main loop, good for freeing Python memory

## Post-processing

- `python -i smilei.py` restores namelist variables into interactive Python
- happi does NOT support multiple `%matplotlib` calls — restart Python when switching simulations

## OpenMPI

- Use `--mca btl ^vader` to disable vader protocol instability
- Cluster may require `module load mpi/openmpi`

## Boundary Conditions

- `silver-muller` EM BC + `remove` particle BC = most stable combination
- PML absorbs better than silver-muller but costs more computation

## `number_of_cells` vs `cell_length`

- **优先用 `number_of_cells`**: 直接锁定格点数, Smilei 据此反算 cell_length, 无浮点漂移风险
- **避免 `cell_length`**: Smilei 内部做 `Nx = grid_length / cell_length`, 浮点精度可能导致 `Lx/dx = 1280.003`, ceil 后变 1281, 对齐 patch/cluster 后格点数偏离预期
- 在 Main 中同时传入 `grid_length` 和 `number_of_cells`, 不传 `cell_length`

## Slurm 日志目录

- `sbatch` 提交时即解析 `--output/--error` 路径, 目录不存在则日志静默丢失, 作业 FAILED 无任何诊断信息
- **必须在提交前 `mkdir -p` 创建日志目录**

## 激光/包络/时间曲线必须在 Main() 之后定义

- `tgaussian()`, `ttrapezoidal()`, `tsin2()` 等时间曲线函数内部会读取 `Main.simulation_time` 等参数
- **必须在 `Main()` 块之后调用这些函数**, 否则会报错: `XXX profile has been defined before Main()`
- 正确顺序: 物理常数 → 网格参数 → `Main(...)` → 时间曲线定义 → `Laser(...)` / `Species(...)`

## 默认诊断配置

写 `input.py` 时，默认包含以下诊断：

| 诊断 | 作用 |
|------|------|
| `DiagScalar(every=...)` | 总能量、动量守恒监控 |
| `DiagFields(every=..., fields=[...])` | 场分布（Ex, Bz, Rho 等） |
| `DiagParticleBinning(every=..., ...)` | 相空间分布（用于 px-x GIF） |
| `DiagTrackParticles(every=...)` | 粒子追踪（可选，按需） |

### 推荐输出频率：10 个光周期

一个光周期 `T0 = 2π/ω0 = 2π Tr`。在 Smilei 单位中 `ω0 = 1`，所以 `T0 = 2π`。

```python
T0 = 2.0 * math.pi  # 一个光周期（Smilei 单位）
every_10cycles = int(10 * T0 / Main.timestep)  # ≈ 198（当 dt=0.317 fs, lambda=1 um）

# 或直接估算：~200 步输出一次
DiagScalar(every=200)
DiagFields(every=200, fields=["Ex", "Bz", "Rho_electron", "Rho_proton"])
DiagParticleBinning(
    every=200,
    species=["electron", "proton"],
    axes=[["x", 0, 80*Lr, 200], ["px", -5, 5, 200]],
)
DiagTrackParticles(species="electron", every=200)
```

### quick 参考

```python
import math
T0 = 2.0 * math.pi
every_10 = max(1, int(10 * T0 / dt))
```

如果用户不指定输出频率，默认按 **每 10 个光周期** 输出一次。对于 `lambda=1 um`、`dt=0.317 fs` 的典型 1D 模拟，约每 200 步输出一次。

## 默认等离子体温度：100 eV

Smilei 中温度归一化到 `m_e c^2 / k_B`：

```python
eV = 1.0 / 511000.0       # 1 eV 的归一化值 (m_e c^2 ≈ 511 keV)
T_eV = 100.0              # 默认温度 [eV]
temperature = [T_eV * eV]  # ≈ 0.000196
```

若用户不指定，默认设为 **100 eV**（避免热效应掩盖物理过程）。
