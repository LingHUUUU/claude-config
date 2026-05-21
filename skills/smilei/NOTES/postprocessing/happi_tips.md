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

Always **transpose** field data before plotting with `imshow`:
```python
data = F.getData()  # shape may be (nx, ny) or (ny, nx)
plt.imshow(data.T)  # transpose for correct orientation
```

## Matplotlib Backend

Do NOT hardcode `matplotlib.use('Agg')` in scripts. Let the environment control the backend.
