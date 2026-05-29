# Time Selections, Checkpoints & Variables

## Time Selections

多个组件（主要是诊断）通过 `every` 参数指定输出时间。五种语法：

```
every = [ period                    ]  # Syntax 1: 从0开始，每 period 输出
every = [ start, period             ]  # Syntax 2: 从 start 开始
every = [ start, end, period        ]  # Syntax 3: start 到 end
every = [ start, end, period, repeat       ]  # Syntax 4: 每个 period 输出 repeat 次
every = [ start, end, period, repeat, spacing ]  # Syntax 5: repeat 间间隔 spacing
```

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `start` | 0 | 第一个输出 timestep |
| `end` | ∞ | 最后一个输出 timestep |
| `period` | 1 | 输出间隔 |
| `repeat` | 1 | 每个 period 的输出次数 |
| `spacing` | 1 | repeat 之间的间隔 |

> **Tip:** `every = period`（不写列表）也接受。值设为 `0` 会被替换为默认值。`every = 0` 表示无输出。数字可为非整数（除 `repeat` 外），自动选择最近 timestep。

---

## Block: Checkpoints

### 概述
在指定时间保存（dump）模拟状态，以便后续从此点重启。

> **重启须知:**
> - 不要重启到同一目录，文件会被覆盖。为新模拟创建新目录
> - 每个 MPI 进程 dump 一个文件，总量可能很大
> - 重启运行必须使用相同的 namelist（除 Checkpoints block 可修改）

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| dump_step | int | `0`（不 dump） | dump 之间的 timestep 数 |
| dump_minutes | float | `0.`（不 dump） | dump 之间的分钟数。可与 `dump_step` 组合使用 |
| exit_after_dump | bool | `True` | `True`: 首次 dump 后停止。`False`: 继续模拟 |
| keep_n_dumps | int | `2` | 保留最近 n 个 dump（旧 dump 被覆盖）。默认 2 防止崩溃时丢失 |
| file_grouping | int | `0`（不分组） | 每个目录最多存放的 dump 文件数。用于文件数限制的文件系统 |
| dump_deflate | -- | -- | (待文档) |

### 重启参数

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| restart_dir | str | `None` | 之前运行的目录（绝对或相对路径）。首次运行不指定。也可通过命令行传入: `mpirun ... ./smilei input.py "Checkpoints.restart_dir='/path/to/prev'"` |
| restart_number | int | `None` | 使用前一次运行中的第几个 dump（0, 1, 2...）。取最新 dump 对应的编号 |

### 代码示例
```python
Checkpoints(
    dump_step = 10000,
    dump_minutes = 240.,
    exit_after_dump = True,
    keep_n_dumps = 2,
)
```

---

## Smilei 预定义变量

Smilei 向 namelist Python 解释器注入以下变量。**用户不应重新定义它们。** 可在 happi 后处理中通过 `S.namelist.smilei_mpi_size` 等访问。

| 变量 | 说明 |
|------|------|
| `smilei_mpi_rank` | 当前进程的 MPI rank |
| `smilei_mpi_size` | MPI 进程总数 |
| `smilei_omp_threads` | 每个 MPI 的 OpenMP 线程数 |
| `smilei_total_cores` | 总核数 |

---

## Profiles（简要）

部分量可为依赖空间和/或时间的分布函数。详见 [profiles documentation](profiles.html)。
