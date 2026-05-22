## Particle Injector[¶](#particle-injector)

Injectors enable to inject macro-particles in the simulation domain from the boundaries.
By default, some parameters that are not specified are inherited from the associated [`species`](#id99).

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

name[¶](#id9)

The name you want to give to this injector.
If you do not specify a name, it will be attributed automatically.
The name is useful if you want to inject particles at the same position of another injector.

species[¶](#id10)

The name of the species in which to inject the new particles

box_side[¶](#box_side)

From where the macro-particles are injected. Options are:

-

`"xmin"`

-

`"xmax"`

-

`"ymin"`

-

`"ymax"`

-

`"zmax"`

-

`"zmin"`

time_envelope[¶](#time_envelope)

Type:

a python function or a [time profile](profiles.html)

Default:

`tconstant()`

The temporal envelope of the injector.

position_initialization[¶](#id11)

Default:

parameters provided the species

The method for initialization of particle positions. Options are:

-

`"species"` or empty `""`: injector uses the option of the specified [`species`](#id99).

-

`"regular"` for regularly spaced. See [`regular_number`](#id18).

-

`"random"` for randomly distributed

-

`"centered"` for centered in each cell

-

The [`name`](#id93) of another injector from which the positions are copied.
This option requires (1) that the target injector’s positions are initialized
using one of the three other options above.

momentum_initialization[¶](#id12)

Default:

parameters provided the species

The method for initialization of particle momenta. Options are:

-

`"species"` or empty `""`: injector uses the option of the specified [`species`](#id99).

-

`"maxwell-juettner"` for a relativistic maxwellian (see [how it is done](maxwell-juttner.html))

-

`"rectangular"` for a rectangular distribution

mean_velocity[¶](#id13)

Type:

a list of 3 floats or [profiles](profiles.html)

Default:

parameters provided the species

The initial drift velocity of the particles, in units of the speed of light \(c\).

WARNING: For massless particles, this is actually the momentum in units of \(m_e c\).

temperature[¶](#id14)

Type:

a list of 3 floats or [profiles](profiles.html)

Default:

parameters provided the species

The initial temperature of the particles, in units of \(m_ec^2\).

particles_per_cell[¶](#id15)

Type:

float or [profile](profiles.html)

Default:

parameters provided the species

The number of particles per cell to use for the injector.

number_density[¶](#id16)

charge_density[¶](#id17)

Type:

float or [profile](profiles.html)

Default:

parameters provided the species

The absolute value of the number density or charge density (choose one only)
of the particle distribution, in units of the reference density \(N_r\) (see [Units](../Understand/units.html))

regular_number[¶](#id18)

Type:

A list of as many integers as the simulation dimension

Same as for [Species](#species). When `position_initialization = "regular"`, this sets the number of evenly-spaced
particles per cell in each direction: `[Nx, Ny, Nz]` in cartesian geometries.

## Particle Merging[¶](#particle-merging)

The macro-particle merging method is documented in
the [corresponding page](../Understand/particle_merging.html).
Note that for merging to be able to operate either vectorization or cell sorting must be activated.
It is optionnally specified in the `Species` block:

```
Species(
....

# Merging
merging_method = "vranic_spherical",
merge_every = 5,
merge_min_particles_per_cell = 16,
merge_max_packet_size = 4,
merge_min_packet_size = 4,
merge_momentum_cell_size = [16,16,16],
merge_discretization_scale = "linear",
# Extra parameters for experts:
merge_min_momentum_cell_length = [1e-10, 1e-10, 1e-10],
merge_accumulation_correction = True,
)

```

merging_method[¶](#merging_method)

Default:

`"none"`

The particle merging method to use:

-

`"none"`: no merging

-

`"vranic_cartesian"`: method of M. Vranic with a cartesian momentum-space decomposition

-

`"vranic_spherical"`: method of M. Vranic with a spherical momentum-space decomposition

merge_every[¶](#merge_every)

Default:

`0`

Number of timesteps between each merging event
or a [time selection](#timeselections).

min_particles_per_cell[¶](#min_particles_per_cell)

Default:

`4`

The minimum number of particles per cell for the merging.

merge_min_packet_size[¶](#merge_min_packet_size)

Default:

`4`

The minimum number of particles per packet to merge. Must be greater or equal to 4.

merge_max_packet_size[¶](#merge_max_packet_size)

Default:

`4`

The maximum number of particles per packet to merge.

merge_momentum_cell_size[¶](#merge_momentum_cell_size)

Default:

`[16,16,16]`

A list of 3 integers defining the number of sub-groups in each direction
for the momentum-space discretization.

merge_discretization_scale[¶](#merge_discretization_scale)

Default:

`"linear"`

The momentum discretization scale:: `"linear"` or `"log"`.
The `"log"` scale only works with the spherical discretization at the moment.

merge_min_momentum[¶](#merge_min_momentum)

Default:

`1e-5`

[for experts] The minimum momentum value when the log scale
is chosen (`merge_discretization_scale = log`).
This avoids a potential 0 value in the log domain.

merge_min_momentum_cell_length[¶](#merge_min_momentum_cell_length)

Default:

`[1e-10,1e-10,1e-10]`

[for experts] The minimum sub-group length for the momentum-space
discretization (below which the number of sub-groups is set to 1).

merge_accumulation_correction[¶](#merge_accumulation_correction)

Default:

`True`

[for experts] Activates the accumulation correction
(see [Particle Merging](../Understand/particle_merging.html) for more information).
The correction only works in linear scale.
