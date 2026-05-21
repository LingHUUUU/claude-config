## Species[¶](#species "Link to this heading")

Each species has to be defined in a `Species` block:

```
Species(
    name      = "electrons1",
    position_initialization = "random",
    momentum_initialization = "maxwell-juettner",
    regular_number = [],
    particles_per_cell = 100,
    mass = 1.,
    atomic_number = None,
    #maximum_charge_state = None,
    number_density = 10.,
    # charge_density = None,
    charge = -1.,
    mean_velocity = [0.],
    #mean_velocity_AM = [0.],
    temperature = [1e-10],
    boundary_conditions = [
        ["reflective", "reflective"],
    #    ["periodic", "periodic"],
    #    ["periodic", "periodic"],
    ],
    # thermal_boundary_temperature = None,
    # thermal_boundary_velocity = None,
    time_frozen = 0.0,
    # ionization_model = "none",
    # ionization_electrons = None,
    # ionization_rate = None,
    is_test = False,
    pusher = "boris",

    # Radiation reaction, for particles only:
    radiation_model = "none",
    radiation_photon_species = "photon",
    radiation_photon_sampling = 1,
    radiation_photon_gamma_threshold = 2,
    radiation_max_emissions = 10,

    # Relativistic field initialization:
    relativistic_field_initialization = "False",

    # For photon species only:
    multiphoton_Breit_Wheeler = ["electron","positron"],
    multiphoton_Breit_Wheeler_sampling = [1,1]

    # Merging
    merging_method = "vranic_spherical",
    merge_every = 5,
    merge_min_particles_per_cell = 16,
    merge_max_packet_size = 4,
    merge_min_packet_size = 4,
    merge_momentum_cell_size = [16,16,16],
)
```

name[¶](#name "Link to this definition")
:   The name you want to give to this species.
    It should be more than one character and can not start with `"m_"`.

position\_initialization[¶](#position_initialization "Link to this definition")
:   The method for initialization of particle positions. Options are:

    - `"regular"` for regularly spaced. See [`regular_number`](#id18 "regular_number").
    - `"random"` for randomly distributed.
    - `"centered"` for centered in each cell (not supported in `AMcylindrical` geometry.
    - The [`name`](#id93 "name") of another species from which the positions are copied.
      The *source* species must have positions initialized using one of the three
      other options above, and must be defined before this species.
    - A *numpy* array or an *HDF5* file defining all the positions of the particles.
      In this case you must also provide the weight of each particle (see [Macro-particle weights](../Understand/units.html#weights)).
      See [Initialize particles from an array or a file](particle_initialization.html).

regular\_number[¶](#regular_number "Link to this definition")
:   Type:
    :   A list of as many integers as the simulation dimension

    When `position_initialization = "regular"`, this sets the number of evenly-spaced
    particles per cell in each direction: `[Nx, Ny, Nz]` in cartesian geometries and
    `[Nx, Nr, Ntheta]` in `AMcylindrical` in which case we recommend
    `Ntheta` \(\geq 4\times (\) `number_of_AM` \(-1)\).
    If unset, `particles_per_cell` must be a power of the simulation dimension,
    for instance, a power of 2 in `2Dcartesian`.

momentum\_initialization[¶](#momentum_initialization "Link to this definition")
:   The method for initialization of particle momenta. Options are:

    - `"maxwell-juettner"` for a relativistic maxwellian (see [how it is done](maxwell-juttner.html))
    - `"rectangular"` for a rectangular distribution
    - `"cold"` for zero temperature
    - A *numpy* array or an *HDF5* file defining all the momenta of the particles.
      See [Initialize particles from an array or a file](particle_initialization.html).

    The first 2 distributions depend on the parameter [`temperature`](#id14 "temperature") explained below.

particles\_per\_cell[¶](#particles_per_cell "Link to this definition")
:   Type:
    :   float or [profile](profiles.html)

    The number of particles per cell.

mass[¶](#mass "Link to this definition")
:   The mass of particles, in units of the electron mass \(m\_e\).

atomic\_number[¶](#atomic_number "Link to this definition")
:   Default:
    :   0

    The atomic number of the particles (must be below 101).
    It is required for ionization and nuclear reactions.
    It has an effect on collisions by accounting for the atomic screening
    (if not defined, or set to 0 for ions, screening is discarded as if
    the ion was fully ionized).

maximum\_charge\_state[¶](#maximum_charge_state "Link to this definition")
:   Default:
    :   0

    The maximum charge state of a species for which the ionization model is `"from_rate"`.

number\_density[¶](#number_density "Link to this definition")
