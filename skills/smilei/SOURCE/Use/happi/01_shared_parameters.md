# Shared Parameters

These parameters are shared across multiple diagnostic constructors. They are documented once here and referenced from each diagnostic.

---

## `timesteps` / `timestep_indices`

**Applies to:** Scalar, Field, Probe, ParticleBinning, Screen, RadiationSpectrum, TrackParticles, Performances

Controls which timesteps to read:

- **Omitted:** all timesteps are used
- **Single number:** nearest available timestep
- **Two numbers:** all timesteps in between (range)

`timesteps` provides the timestep numbers themselves; `timestep_indices` provides their indices in the available list.

---

## `units`

**Type:** list / dict / `happi.Units` object
**Applies to:** Scalar, Field, Probe, ParticleBinning, Screen, RadiationSpectrum, TrackParticles, NewParticles, Performances

Three syntaxes:

1. **List**: `units = ["um/ns", "W/cm^2"]` — any quantity matching the dimension of one of these units is converted
2. **Dictionary**: `units = {"x":"um", "y":"um", "v":"Joule"}` — per-axis and per-value specification
3. **`happi.Units` object**: `units = happi.Units("um/ns", "feet", x="um")` — combines list and dict syntaxes

**Requirements:**
- [Pint](https://pypi.python.org/pypi/Pint/) package
- `reference_angular_frequency_SI` must be set in the simulation namelist, **or** passed to `happi.Open()` as an override

---

## `subset`

**Type:** dict
**Applies to:** Field, Probe, ParticleBinning, Screen, RadiationSpectrum

Extracts a selection of coordinates from the data. Three syntaxes:

| Syntax | Format | Meaning |
|--------|--------|---------|
| 1 | `{axis: location}` | Single coordinate |
| 2 | `{axis: [start, stop]}` | Range of coordinates |
| 3 | `{axis: [start, stop, step]}` | Range with step |

**Axis availability by diagnostic:**

| Diagnostic | Available axes | Step unit |
|------------|---------------|-----------|
| Field | `"x"`, `"y"`, `"z"`, `"r"` | Number of **cells** |
| Probe | `"axis1"`, `"axis2"`, `"axis3"` | Number of probe cells. Coordinates are relative to the probe's `origin`, NOT the overall origin |
| ParticleBinning | `"x"`, `"y"`, `"z"`, `"px"`, `"py"`, `"pz"`, `"p"`, `"gamma"`, `"ekin"`, `"vx"`, `"vy"`, `"vz"`, `"v"`, `"charge"` | Number of **bins** |
| Screen | Same as ParticleBinning | Number of bins |
| RadiationSpectrum | Same as ParticleBinning | Number of bins |

> **Warning:** For Field, `step` is a number of **cells**. For ParticleBinning/Screen/RadiationSpectrum, `step` is a number of **bins**.

---

## `average`

**Type:** dict
**Applies to:** Field, Probe, ParticleBinning, Screen, RadiationSpectrum

Averages data over selected axes. Three syntaxes:

| Syntax | Format | Meaning |
|--------|--------|---------|
| 1 | `{axis: "all"}` | Average over entire axis |
| 2 | `{axis: location}` | Keep only the bin closest to `location` |
| 3 | `{axis: [start, stop]}` | Average over range from `start` to `stop` |

Axis availability is the same as for [`subset`](#subset).

Example: `average = {"x":[4,5]}` averages data for \(x\) within [4,5].

---

## `data_log`

**Type:** bool
**Default:** `False`
**Applies to:** Scalar, Field, Probe, ParticleBinning, Screen, RadiationSpectrum, Performances

If `True`, \(\log_{10}\) is applied to the output data.

---

## `data_transform`

**Type:** function
**Default:** `None`
**Applies to:** Scalar, Field, Probe, ParticleBinning, Screen, RadiationSpectrum, Performances

If set to a function `f`, the function is applied to the output before plotting: `f(data)`.

---

## `export_dir`

**Type:** str
**Default:** `None`
**Applies to:** Field, Probe, ParticleBinning, Screen, RadiationSpectrum, TrackParticles, Performances

Directory for VTK file export (see [toVTK](03_data_methods.md)).

---

## `**kwargs` — Plotting Options

All diagnostics accept these keyword arguments for plot customization. See [Advanced plotting options](04_plotting.md#advanced-plotting-options) for additional matplotlib arguments.

| Argument | Type | Description |
|----------|------|-------------|
| `figure` | int | Matplotlib figure number |
| `vmin`, `vmax` | float | Data value limits for colormap |
| `vsym` | bool/float | Symmetric limits about 0: `True` = autoscale, number = [-n, n]. Sets colormap to `smileiD`. |
| `xmin`, `xmax`, `ymin`, `ymax` | float | Axis limits |
| `xfactor`, `yfactor` | float | Axis rescaling factors |
| `xoffset`, `yoffset` | float | Coordinate offsets in normalized units (before factor/unit conversion) |
| `title` | str | Plot title. Supports `{time}` and `{time_units}` placeholders with formatting, e.g., `title = "Density @ $t = {time:.0f} {time_units}$"` |
| `side` | str | `"left"` (default) or `"right"` — which side to place y-axis |
| `transparent` | None/str/function | Colormap transparency: `None`, `"over"`, `"under"`, `"both"`, or a function `f(x)` mapping data value ∈ [0,1] to transparency ∈ [0,1] |
