> omega\_m[¶](#omega_m "Link to this definition")
> :   Type:
>     :   a double
>
>     Default:
>
>     Modulation frequency for `"Broadband Laser"`. It’s a fraction of the central angular frequency.
>
> modulation\_depth[¶](#modulation_depth "Link to this definition")
> :   Type:
>     :   an int
>
>     Default:
>     :   0
>
>     For `"Broadband Laser"`, depth *‘m’* of modulation and frequency bandwith = 2m
>
> rpp\_per\_mode[¶](#rpp_per_mode "Link to this definition")
> :   Type:
>     :   bool
>
>     Default:
>     :   False
>
>     For `"Broadband Laser"`, Change the Random Phase Plate for each mode when set to `True`
>
> rpp\_seed\_per\_mode[¶](#rpp_seed_per_mode "Link to this definition")
> :   Type:
>     :   a list of *int*
>
>     Default:
>     :   [42]
>
>     For `"Broadband Laser"`, a list of seed for each RRP. len(rpp\_seed\_per\_mode) have to be the same as 2\*modulation\_depth+1
>
> omega\_m\_trans[¶](#omega_m_trans "Link to this definition")
> :   Type:
>     :   double
>
>     Default:
>
>     For `"TSSD"`, modulation frequency for transverse SSD.
>
> modulation\_depth\_trans[¶](#modulation_depth_trans "Link to this definition")
> :   Type:
>     :   int
>
>     Default:
>     :   0
>
>     For `"TSSD"`, depth ‘m’ of modulation. Frequency bandwith = 2m for transverse SSD.
>
> mode2generate\_trans[¶](#mode2generate_trans "Link to this definition")
> :   Type:
>     :   int
>
>     Default:
>     :   None
>
>     For `"TSSD"`, user can choose to generate only one mode, for ebug purpose.
>
> omega\_m\_longi[¶](#omega_m_longi "Link to this definition")
> :   Type:
>     :   double
>
>     Default:
>
>     For `"LSSD"`, modulation frequency for longitudinal SSD.
>
> modulation\_depth\_longi[¶](#modulation_depth_longi "Link to this definition")
> :   Type:
>     :   int
>
>     Default:
>     :   0
>
>     For `"LSSD"`, depth ‘m’ of modulation. Frequency bandwith = 2m for longitudinal SSD.
>
> mode2generate\_longi[¶](#mode2generate_longi "Link to this definition")
> :   Type:
>     :   int
>
>     Default:
>     :   None
>
>     For `"LSSD"`, user can choose to generate only one mode, for ebug purpose.
>
> time\_envelope[¶](#id30 "Link to this definition")
> :   Type:
>     :   a *python* function or a [time profile](profiles.html)
>
>     Default:
>     :   `tconstant()`
>
>     The temporal envelope of the laser (field, not intensity).
>
> space\_envelope[¶](#id31 "Link to this definition")
> :   Type:
>     :   a list of two *python* functions or two [spatial profiles](profiles.html)
>
>     Default:
>     :   `lambda y:1.`
>
>     The two spatial envelopes \(S\_y\) and \(S\_z\). It super-impose a user spatial profile on the phase plate spatial profile

7. Defining 2D smoothed beam with periodic Boundary Condition

For two-dimensional simulations with peridic Boundary Condition, you may use the specific laser creator for define smoothed laser beam. It’s the same as previous block, but user have to be carefull of the `fnumber` value and/or the number `N` of element. Giving \(L\_y\) the transverse size of the box:

> \[fnumber = L\_y (k\_0 / 2 \pi) / N\]

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
