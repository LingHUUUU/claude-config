# Diagnostics Reference

Each diagnostic is opened as a method on the `happi.Open()` return object `S`. All diagnostics share common parameters documented in [Shared Parameters](01_shared_parameters.md).

---

## Scalar

```python
S.Scalar(scalar=None, timesteps=None, units=[''], data_log=False, data_transform=None, **kwargs)
```

### Unique Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `scalar` | str | None | Scalar name (e.g., `"Utot"`, `"Uelm"`, `"Ukin"`) or an operation like `"Uelm+Ukin"`. If omitted, prints available scalars. |

### Shared Parameters
- [timesteps](01_shared_parameters.md#timesteps--timestep_indices)
- [units](01_shared_parameters.md#units)
- [data_log](01_shared_parameters.md#data_log)
- [data_transform](01_shared_parameters.md#data_transform)
- [**kwargs](01_shared_parameters.md#kwargs--plotting-options)

### Example
```python
S = happi.Open("path/to/my/results")
Diag = S.Scalar("Utot")
```

---

## Field

```python
S.Field(diagNumber=None, field=None, timesteps=None, subset=None, average=None,
        units=[''], data_log=False, data_transform=None, moving=False,
        export_dir=None, **kwargs)
```

### Unique Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `diagNumber` | int/str | None | Diagnostic number or `name`. If omitted, prints available diagnostics. |
| `field` | str | None | Field name (`"Ex"`, `"Ey"`, `"Ez"`, `"Bx"`, `"By"`, `"Bz"`, `"Jx"`, `"Jy"`, `"Jz"`, `"Rho"`) or an operation like `"Jx+Jy"`. If omitted, prints available fields. |
| `moving` | bool | False | Use moving-window X coordinates for plots and axis retrieval. |

### AMcylindrical-only Parameters

Must choose one of `theta` or `build3d` to construct real fields from complex Fourier modes.

| Parameter | Type | Description |
|-----------|------|-------------|
| `theta` | float | Angle (radians). Calculates the field in a plane through \(r=0\) at angle `theta` from the \(xy\) plane. |
| `build3d` | list of 3 ranges | Interpolate to a 3D \(xyz\) grid. Each range is `[start, stop, step]`. |
| `modes` | int / list[int] | Which Fourier modes to use. All modes if omitted. |

### Shared Parameters
- [timesteps](01_shared_parameters.md#timesteps--timestep_indices)
- [subset](01_shared_parameters.md#subset) — axes: `"x"`, `"y"`, `"z"`, `"r"`
- [average](01_shared_parameters.md#average) — axes: `"x"`, `"y"`, `"z"`, `"r"`
- [units](01_shared_parameters.md#units)
- [data_log](01_shared_parameters.md#data_log)
- [data_transform](01_shared_parameters.md#data_transform)
- [export_dir](01_shared_parameters.md#export_dir)
- [**kwargs](01_shared_parameters.md#kwargs--plotting-options)

### Example
```python
S = happi.Open("path/to/my/results")
Diag = S.Field(0, "Ex", average={"x":[4,5]}, theta=math.pi/4.)
```

---

## Probe

```python
S.Probe(probeNumber=None, field=None, timesteps=None, subset=None, average=None,
        units=[''], data_log=False, data_transform=None, **kwargs)
```

### Unique Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `probeNumber` | int/str | None | Probe number (0-based) or `name`. If omitted, prints available probes. |
| `field` | str | None | Field name (`"Ex"`, `"Ey"`, `"Ez"`, `"Bx"`, `"By"`, `"Bz"`, `"Jx"`, `"Jy"`, `"Jz"`, `"Rho"`) or operation. If omitted, prints available fields. |

### Shared Parameters
- [timesteps](01_shared_parameters.md#timesteps--timestep_indices)
- [subset](01_shared_parameters.md#subset) — axes: `"axis1"`, `"axis2"`, `"axis3"`. Coordinates are relative to the probe's `origin`, NOT the overall origin
- [average](01_shared_parameters.md#average) — axes: `"axis1"`, `"axis2"`, `"axis3"`. Same origin note
- [units](01_shared_parameters.md#units)
- [data_log](01_shared_parameters.md#data_log)
- [data_transform](01_shared_parameters.md#data_transform)
- [export_dir](01_shared_parameters.md#export_dir)
- [**kwargs](01_shared_parameters.md#kwargs--plotting-options)

### `Probe.changeField(field)`
Switch between different fields of an already-open Probe diagnostic (useful for performance). `field` argument is the same as in `Probe()`.

### Example
```python
S = happi.Open("path/to/my/results")
Diag = S.Probe(0, "Ex")
```

---

## ParticleBinning

```python
S.ParticleBinning(diagNumber=None, timesteps=None, subset=None, average=None,
                  units=[''], data_log=False, data_transform=None, **kwargs)
```

### Unique Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `diagNumber` | int/str/operation | None | Diagnostic number or `name` (0-based). Can also be an operation between diagnostics, e.g., `"#0/#1"` divides diag 0 by diag 1. If omitted, prints available diagnostics. |

### Shared Parameters
- [timesteps](01_shared_parameters.md#timesteps--timestep_indices)
- [subset](01_shared_parameters.md#subset) — axes: `"x"`, `"y"`, `"z"`, `"px"`, `"py"`, `"pz"`, `"p"`, `"gamma"`, `"ekin"`, `"vx"`, `"vy"`, `"vz"`, `"v"`, `"charge"`. Step is number of **bins**
- [average](01_shared_parameters.md#average) — same axes as subset
- [units](01_shared_parameters.md#units)
- [data_log](01_shared_parameters.md#data_log)
- [data_transform](01_shared_parameters.md#data_transform)
- [export_dir](01_shared_parameters.md#export_dir)
- [**kwargs](01_shared_parameters.md#kwargs--plotting-options)

> **Units:** See [binning units reference](binning_units.html) for details on output units.

### Example
```python
S = happi.Open("path/to/my/results")
Diag = S.ParticleBinning(1)
```

---

## Screen

```python
S.Screen(diagNumber=None, timesteps=None, subset=None, average=None,
         units=[''], data_log=False, data_transform=None, **kwargs)
```

### Unique Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `diagNumber` | int/str | None | Diagnostic number or `name`. If omitted, prints available diagnostics. |

`subset` and `average` are identical to [ParticleBinning](#particlebinning).

### Shared Parameters
Same as [ParticleBinning](#particlebinning).

### Example
```python
S = happi.Open("path/to/my/results")
Diag = S.Screen(0)
```

---

## RadiationSpectrum

```python
S.RadiationSpectrum(diagNumber=None, timesteps=None, subset=None, average=None,
                    units=[''], data_log=False, data_transform=None, **kwargs)
```

### Unique Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `diagNumber` | int/str | None | Diagnostic number or `name`. If omitted, prints available diagnostics. |

`subset` and `average` are identical to [ParticleBinning](#particlebinning).

> **Note:** The resulting spectral power is in units of \(\omega_r\). If additional axes are used, the power spectrum is divided by the size of the bins of each axis.

### Shared Parameters
Same as [ParticleBinning](#particlebinning).

### Example
```python
S = happi.Open("path/to/my/results")
Diag = S.RadiationSpectrum(0)
```

---

## TrackParticles

```python
S.TrackParticles(species=None, select='', axes=[], timesteps=None,
                 sort=True, length=None, units=[''], **kwargs)
```

### Unique Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `species` | str | None | Tracked-particle species name. If omitted, prints available species. |
| `select` | str/list | `''` | Particle selection. See select syntax below. |
| `axes` | list[str] | `[]` | Axes for plotting/data. Any [tracked attribute](namelist.html#attributes) plus `"moving_x"` (when moving window active). Examples: `["x"]`, `["x","y"]`, `["x","px"]`. |
| `sort` | bool/str | `True` | `False`: no sorting (fast, but only `getData`/`iterParticles` available). `True`: sort into new file (reuses existing sorted file). `str`: select+sort (same syntax as `select`), requires `sorted_as`. |
| `sorted_as` | str | None | Filename for sorted output when `sort` is a selection string. |
| `length` | int | None | Trajectory length in number of timesteps. |

> **Performance Note:** Particle sorting (default `sort=True`) is the main I/O bottleneck — happi reads and reorders particles by ID across timesteps to enable trajectory tracking. When you only need a **single-timestep snapshot** (e.g., spatial distribution, energy spectrum at one time), always set `sort=False` to skip the sorting pass. Combine with `timesteps=<exact_step>` to avoid scanning all chunks.

### `select` Syntax

Three forms:

1. **`"any(times, condition)"`** — particles satisfying `condition` at **any** of the `times`. Example: `"any(t>0, px>1.)"`
2. **`"all(times, condition)"`** — particles satisfying `condition` at **all** `times`. Example: `"all(t<40, px<1)"`
3. **`[ID1, ID2, ...]`** — explicit particle IDs

Logical operators: `+` = OR, `*` = AND, `~` = NOT.

Example: `select = "any((t>30)*(t<60), px>1) + all(t>0, (x>1)*(x<2))"`

### Shared Parameters
- [timesteps](01_shared_parameters.md#timesteps--timestep_indices)
- [units](01_shared_parameters.md#units)
- [export_dir](01_shared_parameters.md#export_dir)
- [**kwargs](01_shared_parameters.md#kwargs--plotting-options)

### Example
```python
S = happi.Open("path/to/my/results")
Diag = S.TrackParticles("electrons", axes=["px","py"])
```

---

## NewParticles

```python
S.NewParticles(species=None, select='', axes=[], units=[''], **kwargs)
```

### Unique Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `species` | str | None | Same as [TrackParticles](#trackparticles). |
| `axes` | list[str] | `[]` | Same as TrackParticles, plus an additional axis `"t"` representing the time when each particle was created. |
| `select` | str/list | `''` | Condition on particle properties (e.g., `"px>0"`) or explicit ID list. Supports `+` (OR), `*` (AND), `~` (NOT). |

### Shared Parameters
- [units](01_shared_parameters.md#units)
- [**kwargs](01_shared_parameters.md#kwargs--plotting-options)

---

## Performances

```python
S.Performances(raw=None, map=None, histogram=None, timesteps=None,
               units=[''], data_log=False, data_transform=None,
               species=None, cumulative=True, **kwargs)
```

Must choose exactly ONE mode: `raw`, `map`, or `histogram`.

### Unique Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `raw` | str | None | Quantity name (or operation) to list per MPI process. |
| `map` | str | None | Quantity name (or operation) to map vs. space (1D/2D only). |
| `histogram` | list | None | `["quantity", min, max, nsteps]` — histogram with `nsteps` bins. |
| `species` | str | None | Required for `"vecto"` patch-level quantity. |
| `cumulative` | bool | `True` | `True`: timers accumulated over simulation. `False`: timers reset at each output. |

### Available Quantities (MPI-process level)

| Quantity | Description |
|----------|-------------|
| `hindex` | Starting index of each proc in Hilbert curve |
| `number_of_cells` | Number of cells in each proc |
| `number_of_particles` | Total non-frozen macro-particles per proc (all species) |
| `number_of_frozen_particles` | Frozen particles per proc |
| `total_load` | Load per proc (particles + cells weighted by cell_load) |
| `timer_global` | Global simulation time (proc 0 only) |
| `timer_particles` | Time in particle computation |
| `timer_maxwell` | Time in Maxwell solver |
| `timer_envelope` | Time in envelope propagation |
| `timer_densities` | Time in density projection |
| `timer_collisions` | Time in collision computation |
| `timer_movWindow` | Time in moving window |
| `timer_loadBal` | Time in load balancing (includes global comm) |
| `timer_partMerging` | Time in particle merging |
| `timer_syncPart` | Time in particle synchronization (proc-to-proc) |
| `timer_syncField` | Time in field synchronization |
| `timer_syncDens` | Time in density synchronization |
| `timer_syncSusceptibility` | Time in susceptibility synchronization |
| `timer_diags` | Time in diagnostics write (includes global comm) |
| `timer_total` | Sum of all timers (except timer_global) |
| `memory_total` | Total RSS memory per process (GB) |
| `memory_peak` | Peak RSS memory per process (GB) |

> **Warning:** `timer_loadBal` and `timer_diags` include global communications (may include wait time). `timer_sync*` include proc-to-proc communications.

### Patch-level Quantities

Requires `patch_information` in namelist. Only compatible with `raw` mode in `3Dcartesian`.

| Quantity | Description |
|----------|-------------|
| `mpi_rank` | MPI rank containing the patch |
| `vecto` | Vectorized/scalar mode of `species` (when adaptive mode active) |

### Shared Parameters
- [timesteps](01_shared_parameters.md#timesteps--timestep_indices)
- [units](01_shared_parameters.md#units)
- [data_log](01_shared_parameters.md#data_log)
- [data_transform](01_shared_parameters.md#data_transform)
- [export_dir](01_shared_parameters.md#export_dir)
- [**kwargs](01_shared_parameters.md#kwargs--plotting-options)

### Examples
```python
# MPI-level: map total load
Diag = S.Performances(map="total_load")

# Patch-level: vectorization mode per patch
Diag = S.Performances(raw="vecto", species="electron")
```
