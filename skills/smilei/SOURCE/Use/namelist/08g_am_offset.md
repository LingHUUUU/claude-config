9. Defining 3D smoothed beam with periodic Boundary Condition

For three-dimensional simulations with peridic Boundary Condition, you may use the specific laser creator for define smoothed laser beam. It’s the same as previous block, but user have to paid attention in the `fnumber` value and/or the number `N` of element. Giving \(L\_y\) the transverse size of the box:

> \[\begin{split}fnumber = L\_y (k\_0 / 2 \pi) / N\_y \\
> fnumber = L\_z (k\_0 / 2 \pi) / N\_z\end{split}\]

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

> For simulations with `"AMcylindrical"` geometry, you may use the simplified laser creator:
>
> ```
> LaserGaussianAM(
>     box_side         = "xmin",
>     a0               = 1.,
>     omega            = 1.,
>     focus            = [50.],
>     waist            = 3.,
>     polarization_phi = 0.,
>     ellipticity      = 0.,
>     time_envelope    = tconstant()
> )
> ```
>
> Note that here the focus is given in [x] coordinates, since it propagates on the r=0 axis .

7. Defining a generic wave at some distance from the boundary

> In some cases, the laser field is not known at the box boundary, but rather at some
> plane inside the box. Smilei can pre-calculate the corresponding wave at the boundary
> using the *angular spectrum method*. This technique is only available in 2D and 3D
> cartesian geometries and requires the python packages *numpy*.
> A [detailed explanation](laser_offset.html) of the method is available.
> The laser is introduced using:
>
> ```
> LaserOffset(
>     box_side               = "xmin",
>     space_time_profile     = [ By_profile, Bz_profile ],
>     offset                 = 10.,
>     extra_envelope          = tconstant(),
>     keep_n_strongest_modes = 100,
>     angle = 10./180.*3.14159
> )
> ```
>
> space\_time\_profile[¶](#id58 "Link to this definition")
> :   Type:
>     :   A list of two *python* functions
>
>     The magnetic field profiles at some arbitrary plane, as a function of space and time.
>     The arguments of these profiles are `(y,t)` in 2D and `(y,z,t)` in 3D.
>
> offset[¶](#offset "Link to this definition")
> :   The distance from the box boundary to the plane where [`space_time_profile`](#id69 "space_time_profile")
>     is defined.
>
> extra\_envelope[¶](#extra_envelope "Link to this definition")
> :   Type:
>     :   a *python* function or a [python profile](profiles.html)
>
>     Default:
>     :   `lambda *z: 1.`, which means a profile of value 1 everywhere
>
>     An extra envelope applied at the boundary, on top of the [`space_time_profile`](#id69 "space_time_profile").
>     This envelope takes two arguments (`y`, `t`) in 2D, and three arguments (`y`, `z`, `t`)
>     in 3D.
>     As the wave propagation technique stores a limited number of Fourier modes (in the time
>     domain) of the wave, some periodicity can be obtained in the actual laser.
>     One may thus observe that the laser pulse is repeated several times.
>     The envelope can be used to remove these spurious repetitions.
>
> keep\_n\_strongest\_modes[¶](#keep_n_strongest_modes "Link to this definition")
> :   Default:
>     :   100
>
>     The number of temporal Fourier modes that are kept during the pre-processing.
>     See [this page](laser_offset.html) for more details.
>
> angle[¶](#angle "Link to this definition")
> :   Default:
>
>     Angle between the boundary and the profile’s plane, the rotation being around \(z\).
>     See [this page](laser_offset.html) for more details.
>
> fft\_time\_window[¶](#fft_time_window "Link to this definition")
> :   Default:
>     :   [`simulation_time`](#simulation_time "simulation_time")
>
>     Time during which the `space_time_profile` is sampled (calculating the
>     `LaserOffset` on the whole simulation duration can be costly). Note that
>     the Fourier approach will naturally repeat the signal periodically.
>
> fft\_time\_step[¶](#fft_time_step "Link to this definition")
> :   Default:
>     :   [`timestep`](#timestep "timestep")
>
>     Temporal step between each sample of the `space_time_profile`.
>     Chosing a larger step can help reduce the memory load but will remove high temporal frequencies.
>
> number\_of\_processes[¶](#number_of_processes "Link to this definition")
> :   Default:
>     :   *all available processes*
>
>     The number of MPI processes that will be used for computing the `LaserOffset`.
>     Using more processes computes the FFT faster, but too many processes may
>     be very costly in communication. In addition, using too few may not allow
>     the arrays to fit in memory.
>
> file[¶](#file "Link to this definition")
> :   Default:
>     :   `None`
>
>     The path to a `LaserOffset*.h5` file generated from a previous simulation. This option
>     can help reduce the computation time by re-using the `LaserOffset` computation
>     from a previous simulation.

---
