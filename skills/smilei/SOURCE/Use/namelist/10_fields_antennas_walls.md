## External fields[¶](#external-fields "Link to this heading")

An initial field can be applied over the whole box
at the beginning of the simulation using the `ExternalField` block:

```
ExternalField(
    field = "Ex",
    profile = constant(0.01, xvacuum=0.1)
)
```

field[¶](#field "Link to this definition")
:   Field names in Cartesian geometries: `"Ex"`, `"Ey"`, `"Ez"`, `"Bx"`, `"By"`, `"Bz"`, `"Bx_m"`, `"By_m"`, `"Bz_m"`.
    Field names in AM geometry: `"El_mode_m"`, `"Er_mode_m"`, `"Et_mode_m"`, `"Bl_mode_m"`, `"Br_mode_m"`, `"Bt_mode_m"`, `"Bl_m_mode_m"`, `"Br_m_mode_m"`, `"Bt_m_mode_m"`, `"A_mode_1"`, `"A0_mode_1"` .

profile[¶](#profile "Link to this definition")
:   Type:
    :   float or [profile](profiles.html)

    The initial spatial profile of the applied field.
    Refer to [Units](../Understand/units.html) to understand the units of this field.

    Note that when using standard FDTD schemes, `B` fields are given at time `t=0.5 dt` and `B_m` fields at time `t=0` like `E` fields.
    It is important to initialize `B_m` fields at `t=0` if there are particles in the simulation domain at the start of the simulation.
    If `B_m` is omited, it is assumed that the magnetic field is constant and that `B_m=B`.

    Note that in AM geometry all field names must be followed by the number `"i"` of the mode that is currently passed with the string `"_mode_i"`. For instance `"Er_mode_1"`.
    In this geometry, an external envelope field can also be used. It needs to be initialized at times `"t=0"` in `"A_mode_1"` and `"t=-dt"` in `"A0_mode_1"`.
    The user must use the `"_mode_1"` suffix for these two fields because there is no other possible mode for them.

---

## Prescribed fields[¶](#prescribed-fields "Link to this heading")

User-defined electromagnetic fields, with spatio-temporal dependence,
can be superimposed to the self-consistent Maxwell fields.
These fields push the particles but **do not participate in the Maxwell solver**:
they are not self-consistent.
They are however useful to describe charged particles’ dynamics in a given
electromagnetic field.

This feature is accessible using the `PrescribedField` block:

```
from numpy import cos, sin
def myPrescribedProfile(x,t):
      return cos(x)*sin(t)

PrescribedField(
    field = "Ex",
    profile = myPrescribedProfile
)
```

field[¶](#id65 "Link to this definition")
:   Field names in Cartesian geometries: `"Ex"`, `"Ey"`, `"Ez"`, `"Bx_m"`, `"By_m"` or `"Bz_m"`.
    Field names in AM geometry: `"El_mode_m"`, `"Er_mode_m"`, `"Et_mode_m"`, `"Bl_m_mode_m"`, `"Br_m_mode_m"` or `"Bt_m_mode_m"`.

Warning

When prescribing a magnetic field, always use the time-centered fields `"Bx_m"`, `"By_m"` or `"Bz_m"`.
These fields are those used in the particle pusher, and are defined at integer time-steps.

Warning

When prescribing a field in AM geometry, the mode “m” must be specified explicitly in the name of the field and the profile
must return a complex value.

Warning

`PrescribedFields` are not visible in the `Field` diagnostic,
but can be visualised through `Probes` and with the fields attributes of `TrackParticles`
(since they sample the total field acting on the macro-particles).

profile[¶](#id66 "Link to this definition")
:   Type:
    :   float or [profile](profiles.html)

    The spatio-temporal profile of the applied field: a *python* function
    with arguments (*x*, *t*) or (*x*, *y*, *t*), etc.
    Refer to [Units](../Understand/units.html) to understand the units of this field.

---

## Antennas[¶](#antennas "Link to this heading")

An antenna is an extra current applied during the whole simulation.
It is applied using an `Antenna` block:

```
Antenna(
    field = "Jz",
    space_profile = gaussian(0.01),
    time_profile = tcosine(base=0., duration=1., freq=0.1)
)
```

field[¶](#id68 "Link to this definition")
:   The name of the current: `"Jx"`, `"Jy"` or `"Jz"`.

space\_profile[¶](#space_profile "Link to this definition")
:   Type:
    :   float or [profile](profiles.html)

    The initial spatial profile of the applied antenna.
    Refer to [Units](../Understand/units.html) to understand the units of this current.

time\_profile[¶](#time_profile "Link to this definition")
:   Type:
    :   float or [profile](profiles.html)

    The temporal profile of the applied antenna. It multiplies `space_profile`.

space\_time\_profile[¶](#id69 "Link to this definition")
:   Type:
    :   float or [profile](profiles.html)

    A space & time profile for the antenna (not compatible with `space_profile`
    or `time_profile`). It should have ``` N+1``arguments, where ``N ``` is the dimension
    of the simulation. For instance `(x,t)` in 1D, `(x,y,t)` in 2D, etc.

    The function must accept `x`, `y` and `z` either as floats or numpy arrays.
    If it accepts floats, the return value must be a float.
    If it accepts numpy arrays, these arrays will correspond to the coordinates of 1 patch,
    and the return value must be a numpy array of the same size.

---

## Walls[¶](#walls "Link to this heading")

A wall can be introduced using a `PartWall` block in order to
reflect, stop, thermalize or kill particles which reach it:

```
PartWall(
    kind = "reflective",
    x = 20.
)
```

kind[¶](#kind "Link to this definition")
:   The kind of wall: `"reflective"`, `"stop"`, `"thermalize"` or `"remove"`.

x[¶](#x "Link to this definition")

y[¶](#y "Link to this definition")

z[¶](#z "Link to this definition")
:   Position of the wall in the desired direction. Use only one of `x`, `y` or `z`.

---
