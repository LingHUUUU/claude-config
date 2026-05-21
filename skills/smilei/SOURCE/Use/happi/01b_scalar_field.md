## Open a Scalar diagnostic[¶](#open-a-scalar-diagnostic "Link to this heading")

Scalar(*scalar=None*, *timesteps=None*, *units=['']*, *data\_log=False*, *data\_transform=None*, *\*\*kwargs*)[¶](#Scalar "Link to this definition")
:   - `scalar`: The name of the scalar, or an operation on scalars, such as `"Uelm+Ukin"`.
    - `timesteps` or `timestep_indices`: The requested range of timesteps.

      > - If omitted, all timesteps are used.
      > - If one number given, the nearest timestep available is used.
      > - If two numbers given, all the timesteps in between are used.
      >
      > When using `timesteps`, provide the timesteps themselves, but
      > when using `timestep_indices`, provide their indices in the list
      > of the available timesteps.
    - `units`: A unit specification (see [Specifying units](#units))
    - `data_log`:
      :   If `True`, then \(\log\_{10}\) is applied to the output.
    - `data_transform`:
      :   If this is set to a function, the function is applied to the output before plotting.
    - See also [Other arguments for diagnostics](#otherkwargs)

**Example**:

```
S = happi.Open("path/to/my/results")
Diag = S.Scalar("Utot")
```

---

## Open a Field diagnostic[¶](#open-a-field-diagnostic "Link to this heading")

Field(*diagNumber=None*, *field=None*, *timesteps=None*, *subset=None*, *average=None*, *units=['']*, *data\_log=False*, *data\_transform=None*, *moving=False*, *export\_dir=None*, *\*\*kwargs*)[¶](#Field "Link to this definition")
:   - `timesteps` (or `timestep_indices`), `units`, `data_log`, `data_transform`: same as before.
    - `diagNumber`: number or `name` of the fields diagnostic
      :   If not given, then a list of available diagnostic numbers is printed.
    - `field`: The name of a field (`"Ex"`, `"Ey"`, etc.)
      :   If not given, then a list of available fields is printed.

          The string can also be an operation between several fields, such as `"Jx+Jy"`.
    - `subset`: A selection of coordinates to be extracted.
      :   Syntax 1: `subset = { axis : location, ... }`

          Syntax 2: `subset = { axis : [start, stop] , ... }`

          Syntax 3: `subset = { axis : [start, stop, step] , ... }`

          `axis` must be `"x"`, `"y"` , `"z"` or `"r"`.

          Only the data within the chosen axes’ selections is extracted.

          **WARNING:** THE VALUE OF `step` IS A NUMBER OF CELLS.

          Example: `subset = {"y":[10, 80, 4]}`
    - `average`: A selection of coordinates on which to average.
      :   Syntax 1: `average = { axis : "all", ... }`

          Syntax 2: `average = { axis : location, ... }`

          Syntax 3: `average = { axis : [start, stop] , ... }`

          `axis` must be `"x"`, `"y"` , `"z"` or `"r"`.

          The chosen axes will be removed:

          - With syntax 1, an average is performed over all the axis.

          - With syntax 2, only the bin closest to `location` is kept.

          - With syntax 3, an average is performed from `start` to `stop`.

          Example: `average = {"x":[4,5]}` will average for \(x\) within [4,5].
    - `moving`: If `True`, plots will display the X coordinates evolving according to the
      [moving window](namelist.html#movingwindow)
    - `export_dir`: The directory where to export VTK files.
    - See also [Other arguments for diagnostics](#otherkwargs)

    In the case of an azimuthal mode cylindrical geometry (`AMcylindrical`), additional argument are
    available. You must choose one of `theta` or `build3d`, defined below, in order
    to construct fields from their complex angular Fourier modes. In addition, the `modes`
    argument is optional.

    - `theta`: An angle (in radians)
      :   Calculates the field in a plane passing through the \(r=0\) axis

          and making an angle `theta` with the \(xy\) plane.
    - `build3d`: A list of three *ranges*
      :   Calculates the field interpolated in a 3D \(xyz\) grid.

          Each *range* is a list `[start, stop, step]` indicating the beginning,

          the end and the step of this grid.
    - `modes`: An integer or a list of integers
      :   Only these modes numbers will be used in the calculation. If omited, all modes are used.

**Example**:

```
S = happi.Open("path/to/my/results")
Diag = S.Field(0, "Ex", average = {"x":[4,5]}, theta=math.pi/4.)
```

---

## Open a Probe diagnostic[¶](#open-a-probe-diagnostic "Link to this heading")
