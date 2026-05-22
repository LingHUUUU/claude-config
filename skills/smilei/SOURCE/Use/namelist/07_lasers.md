## Lasers[¶](#lasers)

A laser consists in applying oscillating boundary conditions for the magnetic
field on one of the box sides. The only boundary conditions that support lasers
are `"silver-muller"` and `"PML"` (see [`EM_boundary_conditions`](#EM_boundary_conditions)).
There are several syntaxes to introduce a laser in Smilei:

Note

The following definitions are given for lasers incoming from the `xmin` or `xmax`
boundaries. For lasers incoming from `ymin` or `ymax`, replace the `By`
profiles by `Bx` profiles. For lasers incoming from `zmin` or `zmax`,
replace `By` and `Bz` profiles by `Bx` and `By` profiles, respectively.

1. Defining a generic wave

```
Laser(
box_side = "xmin",
space_time_profile = [ By_profile, Bz_profile ]
space_time_profile_AM = [ Br_mode0, Bt_mode0, Br_mode1, Bt_mode1, ... ]
)

```

box_side[¶](#id21)

Default:

`"xmin"`

Side of the box from which the laser originates: `"xmin"`, `"xmax"`, `"ymin"`,
`"ymax"`, `"zmin"` or `"zmax"`.

In the cases of `"ymin"` or `"ymax"`, replace, in the following profiles,
coordinates y by x, and fields \(B_y\) by \(B_x\).

In the cases of `"zmin"` or `"zmax"`, replace, in the following profiles,
coordinates y by x, coordinates z by y, fields \(B_y\) by \(B_x\)
and fields \(B_z\) by \(B_y\).

space_time_profile[¶](#space_time_profile)

Type:

A list of two python functions

The full wave expression at the chosen box side. It is a list of two python
functions taking several arguments depending on the simulation dimension:
\((t)\) for a 1-D simulation, \((y,t)\) for a 2-D simulation (etc.)
The two functions represent \(B_y\) and \(B_z\), respectively.
This can be used only in Cartesian geometries.

space_time_profile_AM[¶](#space_time_profile_AM)

Type:

A list of maximum 2 x `number_of_AM` complex valued python functions.

These profiles define the first modes of \(B_r\) and \(B_\theta\) of the laser in the
order shown in the above example. Higher undefined modes are considered zero.
This can be used only in `AMcylindrical` geometry. In this
geometry a two-dimensional \((x,r)\) grid is used and the laser is injected from a
\(x\) boundary, thus the provided profiles must be a function of \((r,t)\).

2. Defining the wave envelopes

```
Laser(
box_side       = "xmin",
omega          = 1.,
chirp_profile  = tconstant(),
time_envelope  = tgaussian(),
space_envelope = [ By_profile  , Bz_profile   ],
phase          = [ PhiY_profile, PhiZ_profile ],
delay_phase    = [ 0., 0. ]
)

```

This implements a wave of the form:

\[ \begin{align}\begin{aligned}B_y(\mathbf{x}, t) = S_y(\mathbf{x})\; T\left(t-t_{0y}\right)
\;\sin\left( \omega(t) t - \phi_y(\mathbf{x}) \right)\\B_z(\mathbf{x}, t) = S_z(\mathbf{x})\; T\left(t-t_{0z}\right)
\;\sin\left( \omega(t) t - \phi_z(\mathbf{x}) \right)\end{aligned}\end{align} \]

where \(T\) is the temporal envelope, \(S_y\) and \(S_z\) are the
spatial envelopes, \(\omega\) is the time-varying frequency,
\(\phi_y\) and \(\phi_z\) are the phases, and we defined the delays
\(t_{0y} = (\phi_y(\mathbf{x})-\varphi_y)/\omega(t)\) and
\(t_{0z} = (\phi_z(\mathbf{x})-\varphi_z)/\omega(t)\).

omega[¶](#omega)

Default:

-

The laser angular frequency.

chirp_profile[¶](#chirp_profile)

Type:

a python function or a [time profile](profiles.html)

Default:

`tconstant()`

The variation of the laser frequency over time, such that
\(\omega(t)=\) `omega` x `chirp_profile` \((t)\).

Warning

This definition of the chirp profile is not standard.
Indeed, \(\omega(t)\) as defined here is not the instantaneous frequency, \(\omega_{\rm inst}(t)\),
which is obtained from the time derivative of the phase \(\omega(t) t\).

Should one define the chirp as \(C(t) = \omega_{\rm inst}(t)/\omega\) (with \(\omega\) defined by the input
parameter \(\mathtt{omega}\)), the user can easily obtain the corresponding chirp profile as defined in
Smilei as:

\[\mathtt{chirp\_profile}(t) = \frac{1}{t} \int_0^t dt' C(t')\,.\]

Let us give as an example the case of a linear chirp, with the instantaneous frequency
\(\omega_{\rm inst}(t) = \omega [1+\alpha\,\omega(t-t_0)]\).
\(C(t) = 1+\alpha\,\omega(t-t_0)\). The corresponding input chirp profile reads:

\[\mathtt{chirp\_profile}(t) = 1 - \alpha\, \omega t_0 + \frac{\alpha}{2} \omega t\]

Similarly, for a geometric (exponential) chirp such that \(\omega_{\rm inst}(t) = \omega\, \alpha^{\omega t}\),
\(C(t) = \alpha^{\omega t}\), and the corresponding input chirp profile reads:

\[\mathtt{chirp\_profile}(t) = \frac{\alpha^{\omega t} - 1}{\omega t \, \ln \alpha}\,.\]

time_envelope[¶](#id22)

Type:

a python function or a [time profile](profiles.html)

Default:

`tconstant()`

The temporal envelope of the laser (field, not intensity).

space_envelope[¶](#space_envelope)

Type:

a list of two python functions or two [spatial profiles](profiles.html)

Default:

`[ 1., 0. ]`

The two spatial envelopes \(S_y\) and \(S_z\).

phase[¶](#phase)

Type:

a list of two python functions or two [spatial profiles](profiles.html)

Default:

`[ 0., 0. ]`

The two spatially-varying phases \(\phi_y\) and \(\phi_z\).

delay_phase[¶](#delay_phase)

Type:

a list of two floats

Default:

`[ 0., 0. ]`

An extra delay for the time envelopes of \(B_y\) and \(B_z\),
expressed in terms of phase (\(=\omega t\)). This delay is applied to the
[`time_envelope`](#id63), but not to the carrier wave.
This option is useful in the
case of elliptical polarization where the two temporal profiles should have a slight
delay due to the mismatched [`phase`](#phase).

3. Defining a 1D planar wave

For one-dimensional simulations, you may use the simplified laser creator:

```
LaserPlanar1D(
box_side         = "xmin",
a0               = 1.,
omega            = 1.,
polarization_phi = 0.,
ellipticity      = 0.,
time_envelope    = tconstant(),
phase_offset     = 0.,
)

```

a0[¶](#a0)

Default:

-

The normalized vector potential

polarization_phi[¶](#polarization_phi)

Default:

-

The angle of the polarization ellipse major axis relative to the X-Y plane, in radians.

ellipticity[¶](#ellipticity)

Default:

-

The polarization ellipticity: 0 for linear and \(\pm 1\) for circular.

phase_offset[¶](#phase_offset)

Default:

-

An extra phase added to both the envelope and to the carrier wave.

4. Defining a 2D gaussian wave

For two-dimensional simulations, you may use the simplified laser creator:

```
LaserGaussian2D(
box_side         = "xmin",
a0               = 1.,
omega            = 1.,
focus            = [50., 40.],
waist            = 3.,
incidence_angle  = 0.,
polarization_phi = 0.,
ellipticity      = 0.,
time_envelope    = tconstant(),
phase_offset     = 0.,
)

```

This is similar to `LaserPlanar1D`, with some additional arguments for
specific 2D aspects.

focus[¶](#focus)

Type:

A list of two floats `[X, Y]`

The `X` and `Y` positions of the laser focus.

waist[¶](#waist)

The waist value. Transverse coordinate at which the field is at 1/e of its maximum value.

incidence_angle[¶](#incidence_angle)

Default:

-

The angle of the laser beam relative to the normal to the injection plane, in radians.

5. Defining a 3D gaussian wave

For three-dimensional simulations, you may use the simplified laser creator:

```
LaserGaussian3D(
box_side         = "xmin",
a0               = 1.,
omega            = 1.,
focus            = [50., 40., 40.],
waist            = 3.,
incidence_angle  = [0., 0.1],
polarization_phi = 0.,
ellipticity      = 0.,
time_envelope    = tconstant(),
phase_offset     = 0.,
)

```

This is almost the same as `LaserGaussian2D`, with the `focus` parameter having
now 3 elements (focus position in 3D), and the `incidence_angle` being a list of
two angles, corresponding to rotations around `y` and `z`, respectively.

When injecting on `"ymin"` or `"ymax"`, the incidence angles corresponds to
rotations around `x` and `z`, respectively.

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

\[\begin{split}\begin{multline}
\widetilde{E}(x,y,z,n=0) = \frac{E_0}{2\sqrt{\pi}} \sqrt{\frac{f_0}{f_0-x}} \mathrm{e}^{ik_0x}\mathrm{e}^{-\frac{ik_0 y^2}{2(f_0-x)} } \times \text{...} \\
\text{...} \sum_{N_y} \mathrm{e}^{i (\varphi_N+\delta_N)} \big[\mathrm{erf}(\mathrm{e}^{-\frac{i \pi}{4}} K_0(x)\cdot (a_{N_y+1} - \frac{yf_0}{f_0-x})) - \mathrm{erf}(\mathrm{e}^{-\frac{i \pi}{4}} K_0(x)\cdot (a_{N_y} - \frac{yf_0}{f_0-x})) \big] \big]
\end{multline}\end{split}\]

with \(k_0\) the wavenumber, \(E_0\) the field amplitude, \(f_0\) the focal length \(K_0(x)=\lvert k_0(f_0-x)/(2xf_0) \lvert\)
and \(\varphi_N + \delta_N = \varphi_{N_y,N_Z} + \delta_{N_y,N_Z}\) is the random phase, and optical delay induced by each element of the plate (\(\varphi_N=\{0,\pi\}\) for RPP or \([0,2\pi[\) for CPP and \(\delta_N=[0,2\pi[\) for an Echelon).

To avoid space correlation, \(\varphi_{N_y,N_Z}\neq\varphi_{N_y}+\varphi_{N_Z}\) \(\delta_{N_y,N_Z}\neq\delta_{N_y}+\delta_{N_Z}\).

In order to take into account the temporal behaviour of the field and the bandwidth of the beam (smoothing by temporal dispersion), we must consider the field is no longer monochromatic and each mode will have it’s own amplitude and phase, relying on the smoothing technic used (Longitudinal Smoothing by Spectral Dispersion LSSD, Transverse Smoothing by Spectral Dispersion TSSD or Broadband). Each mode routinely produce one `Laser Block`

box_side[¶](#id23)

Type:

a string

Default:

`"xmin"`

Side of the box from which the laser originates: `"xmin"`, `"xmax"`, `"ymin"`,
`"ymax"`.

In the cases of `"ymin"` or `"ymax"`, replace, in the following profiles,
coordinates y by x, and fields \(B_y\) by \(B_x\).

a0[¶](#id24)

Type:

double

Default:

-

The normalized vector potential at focus. Note that \(E_0 = (a_0 \omega/N_{tot}) / \sqrt{k_0 (dy)^2 / (2 L_f \pi^2) } ` with :math:`dy=D/N_y\)
and where D is the effective aperture of the optical system (typically the size of the phase plate)

omega[¶](#id25)

Type:

double

Default:

-

The laser angular frequency.

focus[¶](#id26)

Type:

A list of two floats `[X, Y]`

Default:

`[0,0]`

The `X`, `Y` positions of the laser focus.

incidence_angle[¶](#id27)

Type:

double

Default:

-

The angle of the laser beam relative to the normal to the injection plane, in radians, in the `X`, `Y` plane.

polarization_phi[¶](#id28)

Type:

double

Default:

-

The angle of the polarization ellipse major axis relative to the X-Y plane, in radians.

ellipticity[¶](#id29)

Type:

double

Default:

-

The polarization ellipticity: 0 for linear and \(\pm 1\) for circular.
Only linear is taking into account for now.

phase_zero[¶](#phase_zero)

Type:

double

Default:

-

An extra phase added to both the envelope and to the carrier wave.

Lf[¶](#Lf)

Type:

double

Default:

3.00e6

The focal length in code units

fnumber[¶](#fnumber)

Type:

double

Default:

-

The ratio \(L_f/D\) where D is the effective aperture of the optical system (typically the size of the phase plate)

N[¶](#N)

Type:

int

Default:

6

List of number of phase plate element in D

rpp_random_seed[¶](#rpp_random_seed)

Type:

integer

Default:

10

`None` or an int to chose a seed in order to define each phase element of a random phase plate (`None` is equal no random, all element have zero phase-shift)

temporal_smoothing[¶](#temporal_smoothing)

Type:

a string

Default:

None

Type of temporal smoothing `None/"Broadband"/"TSSD"/"LSSD"`

temporal_smoothing_random_seed[¶](#temporal_smoothing_random_seed)

Type:

integer

Default:

42

Seed in order to have a Random Phase for each mode for `"Broadband Laser"`

omega_m[¶](#omega_m)

Type:

a double

Default:

-

Modulation frequency for `"Broadband Laser"`. It’s a fraction of the central angular frequency.

modulation_depth[¶](#modulation_depth)

Type:

an int

Default:

0

For `"Broadband Laser"`, depth ‘m’ of modulation and frequency bandwith = 2m

rpp_per_mode[¶](#rpp_per_mode)

Type:

bool

Default:

False

For `"Broadband Laser"`, Change the Random Phase Plate for each mode when set to `True`

rpp_seed_per_mode[¶](#rpp_seed_per_mode)

Type:

a list of int

Default:

[42]

For `"Broadband Laser"`, a list of seed for each RRP. len(rpp_seed_per_mode) have to be the same as 2*modulation_depth+1

omega_m_trans[¶](#omega_m_trans)

Type:

double

Default:

-

For `"TSSD"`, modulation frequency for transverse SSD.

modulation_depth_trans[¶](#modulation_depth_trans)

Type:

int

Default:

0

For `"TSSD"`, depth ‘m’ of modulation. Frequency bandwith = 2m for transverse SSD.

mode2generate_trans[¶](#mode2generate_trans)

Type:

int

Default:

None

For `"TSSD"`, user can choose to generate only one mode, for ebug purpose.

omega_m_longi[¶](#omega_m_longi)

Type:

double

Default:

-

For `"LSSD"`, modulation frequency for longitudinal SSD.

modulation_depth_longi[¶](#modulation_depth_longi)

Type:

int

Default:

0

For `"LSSD"`, depth ‘m’ of modulation. Frequency bandwith = 2m for longitudinal SSD.

mode2generate_longi[¶](#mode2generate_longi)

Type:

int

Default:

None

For `"LSSD"`, user can choose to generate only one mode, for ebug purpose.

time_envelope[¶](#id30)

Type:

a python function or a [time profile](profiles.html)

Default:

`tconstant()`

The temporal envelope of the laser (field, not intensity).

space_envelope[¶](#id31)

Type:

a list of two python functions or two [spatial profiles](profiles.html)

Default:

`lambda y:1.`

The two spatial envelopes \(S_y\) and \(S_z\). It super-impose a user spatial profile on the phase plate spatial profile

7. Defining 2D smoothed beam with periodic Boundary Condition

For two-dimensional simulations with peridic Boundary Condition, you may use the specific laser creator for define smoothed laser beam. It’s the same as previous block, but user have to be carefull of the `fnumber` value and/or the number `N` of element. Giving \(L_y\) the transverse size of the box:

\[fnumber = L_y (k_0 / 2 \pi) / N\]

As an example:

```
import numpy as np

l0 = 2*np.pi # The unit length of the simulation or laser central wavelength
Lsim = [256*l0,64*l0]

myNRPPElement = 16
myfnumber = 64 / myNRPPElement # Lsim[1]/l0 / myNRPPElement

LaserSmoothingPeriodic2D(
....
fnumber = myfnumber,
N       = myNRPPElement,
....
)

```

8. Defining 3D smoothed beam

For three-dimensional simulations, you may use the specific laser creator for define smoothed laser beam:

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
N                              = [6,6],
rpp_random_seed                = 10.,
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

\[\begin{split}\begin{multline}
\widetilde{E}(x,y,z,n=0) = \frac{E_0}{2\sqrt{\pi}} \sqrt{\frac{f_0}{f_0-x}} \mathrm{e}^{ik_0x}\mathrm{e}^{-\frac{ik_0(y^2+z^2)}{2(f_0-x)} } \times \text{...} \\
\text{...} \sum_{N_y} \sum_{N_z} \mathrm{e}^{i (\varphi_N+\delta_N)} \big[\mathrm{erf}(\mathrm{e}^{-\frac{i \pi}{4}} K_0(x)\cdot (a_{N_y+1} - \frac{yf_0}{f_0-x})) - \mathrm{erf}(\mathrm{e}^{-\frac{i \pi}{4}} K_0(x)\cdot (a_{N_y} - \frac{yf_0}{f_0-x})) \big] \times \text{...} \\
\text{...} \big[\mathrm{erf}(\mathrm{e}^{-\frac{i \pi}{4}} K_0(x)\cdot (b_{N_z+1} - \frac{zf_0}{f_0-x})) - \mathrm{erf}(\mathrm{e}^{-\frac{i \pi}{4}} K_0(x)\cdot (b_{N_z} - \frac{zf_0}{f_0-x})) \big]
\end{multline}\end{split}\]

with \(k_0\) the wavenumber, \(E_0\) the field amplitude, \(f_0\) the focal length \(K_0(x)=\lvert k_0(f_0-x)/(2xf_0) \lvert\)
and \(\varphi_N + \delta_N = \varphi_{N_y,N_Z} + \delta_{N_y,N_Z}\) is the random phase, and optical delay induced by each element of the plate (\(\varphi_N=\{0,\pi\}\) for RPP or \([0,2\pi[\) for CPP and \(\delta_N=[0,2\pi[\) for an Echelon).

To avoid space correlation, \(\varphi_{N_y,N_Z}\neq\varphi_{N_y}+\varphi_{N_Z}\) \(\delta_{N_y,N_Z}\neq\delta_{N_y}+\delta_{N_Z}\).

In order to take into account the temporal behaviour of the field and the bandwidth of the beam (smoothing by temporal dispersion), we must consider the field is no longer monochromatic and each mode will have it’s own amplitude and phase, relying on the smoothing technic used (Longitudinal Smoothing by Spectral Dispersion LSSD, Transverse Smoothing by Spectral Dispersion TSSD or Broadband). Each mode routinely produce one `Laser Block`

box_side[¶](#id32)

Type:

a string

Default:

`"xmin"`

Side of the box from which the laser originates: `"xmin"`, `"xmax"`, `"ymin"`,
`"ymax"`, `"zmin"` or `"zmax"`.

In the cases of `"ymin"` or `"ymax"`, replace, in the following profiles,
coordinates y by x, and fields \(B_y\) by \(B_x\).

In the cases of `"zmin"` or `"zmax"`, replace, in the following profiles,
coordinates y by x, coordinates z by y, fields \(B_y\) by \(B_x\)
and fields \(B_z\) by \(B_y\).

a0[¶](#id33)

Type:

double

Default:

-

The normalized vector potential at focus. Note that \(E_0 = (a_0 \omega/N_{tot}) / \sqrt{k_0 (dy)^2 / (2 L_f \pi^2) } / \sqrt{k_0 (dz)^2 / (2 L_f \pi^2)}\) with \(dy=D/N_y\) and \(dz=D/N_z\)
and where D is the effective aperture of the optical system (typically the size of the phase plate)

omega[¶](#id34)

Type:

double

Default:

-

The laser angular frequency.

focus[¶](#id35)

Type:

A list of three floats `[X, Y, Z]`

Default:

`[0,0,0]`

The `X`, `Y` and `Z` positions of the laser focus.

incidence_angle[¶](#id36)

Type:

double

Default:

-

The angle of the laser beam relative to the normal to the injection plane, in radians, in the `X`, `Y` plane.

polarization_phi[¶](#id37)

Type:

double

Default:

-

The angle of the polarization ellipse major axis relative to the X-Y plane, in radians.

ellipticity[¶](#id38)

Type:

double

Default:

-

The polarization ellipticity: 0 for linear and \(\pm 1\) for circular.
Only linear is taking into account for now.

phase_zero[¶](#id39)

Type:

double

Default:

-

An extra phase added to both the envelope and to the carrier wave.

Lf[¶](#id40)

Type:

double

Default:

3.00e6

The focal length in code units

fnumber[¶](#id41)

Type:

double

Default:

-

The ratio \(L_f/D\) where D is the effective aperture of the optical system (typically the size of the phase plate)

N[¶](#id42)

Type:

a list of two int

Default:

`[ 0, 0 ]`

List of number of phase plate element per direction (for Ntot=36, then `N=[6,6]`)

rpp_random_seed[¶](#id43)

Type:

integer

Default:

10

`None` or an int to chose a seed in order to define each phase element of a random phase plate (`None` is equal no random, all element have zero phase-shift)

temporal_smoothing[¶](#id44)

Type:

a string

Default:

None

Type of temporal smoothing `None/"Broadband"/"TSSD"/"LSSD"`

temporal_smoothing_random_seed[¶](#id45)

Type:

integer

Default:

42

Seed in order to have a Random Phase for each mode for `"Broadband Laser"`

omega_m[¶](#id46)

Type:

a double

Default:

-

Modulation frequency for `"Broadband Laser"`. It’s a fraction of the central angular frequency.

modulation_depth[¶](#id47)

Type:

an int

Default:

0

For `"Broadband Laser"`, depth ‘m’ of modulation and frequency bandwith = 2m

rpp_per_mode[¶](#id48)

Type:

bool

Default:

False

For `"Broadband Laser"`, Change the Random Phase Plate for each mode when set to `True`

rpp_seed_per_mode[¶](#id49)

Type:

a list of int

Default:

[42]

For `"Broadband Laser"`, a list of seed for each RRP. len(rpp_seed_per_mode) have to be the same as 2*modulation_depth+1

omega_m_trans[¶](#id50)

Type:

double

Default:

-

For `"TSSD"`, modulation frequency for transverse SSD.

modulation_depth_trans[¶](#id51)

Type:

int

Default:

0

For `"TSSD"`, depth ‘m’ of modulation. Frequency bandwith = 2m for transverse SSD.

mode2generate_trans[¶](#id52)

Type:

int

Default:

None

For `"TSSD"`, user can choose to generate only one mode, for ebug purpose.

omega_m_longi[¶](#id53)

Type:

double

Default:

-

For `"LSSD"`, modulation frequency for longitudinal SSD.

modulation_depth_longi[¶](#id54)

Type:

int

Default:

0

For `"LSSD"`, depth ‘m’ of modulation. Frequency bandwith = 2m for longitudinal SSD.

mode2generate_longi[¶](#id55)

Type:

int

Default:

None

For `"LSSD"`, user can choose to generate only one mode, for ebug purpose.

direction[¶](#direction)

Type:

a string

Default:

‘y’

Direction of transverse TSSD : ‘y’ or ‘z’

time_envelope[¶](#id56)

Type:

a python function or a [time profile](profiles.html)

Default:

`tconstant()`

The temporal envelope of the laser (field, not intensity).

space_envelope[¶](#id57)

Type:

a list of two python functions or two [spatial profiles](profiles.html)

Default:

`lambda y,z:1.`

The two spatial envelopes \(S_y\) and \(S_z\). It super-impose a user spatial profile on the phase plate spatial profile

9. Defining 3D smoothed beam with periodic Boundary Condition

For three-dimensional simulations with peridic Boundary Condition, you may use the specific laser creator for define smoothed laser beam. It’s the same as previous block, but user have to paid attention in the `fnumber` value and/or the number `N` of element. Giving \(L_y\) the transverse size of the box:

\[\begin{split}fnumber = L_y (k_0 / 2 \pi) / N_y \\
fnumber = L_z (k_0 / 2 \pi) / N_z\end{split}\]

As an example:

```
import numpy as np

l0 = 2*np.pi # The unit length of the simulation or laser central wavelength
Lsim = [256*l0,64*l0,128*l0]

myNRPPElement = [16,32]
myfnumber = 64 / myNRPPElement[0] # Lsim[1]/l0 / myNRPPElement[0]
# Same for myfnumber = 128 / myNRPPElement[1] # Lsim[2]/l0 / myNRPPElement[1]

LaserSmoothingPeriodic2D(
....
fnumber = myfnumber,
N       = myNRPPElement,
....
)

```

10. Defining a gaussian wave with Azimuthal Fourier decomposition

For simulations with `"AMcylindrical"` geometry, you may use the simplified laser creator:

```
LaserGaussianAM(
box_side         = "xmin",
a0               = 1.,
omega            = 1.,
focus            = [50.],
waist            = 3.,
polarization_phi = 0.,
ellipticity      = 0.,
time_envelope    = tconstant()
)

```

Note that here the focus is given in [x] coordinates, since it propagates on the r=0 axis .

7. Defining a generic wave at some distance from the boundary

In some cases, the laser field is not known at the box boundary, but rather at some
plane inside the box. Smilei can pre-calculate the corresponding wave at the boundary
using the angular spectrum method. This technique is only available in 2D and 3D
cartesian geometries and requires the python packages numpy.
A [detailed explanation](laser_offset.html) of the method is available.
The laser is introduced using:

```
LaserOffset(
box_side               = "xmin",
space_time_profile     = [ By_profile, Bz_profile ],
offset                 = 10.,
extra_envelope          = tconstant(),
keep_n_strongest_modes = 100,
angle = 10./180.*3.14159
)

```

space_time_profile[¶](#id58)

Type:

A list of two python functions

The magnetic field profiles at some arbitrary plane, as a function of space and time.
The arguments of these profiles are `(y,t)` in 2D and `(y,z,t)` in 3D.

offset[¶](#offset)

The distance from the box boundary to the plane where [`space_time_profile`](#id69)
is defined.

extra_envelope[¶](#extra_envelope)

Type:

a python function or a [python profile](profiles.html)

Default:

`lambda *z: 1.`, which means a profile of value 1 everywhere

An extra envelope applied at the boundary, on top of the [`space_time_profile`](#id69).
This envelope takes two arguments (`y`, `t`) in 2D, and three arguments (`y`, `z`, `t`)
in 3D.
As the wave propagation technique stores a limited number of Fourier modes (in the time
domain) of the wave, some periodicity can be obtained in the actual laser.
One may thus observe that the laser pulse is repeated several times.
The envelope can be used to remove these spurious repetitions.

keep_n_strongest_modes[¶](#keep_n_strongest_modes)

Default:

100

The number of temporal Fourier modes that are kept during the pre-processing.
See [this page](laser_offset.html) for more details.

angle[¶](#angle)

Default:

-

Angle between the boundary and the profile’s plane, the rotation being around \(z\).
See [this page](laser_offset.html) for more details.

fft_time_window[¶](#fft_time_window)

Default:

[`simulation_time`](#simulation_time)

Time during which the `space_time_profile` is sampled (calculating the
`LaserOffset` on the whole simulation duration can be costly). Note that
the Fourier approach will naturally repeat the signal periodically.

fft_time_step[¶](#fft_time_step)

Default:

[`timestep`](#timestep)

Temporal step between each sample of the `space_time_profile`.
Chosing a larger step can help reduce the memory load but will remove high temporal frequencies.

number_of_processes[¶](#number_of_processes)

Default:

all available processes

The number of MPI processes that will be used for computing the `LaserOffset`.
Using more processes computes the FFT faster, but too many processes may
be very costly in communication. In addition, using too few may not allow
the arrays to fit in memory.

file[¶](#file)

Default:

`None`

The path to a `LaserOffset*.h5` file generated from a previous simulation. This option
can help reduce the computation time by re-using the `LaserOffset` computation
from a previous simulation.
