## Open a Probe diagnostic[¶](#open-a-probe-diagnostic "Link to this heading")

Probe(*probeNumber=None*, *field=None*, *timesteps=None*, *subset=None*, *average=None*, *units=['']*, *data\_log=False*, *data\_transform=None*, *\*\*kwargs*)[¶](#Probe "Link to this definition")
:   - `timesteps` (or `timestep_indices`), `units`, `data_log`, `data_transform`, `export_dir`: same as before.
    - `probeNumber`: number or `name` of the probe (the first one has number 0).
      :   If not given, a list of available probes is printed.
    - `field`: name of the field (`"Bx"`, `"By"`, `"Bz"`, `"Ex"`, `"Ey"`, `"Ez"`, `"Jx"`, `"Jy"`, `"Jz"` or `"Rho"`).
      :   If not given, a list of available fields is printed.

          The string can also be an operation between several fields, such as `"Jx+Jy"`.
    - `subset` and `average` are very similar to those of
      [`Field()`](#Field "Field"), but they can only have the axes: `"axis1"`, `"axis2"` and `"axis3"`.
      For instance, `average={"axis1":"all"}`. Note that the axes are not necessarily
      equal to \(x\), \(y\) or \(z\) because the probe mesh is arbitrary.

      **WARNING:** UNLIKE [`Field()`](#Field "Field"), THE LOCATIONS ARE RELATIVE TO THE PROBE’S [`origin`](namelist.html#origin "origin"), NOT TO THE OVERALL ORIGIN.
    - See also [Other arguments for diagnostics](#otherkwargs)

**Example**:

```
S = happi.Open("path/to/my/results")
Diag = S.Probe(0, "Ex")
```

Probe.changeField(*field*)[¶](#Probe.changeField "Link to this definition")
:   In cases where happi’s performance is an issue, it is possible to switch between different fields
    of an open `Probe` diagnostic using this method. The `field` argument is the same as in `Probe(...)` above.

---

## Open a ParticleBinning diagnostic[¶](#open-a-particlebinning-diagnostic "Link to this heading")

ParticleBinning(*diagNumber=None*, *timesteps=None*, *subset=None*, *average=None*, *units=['']*, *data\_log=False*, *data\_transform=None*, *\*\*kwargs*)[¶](#ParticleBinning "Link to this definition")
:   - `timesteps` (or `timestep_indices`), `units`, `data_log`, `data_transform`, `export_dir`: same as before.
    - `diagNumber`: number or `name` of the particle binning diagnostic (starts at 0).
      :   If not given, a list of available diagnostics is printed.

          It can also be an operation between several diagnostics.

          For example, `"#0/#1"` computes the division by diagnostics 0 and 1.
    - `subset` is similar to that of [`Field()`](#Field "Field"), although the axis must be one of
      :   `"x"`, `"y"`, `"z"`, `"px"`, `"py"`, `"pz"`, `"p"`, `"gamma"`, `"ekin"`, `"vx"`, `"vy"`, `"vz"`, `"v"` or `"charge"`.

          **WARNING:** With the syntax `subset={axis:[start, stop, step]}`, the value of `step`
          is a number of bins.
    - `average`: a selection of coordinates on which to average the data.
      :   Syntax 1: `average = { axis : "all", ... }`

          Syntax 2: `average = { axis : location, ... }`

          Syntax 3: `average = { axis : [begin, end] , ... }`

          `axis` must be `"x"`, `"y"`, `"z"`, `"px"`, `"py"`, `"pz"`, `"p"`, `"gamma"`, `"ekin"`, `"vx"`, `"vy"`, `"vz"`, `"v"` or `"charge"`.

          The chosen axes will be removed:

          - With syntax 1, an average is performed over all the axis.

          - With syntax 2, only the bin closest to `location` is kept.

          - With syntax 3, an average is performed between `begin` and `end`.

          Example: `average={"x":[4,5]}` will average all the data for x within [4,5].
    - See also [Other arguments for diagnostics](#otherkwargs)

**Example**:

```
S = happi.Open("path/to/my/results")
Diag = S.ParticleBinning(1)
```

**Units of the results:**

> [Details on the units from this diagnostic’s output](binning_units.html).

---

## Open a Screen diagnostic[¶](#open-a-screen-diagnostic "Link to this heading")
