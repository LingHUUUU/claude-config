3. Defining a 1D planar wave

> For one-dimensional simulations, you may use the simplified laser creator:
>
> ```
> LaserPlanar1D(
>     box_side         = "xmin",
>     a0               = 1.,
>     omega            = 1.,
>     polarization_phi = 0.,
>     ellipticity      = 0.,
>     time_envelope    = tconstant(),
>     phase_offset     = 0.,
> )
> ```
>
> a0[¶](#a0 "Link to this definition")
> :   Default:
>
>     The normalized vector potential
>
> polarization\_phi[¶](#polarization_phi "Link to this definition")
> :   Default:
>
>     The angle of the polarization ellipse major axis relative to the X-Y plane, in radians.
>
> ellipticity[¶](#ellipticity "Link to this definition")
> :   Default:
>
>     The polarization ellipticity: 0 for linear and \(\pm 1\) for circular.
>
> phase\_offset[¶](#phase_offset "Link to this definition")
> :   Default:
>
>     An extra phase added to both the envelope and to the carrier wave.

4. Defining a 2D gaussian wave

> For two-dimensional simulations, you may use the simplified laser creator:
>
> ```
> LaserGaussian2D(
>     box_side         = "xmin",
>     a0               = 1.,
>     omega            = 1.,
>     focus            = [50., 40.],
>     waist            = 3.,
>     incidence_angle  = 0.,
>     polarization_phi = 0.,
>     ellipticity      = 0.,
>     time_envelope    = tconstant(),
>     phase_offset     = 0.,
> )
> ```
>
> This is similar to `LaserPlanar1D`, with some additional arguments for
> specific 2D aspects.
>
> focus[¶](#focus "Link to this definition")
> :   Type:
>     :   A list of two floats `[X, Y]`
>
>     The `X` and `Y` positions of the laser focus.
>
> waist[¶](#waist "Link to this definition")
> :   The waist value. Transverse coordinate at which the field is at 1/e of its maximum value.
>
> incidence\_angle[¶](#incidence_angle "Link to this definition")
> :   Default:
>
>     The angle of the laser beam relative to the normal to the injection plane, in radians.

5. Defining a 3D gaussian wave

> For three-dimensional simulations, you may use the simplified laser creator:
>
> ```
> LaserGaussian3D(
>     box_side         = "xmin",
>     a0               = 1.,
>     omega            = 1.,
>     focus            = [50., 40., 40.],
>     waist            = 3.,
>     incidence_angle  = [0., 0.1],
>     polarization_phi = 0.,
>     ellipticity      = 0.,
>     time_envelope    = tconstant(),
>     phase_offset     = 0.,
> )
> ```
>
> This is almost the same as `LaserGaussian2D`, with the `focus` parameter having
> now 3 elements (focus position in 3D), and the `incidence_angle` being a list of
> two angles, corresponding to rotations around `y` and `z`, respectively.
>
> When injecting on `"ymin"` or `"ymax"`, the incidence angles corresponds to
> rotations around `x` and `z`, respectively.

6. Defining 2D smoothed beam
