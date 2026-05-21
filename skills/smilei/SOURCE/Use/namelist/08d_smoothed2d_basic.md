6. Defining 2D smoothed beam

For two-dimensional simulations, you may use the specific laser creator for define smoothed laser beam:

```
LaserSmoothing3D(
    box_side                       = "xmin",
    a0                             = 1.,
    omega                          = 1.,
    focus                          = None,
    incidence_angle                = 0.,
    polarization_phi               = 0.,
    ellipticity                    = 0.,
    phase_zero                     = 0.,
    Lf                             = 3.00e6,
    fnumber                        = 8.00,
    N                              = 6,
    rpp_random_seed                = 10,
    temporal_smoothing             = None,
    temporal_smoothing_random_seed = 42,
    omega_m                        = 0.,
    modulation_depth               = 0,
    rpp_per_mode                   = False,
    rpp_seed_per_mode              = [42],
    omega_m_trans                  = 0.,
    modulation_depth_trans         = 0,
    mode2generate_trans            = None,
    omega_m_longi                  = 0.,
    modulation_depth_longi         = 0,
    mode2generate_longi            = None,
    space_envelope                 = lambda y,z:1.,
    time_envelope                  = tconstant(),
    chirp_profile                  = tconstant()
)
```

Assuming the beam propagate along x direction, this implements a specific spatial and phase profile produced by a random phase plate of the form ([Cross-beam energy transfer between spatially smoothed laser beams” [A. Oudin, A. Debayle, C. Ruyer]](https://doi.org/10.1063/5.0109511)):

> \[\begin{split}\begin{multline}
> \widetilde{E}(x,y,z,n=0) = \frac{E\_0}{2\sqrt{\pi}} \sqrt{\frac{f\_0}{f\_0-x}} \mathrm{e}^{ik\_0x}\mathrm{e}^{-\frac{ik\_0 y^2}{2(f\_0-x)} } \times \text{...} \\
> \text{...} \sum\_{N\_y} \mathrm{e}^{i (\varphi\_N+\delta\_N)} \big[\mathrm{erf}(\mathrm{e}^{-\frac{i \pi}{4}} K\_0(x)\cdot (a\_{N\_y+1} - \frac{yf\_0}{f\_0-x})) - \mathrm{erf}(\mathrm{e}^{-\frac{i \pi}{4}} K\_0(x)\cdot (a\_{N\_y} - \frac{yf\_0}{f\_0-x})) \big] \big]
> \end{multline}\end{split}\]

with \(k\_0\) the wavenumber, \(E\_0\) the field amplitude, \(f\_0\) the focal length \(K\_0(x)=\lvert k\_0(f\_0-x)/(2xf\_0) \lvert\)
and \(\varphi\_N + \delta\_N = \varphi\_{N\_y,N\_Z} + \delta\_{N\_y,N\_Z}\) is the random phase, and optical delay induced by each element of the plate (\(\varphi\_N=\{0,\pi\}\) for RPP or \([0,2\pi[\) for CPP and \(\delta\_N=[0,2\pi[\) for an Echelon).

To avoid space correlation, \(\varphi\_{N\_y,N\_Z}\neq\varphi\_{N\_y}+\varphi\_{N\_Z}\) \(\delta\_{N\_y,N\_Z}\neq\delta\_{N\_y}+\delta\_{N\_Z}\).

In order to take into account the temporal behaviour of the field and the bandwidth of the beam (smoothing by temporal dispersion), we must consider the field is no longer monochromatic and each mode will have it’s own amplitude and phase, relying on the smoothing technic used (Longitudinal Smoothing by Spectral Dispersion LSSD, Transverse Smoothing by Spectral Dispersion TSSD or Broadband). Each mode routinely produce one `Laser Block`

> box\_side[¶](#id23 "Link to this definition")
> :   Type:
>     :   a string
>
>     Default:
>     :   `"xmin"`
>
>     Side of the box from which the laser originates: `"xmin"`, `"xmax"`, `"ymin"`,
>     `"ymax"`.
>
>     In the cases of `"ymin"` or `"ymax"`, replace, in the following profiles,
>     coordinates *y* by *x*, and fields \(B\_y\) by \(B\_x\).
>
> a0[¶](#id24 "Link to this definition")
> :   Type:
>     :   double
>
>     Default:
>
>     The normalized vector potential at focus. Note that \(E\_0 = (a\_0 \omega/N\_{tot}) / \sqrt{k\_0 (dy)^2 / (2 L\_f \pi^2) } ` with :math:`dy=D/N\_y\)
>     and where D is the effective aperture of the optical system (typically the size of the phase plate)
>
> omega[¶](#id25 "Link to this definition")
> :   Type:
>     :   double
>
>     Default:
>
>     The laser angular frequency.
>
> focus[¶](#id26 "Link to this definition")
> :   Type:
>     :   A list of two floats `[X, Y]`
>
>     Default:
>     :   `[0,0]`
>
>     The `X`, `Y` positions of the laser focus.
>
> incidence\_angle[¶](#id27 "Link to this definition")
> :   Type:
>     :   double
>
>     Default:
>
>     The angle of the laser beam relative to the normal to the injection plane, in radians, in the `X`, `Y` plane.
>
> polarization\_phi[¶](#id28 "Link to this definition")
> :   Type:
>     :   double
>
>     Default:
>
>     The angle of the polarization ellipse major axis relative to the X-Y plane, in radians.
>
> ellipticity[¶](#id29 "Link to this definition")
> :   Type:
>     :   double
>
>     Default:
>
>     The polarization ellipticity: 0 for linear and \(\pm 1\) for circular.
>     Only linear is taking into account for now.
>
