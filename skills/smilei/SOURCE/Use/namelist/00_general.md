# General Rules & Python Workflow

## Namelist 基本规则

### Block 语法
Smilei 通过 Python block（函数调用）定义模拟参数。在 block 外部可自由计算；在 block 内部只能定义 Smilei 变量。

```python
Main(
    timestep = 0.01,
    grid_length = [10., 20.],
)
```

### Python 缩进
遵循标准 Python 缩进规则（4 空格）：

```python
if a == 0:
    timestep = 0.1
    if b == 1:
        timestep = 0.2
else:
    timestep = 0.3
```

### 列表
Python 列表使用 `[]` 并用逗号分隔：`mean_velocity = [0., 1.1, 3.]`

### 导入
可自由导入任何已安装 Python 包：`from math import pi`

### 单位归一化
所有量以任意参考值归一化。详见 [Units](../Understand/units.html)。

---

## Python 工作流

Smilei 在每个 MPI 进程启动一个 Python 解释器，执行以下步骤：

1. **Smilei 传递变量给 Python**:
   - [`smilei_mpi_rank`](#smilei_mpi_rank) — 当前 MPI rank
   - [`smilei_mpi_size`](#smilei_mpi_size) — MPI 进程总数
   - [`smilei_omp_threads`](#smilei_omp_threads) — 每 MPI 的 OpenMP 线程数
   - [`smilei_total_cores`](#smilei_total_cores) — 总核数

2. **执行 namelist**

3. **`preprocess()`** — 若用户定义，在此执行。适合计算 happi 后处理不需要的量

4. **模拟初始化** — 包括场和粒子数组分配

5. **`cleanup()`** — 若用户定义，在此执行。适合删除不再需要的大型变量

6. **Python 解释器检查** — 若模拟中不需要 Python（如无 temporal profile），Python 被停止

所有指令汇总在 `smilei.py` 文件中，用户可直接运行 `python -i smilei.py` 进行后处理。

---

## 命令行参数

任何 Python 指令可作为命令行参数传入：

```bash
mpirun -n 4 ./smilei input.py "Main.print_every=10"
```

这在重启时特别有用：
```bash
mpirun ... ./smilei mynamelist.py "Checkpoints.restart_dir='/path/to/prev'"
```
