## Particle Injector[¶](#particle-injector "Link to this heading")

Injectors enable to inject macro-particles in the simulation domain from the boundaries.
By default, some parameters that are not specified are inherited from the associated [`species`](#id99 "species").

Each particle injector has to be defined in a `ParticleInjector` block:

```
ParticleInjector(
    name      = "injector1",
    species   = "electrons1",
    box_side  = "xmin",
    time_envelope = tgaussian(start=0, duration=10., order=4),

    # Parameters inherited from the associated ``species`` by default

    position_initialization = "species",
    momentum_initialization = "rectangular",
    mean_velocity = [0.5,0.,0.],
    temperature = [1e-30],
    number_density = 1,
    particles_per_cell = 16,
)
```

name[¶](#id9 "Link to this definition")
:   The name you want to give to this injector.
    If you do not specify a name, it will be attributed automatically.
    The name is useful if you want to inject particles at the same position of another injector.

species[¶](#id10 "Link to this definition")
:   The name of the species in which to inject the new particles

box\_side[¶](#box_side "Link to this definition")
:   From where the macro-particles are injected. Options are:

    - `"xmin"`
    - `"xmax"`
    - `"ymin"`
    - `"ymax"`
    - `"zmax"`
    - `"zmin"`

time\_envelope[¶](#time_envelope "Link to this definition")
:   Type:
    :   a *python* function or a [time profile](profiles.html)

    Default:
    :   `tconstant()`

    The temporal envelope of the injector.

position\_initialization[¶](#id11 "Link to this definition")
:   Default:
    :   parameters provided the species

    The method for initialization of particle positions. Options are:

    - `"species"` or empty `""`: injector uses the option of the specified [`species`](#id99 "species").
    - `"regular"` for regularly spaced. See [`regular_number`](#id18 "regular_number").
    - `"random"` for randomly distributed
    - `"centered"` for centered in each cell
    - The [`name`](#id93 "name") of another injector from which the positions are copied.
      This option requires (1) that the *target* injector’s positions are initialized
      using one of the three other options above.

momentum\_initialization[¶](#id12 "Link to this definition")
:   Default:
    :   parameters provided the species

    The method for initialization of particle momenta. Options are:

    - `"species"` or empty `""`: injector uses the option of the specified [`species`](#id99 "species").
    - `"maxwell-juettner"` for a relativistic maxwellian (see [how it is done](maxwell-juttner.html))
    - `"rectangular"` for a rectangular distribution

mean\_velocity[¶](#id13 "Link to this definition")
:   Type:
    :   a list of 3 floats or [profiles](profiles.html)

    Default:
    :   parameters provided the species

    The initial drift velocity of the particles, in units of the speed of light \(c\).

    **WARNING**: For massless particles, this is actually the momentum in units of \(m\_e c\).

temperature[¶](#id14 "Link to this definition")
:   Type:
    :   a list of 3 floats or [profiles](profiles.html)

    Default:
    :   parameters provided the species

    The initial temperature of the particles, in units of \(m\_ec^2\).

particles\_per\_cell[¶](#id15 "Link to this definition")
:   Type:
    :   float or [profile](profiles.html)

    Default:
    :   parameters provided the species

    The number of particles per cell to use for the injector.

number\_density[¶](#id16 "Link to this definition")

charge\_density[¶](#id17 "Link to this definition")
:   Type:
    :   float or [profile](profiles.html)

    Default:
    :   parameters provided the species

    The absolute value of the number density or charge density (choose one only)
    of the particle distribution, in units of the reference density \(N\_r\) (see [Units](../Understand/units.html))

regular\_number[¶](#id18 "Link to this definition")
:   Type:
    :   A list of as many integers as the simulation dimension

    Same as for [Species](#species). When `position_initialization = "regular"`, this sets the number of evenly-spaced
    particles per cell in each direction: `[Nx, Ny, Nz]` in cartesian geometries.

---
