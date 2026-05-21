>     Default:
>     :   `[ 0, 0 ]`
>
>     List of number of phase plate element per direction (for Ntot=36, then `N=[6,6]`)
>
> rpp\_random\_seed[¶](#id43 "Link to this definition")
> :   Type:
>     :   integer
>
>     Default:
>     :   10
>
>     `None` or an int to chose a seed in order to define each phase element of a random phase plate (`None` is equal no random, all element have zero phase-shift)
>
> temporal\_smoothing[¶](#id44 "Link to this definition")
> :   Type:
>     :   a string
>
>     Default:
>     :   None
>
>     Type of temporal smoothing `None/"Broadband"/"TSSD"/"LSSD"`
>
> temporal\_smoothing\_random\_seed[¶](#id45 "Link to this definition")
> :   Type:
>     :   integer
>
>     Default:
>     :   42
>
>     Seed in order to have a Random Phase for each mode for `"Broadband Laser"`
>
> omega\_m[¶](#id46 "Link to this definition")
> :   Type:
>     :   a double
>
>     Default:
>
>     Modulation frequency for `"Broadband Laser"`. It’s a fraction of the central angular frequency.
>
> modulation\_depth[¶](#id47 "Link to this definition")
> :   Type:
>     :   an int
>
>     Default:
>     :   0
>
>     For `"Broadband Laser"`, depth *‘m’* of modulation and frequency bandwith = 2m
>
> rpp\_per\_mode[¶](#id48 "Link to this definition")
> :   Type:
>     :   bool
>
>     Default:
>     :   False
>
>     For `"Broadband Laser"`, Change the Random Phase Plate for each mode when set to `True`
>
> rpp\_seed\_per\_mode[¶](#id49 "Link to this definition")
> :   Type:
>     :   a list of *int*
>
>     Default:
>     :   [42]
>
>     For `"Broadband Laser"`, a list of seed for each RRP. len(rpp\_seed\_per\_mode) have to be the same as 2\*modulation\_depth+1
>
> omega\_m\_trans[¶](#id50 "Link to this definition")
> :   Type:
>     :   double
>
>     Default:
>
>     For `"TSSD"`, modulation frequency for transverse SSD.
>
> modulation\_depth\_trans[¶](#id51 "Link to this definition")
> :   Type:
>     :   int
>
>     Default:
>     :   0
>
>     For `"TSSD"`, depth ‘m’ of modulation. Frequency bandwith = 2m for transverse SSD.
>
> mode2generate\_trans[¶](#id52 "Link to this definition")
> :   Type:
>     :   int
>
>     Default:
>     :   None
>
>     For `"TSSD"`, user can choose to generate only one mode, for ebug purpose.
>
> omega\_m\_longi[¶](#id53 "Link to this definition")
> :   Type:
>     :   double
>
>     Default:
>
>     For `"LSSD"`, modulation frequency for longitudinal SSD.
>
> modulation\_depth\_longi[¶](#id54 "Link to this definition")
> :   Type:
>     :   int
>
>     Default:
>     :   0
>
>     For `"LSSD"`, depth ‘m’ of modulation. Frequency bandwith = 2m for longitudinal SSD.
>
> mode2generate\_longi[¶](#id55 "Link to this definition")
> :   Type:
>     :   int
>
>     Default:
>     :   None
>
>     For `"LSSD"`, user can choose to generate only one mode, for ebug purpose.
>
> direction[¶](#direction "Link to this definition")
> :   Type:
>     :   a string
>
>     Default:
>     :   ‘y’
>
>     Direction of transverse TSSD : ‘y’ or ‘z’
>
> time\_envelope[¶](#id56 "Link to this definition")
> :   Type:
>     :   a *python* function or a [time profile](profiles.html)
>
>     Default:
>     :   `tconstant()`
>
>     The temporal envelope of the laser (field, not intensity).
>
> space\_envelope[¶](#id57 "Link to this definition")
> :   Type:
>     :   a list of two *python* functions or two [spatial profiles](profiles.html)
>
>     Default:
>     :   `lambda y,z:1.`
>
>     The two spatial envelopes \(S\_y\) and \(S\_z\). It super-impose a user spatial profile on the phase plate spatial profile

9. Defining 3D smoothed beam with periodic Boundary Condition
