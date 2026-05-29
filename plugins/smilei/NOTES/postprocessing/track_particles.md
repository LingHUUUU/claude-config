# TrackParticles: High-Performance Reading

## Physical Time → Iteration Step

Convert desired physical time to the exact diagnostic output step:

```python
import happi

S = happi.Open("../data", verbose=False)
target_time_fs = 120.0

omega0 = S.namelist.Main.reference_angular_frequency_SI
Tr = 1.0 / omega0
fs_sim = 1e-15 / Tr          # 1 fs in Smilei units
dt = S.namelist.Main.timestep
diag_every = S.namelist.DiagTrackParticles[0].every

target_step_theory = target_time_fs * fs_sim / dt
target_step = int(round(target_step_theory / diag_every) * diag_every)
```

## Fast Reading: sort=False + axes Restriction

Without `timesteps` specification, happi scans ALL HDF5 chunks — can cause OOM or minutes of I/O on large datasets.

```python
track_diag = S.TrackParticles(
    "electron",
    axes=["px", "py", "w"],     # Only read what you need
    timesteps=target_step,       # Pinpoint the exact step
    sort=False                   # Skip expensive per-particle-ID sorting
)
```

## Nested Dict Return Structure

When `sort=False`, `getData()` returns a **nested dict**, NOT a simple list:

```python
data_dict = track_diag.getData()
# Structure:
# {
#     'times': [actual_step_number, ...],
#     actual_step: {
#         'px': numpy_array,
#         'py': numpy_array,
#         'w':  numpy_array
#     }
# }

actual_step = data_dict['times'][0]
particle_data = data_dict[actual_step]
px = particle_data["px"]
py = particle_data["py"]
w  = particle_data["w"]
```

- Using `getData()[0]` will trigger `IndexError` or `KeyError`
- Always check `data_dict['times']` to get the actual step key

## Attribute Name Differences

| Diagnostic Type | Weight Attribute |
|-----------------|-----------------|
| TrackParticles | `"w"` |
| ParticleBinning | `"weight"` |

## 输出频率建议

- TrackParticles 数据可用于绘制粒子相空间图
- 若用户未指定频率, **默认每 20 个光周期输出一次**
- 换算公式: `diag_every = int(20.0 * 2.0 * math.pi / dt)`, 其中 `2π/dt` 是一个光周期的步数
- 场诊断 (`DiagFields`) 同理, 需要用户指定频率, 否则按 20 光周期
