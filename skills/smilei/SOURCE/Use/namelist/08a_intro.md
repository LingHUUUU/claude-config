## Lasers[¶](#lasers "Link to this heading")

A laser consists in applying oscillating boundary conditions for the magnetic
field on one of the box sides. The only boundary conditions that support lasers
are `"silver-muller"` and `"PML"` (see [`EM_boundary_conditions`](#EM_boundary_conditions "EM_boundary_conditions")).
There are several syntaxes to introduce a laser in **Smilei**:

Note

The following definitions are given for lasers incoming from the `xmin` or `xmax`
boundaries. For lasers incoming from `ymin` or `ymax`, replace the `By`
profiles by `Bx` profiles. For lasers incoming from `zmin` or `zmax`,
replace `By` and `Bz` profiles by `Bx` and `By` profiles, respectively.

1. Defining a generic wave

> ```
> Laser(
>     box_side = "xmin",
>     space_time_profile = [ By_profile, Bz_profile ]
>     space_time_profile_AM = [ Br_mode0, Bt_mode0, Br_mode1, Bt_mode1, ... ]
> )
> ```

box\_side[¶](#id21 "Link to this definition")
:   Default:
    :   `"xmin"`

    Side of the box from which the laser originates: `"xmin"`, `"xmax"`, `"ymin"`,
    `"ymax"`, `"zmin"` or `"zmax"`.

    In the cases of `"ymin"` or `"ymax"`, replace, in the following profiles,
    coordinates *y* by *x*, and fields \(B\_y\) by \(B\_x\).

    In the cases of `"zmin"` or `"zmax"`, replace, in the following profiles,
    coordinates *y* by *x*, coordinates *z* by *y*, fields \(B\_y\) by \(B\_x\)
    and fields \(B\_z\) by \(B\_y\).

space\_time\_profile[¶](#space_time_profile "Link to this definition")
:   Type:
    :   A list of two *python* functions

    The full wave expression at the chosen box side. It is a list of **two** *python*
    functions taking several arguments depending on the simulation dimension:
    \((t)\) for a 1-D simulation, \((y,t)\) for a 2-D simulation (etc.)
    The two functions represent \(B\_y\) and \(B\_z\), respectively.
    This can be used only in Cartesian geometries.

space\_time\_profile\_AM[¶](#space_time_profile_AM "Link to this definition")
:   Type:
    :   A list of maximum 2 x `number_of_AM` complex valued *python* functions.

    These profiles define the first modes of \(B\_r\) and \(B\_\theta\) of the laser in the
    order shown in the above example. Higher undefined modes are considered zero.
    This can be used only in `AMcylindrical` geometry. In this
    geometry a two-dimensional \((x,r)\) grid is used and the laser is injected from a
    \(x\) boundary, thus the provided profiles must be a function of \((r,t)\).

2. Defining the wave envelopes
