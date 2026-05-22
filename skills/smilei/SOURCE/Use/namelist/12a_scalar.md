## Scalar diagnostics[¶](#scalar-diagnostics)

Smilei can collect various scalar data, such as total particle energy, total field energy, etc.
This is done by including the block `DiagScalar`:

```
DiagScalar(
every = 10 ,
vars = ["Utot", "Ukin", "Uelm"],
precision = 10
)

```

every[¶](#id73)

Number of timesteps between each output or a [time selection](#timeselections).

vars[¶](#vars)

Default:

`[]`

List of scalars that will be actually output. Note that most scalars are computed anyways.
Omit this argument to include all scalars.

precision[¶](#precision)

Default:

10

Number of digits of the outputs.

Warning

Scalars diagnostics min/max cell are not yet supported in `"AMcylindrical"` geometry.

The full list of available scalars is given in the table below.

Warning

As some of these quantities are integrated in space and/or time, their
units are unusual, and depend on the simulation dimension.
All details [here](../Understand/units.html#integrated-quantities).

Space-integrated energy densities

Utot

Total

Ukin

Total kinetic (in the particles)

Uelm

Total electromagnetic (in the fields)

Uexp

Expected (Initial \(-\) lost \(+\) gained)

Ubal

Balance (Utot \(-\) Uexp)

Ubal_norm

Normalized balance (Ubal \(/\) Utot)

Uelm_Ex

Ex field contribution (\(\int E_x^2 dV /2\))

… same for fields Ey, Ez, Bx_m, By_m and Bz_m

Urad

Total radiated

UmBWpairs

Total energy converted into electron-position pairs

Space- & time-integrated Energies lost/gained at boundaries

Ukin_bnd

Time-accumulated kinetic energy exchanged at the boundaries

Uelm_bnd

Time-accumulated EM energy exchanged at boundaries

PoyXminInst

Poynting contribution through xmin boundary during the timestep

PoyXmin

Time-accumulated Poynting contribution through xmin boundary

… same for other boundaries

Ukin_new

Time-accumulated kinetic energy from new particles (injector)

Ukin_out_mvw

Time-accumulated kinetic energy lost by the moving window

Ukin_inj_mvw

Time-accumulated kinetic energy gained by the moving window

Uelm_out_mvw

Time-accumulated EM energy lost by the moving window

Uelm_inj_mvw

Time-accumulated EM energy gained by the moving window

Particle information

Zavg_abc

Average charge of species “abc” (equals `nan` if no particle)

Dens_abc

… its integrated density

Ukin_abc

… its integrated kinetic energy density

Urad_abc

… its integrated radiated energy density

Ntot_abc

… and number of macro-particles

Fields information

ExMin

Minimum of \(E_x\)

ExMinCell

… and its location (cell index)

ExMax

Maximum of \(E_x\)

ExMaxCell

… and its location (cell index)

… same for fields Ey Ez Bx_m By_m Bz_m Jx Jy Jz Rho

Checkout the [post-processing](post-processing.html) documentation as well.
