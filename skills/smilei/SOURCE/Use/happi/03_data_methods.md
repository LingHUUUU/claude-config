# Data Methods

Methods for retrieving data from diagnostic objects. Available on: Scalar, Field, Probe, ParticleBinning, Screen, RadiationSpectrum, TrackParticles, Performances (except where noted).

---

## `getData(timestep=None)`

Returns a list of data arrays (one element per requested timestep).

| Diagnostic | Return type | Notes |
|------------|-------------|-------|
| Scalar | list of scalars | |
| Field | list of ndarray | |
| Probe | list of ndarray | |
| ParticleBinning | list of ndarray | |
| Screen | list of ndarray | |
| RadiationSpectrum | list of ndarray | |
| TrackParticles | dict | Keys = axis names. If `sort=False`, entries nested inside per-timestep keys. |

**Parameters:**
- `timestep` (int, optional): If specified, reads and returns only that single timestep.

**Example:**
```python
S = happi.Open("path/to/results")
Diag = S.Field(0, "Ex")
result = Diag.getData()  # list of Ex arrays (one per time)
```

---

## `getTimesteps()`

Returns a list of the requested timestep numbers.

Available on: Scalar, Field, Probe, ParticleBinning, Screen, TrackParticles.

---

## `getTimes()`

Returns a list of the requested times. By default in code units; converted if `units` was specified when opening the diagnostic.

Available on: Scalar, Field, Probe, ParticleBinning, Screen, TrackParticles.

---

## `getAxis(axis, timestep=None)`

Returns the list of positions along the requested axis. Empty list if axis not available. By default in code units; converted if `units` was specified.

**Parameters:**
- `axis` (str): Axis name:
  - Field: `"x"`, `"y"`, `"z"`
  - Probe: `"axis1"`, `"axis2"`, `"axis3"`
  - ParticleBinning / Screen / RadiationSpectrum: the `type` of the axis defined in namelist. For user-defined axes, the name is `"user_functionN"` (N = 0-based index). Print the diagnostic to see available axes.
- `timestep` (int, optional): Only matters when:
  - ParticleBinning / Screen / RadiationSpectrum with `auto` axis limits
  - Field with `moving=True`

Available on: Scalar (no timestep needed), Field, Probe, ParticleBinning, Screen.

---

## `getXmoved(timestep)`

Returns the displacement of the moving window at the given `timestep`.

Available on: Field, Probe, TrackParticles.

---

## `TrackParticles.iterParticles(timestep, chunksize=1)`

Fast iterator on chunks of particles for a given timestep. Particles are **not ordered** by ID (different ordering across timesteps).

Returns per-iteration: `{axis: array}` dict with axis → particle values.

**Parameters:**
- `timestep` (int): Which timestep to read
- `chunksize` (int): Number of particles per chunk

**Example:**
```python
S = happi.Open("path/to/my/results")
Diag = S.TrackParticles("my_particles")
npart, sum_px = 0, 0.
for chunk in Diag.iterParticles(100, chunksize=10000):
    npart += chunk["px"].size
    sum_px += chunk["px"].sum()
mean_px = sum_px / npart
```

---

## `toVTK(numberOfPieces=1)`

Exports data to VTK format. The `export_dir` parameter (set when opening the diagnostic) specifies the output directory.

Available on: Field, Probe, ParticleBinning, Screen, Performances.

**Parameters:**
- `numberOfPieces` (int): Number of files to split the data into.

### `TrackParticles.toVTK(rendering='trajectory', data_format='xml')`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `rendering` | str | `"trajectory"` | `"trajectory"`: one file for all trajectories (requires sorted). `"cloud"`: one file per iteration (no sorting required). |
| `data_format` | str | `"xml"` | `"xml"` or `"vtk"` (ASCII). |

**Example:**
```python
tracked = S.TrackParticles("electron", axes=["x","y","z","px","py","pz","Id"], timesteps=[1,10])
tracked.toVTK(rendering="cloud", data_format="xml")    # separate files per iteration
tracked.toVTK(rendering="trajectory", data_format="xml")  # single trajectory file
```
