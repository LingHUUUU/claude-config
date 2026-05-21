## Laser envelope model[¶](#laser-envelope-model "Link to this heading")

In all the available geometries, it is possible to model a laser pulse
propagating in the `x` direction
using an envelope model (see [Laser envelope model](../Understand/laser_envelope.html) for the advantages
and limits of this approximation).
The fast oscillations of the laser are neglected and all the physical
quantities of the simulation, including the electromagnetic fields and
their source terms, as well as the particles positions and momenta, are
meant as an average over one or more optical cycles.
Effects involving characteristic lengths comparable to the laser central
wavelength (i.e. sharp plasma density profiles) cannot be modeled with
this option.

Note

The envelope model in `"AMcylindrical"` geometry is implemented only in the hypothesis of
cylindrical symmetry, i.e. only one azimuthal mode. Therefore, to use it the user must choose
`number_of_AM = 1`.

Contrarily to a standard `Laser` initialized with the Silver-Müller
boundary conditions, the laser envelope can be initialized either entirely inside
the simulation box at the start of the simulation (default method) or as a standard `Laser` through boundary conditions at the left `x` border of the window.
See `box_side` for more details.

Currently only one laser pulse of a given frequency propagating in the positive
x direction can be speficified. However, a multi-pulse set-up can be initialized
e.g. if the envelope profile is given by two adjacents gaussian functions.
The whole multi-pulse profile would have the same carrier frequency and would propagate in the positive
x direction. For the moment it is not possible to specify more than one laser envelope profile, e.g.
two counterpropagating lasers, or two lasers with different carrier frequency.

Please note that describing a laser through its complex envelope loses physical accuracy if its
characteristic space-time variation scales are too small, i.e. of the order of the laser
central wavelength (see [Laser envelope model](../Understand/laser_envelope.html)).
Thus, space-time profiles with variation scales larger than this length should be used.

1. Defining a generic laser envelope

Following is the generic laser envelope creator

```
LaserEnvelope(
    omega            = 1.,
    envelope_solver  = 'explicit',
    box_side         = "inside",
    envelope_profile = envelope_profile,
    Envelope_boundary_conditions = [["reflective"]]
    polarization_phi = 0.,
    ellipticity      = 0.
)
```

omega[¶](#id59 "Link to this definition")
:   Default:
    :   `1.`

    The laser angular frequency.

box\_side[¶](#id60 "Link to this definition")
:   Default:
    :   `"inside"`

    The way the laser envelope is integrated in the simulation. Currently only `"inside"` and `"xmin"` are supported.
    `"inside"`: the laser envelope is added only at the start of the simulation. In this case, the temporal coordinate of the laser envelope profile is
    interpreted as the coordinate along the `x` axis. If the laser puse length is short enough, it can entirely fit inside the simulation window.
    `"xmin"`: the laser is progressively injected in the window from the left window border in the `x` direction. The time coordinate
    in the laser envelope profile is treated as in a `Laser` block. See also the parameter `envelope_profile`.

envelope\_profile[¶](#envelope_profile "Link to this definition")
:   Type:
    :   a *python* function or a [python profile](profiles.html)

    Default:
    :   None

    The complex laser envelope profile.
    If the parameter `box_side` is `"inside"`, the profile arguments are all the coordinates and time.
    If the parameter `box_side` is `"xmin"`, the profile arguments are all the transverse coordinates at plane `x=0` and time,
    as in a `Laser` block with `box_side="xmin"`.
    For example, if the geometry is `"3Dcartesian"`, a complex-valued function of 4 arguments (3 for space, 1 for time) is necessary if `box_side="inside"`.
    Instead, if `box_side="xmin"`, the needed profile is a complex-valued function of 3 arguments (2 for the transverse coordinates, 1 for time).
    See also the parameter `box_side`.
    It is recommended to initialize the laser envelope in vacuum, separated from the plasma, to avoid unphysical
    results.
    Envelopes with variation scales in space and time close to the laser wavelength do not
    satisfy the assumptions of the envelope model (see [Laser envelope model](../Understand/laser_envelope.html)):
    their simulation yieldss inaccurate results.
    Since at the moment the paraxial hypothesis is used when `box_side="xmin"`, the requested `envelope_profile` should satisfy this hypothesis.

envelope\_solver[¶](#envelope_solver "Link to this definition")
:   Default:
    :   `explicit`

    The solver scheme for the envelope equation.

    - `"explicit"`: an explicit scheme based on central finite differences.
    - `"explicit_reduced_dispersion"`: the finite difference derivatives along `x` in the `"explicit"` solver are substituted by
      optimized derivatives to reduce numerical dispersion. For more accurate results over long distances, the use of this solver is recommended.
      Please note that the CFL limit of this solver is lower than the one of the `"explicit"` solver. Thus, a smaller integration
      timestep may be necessary.

Envelope\_boundary\_conditions[¶](#Envelope_boundary_conditions "Link to this definition")
:   Type:
    :   list of lists of strings

    Default:
    :   `[["reflective"]]`

    Defines the boundary conditions used for the envelope. Either `"reflective"` or `"PML"`.
    In the case of `"PML"`, make sure to define `"number_of_pml_cells"` in the `Main` block.

polarization\_phi[¶](#id61 "Link to this definition")
:   Default:
