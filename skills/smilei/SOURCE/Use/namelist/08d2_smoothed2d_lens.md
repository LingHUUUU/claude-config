> phase\_zero[¶](#phase_zero "Link to this definition")
> :   Type:
>     :   double
>
>     Default:
>
>     An extra phase added to both the envelope and to the carrier wave.
>
> Lf[¶](#Lf "Link to this definition")
> :   Type:
>     :   double
>
>     Default:
>     :   3.00e6
>
>     The focal length in code units
>
> fnumber[¶](#fnumber "Link to this definition")
> :   Type:
>     :   double
>
>     Default:
>
>     The ratio \(L\_f/D\) where D is the effective aperture of the optical system (typically the size of the phase plate)
>
> N[¶](#N "Link to this definition")
> :   Type:
>     :   int
>
>     Default:
>     :   6
>
>     List of number of phase plate element in D
>
> rpp\_random\_seed[¶](#rpp_random_seed "Link to this definition")
> :   Type:
>     :   integer
>
>     Default:
>     :   10
>
>     `None` or an int to chose a seed in order to define each phase element of a random phase plate (`None` is equal no random, all element have zero phase-shift)
>
> temporal\_smoothing[¶](#temporal_smoothing "Link to this definition")
> :   Type:
>     :   a string
>
>     Default:
>     :   None
>
>     Type of temporal smoothing `None/"Broadband"/"TSSD"/"LSSD"`
>
> temporal\_smoothing\_random\_seed[¶](#temporal_smoothing_random_seed "Link to this definition")
> :   Type:
>     :   integer
>
>     Default:
>     :   42
>
>     Seed in order to have a Random Phase for each mode for `"Broadband Laser"`
>
> omega\_m[¶](#omega_m "Link to this definition")
