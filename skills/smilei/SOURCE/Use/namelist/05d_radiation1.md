is\_test[¶](#is_test "Link to this definition")
:   Default:
    :   `False`

    Flag for test particles. If `True`, this species will contain only test particles
    which do not participate in the charge and currents.

pusher[¶](#pusher "Link to this definition")
:   Default:
    :   `"boris"`

    Type of pusher to be used for this species. Options are:

    - `"boris"`: The relativistic Boris pusher
    - `"borisnr"`: The non-relativistic Boris pusher
    - `"vay"`: The relativistic pusher of J. L. Vay
    - `"higueracary"`: The relativistic pusher of A. V. Higuera and J. R. Cary
    - `"norm"`: For photon species only (rectilinear propagation)
    - `"ponderomotive_boris"`: modified relativistic Boris pusher for species interacting with the laser envelope model. Valid only if the species has non-zero mass
    - `"borisBTIS3"`: as `"boris"`, but using B fields interpolated with the B-TIS3 scheme.
    - `"ponderomotive_borisBTIS3"`: as `"ponderomotive_boris"`, but using B fields interpolated with the B-TIS3 scheme.

    **WARNING**: `"borisBTIS3"` and `"ponderomotive_borisBTIS3"` can be used only when `use_BTIS3_interpolation=True` in the `Main` block.

radiation\_model[¶](#radiation_model "Link to this definition")
:   Default:
    :   `"none"`

    The **radiation reaction** model used for this species (see [High-energy photon emission & radiation reaction](../Understand/radiation_loss.html)).

    - `"none"`: no radiation
    - `"Landau-Lifshitz"` (or `ll`): Landau-Lifshitz model approximated for high energies
    - `"corrected-Landau-Lifshitz"` (or `cll`): with quantum correction
    - `"Niel"`: a [stochastic radiation model](https://arxiv.org/abs/1707.02618) based on the work of Niel et al..
    - `"Monte-Carlo"` (or `mc`): Monte-Carlo radiation model. This model can be configured to generate macro-photons with [`radiation_photon_species`](#radiation_photon_species "radiation_photon_species").

    This parameter cannot be assigned to photons (mass = 0).

    Radiation is emitted only with the `"Monte-Carlo"` model when
    [`radiation_photon_species`](#radiation_photon_species "radiation_photon_species") is defined.

radiation\_photon\_species[¶](#radiation_photon_species "Link to this definition")
:   The [`name`](#id93 "name") of the photon species in which the Monte-Carlo [`radiation_model`](#radiation_model "radiation_model")
    will generate macro-photons. If unset (or `None`), no macro-photon will be created.
    The *target* photon species must be have its mass set to 0, and appear *after* the
    particle species in the namelist.

    This parameter cannot be assigned to photons (mass = 0).

radiation\_photon\_sampling[¶](#radiation_photon_sampling "Link to this definition")
:   Default:
    :   `1`

    The number of macro-photons generated per emission event, when the macro-photon creation
    is activated (see [`radiation_photon_species`](#radiation_photon_species "radiation_photon_species")). The total macro-photon weight
    is still conserved.

    A large number may rapidly slow down the performances and lead to memory saturation.

    This parameter cannot be assigned to photons (mass = 0).

radiation\_max\_emissions[¶](#radiation_max_emissions "Link to this definition")
:   Default:
    :   `10`

    The maximum number of emission Monte-Carlo event a macro-particle can undergo during a timestep.
    Since this value is used to allocate some buffers, a high value can saturate memory.

    This parameter cannot be assigned to photons (mass = 0).

radiation\_photon\_gamma\_threshold[¶](#radiation_photon_gamma_threshold "Link to this definition")
