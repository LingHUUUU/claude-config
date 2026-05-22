## Open a Scalar diagnostic[¶](#open-a-scalar-diagnostic "Link to this heading")

Scalar(_scalar\=None_, _timesteps\=None_, _units\=\[''\]_, _data\_log\=False_, _data\_transform\=None_, _\*\*kwargs_)[¶](#Scalar "Link to this definition")

* `scalar`: The name of the scalar, or an operation on scalars, such as `"Uelm+Ukin"`.
* `timesteps` or `timestep_indices`: The requested range of timesteps.  
>   * If omitted, all timesteps are used.  
>   * If one number given, the nearest timestep available is used.  
>   * If two numbers given, all the timesteps in between are used.  
>  
> When using `timesteps`, provide the timesteps themselves, but when using `timestep_indices`, provide their indices in the list of the available timesteps.
* `units`: A unit specification (see [Specifying units](#units))
* `data_log`:  
If `True`, then \\(\\log\_{10}\\) is applied to the output.
* `data_transform`:  
If this is set to a function, the function is applied to the output before plotting.
* See also [Other arguments for diagnostics](#otherkwargs)

**Example**:

S = happi.Open("path/to/my/results")
Diag = S.Scalar("Utot")

---

## Open a Field diagnostic[¶](#open-a-field-diagnostic "Link to this heading")

Field(_diagNumber\=None_, _field\=None_, _timesteps\=None_, _subset\=None_, _average\=None_, _units\=\[''\]_, _data\_log\=False_, _data\_transform\=None_, _moving\=False_, _export\_dir\=None_, _\*\*kwargs_)[¶](#Field "Link to this definition")

* `timesteps` (or `timestep_indices`), `units`, `data_log`, `data_transform`: same as before.
* `diagNumber`: number or `name` of the fields diagnostic  
If not given, then a list of available diagnostic numbers is printed.
* `field`: The name of a field (`"Ex"`, `"Ey"`, etc.)  
If not given, then a list of available fields is printed.  
The string can also be an operation between several fields, such as `"Jx+Jy"`.
* `subset`: A selection of coordinates to be extracted.  
Syntax 1: `subset = { axis : location, ... }`  
Syntax 2: `subset = { axis : [start, stop] , ... }`  
Syntax 3: `subset = { axis : [start, stop, step] , ... }`  
`axis` must be `"x"`, `"y"` , `"z"` or `"r"`.  
Only the data within the chosen axes’ selections is extracted.  
**WARNING:** THE VALUE OF `step` IS A NUMBER OF CELLS.  
Example: `subset = {"y":[10, 80, 4]}`
* `average`: A selection of coordinates on which to average.  
Syntax 1: `average = { axis : "all", ... }`  
Syntax 2: `average = { axis : location, ... }`  
Syntax 3: `average = { axis : [start, stop] , ... }`  
`axis` must be `"x"`, `"y"` , `"z"` or `"r"`.  
The chosen axes will be removed:  
\- With syntax 1, an average is performed over all the axis.  
\- With syntax 2, only the bin closest to `location` is kept.  
\- With syntax 3, an average is performed from `start` to `stop`.  
Example: `average = {"x":[4,5]}` will average for \\(x\\) within \[4,5\].
* `moving`: If `True`, plots will display the X coordinates evolving according to the[moving window](namelist.html#movingwindow)
* `export_dir`: The directory where to export VTK files.
* See also [Other arguments for diagnostics](#otherkwargs)

In the case of an azimuthal mode cylindrical geometry (`AMcylindrical`), additional argument are available. You must choose one of `theta` or `build3d`, defined below, in order to construct fields from their complex angular Fourier modes. In addition, the `modes`argument is optional.

* `theta`: An angle (in radians)  
Calculates the field in a plane passing through the \\(r=0\\) axis  
and making an angle `theta` with the \\(xy\\) plane.
* `build3d`: A list of three _ranges_  
Calculates the field interpolated in a 3D \\(xyz\\) grid.  
Each _range_ is a list `[start, stop, step]` indicating the beginning,  
the end and the step of this grid.
* `modes`: An integer or a list of integers  
Only these modes numbers will be used in the calculation. If omited, all modes are used.

**Example**:

S = happi.Open("path/to/my/results")
Diag = S.Field(0, "Ex", average = {"x":[4,5]}, theta=math.pi/4.)

---

## Open a Probe diagnostic[¶](#open-a-probe-diagnostic "Link to this heading")

Probe(_probeNumber\=None_, _field\=None_, _timesteps\=None_, _subset\=None_, _average\=None_, _units\=\[''\]_, _data\_log\=False_, _data\_transform\=None_, _\*\*kwargs_)[¶](#Probe "Link to this definition")

* `timesteps` (or `timestep_indices`), `units`, `data_log`, `data_transform`, `export_dir`: same as before.
* `probeNumber`: number or `name` of the probe (the first one has number 0).  
If not given, a list of available probes is printed.
* `field`: name of the field (`"Bx"`, `"By"`, `"Bz"`, `"Ex"`, `"Ey"`, `"Ez"`, `"Jx"`, `"Jy"`, `"Jz"` or `"Rho"`).  
If not given, a list of available fields is printed.  
The string can also be an operation between several fields, such as `"Jx+Jy"`.
* `subset` and `average` are very similar to those of[Field()](#Field "Field"), but they can only have the axes: `"axis1"`, `"axis2"` and `"axis3"`. For instance, `average={"axis1":"all"}`. Note that the axes are not necessarily equal to \\(x\\), \\(y\\) or \\(z\\) because the probe mesh is arbitrary.  
**WARNING:** UNLIKE [Field()](#Field "Field"), THE LOCATIONS ARE RELATIVE TO THE PROBE’S [origin](namelist.html#origin "origin"), NOT TO THE OVERALL ORIGIN.
* See also [Other arguments for diagnostics](#otherkwargs)

**Example**:

S = happi.Open("path/to/my/results")
Diag = S.Probe(0, "Ex")

Probe.changeField(_field_)[¶](#Probe.changeField "Link to this definition")

In cases where happi’s performance is an issue, it is possible to switch between different fields of an open `Probe` diagnostic using this method. The `field` argument is the same as in `Probe(...)` above.

---

## Open a ParticleBinning diagnostic[¶](#open-a-particlebinning-diagnostic "Link to this heading")

ParticleBinning(_diagNumber\=None_, _timesteps\=None_, _subset\=None_, _average\=None_, _units\=\[''\]_, _data\_log\=False_, _data\_transform\=None_, _\*\*kwargs_)[¶](#ParticleBinning "Link to this definition")

* `timesteps` (or `timestep_indices`), `units`, `data_log`, `data_transform`, `export_dir`: same as before.
* `diagNumber`: number or `name` of the particle binning diagnostic (starts at 0).  
If not given, a list of available diagnostics is printed.  
It can also be an operation between several diagnostics.  
For example, `"#0/#1"` computes the division by diagnostics 0 and 1.
* `subset` is similar to that of [Field()](#Field "Field"), although the axis must be one of  
`"x"`, `"y"`, `"z"`, `"px"`, `"py"`, `"pz"`, `"p"`, `"gamma"`, `"ekin"`, `"vx"`, `"vy"`, `"vz"`, `"v"` or `"charge"`.  
**WARNING:** With the syntax `subset={axis:[start, stop, step]}`, the value of `step`is a number of bins.
* `average`: a selection of coordinates on which to average the data.  
Syntax 1: `average = { axis : "all", ... }`  
Syntax 2: `average = { axis : location, ... }`  
Syntax 3: `average = { axis : [begin, end] , ... }`  
`axis` must be `"x"`, `"y"`, `"z"`, `"px"`, `"py"`, `"pz"`, `"p"`, `"gamma"`, `"ekin"`, `"vx"`, `"vy"`, `"vz"`, `"v"` or `"charge"`.  
The chosen axes will be removed:  
\- With syntax 1, an average is performed over all the axis.  
\- With syntax 2, only the bin closest to `location` is kept.  
\- With syntax 3, an average is performed between `begin` and `end`.  
Example: `average={"x":[4,5]}` will average all the data for x within \[4,5\].
* See also [Other arguments for diagnostics](#otherkwargs)

**Example**:

S = happi.Open("path/to/my/results")
Diag = S.ParticleBinning(1)

**Units of the results:**

> [Details on the units from this diagnostic’s output](binning%5Funits.html).

---

## Open a Screen diagnostic[¶](#open-a-screen-diagnostic "Link to this heading")

Screen(_diagNumber\=None_, _timesteps\=None_, _subset\=None_, _average\=None_, _units\=\[''\]_, _data\_log\=False_, _data\_transform\=None_, _\*\*kwargs_)[¶](#Screen "Link to this definition")

* `timesteps` (or `timestep_indices`), `units`, `data_log`, `data_transform`, `export_dir`: same as before.
* `diagNumber`, `subset` and `average`: identical to that of ParticleBinning diagnostics.
* See also [Other arguments for diagnostics](#otherkwargs)

**Example**:

S = happi.Open("path/to/my/results")
Diag = S.Screen(0)

---

## Open a RadiationSpectrum diagnostic[¶](#open-a-radiationspectrum-diagnostic "Link to this heading")

RadiationSpectrum(_diagNumber\=None_, _timesteps\=None_, _subset\=None_, _average\=None_, _units\=\[''\]_, _data\_log\=False_, _data\_transform\=None_, _\*\*kwargs_)[¶](#RadiationSpectrum "Link to this definition")

* `timesteps` (or `timestep_indices`), `units`, `data_log`, `data_transform`, `export_dir`: same as before.
* `diagNumber`, `subset` and `average`: identical to that of ParticleBinning diagnostics.
* See also [Other arguments for diagnostics](#otherkwargs)

**Example**:

S = happi.Open("path/to/my/results")
Diag = S.RadiationSpectrum(0)

Note

The resulting spectral power is in units of \\(\\omega\_r\\). If additional axes are used, the power spectrum is divided by the size of the bins of each axes.

---

## Open a TrackParticles diagnostic[¶](#open-a-trackparticles-diagnostic "Link to this heading")

TrackParticles(_species\=None_, _select\=''_, _axes\=\[\]_, _timesteps\=None_, _sort\=True_, _length\=None_, _units\=\[''\]_, _\*\*kwargs_)[¶](#TrackParticles "Link to this definition")

* `timesteps` (or `timestep_indices`), `units`, `export_dir`: same as before.
* `species`: the name of a tracked-particle species. If omitted, a list of available tracked-particle species is printed.
* `select`: Instructions for selecting particles among those available. A detailed explanation is provided below
* `axes`: A list of axes for plotting the trajectories or obtaining particle data.  
Each axis is one of the [attributes](namelist.html#attributes "attributes") defined in the namelist. In addition, when there is a moving window, the axis `"moving_x"` is automatically available.  
**Example:** `axes = ["x"]` corresponds to \\(x\\) versus time.  
**Example:** `axes = ["x","y"]` correspond to 2-D trajectories.  
**Example:** `axes = ["x","px"]` correspond to phase-space trajectories.
* `sort`: may be either  
   * `False`: the particles are not sorted by ID. This can save significant time, but prevents plotting, exporting to VTK, and the `select` argument. Only`getData` and `iterParticles` are available in this mode. Read [this](ids.html) for more information on particle IDs.  
   * `True`: the particles are sorted in a new file, unless this file already exists. If it does, sorted particles are directly read from the sorted file.  
   * A string for selecting particles (same syntax as `select`): only selected particles are sorted in a new file. The file name must be defined in the argument `sorted_as`. If `timesteps` is used, only selected timesteps will be included in the created file.
* `sorted_as`: a keyword that defines the new sorted file name (when `sort` is a selection) or refers to a previously user-defined sorted file name (when `sort` is not given).
* `length`: The length of each plotted trajectory, in number of timesteps.
* See also [Other arguments for diagnostics](#otherkwargs)

**Example**:

S = happi.Open("path/to/my/results")
Diag = S.TrackParticles("electrons", axes=["px","py"])

Detailed explanation of the `select` parameter

Say `times` is a condition on timesteps `t`, for instance `t>50`.

Say `condition` is a condition on particles properties (`x`, `y`, `z`, `px`, `py`, `pz`), for instance `px>0`.

* **Syntax 1:** `select="any(times, condition)"`  
Selects particles satisfying `condition` for at least one of the `times`.  
For example, `select="any(t>0, px>1.)"` selects those reaching \\(p\_x>1\\) at some point.
* **Syntax 2:** `select="all(times, condition)"`  
Selects particles satisfying `condition` at all `times`.  
For example, `select="all(t<40, px<1)"` selects those having \\(p\_x<1\\) until timestep 40.
* **Syntax 3:** `select=[ID1, ID2, ...]`  
Selects the provided particle IDs.
* It is possible to make logical operations: `+` is _OR_; `*` is _AND_; `~` is _NOT_.  
For example, `select="any((t>30)*(t<60), px>1) + all(t>0, (x>1)*(x<2))"`

---

## Open a NewParticles diagnostic[¶](#open-a-newparticles-diagnostic "Link to this heading")

NewParticles(_species\=None_, _select\=''_, _axes\=\[\]_, _units\=\[''\]_, _\*\*kwargs_)[¶](#NewParticles "Link to this definition")

* `units`: same as before.
* `species`: same as for `TrackParticles`
* `axes`: same as for `TrackParticles`, with the addition of another axis `t`that represents the time when the particle was born.
* `select`: Instructions for selecting particles among those available. It must be a condition on particles properties `axes`, for instance `px>0`. It is possible to make logical operations: `+` is _OR_; `*` is _AND_; `~` is _NOT_.  
**Example:** `select="(x>1)*(x<2)"`  
It is also possible to select directly a list of IDs.  
**Example:** `select=[ID1, ID2, ...]`

---

## Open a Performances diagnostic[¶](#open-a-performances-diagnostic "Link to this heading")

The post-processing of the _performances_ diagnostic may be achieved in three different modes: `raw`, `map`, or `histogram`, described further below. You must choose one and only one mode between those three.

Performances(_raw\=None_, _map\=None_, _histogram\=None_, _timesteps\=None_, _units\=\[''\]_, _data\_log\=False_, _data\_transform\=None_, _species\=None_, _cumulative\=True_, _\*\*kwargs_)[¶](#Performances "Link to this definition")

* `timesteps`, `units`, `data_log`, `data_transform`, `export_dir`: same as before.
* `raw`: The name of a quantity, or an operation between them (see quantities below). The requested quantity is listed for each process.
* `map`: The name of a quantity, or an operation between them (see quantities below). The requested quantity is mapped vs. space coordinates (1D and 2D only).
* `histogram`: the list `["quantity", min, max, nsteps]`. Makes a histogram of the requested quantity between `min` an `max`, with `nsteps` bins. The `"quantity"` may be an operation between the quantities listed further below.
* `cumulative`: may be `True` for timers accumulated for the duration of the simulation, or `False` for timers reset to 0 at each output.
* See also [Other arguments for diagnostics](#otherkwargs)

**Quantities at the MPI-process level** (contain many patches):

> * `hindex` : the starting index of each proc in the hilbert curve
> * `number_of_cells` : the number of cells in each proc
> * `number_of_particles` : the total number of non-frozen macro-particles in each proc (includes all species)
> * `number_of_frozen_particles` : the number of frozen particles in each proc
> * `total_load` : the load of each proc (number of macro-particles and cells weighted by cell\_load coefficients)
> * `timer_global` : global simulation time (only available for proc 0)
> * `timer_particles` : time spent computing particles by each proc
> * `timer_maxwell` : time spent solving maxwell by each proc
> * `timer_envelope` : time spent solving the envelope propagation by each proc
> * `timer_densities` : time spent projecting densities by each proc
> * `timer_collisions` : time spent computing collisions by each proc
> * `timer_movWindow` : time spent handling the moving window by each proc
> * `timer_loadBal` : time spent balancing the load by each proc
> * `timer_partMerging` : time spent merging particles by each proc
> * `timer_syncPart` : time spent synchronzing particles by each proc
> * `timer_syncField` : time spent synchronzing fields by each proc
> * `timer_syncDens` : time spent synchronzing densities by each proc
> * `timer_syncSusceptibility` : time spent synchronzing susceptibility by each proc
> * `timer_diags` : time spent by each proc calculating and writing diagnostics
> * `timer_total` : the sum of all timers above (except timer\_global)
> * `memory_total` : the total memory (RSS) used by the process in GB
> * `memory_peak` : the peak memory (peak RSS) used by the process in GB
> 
> **WARNING**: The timers `loadBal` and `diags` include _global_ communications. This means they might contain time doing nothing, waiting for other processes. The `sync***` timers contain _proc-to-proc_ communications, which also represents some waiting time.

**Quantities at the patch level**:

> This requires [patch\_information](namelist.html#patch%5Finformation "patch_information") in the namelist.
> 
> * `mpi_rank` : the MPI rank that contains the current patch
> * `vecto` : the mode of the specified species in the current patch (vectorized of scalar) when the adaptive mode is activated. Here the `species` argument has to be specified.
> 
> **WARNING**: The patch quantities are only compatible with the `raw` mode and only in `3Dcartesian` [geometry](namelist.html#geometry "geometry"). The result is a patch matrix with the quantity on each patch.

**Example**: performance diagnostic at the MPI level:

S = happi.Open("path/to/my/results")
Diag = S.Performances(map="total_load")

**Example**: performance diagnostic at the patch level:

S = happi.Open("path/to/my/results")
Diag = S.Performances(raw="vecto", species="electron")

---

## Specifying units[¶](#specifying-units "Link to this heading")

By default, all the diagnostics data is in code units (see [Units](../Understand/units.html)).

To change the units, all the methods [Scalar()](#Scalar "Scalar"),[Field()](#Field "Field"), [Probe()](#Probe "Probe"),[ParticleBinning()](#ParticleBinning "ParticleBinning") and[TrackParticles()](#TrackParticles "TrackParticles") support a `units` argument. It has three different syntaxes:

1. **A list**, for example `units = ["um/ns", "feet", "W/cm^2"]`  
In this case, any quantity found to be of the same dimension as one of these units will be converted.
2. **A dictionary**, for example `units = {"x":"um", "y":"um", "v":"Joule"}`  
In this case, we specify the units separately for axes `x` and `y`, and for the data values `v`.
3. **A** `Units` **object**, for example `units = happi.Units("um/ns", "feet", x="um")`  
This version combines the two previous ones.

Requirements for changing units

* The [Pint module](https://pypi.python.org/pypi/Pint/).
* To obtain units in a non-normalized system (e.g. SI), the simulation must have the parameter [reference\_angular\_frequency\_SI](namelist.html#reference%5Fangular%5Ffrequency%5FSI "reference_angular_frequency_SI") set to a finite value. Otherwise, this parameter can be set during post-processing as an argument to the[happi.Open()](#happi.Open "happi.Open") function.

---
