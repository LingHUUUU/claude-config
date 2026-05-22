## Probe diagnostics[¶](#probe-diagnostics)

The fields from the previous section are taken at the PIC grid locations,
but it is also possible to obtain the fields at arbitrary locations.
These are called probes.

A probe interpolates the fields at either one point (0-D),
several points arranged in a line (1-D),
or several points arranged in a 2-D or 3-D grid.

Note

-

Probes follow the moving window.
To obtain the fields at fixed points in the plasma instead, create a cold,
chargeless species, and [track the particles](#diagtrackparticles).

-

In “AMcylindrical” geometry, probes are defined with 3D Cartesian coordinates
and cannot be separated per mode. Use Field diagnostics for cylindrical coordinates and
information per mode.

-

Probes rely on the particle interpolator to compute fields so that the
magnetic field is shifted by half a timestep compared to that of Fields diagnostics.

To add one probe diagnostic, include the block `DiagProbe`:

```
DiagProbe(
#name = "my_probe",
every    = 10,
origin   = [1., 1.],
corners  = [
[1.,10.],
[10.,1.],
],
number   = [100, 100],
fields   = ["Ex", "Ey", "Ez"]
)

```

name[¶](#id76)

Optional name of the diagnostic. Used only for post-processing purposes.

every[¶](#id77)

Number of timesteps between each output or a [time selection](#timeselections).

flush_every[¶](#id78)

Default:

1

Number of timesteps or a [time selection](#timeselections).

When `flush_every` coincides with `every`, the output
file is actually written (“flushed” from the buffer). Flushing
too often can dramatically slow down the simulation.

origin[¶](#origin)

Type:

A list of floats, of length equal to the simulation dimensionality.

The coordinates of the origin of the probe grid

corners[¶](#corners)

vectors[¶](#vectors)

Type:

A list of lists of floats.

Defines the corners of the probe grid.
Each corner is a list of coordinates (as many as the simulation dimensions).

When using `corners`, the absolute coordinates of each corner must be specified.
When using `vectors`, the coordinates relative to [`origin`](#origin) must be specified.

number[¶](#number)

Type:

A list of integers, one for each dimension of the probe.

The number of points in each probe axis. Must not be defined for a 0-D probe.

fields[¶](#id79)

Default:

`[]`, which means `["Ex", "Ey", "Ez", "Bx", "By", "Bz", "Jx", "Jy", "Jz", "Rho"]`

A list of fields among:

-

the electric field components `"Ex"`, `"Ey"`, `"Ez"`

-

the magnetic field components `"Bx"`, `"By"`, `"Bz"`

-

the Poynting vector components `"PoyX"`, `"PoyY"`, `"PoyZ"`

-

the current density components `"Jx"`, `"Jy"`, `"Jz"` and charge density `"Rho"`

-

the current density `"Jx_abc"`, `"Jy_abc"`, `"Jz_abc"` and charge density `"Rho_abc"`
of a given species named `"abc"`

In the case of an envelope model for the laser (see [Laser envelope model](../Understand/laser_envelope.html)),
the following fields are also available: `"Env_Chi"`, `"Env_A_abs"`, `"Env_E_abs"`, `"Env_Ex_abs"`.
They are respectively the susceptibility, the envelope of the laser transverse vector potential,
the envelope of the laser transverse electric field and the envelope of the laser longitudinal
electric field.

If the B-TIS3 interpolation scheme is activated (see [PIC algorithms](../Understand/algorithms.html)),
the following fields are also available: `"ByBTIS3"`, `"BzBTIS3"`.

time_integral[¶](#time_integral)

Default:

`False`

If `True`, the output is integrated over time. As this option forces field interpolation
at every timestep, it is recommended to use few probe points.

datatype[¶](#id80)

Default:

`"double"`

The data type when written to the HDF5 file. Accepts `"double"` (8 bytes) or `"float"` (4 bytes).

Examples of probe diagnostics

-

0-D probe in 1-D simulation

```
DiagProbe(
every = 1,
origin = [1.2]
)

```

-

1-D probe in 1-D simulation

```
DiagProbe(
every = 1,
origin  = [1.2],
corners = [[5.6]],
number  = [100]
)

```

-

1-D probe in 2-D simulation

```
DiagProbe(
every = 1,
origin  = [1.2, 4.],
corners = [[5.6, 4.]],
number  = [100]
)

```

-

2-D probe in 2-D simulation

```
DiagProbe(
every = 1,
origin   = [0., 0.],
corners  = [ [10.,0.], [0.,10.] ],
number   = [100, 100]
)

```
