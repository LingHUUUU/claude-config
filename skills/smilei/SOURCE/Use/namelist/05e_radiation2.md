radiation\_photon\_gamma\_threshold[¶](#radiation_photon_gamma_threshold "Link to this definition")
:   Default:
    :   `2`

    The threshold on the photon energy for the macro-photon emission when using the
    radiation reaction Monte-Carlo process.
    Under this threshold, the macro-photon from the radiation reaction Monte-Carlo
    process is not created but still taken into account in the energy balance.
    The default value corresponds to twice the electron rest mass energy that
    is the required energy to decay into electron-positron pairs.

    This parameter cannot be assigned to photons (mass = 0).

relativistic\_field\_initialization[¶](#relativistic_field_initialization "Link to this definition")
:   Default:
    :   `False`

    Flag for relativistic particles. If `True`, the electromagnetic fields of this species will added to the electromagnetic fields already present in the simulation.
    This operation will be performed when time equals [`time_frozen`](#id71 "time_frozen"). See [Field initialization for relativistic species](../Understand/relativistic_fields_initialization.html) for details on the computation of the electromagentic fields of a relativistic species.
    To have physically meaningful results, we recommend to place a species which requires this method of field initialization far from other species, otherwise the latter could experience instantly turned-on unphysical forces by the relativistic species’ fields.

multiphoton\_Breit\_Wheeler[¶](#multiphoton_Breit_Wheeler "Link to this definition")
:   Default:
    :   `[None,None]`

    An list of the [`name`](#id93 "name") of two species: electrons and positrons created through
    the [Multiphoton Breit-Wheeler pair creation](../Understand/multiphoton_Breit_Wheeler.html).
    By default, the process is not activated.

    This parameter can **only** be assigned to photons species (mass = 0).

multiphoton\_Breit\_Wheeler\_sampling[¶](#multiphoton_Breit_Wheeler_sampling "Link to this definition")
:   Default:
    :   `[1,1]`

    A list of two integers: the number of electrons and positrons generated per photon decay
    in the [Multiphoton Breit-Wheeler pair creation](../Understand/multiphoton_Breit_Wheeler.html). The total macro-particle weight is still
    conserved.

    Large numbers may rapidly slow down the performances and lead to memory saturation.

    This parameter can **only** be assigned to photons species (mass = 0).

keep\_interpolated\_fields[¶](#keep_interpolated_fields "Link to this definition")
:   Default:
    :   `[]`

    A list of interpolated fields that should be stored in memory for all particles of this species,
    instead of being located in temporary buffers. These fields can then
    be accessed in some diagnostics such as [particle binning](#diagparticlebinning) or
    [tracking](#diagtrackparticles). The available fields are `"Ex"`, `"Ey"`, `"Ez"`,
    `"Bx"`, `"By"` and `"Bz"`.

    Note that magnetic field components, as they originate from the interpolator,
    are shifted by half a timestep compared to those from the *Fields* diagnostics.

    Additionally, the work done by each component of the electric field is available as
    `"Wx"`, `"Wy"` and `"Wz"`. Contrary to the other interpolated fields, these quantities
    are accumulated over time.

---
