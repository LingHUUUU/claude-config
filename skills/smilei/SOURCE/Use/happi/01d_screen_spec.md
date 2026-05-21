## Open a Screen diagnostic[¶](#open-a-screen-diagnostic "Link to this heading")

Screen(*diagNumber=None*, *timesteps=None*, *subset=None*, *average=None*, *units=['']*, *data\_log=False*, *data\_transform=None*, *\*\*kwargs*)[¶](#Screen "Link to this definition")
:   - `timesteps` (or `timestep_indices`), `units`, `data_log`, `data_transform`, `export_dir`: same as before.
    - `diagNumber`, `subset` and `average`: identical to that of ParticleBinning diagnostics.
    - See also [Other arguments for diagnostics](#otherkwargs)

**Example**:

```
S = happi.Open("path/to/my/results")
Diag = S.Screen(0)
```

---

## Open a RadiationSpectrum diagnostic[¶](#open-a-radiationspectrum-diagnostic "Link to this heading")

RadiationSpectrum(*diagNumber=None*, *timesteps=None*, *subset=None*, *average=None*, *units=['']*, *data\_log=False*, *data\_transform=None*, *\*\*kwargs*)[¶](#RadiationSpectrum "Link to this definition")
:   - `timesteps` (or `timestep_indices`), `units`, `data_log`, `data_transform`, `export_dir`: same as before.
    - `diagNumber`, `subset` and `average`: identical to that of ParticleBinning diagnostics.
    - See also [Other arguments for diagnostics](#otherkwargs)

**Example**:

```
S = happi.Open("path/to/my/results")
Diag = S.RadiationSpectrum(0)
```

Note

The resulting spectral power is in units of \(\omega\_r\).
If additional axes are used, the power spectrum is divided by the size of the bins of each axes.

---

## Open a TrackParticles diagnostic[¶](#open-a-trackparticles-diagnostic "Link to this heading")

TrackParticles(*species=None*, *select=''*, *axes=[]*, *timesteps=None*, *sort=True*, *length=None*, *units=['']*, *\*\*kwargs*)[¶](#TrackParticles "Link to this definition")
:   - `timesteps` (or `timestep_indices`), `units`, `export_dir`: same as before.
    - `species`: the name of a tracked-particle species.
      If omitted, a list of available tracked-particle species is printed.
    - `select`: Instructions for selecting particles among those available.
      A detailed explanation is provided below
    - `axes`: A list of axes for plotting the trajectories or obtaining particle data.
      :   Each axis is one of the [`attributes`](namelist.html#attributes "attributes") defined in the namelist.
          In addition, when there is a moving window, the axis `"moving_x"` is automatically available.

          **Example:** `axes = ["x"]` corresponds to \(x\) versus time.

          **Example:** `axes = ["x","y"]` correspond to 2-D trajectories.

          **Example:** `axes = ["x","px"]` correspond to phase-space trajectories.
    - `sort`: may be either

      - `False`: the particles are not sorted by ID. This can save significant
        time, but prevents plotting, exporting to VTK, and the `select` argument. Only
        `getData` and `iterParticles` are available in this mode.
        Read [this](ids.html) for more information on particle IDs.
      - `True`: the particles are sorted in a new file, unless this file already exists.
        If it does, sorted particles are directly read from the sorted file.
      - A string for selecting particles (same syntax as `select`): only selected
        particles are sorted in a new file. The file name must be defined
        in the argument `sorted_as`. If `timesteps` is used, only selected timesteps
        will be included in the created file.
    - `sorted_as`: a keyword that defines the new sorted file name (when `sort` is a
      selection) or refers to a previously user-defined sorted file name (when `sort` is not given).
    - `length`: The length of each plotted trajectory, in number of timesteps.
    - See also [Other arguments for diagnostics](#otherkwargs)

**Example**:

```
S = happi.Open("path/to/my/results")
Diag = S.TrackParticles("electrons", axes=["px","py"])
```

Detailed explanation of the `select` parameter

Say `times` is a condition on timesteps `t`, for instance `t>50`.

Say `condition` is a condition on particles properties (`x`, `y`, `z`, `px`, `py`, `pz`), for instance `px>0`.

- **Syntax 1:** `select="any(times, condition)"`

  Selects particles satisfying `condition` for at least one of the `times`.

  For example, `select="any(t>0, px>1.)"` selects those reaching \(p\_x>1\) at some point.
- **Syntax 2:** `select="all(times, condition)"`

  Selects particles satisfying `condition` at all `times`.

  For example, `select="all(t<40, px<1)"` selects those having \(p\_x<1\) until timestep 40.
- **Syntax 3:** `select=[ID1, ID2, ...]`

  Selects the provided particle IDs.
- It is possible to make logical operations: `+` is *OR*; `*` is *AND*; `~` is *NOT*.

  For example, `select="any((t>30)*(t<60), px>1) + all(t>0, (x>1)*(x<2))"`

---

## Open a NewParticles diagnostic[¶](#open-a-newparticles-diagnostic "Link to this heading")
