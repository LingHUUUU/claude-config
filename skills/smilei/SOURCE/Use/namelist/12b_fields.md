## Fields diagnostics[¶](#fields-diagnostics)

Smilei can collect various field data (electromagnetic fields, currents and density)
taken at the location of the PIC grid, both as instantaneous values and averaged values.
This is done by including a block `DiagFields`:

```
DiagFields(
#name = "my field diag",
every = 10,
time_average = 2,
fields = ["Ex", "Ey", "Ez"],
#subgrid = None
)

```

name[¶](#id74)

Optional name of the diagnostic. Used only for post-processing purposes.

every[¶](#id75)

Number of timesteps between each output or a [time selection](#timeselections).

flush_every[¶](#flush_every)

Default:

1

Number of timesteps or a [time selection](#timeselections).

When `flush_every` coincides with `every`, the output
file is actually written (“flushed” from the buffer). Flushing
too often can dramatically slow down the simulation.

time_average[¶](#time_average)

Default:

`1` (no averaging)

The number of timesteps for time-averaging.

fields[¶](#fields)

Default:

`[]` (all fields are written)

List of the field names that are saved. By default, they all are.
The full list of fields that are saved by this diagnostic:

Bx
By
Bz

Components of the magnetic field

Bx_m
By_m
Bz_m

Components of the magnetic field (time-centered)

Ex
Ey
Ez

Components of the electric field

Jx
Jy
Jz

Components of the total current

Jx_abc
Jy_abc
Jz_abc

Components of the current due to species “abc”

Rho
Rho_abc

Total charge density
Charge density of species “abc”

In `AMcylindrical` geometry, the `x`, `y` and `z`
indices are replaced by `l` (longitudinal), `r` (radial) and `t` (theta). In addition,
the angular Fourier modes are denoted by the suffix `_mode_i` where `i`
is the mode number.
If a field is specified without its associated mode number, all available modes will be included.
In summary, the list of fields reads as follows.

Bl_mode_0, Bl_mode_1, etc.
Br_mode_0, Br_mode_1, etc.
Bt_mode_0, Bt_mode_1, etc.

Components of the magnetic field

El_mode_0, El_mode_1, etc.
Er_mode_0, Er_mode_1, etc.
Et_mode_0, Et_mode_1, etc.

Components of the electric field

The same notation works for Jl, Jr, Jt, and Rho

In the case of an envelope model for the laser (see [Laser envelope model](../Understand/laser_envelope.html)),
the following fields are also available:

Env_A_abs

Module of laser vector potential’s complex envelope
\(\tilde{A}\) (component along the transverse
direction)

Env_Chi

Total  susceptibility \(\chi\)

Env_E_abs

Module of laser electric field’s complex envelope
\(\tilde{E}\) (component along the transverse
direction)

Env_Ex_abs

Module of laser electric field’s complex envelope
\(\tilde{E}_x\) (component along the propagation
direction)

In the case the B-TIS3 interpolation is activated (see [PIC algorithms](../Understand/algorithms.html)),
the following fields are also available:

By_mBTIS3
By_mBTIS3

Components of the magnetic field
for the B-TIS3 interpolation
(time-centered)

Br_mBTIS3_mode_0, Br_mBTIS3_mode_1, etc.
Bt_mBTIS3_mode_0, Bt+mBTIS3_mode_1, etc.

Components of the magnetic field
for the B-TIS3 interpolation
(`AMcylindrical` geometry, time-centered)

Note

In a given DiagFields, all fields must be of the same kind: either real or complex. Therefore To write these last three envelope real fields in `"AMcylindrical"` geometry,
a dedicated block `DiagFields` must be defined, e.g. with `fields = ["Env_A_abs", "Env_Chi"]`.

subgrid[¶](#subgrid)

Default:

`None` (the whole grid is used)

A list of slices indicating a portion of the simulation grid to be written by this
diagnostic. This list must have as many elements as the simulation dimension.
For example, in a 3D simulation, the list has 3 elements. Each element can be:

-

`None`, to select the whole grid along that dimension

-

an integer, to select only the corresponding cell index along that dimension

-

a python [slice object](https://docs.python.org/3/library/functions.html#slice)
to select regularly-spaced cell indices along that dimension.

This can be easily implemented using the
[numpy.s_ expression](https://docs.scipy.org/doc/numpy/reference/generated/numpy.s_.html).
For instance, in a 3D simulation, the following subgrid selects only every other element
in each dimension:

```
from numpy import s_
DiagFields( #...
subgrid = s_[::2, ::2, ::2]
)

```

while this one selects cell indices included in a contiguous parallelepiped:

```
subgrid = s_[100:300, 300:500, 300:600]

```

datatype[¶](#datatype)

Default:

`"double"`

The data type when written to the HDF5 file. Accepts `"double"` (8 bytes) or `"float"` (4 bytes).
