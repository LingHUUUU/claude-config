time\_frozen[¶](#time_frozen "Link to this definition")
:   Default:

    The time during which the particles are “frozen”, in units of \(T\_r\).
    Frozen particles do not move and therefore do not deposit any current density either.
    Nonetheless, they deposit a charge density.
    They are computationally much cheaper than non-frozen particles and oblivious to any EM-fields
    in the simulation. Note that frozen particles can be ionized (this is computationally much cheaper
    if ion motion is not relevant).

ionization\_model[¶](#ionization_model "Link to this definition")
:   Default:
    :   `"none"`

    The model for [field ionization](../Understand/ionization.html#field-ionization):

    - `"tunnel"` for tunnel ionization using [PPT-ADK](../Understand/ionization.html#ppt-adk) (requires species with an [`atomic_number`](#atomic_number "atomic_number"))
    - `"tunnel_full_PPT"` experimental for tunnel ionization using [PPT-ADK with account for magnetic number](../Understand/ionization.html#ppt-adk) (requires species with an [`atomic_number`](#atomic_number "atomic_number"))
    - `"tunnel_envelope_averaged"` for [field ionization with a laser envelope](../Understand/ionization.html#field-ionization-envelope)
    - `"from_rate"`, relying on a [user-defined ionization rate](../Understand/ionization.html#rate-ionization) (requires species with a [`maximum_charge_state`](#maximum_charge_state "maximum_charge_state")).

bsi\_model[¶](#bsi_model "Link to this definition")
:   Default:
    :   `"none"`

    Apply the [Barrier Suppression Ionization](../Understand/ionization.html#barrier-suppression) correction for ionization in strong fields.
    This correction is supported only for `ionization_model` = `"tunnel"` or `tunnel_full_PPT`.
    The available BSI models are:

    - `"Tong_Lin"` for [Tong and Lin](../Understand/ionization.html#tong-lin)’s rate.
    - `"KAG"` for [Kostyukov Artemenko Golovanov](../Understand/ionization.html#kag)’s rate.

ionization\_rate[¶](#ionization_rate "Link to this definition")
:   A python function giving the user-defined ionisation rate as a function of various particle attributes.
    To use this option, the [numpy package](http://www.numpy.org/) must be available in your python installation.
    The function must have one argument, that you may call, for instance, `particles`.
    This object has several attributes `x`, `y`, `z`, `px`, `py`, `pz`, `charge`, `weight` and `id`.
    Each of these attributes are provided as **numpy** arrays where each cell corresponds to one particle.

    The following example defines, for a species with maximum charge state of 2,
    an ionization rate that depends on the initial particle charge
    and linear in the x coordinate:

    ```
    from numpy import exp, zeros_like

    def my_rate(particles):
        rate = zeros_like(particles.x)
        charge_0 = (particles.charge==0)
        charge_1 = (particles.charge==1)
        rate[charge_0] = r0 * particles.x[charge_0]
        rate[charge_1] = r1 * particles.x[charge_1]
        return rate

    Species( ..., ionization_rate = my_rate )
    ```

ionization\_electrons[¶](#ionization_electrons "Link to this definition")
:   The name of the electron species that [`ionization_model`](#ionization_model "ionization_model") uses when creating new electrons.

is\_test[¶](#is_test "Link to this definition")
