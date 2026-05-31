# Happi Tips & Common Pitfalls

## Data Reading: Timesteps from Namelist, Not Diag

When a diagnostic is large, loading it entirely is slow. Instead:
1. Read timesteps from the **namelist object** (fast, no I/O)
2. Use those timesteps to pinpoint the exact step you need
3. Open the diagnostic **with `timesteps=target`** to read only that slice

```python
S = happi.Open("../data", verbose=False)
dt = S.namelist.Main.timestep
diag_every = S.namelist.DiagFields[0].every
target_step = int(round(physical_time / dt / diag_every) * diag_every)
F = S.Field(0, "Ex", timesteps=target_step)
```

## Rho_electron Sign

- `Rho_electron` is **charge density** (q × n), not number density
- Electron charge q = -1, so density of 30 nc appears as **-30** in the data
- Fix: apply `-data` after `getData()`, or set `vmin` negative in colormap

## getTimes() and Units

- Units are set when **creating the diagnostic object**, not when calling `getTimes()`
- Correct: `diag = S.Field(0, "Ex", units=["um", "fs"])` → then `diag.getTimes()` returns fs
- Passing `units` directly to `getTimes()` will error or be ignored

## Array Indexing

`getTimesteps()` returns a `numpy.ndarray`. Use numpy indexing, not Python list methods:
```python
timesteps = diag.getTimesteps()
idx = np.where(timesteps == target)[0][0]   # Correct
# idx = timesteps.index(target)              # Wrong — ndarray has no .index()
```

## Field Plotting

### Data Layout
- Smilei Field data layout: **`bz[ix, iy]`** — axis 0 = x, axis 1 = y
- Shape is `(nx+1, ny+1)` on Yee grid (staggered nodes, +1 from cell count)
- Use `np.squeeze()` to remove singleton dimensions from `getData()`
- For `imshow`: transpose to `bz.T` for (y, x) layout expected by matplotlib

## 用 happi 而非 h5py 读取数据

后处理应始终用 happi，不要直接用 h5py 读 HDF5 文件。原因：

- **Screen 诊断**：happi 读出的是单步增量数据；若需累积谱，需手动遍历 `timesteps` 逐步累加。h5py 直接读出的也是增量，但 happi 会做归一化（除以常数因子），两者数值不同，混用会导致结果不一致。
- **Field/Scalar 等**：happi 提供 `getAxis()`、`getTimes()`、单位转换等便利接口，h5py 需要手动解析 HDF5 结构。
- **唯一例外**：TrackParticles 极大文件（>10 GB）时，happi 的 `iterParticles(chunksize=)` 是推荐方式，无需绕道 h5py。

```python
# ✅ 正确：用 happi 累积 Screen 数据
import happi, numpy as np
S = happi.Open("data")
ts = S.Screen(0).getTimesteps()
total = np.zeros_like(S.Screen(0, timesteps=ts[0]).getData()[0])
for t in ts:
    total += S.Screen(0, timesteps=int(t)).getData()[0]

# ❌ 错误：用 h5py 直接读取
# import h5py
# with h5py.File("data/Screen0.h5") as f:
#     data = f["timestep00004014"][:]  # 数值与 happi 不同，不可混用
```

## Matplotlib Backend

Do NOT hardcode `matplotlib.use('Agg')` in scripts. Let the environment control the backend.

## Field API Quick Reference

### S.Field() 正确用法

```python
# 错误：'Rho_electron' 会作为 diagNumber（诊断索引），不是 field 名
S.Field('Rho_electron', timestep=0)        # ❌

# 正确：field 必须是第二个位置参数或关键字参数
S.Field(0, 'Rho_electron', timesteps=0)    # ✅
S.Field(0, field='Rho_electron', ...)      # ✅
```

### timesteps 是复数

```python
S.Field(0, 'Ex', timestep=0)    # ❌ timestep 是未知参数
S.Field(0, 'Ex', timesteps=0)   # ✅ 复数
```

### getData() 返回 list

```python
S.Field(0, 'Ex', timesteps=0).getData()    # 返回 [array]，不是直接 array
ex = S.Field(0, 'Ex', timesteps=0).getData()[0]  # ✅ 取 [0]
```

### 获取 timesteps 列表

```python
steps = S.Field(0, 'Ex').getTimesteps()    # 需要指定 field
```

### 空间轴

```python
x_axis = S.Field(0, 'Ex', timesteps=0).getAxis('x')  # Smilei 单位
x_axis_um = x_axis * Lr * 1e6  # 转 um
```

### DiagFields 顺序

来自 `input.py` 中 `DiagFields(fields=["Ex", "Bz", "Rho_electron", "Rho_proton"])`：

| Index | Field |
|-------|-------|
| 0 | Ex |
| 1 | Bz |
| 2 | Rho_electron |
| 3 | Rho_proton |

```python
# 通过索引取
data = S.Field(0, timesteps=0).getData()  # ❌ 必须指定 field，不能省略
# 正确方式：逐个取
ex  = S.Field(0, 'Ex', timesteps=0).getData()[0]
bz  = S.Field(0, 'Bz', timesteps=0).getData()[0]
rho = S.Field(0, 'Rho_electron', timesteps=0).getData()[0]
```

### ParticleBinning 通过 name 访问

```python
pb = S.ParticleBinning('electron_phase_space')  # ✅ 直接用 DiagParticleBinning 的 name
steps_p = pb.getTimesteps()
xa = pb.getAxis('x') * Lr * 1e6
pa = pb.getAxis('px')
data = S.ParticleBinning('electron_phase_space', timesteps=N).getData()[0]
```
