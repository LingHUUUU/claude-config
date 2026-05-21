time\_fields\_frozen[¶](#time_fields_frozen "Link to this definition")
:   Default:

    Time, at the beginning of the simulation, during which fields are frozen.

reference\_angular\_frequency\_SI[¶](#reference_angular_frequency_SI "Link to this definition")
:   The value of the reference angular frequency \(\omega\_r\) in SI units,
    **only needed when collisions, ionization, radiation losses
    or multiphoton Breit-Wheeler pair creation are requested**.
    This frequency is related to the normalization length according to \(L\_r\omega\_r = c\)
    (see [Units](../Understand/units.html)).

print\_every[¶](#print_every "Link to this definition")
:   Number of timesteps between each info output on screen. By default, 10 outputs per
    simulation.

print\_expected\_disk\_usage[¶](#print_expected_disk_usage "Link to this definition")
:   Default:
    :   `True`

    If `False`, the calculation of the expected disk usage, that is usually printed in the
    standard output, is skipped. This might be useful in rare cases where this calculation
    is costly.

random\_seed[¶](#random_seed "Link to this definition")
:   Default:
    :   0

    The value of the random seed. Each patch has its own random number generator, with a seed
    equal to `random_seed` + the index of the patch.

number\_of\_AM[¶](#number_of_AM "Link to this definition")
:   Type:
    :   integer

    Default:
    :   2

    The number of azimuthal modes used for the Fourier decomposition in `"AMcylindrical"` geometry.
    The modes range from mode 0 to mode `"number_of_AM-1"`.

number\_of\_AM\_classical\_Poisson\_solver[¶](#number_of_AM_classical_Poisson_solver "Link to this definition")
:   Default:
    :   1

    The number of azimuthal modes used for the field initialization with non relativistic Poisson solver in `"AMcylindrical"` geometry.
    Note that this number must be lower or equal to the number of modes of the simulation.

number\_of\_AM\_relativistic\_field\_initialization[¶](#number_of_AM_relativistic_field_initialization "Link to this definition")
:   Default:
    :   1

    The number of azimuthal modes used for the relativistic field initialization in `"AMcylindrical"` geometry.
    Note that this number must be lower or equal to the number of modes of the simulation.

use\_BTIS3\_interpolation[¶](#use_BTIS3_interpolation "Link to this definition")
:   Default:
    :   `False`

    If `True`, the B-translated interpolation scheme 3 (or B-TIS3) described in [PIC algorithms](../Understand/algorithms.html) is used.

custom\_oversize[¶](#custom_oversize "Link to this definition")
:   Type:
    :   integer

    Default:
    :   2

    The number of ghost-cell for each patches. The default value is set accordingly with
    the `interpolation_order` value.

---
