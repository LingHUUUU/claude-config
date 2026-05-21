number\_density[¶](#number_density "Link to this definition")

charge\_density[¶](#charge_density "Link to this definition")
:   Type:
    :   float or [profile](profiles.html)

    The absolute value of the charge density or number density (choose one only)
    of the particle distribution, in units of the reference density \(N\_r\) (see [Units](../Understand/units.html)).

charge[¶](#charge "Link to this definition")
:   Type:
    :   float or [profile](profiles.html)

    The particle charge, in units of the elementary charge \(e\).

mean\_velocity[¶](#mean_velocity "Link to this definition")
:   Type:
    :   a list of 3 floats or [profiles](profiles.html)

    The initial drift velocity of the particles, in units of the speed of light \(c\), in the x, y and z directions.

    **WARNING**: For massless particles, this is actually the momentum in units of \(m\_e c\).

mean\_velocity\_AM[¶](#mean_velocity_AM "Link to this definition")
:   Type:
    :   a list of 3 floats or [profiles](profiles.html)

    The initial drift velocity of the particles, in units of the speed of light \(c\), in the longitudinal, radial and azimuthal directions.
    This entry is available only in `AMcylindrical` velocity and cannot be used if also `mean_velocity` is used in the same `Species`: only one of the two can be chosen.

    **WARNING**: For massless particles, this is actually the momentum in units of \(m\_e c\).

    **WARNING**: The initial cylindrical drift velocity is applied to each particle, thus it can be computationally demanding.

temperature[¶](#temperature "Link to this definition")
:   Type:
    :   a list of 3 floats or [profiles](profiles.html)

    Default:
    :   `1e-10`

    The initial temperature of the particles, in units of \(m\_ec^2\).

boundary\_conditions[¶](#boundary_conditions "Link to this definition")
:   Type:
    :   a list of lists of strings

    Default:
    :   `[["periodic"]]`

    The boundary conditions for the particles of this species.
    Each boundary may have one of the following conditions:
    `"periodic"`, `"reflective"`, `"remove"` (particles are deleted),
    `"stop"` (particle momenta are set to 0), and `"thermalize"`.
    For photon species (`mass=0`), the last two options are not available.

    **Syntax 1:** `[[bc_all]]`, identical for all boundaries.

    **Syntax 2:** `[[bc_X], [bc_Y], ...]`, different depending on x, y or z.

    **Syntax 3:** `[[bc_Xmin, bc_Xmax], ...]`, different on each boundary.

thermal\_boundary\_temperature[¶](#thermal_boundary_temperature "Link to this definition")
:   Default:
    :   None

    A list of floats representing the temperature of the thermal boundaries (those set to
    `"thermalize"` in [`boundary_conditions`](#boundary_conditions "boundary_conditions")) for each spatial coordinate.
    Currently, only the first coordinate (x) is taken into account.

thermal\_boundary\_velocity[¶](#thermal_boundary_velocity "Link to this definition")
:   Default:
    :   []

    A list of floats representing the components of the particles’ drift velocity after
    encountering the thermal boundaries (those set to `"thermalize"` in [`boundary_conditions`](#boundary_conditions "boundary_conditions")).

time\_frozen[¶](#time_frozen "Link to this definition")
