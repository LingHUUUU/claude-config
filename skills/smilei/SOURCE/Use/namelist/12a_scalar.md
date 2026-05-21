## *Scalar* diagnostics[¶](#scalar-diagnostics "Link to this heading")

**Smilei** can collect various scalar data, such as total particle energy, total field energy, etc.
This is done by including the block `DiagScalar`:

```
DiagScalar(
    every = 10 ,
    vars = ["Utot", "Ukin", "Uelm"],
    precision = 10
)
```

every[¶](#id73 "Link to this definition")
:   Number of timesteps between each output **or** a [time selection](#timeselections).

vars[¶](#vars "Link to this definition")
:   Default:
    :   `[]`

    List of scalars that will be actually output. Note that most scalars are computed anyways.

    Omit this argument to include all scalars.

precision[¶](#precision "Link to this definition")
:   Default:
    :   10

    Number of digits of the outputs.

Warning

Scalars diagnostics min/max cell are not yet supported in `"AMcylindrical"` geometry.

The full list of available scalars is given in the table below.

Warning

As some of these quantities are integrated in space and/or time, their
units are unusual, and depend on the simulation dimension.
All details [here](../Understand/units.html#integrated-quantities).

|  |
| --- |
| **Space-integrated energy densities** |
| |  |  | | --- | --- | | Utot | Total | | Ukin | Total kinetic (in the particles) | | Uelm | Total electromagnetic (in the fields) | | Uexp | Expected (Initial \(-\) lost \(+\) gained) | | Ubal | Balance (Utot \(-\) Uexp) | | Ubal\_norm | Normalized balance (Ubal \(/\) Utot) | | Uelm\_Ex | Ex field contribution (\(\int E\_x^2 dV /2\)) | |  | … same for fields Ey, Ez, Bx\_m, By\_m and Bz\_m | | Urad | Total radiated | | UmBWpairs | Total energy converted into electron-position pairs | |
| **Space- & time-integrated Energies lost/gained at boundaries** |
| |  |  | | --- | --- | | Ukin\_bnd | Time-accumulated kinetic energy exchanged at the boundaries | | Uelm\_bnd | Time-accumulated EM energy exchanged at boundaries | | PoyXminInst | Poynting contribution through xmin boundary during the timestep | | PoyXmin | Time-accumulated Poynting contribution through xmin boundary | |  | … same for other boundaries | | Ukin\_new | Time-accumulated kinetic energy from new particles (injector) | | Ukin\_out\_mvw | Time-accumulated kinetic energy lost by the moving window | | Ukin\_inj\_mvw | Time-accumulated kinetic energy gained by the moving window | | Uelm\_out\_mvw | Time-accumulated EM energy lost by the moving window | | Uelm\_inj\_mvw | Time-accumulated EM energy gained by the moving window | |
| **Particle information** |
| |  |  | | --- | --- | | Zavg\_abc | Average charge of species “abc” (equals `nan` if no particle) | | Dens\_abc | … its integrated density | | Ukin\_abc | … its integrated kinetic energy density | | Urad\_abc | … its integrated radiated energy density | | Ntot\_abc | … and number of macro-particles | |  |  | |
| **Fields information** |
| |  |  | | --- | --- | | ExMin | Minimum of \(E\_x\) | | ExMinCell | … and its location (cell index) | | ExMax | Maximum of \(E\_x\) | | ExMaxCell | … and its location (cell index) | |  | … same for fields Ey Ez Bx\_m By\_m Bz\_m Jx Jy Jz Rho | |

Checkout the [post-processing](post-processing.html) documentation as well.

---

## *Fields* diagnostics[¶](#fields-diagnostics "Link to this heading")
