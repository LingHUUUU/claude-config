:   Default:

    The angle of the polarization ellipse major axis relative to the X-Y plane, in radians. Needed only for ionization.

ellipticity[¶](#id62 "Link to this definition")
:   Default:

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

time\_envelope[¶](#id63 "Link to this definition")
:   The temporal envelope of the laser pulse. See the `box_side` in the `LaserEnvelope` block to understand its definition.
    Temporal envelopes with variation scales near to the laser wavelength do not
    satisfy the assumptions of the envelope model (see [Laser envelope model](../Understand/laser_envelope.html)),
    yielding inaccurate results.

waist[¶](#id64 "Link to this definition")
:   Please note that a waist size smaller or comparable to the laser wavelength does not
    satisfy the assumptions of the envelope model.

It is important to remember that the profile defined through the blocks
`LaserEnvelopePlanar1D`, `LaserEnvelopeGaussian2D`, `LaserEnvelopeGaussian3D`
correspond to the complex envelope of the laser vector potential component
\(\tilde{A}\) in the polarization direction.
The calculation of the correspondent complex envelope for the laser electric field
component in that direction is described in [Laser envelope model](../Understand/laser_envelope.html).

Note that only order 2 interpolation and projection are supported in presence of
the envelope model for the laser.

The parameters `polarization_phi` and `ellipticity` specify the polarization state of the laser. In envelope model implemented in **Smilei**,
they are only used to compute the rate of ionization and the initial momentum of the electrons newly created by ionization,
where the polarization of the laser plays an important role (see [Ionization](../Understand/ionization.html)).
For all other purposes (e.g. the particles equations of motions, the computation of the ponderomotive force,
the evolution of the laser), the polarization angle of the laser plays no role in the envelope model.

---
