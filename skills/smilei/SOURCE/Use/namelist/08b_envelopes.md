2. Defining the wave envelopes

> ```
> Laser(
>     box_side       = "xmin",
>     omega          = 1.,
>     chirp_profile  = tconstant(),
>     time_envelope  = tgaussian(),
>     space_envelope = [ By_profile  , Bz_profile   ],
>     phase          = [ PhiY_profile, PhiZ_profile ],
>     delay_phase    = [ 0., 0. ]
> )
> ```
>
> This implements a wave of the form:
>
> \[ \begin{align}\begin{aligned}B\_y(\mathbf{x}, t) = S\_y(\mathbf{x})\; T\left(t-t\_{0y}\right)
> \;\sin\left( \omega(t) t - \phi\_y(\mathbf{x}) \right)\\B\_z(\mathbf{x}, t) = S\_z(\mathbf{x})\; T\left(t-t\_{0z}\right)
> \;\sin\left( \omega(t) t - \phi\_z(\mathbf{x}) \right)\end{aligned}\end{align} \]
>
> where \(T\) is the temporal envelope, \(S\_y\) and \(S\_z\) are the
> spatial envelopes, \(\omega\) is the time-varying frequency,
> \(\phi\_y\) and \(\phi\_z\) are the phases, and we defined the delays
> \(t\_{0y} = (\phi\_y(\mathbf{x})-\varphi\_y)/\omega(t)\) and
> \(t\_{0z} = (\phi\_z(\mathbf{x})-\varphi\_z)/\omega(t)\).
>
> omega[¶](#omega "Link to this definition")
> :   Default:
>
>     The laser angular frequency.
>
> chirp\_profile[¶](#chirp_profile "Link to this definition")
> :   Type:
>     :   a *python* function or a [time profile](profiles.html)
>
>     Default:
>     :   `tconstant()`
>
>     The variation of the laser frequency over time, such that
>     \(\omega(t)=\) `omega` x `chirp_profile` \((t)\).
>
> Warning
>
> This definition of the chirp profile is not standard.
> Indeed, \(\omega(t)\) as defined here **is not** the instantaneous frequency, \(\omega\_{\rm inst}(t)\),
> which is obtained from the time derivative of the phase \(\omega(t) t\).
>
> Should one define the chirp as \(C(t) = \omega\_{\rm inst}(t)/\omega\) (with \(\omega\) defined by the input
> parameter \(\mathtt{omega}\)), the user can easily obtain the corresponding chirp profile as defined in
> **Smilei** as:
>
> \[\mathtt{chirp\\_profile}(t) = \frac{1}{t} \int\_0^t dt' C(t')\,.\]
>
> Let us give as an example the case of a *linear chirp*, with the instantaneous frequency
> \(\omega\_{\rm inst}(t) = \omega [1+\alpha\,\omega(t-t\_0)]\).
> \(C(t) = 1+\alpha\,\omega(t-t\_0)\). The corresponding input chirp profile reads:
>
> \[\mathtt{chirp\\_profile}(t) = 1 - \alpha\, \omega t\_0 + \frac{\alpha}{2} \omega t\]
>
> Similarly, for a *geometric (exponential) chirp* such that \(\omega\_{\rm inst}(t) = \omega\, \alpha^{\omega t}\),
> \(C(t) = \alpha^{\omega t}\), and the corresponding input chirp profile reads:
>
> \[\mathtt{chirp\\_profile}(t) = \frac{\alpha^{\omega t} - 1}{\omega t \, \ln \alpha}\,.\]
>
> time\_envelope[¶](#id22 "Link to this definition")
> :   Type:
>     :   a *python* function or a [time profile](profiles.html)
>
>     Default:
>     :   `tconstant()`
>
>     The temporal envelope of the laser (field, not intensity).
>
> space\_envelope[¶](#space_envelope "Link to this definition")
> :   Type:
>     :   a list of two *python* functions or two [spatial profiles](profiles.html)
>
>     Default:
>     :   `[ 1., 0. ]`
>
>     The two spatial envelopes \(S\_y\) and \(S\_z\).
>
> phase[¶](#phase "Link to this definition")
> :   Type:
>     :   a list of two *python* functions or two [spatial profiles](profiles.html)
>
>     Default:
>     :   `[ 0., 0. ]`
>
>     The two spatially-varying phases \(\phi\_y\) and \(\phi\_z\).
>
> delay\_phase[¶](#delay_phase "Link to this definition")
> :   Type:
>     :   a list of two floats
>
>     Default:
>     :   `[ 0., 0. ]`
>
>     An extra delay for the time envelopes of \(B\_y\) and \(B\_z\),
>     expressed in terms of phase (\(=\omega t\)). This delay is applied to the
>     [`time_envelope`](#id63 "time_envelope"), but not to the carrier wave.
>     This option is useful in the
>     case of elliptical polarization where the two temporal profiles should have a slight
>     delay due to the mismatched [`phase`](#phase "phase").

3. Defining a 1D planar wave
