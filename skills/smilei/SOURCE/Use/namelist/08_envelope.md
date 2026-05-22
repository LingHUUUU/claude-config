## Laser envelope model[¶](#laser-envelope-model)

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

omega[¶](#id59)

Default:

`1.`

The laser angular frequency.

box_side[¶](#id60)

Default:

`"inside"`

The way the laser envelope is integrated in the simulation. Currently only `"inside"` and `"xmin"` are supported.
`"inside"`: the laser envelope is added only at the start of the simulation. In this case, the temporal coordinate of the laser envelope profile is
interpreted as the coordinate along the `x` axis. If the laser puse length is short enough, it can entirely fit inside the simulation window.
`"xmin"`: the laser is progressively injected in the window from the left window border in the `x` direction. The time coordinate
in the laser envelope profile is treated as in a `Laser` block. See also the parameter `envelope_profile`.

envelope_profile[¶](#envelope_profile)

Type:

a python function or a [python profile](profiles.html)

Default:

None

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

envelope_solver[¶](#envelope_solver)

Default:

`explicit`

The solver scheme for the envelope equation.

-

`"explicit"`: an explicit scheme based  on central finite differences.

-

`"explicit_reduced_dispersion"`: the finite difference derivatives along `x` in the `"explicit"` solver are substituted by
optimized derivatives to reduce numerical dispersion. For more accurate results over long distances, the use of this solver is recommended.
Please note that the CFL limit of this solver is lower than the one of the `"explicit"` solver. Thus, a smaller integration
timestep may be necessary.

Envelope_boundary_conditions[¶](#Envelope_boundary_conditions)

Type:

list of lists of strings

Default:

`[["reflective"]]`

Defines the boundary conditions used for the envelope. Either `"reflective"` or `"PML"`.
In the case of `"PML"`, make sure to define `"number_of_pml_cells"` in the `Main` block.

polarization_phi[¶](#id61)

Default:

-

The angle of the polarization ellipse major axis relative to the X-Y plane, in radians. Needed only for ionization.

ellipticity[¶](#id62)

Default:

-

The polarization ellipticity: 0 for linear and 1 for circular. For the moment, only these two polarizations are available.

2. Defining a 1D laser envelope

Following is the simplified laser envelope creator in 1D

```
LaserEnvelopePlanar1D(
a0              = 1.,
time_envelope   = tgaussian(center=150., fwhm=40.),
envelope_solver = 'explicit',
Envelope_boundary_conditions = [ ["reflective"] ],
polarization_phi = 0.,
ellipticity      = 0.
)

```

3. Defining a 2D gaussian laser envelope

Following is the simplified gaussian laser envelope creator in 2D

```
LaserEnvelopeGaussian2D(
a0              = 1.,
focus           = [150., 40.],
waist           = 30.,
time_envelope   = tgaussian(center=150., fwhm=40.),
envelope_solver = 'explicit',
Envelope_boundary_conditions = [ ["reflective"] ],
polarization_phi = 0.,
ellipticity      = 0.
)

```

4. Defining a 3D gaussian laser envelope

Following is the simplified laser envelope creator in 3D

```
LaserEnvelopeGaussian3D(
a0              = 1.,
focus           = [150., 40., 40.],
waist           = 30.,
time_envelope   = tgaussian(center=150., fwhm=40.),
envelope_solver = 'explicit',
Envelope_boundary_conditions = [ ["reflective"] ],
polarization_phi = 0.,
ellipticity      = 0.
)

```

5. Defining a cylindrical gaussian laser envelope

Following is the simplified laser envelope creator in `"AMcylindrical"` geometry (remember that
in this geometry the envelope model can be used only if `number_of_AM = 1`)

```
LaserEnvelopeGaussianAM(
a0              = 1.,
focus           = [150.],
waist           = 30.,
time_envelope   = tgaussian(center=150., fwhm=40.),
envelope_solver = 'explicit',
Envelope_boundary_conditions = [ ["reflective"] ],
polarization_phi = 0.,
ellipticity      = 0.
)

```

The arguments appearing `LaserEnvelopePlanar1D`, `LaserEnvelopeGaussian2D`,
`LaserEnvelopeGaussian3D` and `LaserEnvelopeGaussianAM` have the same meaning they would have in a
normal `LaserPlanar1D`, `LaserGaussian2D`, `LaserGaussian3D` and `LaserGaussianAM`,
with some differences:

time_envelope[¶](#id63)

The temporal envelope of the laser pulse. See the `box_side` in the `LaserEnvelope` block to understand its definition.
Temporal envelopes with variation scales near to the laser wavelength do not
satisfy the assumptions of the envelope model (see [Laser envelope model](../Understand/laser_envelope.html)),
yielding inaccurate results.

waist[¶](#id64)

Please note that a waist size smaller or comparable to the laser wavelength does not
satisfy the assumptions of the envelope model.

It is important to remember that the profile defined through the blocks
`LaserEnvelopePlanar1D`, `LaserEnvelopeGaussian2D`, `LaserEnvelopeGaussian3D`
correspond to the complex envelope of the laser vector potential component
\(\tilde{A}\) in the polarization direction.
The calculation of the correspondent complex envelope for the laser electric field
component in that direction is described in [Laser envelope model](../Understand/laser_envelope.html).

Note that only order 2 interpolation and projection are supported in presence of
the envelope model for the laser.

The parameters `polarization_phi` and `ellipticity` specify the polarization state of the laser. In envelope model implemented in Smilei,
they are only used to compute the rate of ionization and the initial momentum of the electrons newly created by ionization,
where the polarization of the laser plays an important role (see [Ionization](../Understand/ionization.html)).
For all other purposes (e.g. the particles equations of motions, the computation of the ponderomotive force,
the evolution of the laser), the polarization angle of the laser plays no role in the envelope model.
