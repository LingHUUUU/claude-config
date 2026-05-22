## Screen diagnostics[¶](#screen-diagnostics)

A screen collects data from the macro-particles when they cross a surface.
It processes this data similarly to the [particle binning diagnostics](#diagparticlebinning)
as it makes a histogram of the macro-particle properties. There are two differences:

-

the histogram is made only by the particles that cross the surface

-

the data is accumulated for all timesteps.

You can add a screen by including a block `DiagScreen()` in the namelist,
for instance:

```
DiagScreen(
#name = "my screen",
shape = "plane",
point = [5., 10.],
vector = [1., 0.],
direction = "canceling",
deposited_quantity = "weight",
species = ["electron"],
axes = [["a", -10.*l0, 10.*l0, 40],
["px", 0., 3., 30]],
every = 10
)

```

name[¶](#id86)

Optional name of the diagnostic. Used only for post-processing purposes.

shape[¶](#shape)

The shape of the screen surface: `"plane"`, `"sphere"`, or `"cylinder"`.

point[¶](#point)

Type:

A list of floats `[X]` in 1D,  `[X,Y]` in 2D,  `[X,Y,Z]` in 3D

The coordinates of a point that defines the screen surface:
a point of the `"plane"`, the center of the `"sphere"`,
or a point on the `"cylinder"` axis.

vector[¶](#vector)

Type:

A list of floats `[X]` in 1D,  `[X,Y]` in 2D,  `[X,Y,Z]` in 3D

The coordinates of a vector that defines the screen surface:
the normal to the `"plane"`, a radius of the `"sphere"`.
or the axis of the `"cylinder"` (in the latter case, the vector
norm defines the cylinder radius).

direction[¶](#id87)

Default:

`"both"`

Determines how particles are counted depending on which side of the screen they come from.

-

`"both"` to account for both sides.

-

`"forward"` for only the ones in the direction of the `vector`.

-

`"backward"` for only the ones in the opposite direction.

-

`"canceling"` to count negatively the ones in the opposite direction.

deposited_quantity[¶](#id88)

Identical to the `deposited_quantity` of [particle binning diagnostics](#diagparticlebinning).

every[¶](#id89)

The number of time-steps between each output, or a [time selection](#timeselections).

flush_every[¶](#id90)

Default:

1

Number of timesteps or a [time selection](#timeselections).

When `flush_every` coincides with `every`, the output
file is actually written (“flushed” from the buffer). Flushing
too often can dramatically slow down the simulation.

species[¶](#id91)

A list of one or several species’ [`name`](#id93).
All these species are combined into the same diagnostic.

axes[¶](#id92)

A list of “axes” that define the grid of the histogram.
It is identical to that of [particle binning diagnostics](#diagparticlebinning), with the
addition of four types of axes:

-

If `shape="plane"`, then `"a"` and `"b"` are the axes perpendicular to the `vector`.

-

If `shape="sphere"`, then `"theta"` and `"phi"` are the angles with respect to the `vector`.

-

If `shape="cylinder"`, then `"a"` is along the cylinder axis and `"phi"` is the angle around it.

## RadiationSpectrum diagnostics[¶](#radiationspectrum-diagnostics)

A radiation spectrum diagnostic computes (at a given time) the instantaneous
power spectrum following from the incoherent emission of high-energy
photons by accelerated charge (see [High-energy photon emission & radiation reaction](../Understand/radiation_loss.html) for more details
on the emission process and its implementation in Smilei).

It is similar to the [particle binning diagnostics](#diagparticlebinning),
with an extra axis of binning: the emitted photon energy.
The other axes remain available to the user.

A radiation spectrum diagnostic is defined by a block `RadiationSpectrum()`:

```
DiagRadiationSpectrum(
#name = "my radiation spectrum",
every = 5,
flush_every = 1,
time_average = 1,
species = ["electrons1", "electrons2"],
photon_energy_axis = [0., 1000., 100, 'logscale'],
axes = []
)

```

name[¶](#id93)

Optional name of the diagnostic. Used only for post-processing purposes.

every[¶](#id94)

The number of time-steps between each output, or a [time selection](#timeselections).

flush_every[¶](#id95)

Default:

1

Number of timesteps or a [time selection](#timeselections).

When `flush_every` coincides with `every`, the output
file is actually written (“flushed” from the buffer). Flushing
too often can dramatically slow down the simulation.

time_average[¶](#id96)

Default:

1

The number of time-steps during which the data is averaged before output.

species[¶](#id97)

A list of one or several species’ [`name`](#id93) that emit the radiation.
All these species are combined into the same diagnostic.

photon_energy_axis[¶](#photon_energy_axis)

The axis of photon energies (in units of \(m_e c^2\)).
The syntax is similar to that of
[particle binning diagnostics](#diagparticlebinning).

Syntax: `[min, max, nsteps, "logscale"]`

axes[¶](#id98)

An additional list of “axes” that define the grid.
There may be as many axes as wanted (there may be zero axes).
Their syntax is the same that for “axes” of a
[particle binning diagnostics](#diagparticlebinning).

Examples of radiation spectrum diagnostics

-

Time-integrated over the full duration of the simulation:

```
DiagRadiationSpectrum(
every = Nt,
time_average = Nt,
species = ["electrons"],
photon_energy_axis = [0., 1000., 100, 'logscale'],
axes = []
)

```

-

Angularly-resolved instantaneous radiation spectrum.
The diagnostic considers that all electrons emit radiation in
the direction of their velocity:

```
from numpy import arctan2, pi

def angle(p):
return arctan2(p.py,p.px)

DiagRadiationSpectrum(
every = 10,
species = ["electrons"],
photon_energy_axis = [0., 1000., 100, 'logscale'],
axes = [
[angle,-pi,pi,90]
]
)

```
