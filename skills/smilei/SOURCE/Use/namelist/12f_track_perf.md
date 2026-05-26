# TrackParticles, NewParticles & Performances Diagnostics

## Block: DiagTrackParticles

### 概述
记录宏粒子在不同 timestep 的位置和动量，通常用于绘制轨迹。

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| species | str | 必填 | 被追踪物种的 `name` |
| every | int / time selection | `0` | 输出间隔。若 >0 则写入 `TrackParticlesDisordered_abc.h5`（`abc` = 物种名） |
| flush_every | int / time selection | `1` | 文件刷新间隔。与 `every` 重合时实际写入。刷新过频繁会严重拖慢模拟 |
| filter | Python function | None（全部追踪） | 筛选被追踪粒子的条件函数（见下方） |
| attributes | list[str] | `["x","y","z","px","py","pz","w"]` | 输出的粒子属性（见下方可用属性） |

### 可用 `attributes`

- 空间坐标: `"x"`, `"y"`, `"z"`
- 动量: `"px"`, `"py"`, `"pz"`
- 电荷: `"q"`
- 统计权重: `"w"`
- 量子参数: `"chi"`（仅辐射损失物种）
- 插值场: `"Ex"`, `"Ey"`, `"Ez"`, `"Bx"`, `"By"`, `"Bz"`

> **Note:** 插值场在 Maxwell 求解器之后计算，可能与推进粒子时（半步偏移）的值有差异。需精确值时使用 `keep_interpolated_fields`。

### `filter` 函数规范

参数为一个 `particles` 对象，具有属性 `x`, `y`, `z`, `px`, `py`, `pz`, `charge`, `weight`, `id`（以及 `keep_interpolated_fields` 启用的场属性）。每个属性为 numpy array。函数须返回同形状的 boolean numpy array（`True` = 追踪）。

> **Note:** 在 `filter` 函数中，`px`, `py`, `pz` 实际为 \(\gamma v_x\), \(\gamma v_y\), \(\gamma v_z\)（不是动量）。输出诊断中的值不受此影响。

> **Note:** `id` 属性初始为 0，仅通过 filter 后才获得正数 ID。

> **Note:** 可在 filter 函数中访问 `Main.iteration` 获取当前 PIC 循环迭代号。当前时间 = `Main.iteration * Main.timestep`。

### 代码示例
```python
DiagTrackParticles(
    species = "electron",
    every = 10,
    flush_every = 100,
    filter = my_filter,
    attributes = ["x", "px", "py", "Ex", "Ey", "Bz"]
)
```

选择满足 \(-1 < p_x < 1\) 或 \(p_z > 3\) 的粒子的 filter 示例：
```python
def my_filter(particles):
    return (particles.px > -1.) * (particles.px < 1.) + (particles.pz > 3.)
```

---

## Block: DiagNewParticles

### 概述
仅在粒子被电离或其他物理模块生成时记录宏粒子信息。

### 属性速查表

所有参数与 `DiagTrackParticles` 相同，但有以下特殊注意事项：

- 粒子生成在每个 timestep 都有记录，但 `every` 仅控制写入文件的频率。**推荐使用较大的 `every` 值以保持性能**
- 对于电离产生的电子物种，属性 `"q"` 是电离前**离子**的电荷，而非电子电荷

### 代码示例
```python
DiagNewParticles(
    species = "electron",
    every = 10,
    attributes = ["x", "px", "py", "Ex", "Ey", "Bz"]
)
```

---

## Block: DiagPerformances

### 概述
记录每个 MPI 进程或每个 patch 的计算负载和计时器信息。**每个 namelist 只能有一个 `DiagPerformances` block**。

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| every | int / time selection | `0` | 输出间隔 |
| flush_every | int / time selection | `1` | 文件刷新间隔。刷新过频繁会严重拖慢模拟 |
| patch_information | bool | `False` | 若 `True`，在 patch 级别计算信息（见 [Performances()](post-processing.html#Performances)），可能影响性能 |

### 代码示例
```python
DiagPerformances(
    every = 100,
    flush_every = 100,
    patch_information = True,
)
```
