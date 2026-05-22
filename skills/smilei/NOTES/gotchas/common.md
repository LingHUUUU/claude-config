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
