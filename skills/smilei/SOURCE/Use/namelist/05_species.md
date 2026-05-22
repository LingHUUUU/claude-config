## Species[¶](#species)

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

name[¶](#name)

The name you want to give to this species.
It should be more than one character and can not start with `"m_"`.

position_initialization[¶](#position_initialization)

The method for initialization of particle positions. Options are:

-

`"regular"` for regularly spaced. See [`regular_number`](#id18).

-

`"random"` for randomly distributed.

-

`"centered"` for centered in each cell (not supported in `AMcylindrical` geometry.

-

The [`name`](#id93) of another species from which the positions are copied.
The source species must have positions initialized using one of the three
other options above, and must be defined before this species.

-

A numpy array or an HDF5 file defining all the positions of the particles.
In this case you must also provide the weight of each particle (see [Macro-particle weights](../Understand/units.html#weights)).
See [Initialize particles from an array or a file](particle_initialization.html).

regular_number[¶](#regular_number)

Type:

A list of as many integers as the simulation dimension

When `position_initialization = "regular"`, this sets the number of evenly-spaced
particles per cell in each direction: `[Nx, Ny, Nz]` in cartesian geometries and
`[Nx, Nr, Ntheta]` in `AMcylindrical` in which case we recommend
`Ntheta` \(\geq 4\times (\) `number_of_AM` \(-1)\).
If unset, `particles_per_cell` must be a power of the simulation dimension,
for instance, a power of 2 in `2Dcartesian`.

momentum_initialization[¶](#momentum_initialization)

The method for initialization of particle momenta. Options are:

-

`"maxwell-juettner"` for a relativistic maxwellian (see [how it is done](maxwell-juttner.html))

-

`"rectangular"` for a rectangular distribution

-

`"cold"` for zero temperature

-

A numpy array or an HDF5 file defining all the momenta of the particles.
See [Initialize particles from an array or a file](particle_initialization.html).

The first 2 distributions depend on the parameter [`temperature`](#id14) explained below.

particles_per_cell[¶](#particles_per_cell)

Type:

float or [profile](profiles.html)

The number of particles per cell.

mass[¶](#mass)

The mass of particles, in units of the electron mass \(m_e\).

atomic_number[¶](#atomic_number)

Default:

0

The atomic number of the particles (must be below 101).
It is required for ionization and nuclear reactions.
It has an effect on collisions by accounting for the atomic screening
(if not defined, or set to 0 for ions, screening is discarded as if
the ion was fully ionized).

maximum_charge_state[¶](#maximum_charge_state)

Default:

0

The maximum charge state of a species for which the ionization model is `"from_rate"`.

number_density[¶](#number_density)

charge_density[¶](#charge_density)

Type:

float or [profile](profiles.html)

The absolute value of the charge density or number density (choose one only)
of the particle distribution, in units of the reference density \(N_r\) (see [Units](../Understand/units.html)).

charge[¶](#charge)

Type:

float or [profile](profiles.html)

The particle charge, in units of the elementary charge \(e\).

mean_velocity[¶](#mean_velocity)

Type:

a list of 3 floats or [profiles](profiles.html)

The initial drift velocity of the particles, in units of the speed of light \(c\), in the x, y and z directions.

WARNING: For massless particles, this is actually the momentum in units of \(m_e c\).

mean_velocity_AM[¶](#mean_velocity_AM)

Type:

a list of 3 floats or [profiles](profiles.html)

The initial drift velocity of the particles, in units of the speed of light \(c\), in the longitudinal, radial and azimuthal directions.
This entry is available only in `AMcylindrical` velocity and cannot be used if also `mean_velocity` is used in the same `Species`: only one of the two can be chosen.

WARNING: For massless particles, this is actually the momentum in units of \(m_e c\).

WARNING: The initial cylindrical drift velocity is applied to each particle, thus it can be computationally demanding.

temperature[¶](#temperature)

Type:

a list of 3 floats or [profiles](profiles.html)

Default:

`1e-10`

The initial temperature of the particles, in units of \(m_ec^2\).

boundary_conditions[¶](#boundary_conditions)

Type:

a list of lists of strings

Default:

`[["periodic"]]`

The boundary conditions for the particles of this species.
Each boundary may have one of the following conditions:
`"periodic"`, `"reflective"`, `"remove"` (particles are deleted),
`"stop"` (particle momenta are set to 0), and `"thermalize"`.
For photon species (`mass=0`), the last two options are not available.

Syntax 1: `[[bc_all]]`, identical for all boundaries.
Syntax 2: `[[bc_X], [bc_Y], ...]`, different depending on x, y or z.
Syntax 3: `[[bc_Xmin, bc_Xmax], ...]`,  different on each boundary.

thermal_boundary_temperature[¶](#thermal_boundary_temperature)

Default:

None

A list of floats representing the temperature of the thermal boundaries (those set to
`"thermalize"` in  [`boundary_conditions`](#boundary_conditions)) for each spatial coordinate.
Currently, only the first coordinate (x) is taken into account.

thermal_boundary_velocity[¶](#thermal_boundary_velocity)

Default:

[]

A list of floats representing the components of the particles’ drift velocity after
encountering the thermal boundaries (those set to `"thermalize"` in [`boundary_conditions`](#boundary_conditions)).

time_frozen[¶](#time_frozen)

Default:

-

The time during which the particles are “frozen”, in units of \(T_r\).
Frozen particles do not move and therefore do not deposit any current density either.
Nonetheless, they deposit a charge density.
They are computationally much cheaper than non-frozen particles and oblivious to any EM-fields
in the simulation. Note that frozen particles can be ionized (this is computationally much cheaper
if ion motion is not relevant).

ionization_model[¶](#ionization_model)

Default:

`"none"`

The model for [field ionization](../Understand/ionization.html#field-ionization):

-

`"tunnel"` for tunnel ionization using [PPT-ADK](../Understand/ionization.html#ppt-adk) (requires species with an [`atomic_number`](#atomic_number))

-

`"tunnel_full_PPT"` experimental for tunnel ionization using [PPT-ADK with account for magnetic number](../Understand/ionization.html#ppt-adk) (requires species with an [`atomic_number`](#atomic_number))

-

`"tunnel_envelope_averaged"` for [field ionization with a laser envelope](../Understand/ionization.html#field-ionization-envelope)

-

`"from_rate"`, relying on a [user-defined ionization rate](../Understand/ionization.html#rate-ionization) (requires species with a [`maximum_charge_state`](#maximum_charge_state)).

bsi_model[¶](#bsi_model)

Default:

`"none"`

Apply the [Barrier Suppression Ionization](../Understand/ionization.html#barrier-suppression) correction for ionization in strong fields.
This correction is supported only for `ionization_model` = `"tunnel"` or `tunnel_full_PPT`.
The available BSI models are:

-

`"Tong_Lin"` for [Tong and Lin](../Understand/ionization.html#tong-lin)’s rate.

-

`"KAG"` for [Kostyukov Artemenko Golovanov](../Understand/ionization.html#kag)’s rate.

ionization_rate[¶](#ionization_rate)

A python function giving the user-defined ionisation rate as a function of various particle attributes.
To use this option, the [numpy package](http://www.numpy.org/) must be available in your python installation.
The function must have one argument, that you may call, for instance, `particles`.
This object has several attributes `x`, `y`, `z`, `px`, `py`, `pz`, `charge`, `weight` and `id`.
Each of these attributes are provided as numpy arrays where each cell corresponds to one particle.

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

ionization_electrons[¶](#ionization_electrons)

The name of the electron species that [`ionization_model`](#ionization_model) uses when creating new electrons.

is_test[¶](#is_test)

Default:

`False`

Flag for test particles. If `True`, this species will contain only test particles
which do not participate in the charge and currents.

pusher[¶](#pusher)

Default:

`"boris"`

Type of pusher to be used for this species. Options are:

-

`"boris"`: The relativistic Boris pusher

-

`"borisnr"`: The non-relativistic Boris pusher

-

`"vay"`: The relativistic pusher of J. L. Vay

-

`"higueracary"`: The relativistic pusher of A. V. Higuera and J. R. Cary

-

`"norm"`:  For photon species only (rectilinear propagation)

-

`"ponderomotive_boris"`: modified relativistic Boris pusher for species interacting with the laser envelope model. Valid only if the species has non-zero mass

-

`"borisBTIS3"`: as `"boris"`, but using B fields interpolated with the B-TIS3 scheme.

-

`"ponderomotive_borisBTIS3"`: as `"ponderomotive_boris"`, but using B fields interpolated with the B-TIS3 scheme.

WARNING: `"borisBTIS3"` and `"ponderomotive_borisBTIS3"` can be used only when `use_BTIS3_interpolation=True` in the `Main` block.

radiation_model[¶](#radiation_model)

Default:

`"none"`

The radiation reaction model used for this species (see [High-energy photon emission & radiation reaction](../Understand/radiation_loss.html)).

-

`"none"`: no radiation

-

`"Landau-Lifshitz"` (or `ll`): Landau-Lifshitz model approximated for high energies

-

`"corrected-Landau-Lifshitz"` (or `cll`): with quantum correction

-

`"Niel"`: a [stochastic radiation model](https://arxiv.org/abs/1707.02618) based on the work of Niel et al..

-

`"Monte-Carlo"` (or `mc`): Monte-Carlo radiation model. This model can be configured to generate macro-photons with [`radiation_photon_species`](#radiation_photon_species).

This parameter cannot be assigned to photons (mass = 0).

Radiation is emitted only with the `"Monte-Carlo"` model when
[`radiation_photon_species`](#radiation_photon_species) is defined.

radiation_photon_species[¶](#radiation_photon_species)

The [`name`](#id93) of the photon species in which the Monte-Carlo [`radiation_model`](#radiation_model)
will generate macro-photons. If unset (or `None`), no macro-photon will be created.
The target photon species must be have its mass set to 0, and appear after the
particle species in the namelist.

This parameter cannot be assigned to photons (mass = 0).

radiation_photon_sampling[¶](#radiation_photon_sampling)

Default:

`1`

The number of macro-photons generated per emission event, when the macro-photon creation
is activated (see [`radiation_photon_species`](#radiation_photon_species)). The total macro-photon weight
is still conserved.

A large number may rapidly slow down the performances and lead to memory saturation.

This parameter cannot be assigned to photons (mass = 0).

radiation_max_emissions[¶](#radiation_max_emissions)

Default:

`10`

The maximum number of emission Monte-Carlo event a macro-particle can undergo during a timestep.
Since this value is used to allocate some buffers, a high value can saturate memory.

This parameter cannot be assigned to photons (mass = 0).

radiation_photon_gamma_threshold[¶](#radiation_photon_gamma_threshold)

Default:

`2`

The threshold on the photon energy for the macro-photon emission when using the
radiation reaction Monte-Carlo process.
Under this threshold, the macro-photon from the radiation reaction Monte-Carlo
process is not created but still taken into account in the energy balance.
The default value corresponds to twice the electron rest mass energy that
is the required energy to decay into electron-positron pairs.

This parameter cannot be assigned to photons (mass = 0).

relativistic_field_initialization[¶](#relativistic_field_initialization)

Default:

`False`

Flag for relativistic particles. If `True`, the electromagnetic fields of this species will added to the electromagnetic fields already present in the simulation.
This operation will be performed when time equals [`time_frozen`](#id71). See [Field initialization for relativistic species](../Understand/relativistic_fields_initialization.html) for details on the computation of the electromagentic fields of a relativistic species.
To have physically meaningful results, we recommend to place a species which requires this method of field initialization far from other species, otherwise the latter could experience instantly turned-on unphysical forces by the relativistic species’ fields.

multiphoton_Breit_Wheeler[¶](#multiphoton_Breit_Wheeler)

Default:

`[None,None]`

An list of the [`name`](#id93) of two species: electrons and positrons created through
the [Multiphoton Breit-Wheeler pair creation](../Understand/multiphoton_Breit_Wheeler.html).
By default, the process is not activated.

This parameter can only be assigned to photons species (mass = 0).

multiphoton_Breit_Wheeler_sampling[¶](#multiphoton_Breit_Wheeler_sampling)

Default:

`[1,1]`

A list of two integers: the number of electrons and positrons generated per photon decay
in the [Multiphoton Breit-Wheeler pair creation](../Understand/multiphoton_Breit_Wheeler.html). The total macro-particle weight is still
conserved.

Large numbers may rapidly slow down the performances and lead to memory saturation.

This parameter can only be assigned to photons species (mass = 0).

keep_interpolated_fields[¶](#keep_interpolated_fields)

Default:

`[]`

A list of interpolated fields that should be stored in memory for all particles of this species,
instead of being located in temporary buffers. These fields can then
be accessed in some diagnostics such as [particle binning](#diagparticlebinning) or
[tracking](#diagtrackparticles). The available fields are `"Ex"`, `"Ey"`, `"Ez"`,
`"Bx"`, `"By"` and `"Bz"`.

Note that magnetic field components, as they originate from the interpolator,
are shifted by half a timestep compared to those from the Fields diagnostics.

Additionally, the work done by each component of the electric field is available as
`"Wx"`, `"Wy"` and `"Wz"`. Contrary to the other interpolated fields, these quantities
are accumulated over time.
