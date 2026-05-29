# Plotting Methods

Available on: Scalar, Field, Probe, ParticleBinning, Screen, TrackParticles, RadiationSpectrum.

---

## `plot(timestep=None, saveAs=None, axes=None, dpi=200, **kwargs)`

Static plot at one timestep:
- **1D data** → curve
- **2D data** → colormap
- **0D data** → curve vs. time

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `timestep` | int | None | Timestep to plot |
| `saveAs` | str | None | Save directory/filename. Pattern `mydir/prefix.png` → `prefix0.png`, `prefix1.png`, etc. |
| `axes` | matplotlib.axes | None | Axes handle to plot on. If None, creates new axes. |
| `dpi` | int | 200 | Dots per inch for `saveAs`. |

Also accepts all [shared **kwargs](01_shared_parameters.md#kwargs--plotting-options) and [advanced matplotlib options](#advanced-plotting-options).

**Example:**
```python
S.ParticleBinning(1).plot(timestep=40, vmin=0, vmax=1e14)
```

---

## `streak(saveAs=None, axes=None, **kwargs)`

Streak plot: 1D data over all timesteps → 2D image with time as second axis. Only works for 1D data.

Arguments identical to `plot` except no `timestep`.

**Example:**
```python
S.ParticleBinning(1).streak()
```

---

## `animate(movie='', fps=15, dpi=200, saveAs=None, axes=None, **kwargs)`

Animate data over time.

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `movie` | str | `""` | Output filename (`"movie.avi"`, `"movie.gif"`). No movie if empty. |
| `fps` | int | 15 | Frames per second. |
| `dpi` | int | 200 | Resolution for movie and `saveAs`. |

Other arguments same as `streak`.

**Example:**
```python
S.ParticleBinning(1).animate()
```

---

## `slide(axes=None, **kwargs)`

Interactive time slider. All arguments same as `plot` (except timestep).

**Example:**
```python
S.ParticleBinning(1).slide(vmin=0)
```

---

## Multi-Diagnostic Plotting

### `happi.multiPlot(diag1, diag2, ..., **kwargs)`

Animated figure with multiple diagnostics. If diagnostics are of similar type, they may be overlaid on one plot.

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `diag1, diag2, ...` | diagnostic objects | required | Prepared by `S.Scalar()`, `S.Field()`, `S.Probe()`, etc. |
| `figure` | int | 1 | Matplotlib figure number |
| `shape` | list | vertical stack | `[rows, cols]` arrangement, e.g., `[2,1]`, `[1,2]` |
| `legend_font` | dict | None | Legend font properties: `{'size':15, 'weight':'bold', 'family':'serif', 'color':'k'}` |
| `movie` | str | None | Movie filename |
| `fps` | int | None | Frames per second |
| `dpi` | int | None | Resolution |
| `saveAs` | str | None | Frame save directory/pattern |
| `skipAnimation` | bool | False | If True, plots only the last frame |
| `timesteps` | -- | None | Same as shared [timesteps](01_shared_parameters.md#timesteps--timestep_indices) |

### `happi.multiSlide(diag1, diag2, ..., **kwargs)`

Same as `multiPlot` but uses interactive time slider instead of animation. Supports: `figure`, `shape`, `legend_font`.

**Example:**
```python
S = happi.Open("path/to/my/results")
A = S.Probe(0, field="Ex")
B = S.ParticleBinning(1)
happi.multiPlot(A, B, figure=1)
```

> **Tip:** Use `shape=[1,1]` to overlay diagnostics. Use `side="right"` on one diagnostic for dual y-axes.

---

## `set(**kwargs)`

Update plotting options on an existing diagnostic object. Replaces options given at construction time.

Available on: Scalar, Field, Probe, ParticleBinning, Screen.

**Example:**
```python
A = S.ParticleBinning(0, figure=1, vmax=1)
A.plot(figure=2)
A.set(vmax=2)
A.plot()  # uses figure=1, vmax=2
```

---

## Advanced Plotting Options

All matplotlib arguments listed below can be passed as `**kwargs` to any diagnostic constructor or plotting method. Smilei's default colormaps: `smilei`, `smilei_r`, `smileiD`, `smileiD_r`.

### Figure options
`figsize`, `dpi`, `facecolor`, `edgecolor`
→ [matplotlib figure API](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html)

### Axes options
`aspect`, `axis_facecolor`, `frame_on`, `position`, `visible`, `xlabel`, `xscale`, `xticklabels`, `xticks`, `ylabel`, `yscale`, `yticklabels`, `yticks`, `zorder`
→ [matplotlib axes API](http://matplotlib.org/stable/api/axes_api.html) (functions starting with `set_`)

### Line options
`color`, `dashes`, `drawstyle`, `fillstyle`, `label`, `linestyle`, `linewidth`, `marker`, `markeredgecolor`, `markeredgewidth`, `markerfacecolor`, `markerfacecoloralt`, `markersize`, `markevery`, `visible`, `zorder`
→ [matplotlib Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html)

### Image options
`cmap`, `aspect`, `interpolation`, `norm`
→ [matplotlib imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html)

### Colorbar options
`cbaspect`, `orientation`, `fraction`, `pad`, `shrink`, `anchor`, `panchor`, `extend`, `extendfrac`, `extendrect`, `spacing`, `ticks`, `format`, `drawedges`, `size`, `clabel`
→ [matplotlib colorbar API](https://matplotlib.org/stable/api/colorbar_api.html)

### Tick format options
`style_x`, `scilimits_x`, `useOffset_x`, `style_y`, `scilimits_y`, `useOffset_y`
→ [matplotlib tick label format](http://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ticklabel_format.html)

### Font options (all accept dict)
`title_font`, `xlabel_font`, `xticklabels_font`, `ylabel_font`, `yticklabels_font`, `colorbar_font`

Each is a dict with matplotlib font properties: `{'size':15, 'weight':'bold', 'family':'serif', 'color':'k'}`
→ [matplotlib FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties)

**Example:**
```python
S.ParticleBinning(0, figure=1, cmap="gray").plot()
```
