## ParticleBinning diagnostics[¶](#particlebinning-diagnostics)

A particle binning diagnostic collects data from the macro-particles and processes them during runtime.
It does not provide information on individual particles: instead, it produces
averaged quantities like the particle density, currents, etc.
The raw data and how it is post-processed by happi is described [here](binning_units.html).

The data is discretized inside a “grid” chosen by the user. This grid may be of any dimension.

Examples:

-

1-dimensional grid along the position \(x\) (gives density variation along \(x\))

-

2-dimensional grid along positions \(x\) and \(y\) (gives density map)

-

1-dimensional grid along the velocity \(v_x\) (gives the velocity distribution)

-

2-dimensional grid along position \(x\) and momentum \(p_x\) (gives the phase-space)

-

1-dimensional grid along the kinetic energy \(E_\mathrm{kin}\) (gives the energy distribution)

-

3-dimensional grid along \(x\), \(y\) and \(E_\mathrm{kin}\) (gives the density map for several energies)

-

1-dimensional grid along the charge \(Z^\star\) (gives the charge distribution)

-

0-dimensional grid (simply gives the total integrated particle density)

Each dimension of the grid is called “axis”.

You can add a particle binning diagnostic by including a block `DiagParticleBinning()` in the namelist,
for instance:

```
DiagParticleBinning(
#name = "my binning",
deposited_quantity = "weight",
every = 5,
time_average = 1,
species = ["electrons1", "electrons2"],
axes = [
["x", 0., 10, 100],
["ekin", 0.1, 100, 1000, "logscale", "edge_inclusive"]
]
)

```

name[¶](#id81)

Optional name of the diagnostic. Used only for post-processing purposes.

deposited_quantity[¶](#deposited_quantity)

The type of data that is summed in each cell of the grid.
Consider reading [this](../Understand/units.html#weights) to understand the meaning of the `weight`.

-

`"weight"` results in a number density.

-

`"weight_charge"` results in a charge density.

-

`"weight_charge_vx"` results in the \(j_x\) current density (same with \(y\) and \(z\)).

-

`"weight_p"` results in the momentum density (same with \(p_x\), \(p_y\) and \(p_z\)).

-

`"weight_ekin"` results in the energy density.

-

`"weight_vx_px"` results in the `xx` pressure (same with yy, zz, xy, yz and xz).

-

`"weight_chi"` results in the quantum parameter density (only for species with radiation losses).

-

with a user-defined python function, an arbitrary quantity can be calculated (the numpy
module is necessary). This function should take one argument, for instance
`particles`, which contains the attributes `x`, `y`, `z`, `px`, `py`,
`pz`, `charge`, `weight`, `chi` and `id` (additionally, it may also have the
attributes `Ex`, `Bx`, `Ey`, and so on, depending on [`keep_interpolated_fields`](#keep_interpolated_fields)).
Each of these attributes is a numpy array
containing the data of all particles in one patch. The function must return a numpy
array of the same shape, containing the desired deposition of each particle. For example,
defining the following function:

```
def stuff(particles):
return particles.weight * particles.px

```

passed as `deposited_quantity=stuff`, the diagnostic will sum the weights
\(\times\; p_x\).

You may also pass directly an implicit (lambda) function using:

```
deposited_quantity = lambda p: p.weight * p.px

```

every[¶](#id82)

The number of time-steps between each output, or a [time selection](#timeselections).

flush_every[¶](#id83)

Default:

1

Number of timesteps or a [time selection](#timeselections).

When `flush_every` coincides with `every`, the output
file is actually written (“flushed” from the buffer). Flushing
too often can dramatically slow down the simulation.

time_average[¶](#id84)

Default:

1

The number of time-steps during which the data is averaged. The data is averaged over time_average consecutive iterations after the selected time.

species[¶](#id85)

A list of one or several species’ [`name`](#id93).
All these species are combined into the same diagnostic.

axes[¶](#axes)

A list of axes that define the grid.
There may be as many axes as wanted (there may be zero axes).

Syntax of one axis: `[type, min, max, nsteps, "logscale", "edge_inclusive"]`

-

`type` is one of:

-

`"x"`, `"y"`, `"z"`: spatial coordinates (`"moving_x"` with a [moving window](#movingwindow))

-

`"px"`, `"py"`, `"pz"`, `"p"`: momenta

-

`"vx"`, `"vy"`, `"vz"`, `"v"`: velocities

-

`"gamma"`, `"ekin"`: energies

-

`"chi"`: quantum parameter

-

`"charge"`: the particles’ electric charge

-

or a python function with the same syntax as the `deposited_quantity`.
Namely, this function must accept one argument only, for instance `particles`,
which holds the attributes `x`, `y`, `z`, `px`, `py`, `pz`, `charge`,
`weight` and `id`. Each of these attributes is a numpy array containing the
data of all particles in one patch. The function must return a numpy array of
the same shape, containing the desired quantity of each particle that will decide
its location in the histogram binning.

-

The axis is discretized for `type` from `min` to `max` in `nsteps` bins.

-

The `min` and `max` may be set to `"auto"` so that they are automatically
computed from all the particles in the simulation. This option can be bad for performances.

-

The optional keyword `logscale` sets the axis scale to logarithmic instead of linear
(bins become uneven).

-

The optional keyword `edge_inclusive` includes the particles outside the range
[`min`, `max`] into the extrema bins.

Examples of particle binning diagnostics

-

Variation of the density of species `electron1`
from \(x=0\) to 1, every 5 time-steps, without time-averaging

```
DiagParticleBinning(
deposited_quantity = "weight",
every = 5,
time_average = 1,
species = ["electron1"],
axes = [ ["x",    0.,    1.,    30] ]
)

```

-

Density map from \(x=0\) to 1, \(y=0\) to 1

```
DiagParticleBinning(
deposited_quantity = "weight",
every = 5,
time_average = 1,
species = ["electron1"],
axes = [ ["x",    0.,    1.,    30],
["y",    0.,    1.,    30] ]
)

```

-

Velocity distribution from \(v_x = -0.1\) to \(0.1\)

```
DiagParticleBinning(
deposited_quantity = "weight",
every = 5,
time_average = 1,
species = ["electron1"],
axes = [ ["vx",   -0.1,    0.1,    100] ]
)

```

-

Phase space from \(x=0\) to 1 and from \(px=-1\) to 1

```
DiagParticleBinning(
deposited_quantity = "weight",
every = 5,
time_average = 1,
species = ["electron1"],
axes = [ ["x",    0.,    1.,    30],
["px",   -1.,   1.,    100] ]
)

```

-

Energy distribution from 0.01 to 1 MeV in logarithmic scale.
Note that the input units are \(m_ec^2 \sim 0.5\) MeV

```
DiagParticleBinning(
deposited_quantity = "weight",
every = 5,
time_average = 1,
species = ["electron1"],
axes = [ ["ekin",    0.02,    2.,   100, "logscale"] ]
)

```

-

\(x\)-\(y\) density maps for three bands of energy: \([0,1]\), \([1,2]\), \([2,\infty]\).
Note the use of `edge_inclusive` to reach energies up to \(\infty\)

```
DiagParticleBinning(
deposited_quantity = "weight",
every = 5,
time_average = 1,
species = ["electron1"],
axes = [ ["x",    0.,    1.,    30],
["y",    0.,    1.,    30],
["ekin", 0.,    6.,    3,  "edge_inclusive"] ]
)

```

-

Charge distribution from \(Z^\star =0\) to 10

```
DiagParticleBinning(
deposited_quantity = "weight",
every = 5,
time_average = 1,
species = ["electron1"],
axes = [ ["charge",    -0.5,   10.5,   11] ]
)

```
