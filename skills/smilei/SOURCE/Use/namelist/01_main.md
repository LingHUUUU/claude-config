## Main variables[¶](#main-variables)

The block `Main` is mandatory and has the following syntax:

```
Main(
geometry = "1Dcartesian",
interpolation_order = 2,
interpolator = "momentum-conserving",
grid_length  = [16. ],
cell_length = [0.01],
simulation_time    = 15.,
timestep    = 0.005,
number_of_patches = [64],
cluster_width = 5,
maxwell_solver = 'Yee',
EM_boundary_conditions = [
["silver-muller", "silver-muller"],
#        ["silver-muller", "silver-muller"],
#        ["silver-muller", "silver-muller"],
],
time_fields_frozen = 0.,
reference_angular_frequency_SI = 0.,
print_every = 100,
random_seed = 0,
)

```

geometry[¶](#geometry)

The geometry of the simulation:

-

`"1Dcartesian"`

-

`"2Dcartesian"`

-

`"3Dcartesian"`

-

`"AMcylindrical"`: cylindrical geometry with [Azimuthal modes decomposition](../Understand/azimuthal_modes_decomposition.html).

In the following documentation, all references to dimensions or coordinates
depend on the `geometry`.
1D, 2D and 3D stand for 1-dimensional, 2-dimensional and 3-dimensional cartesian
geometries, respectively. All coordinates are ordered as \((x)\), \((x,y)\) or \((x,y,z)\).
In the `"AMcylindrical"` case, all grid coordinates are 2-dimensional
\((x,r)\), while particle coordinates (in [Species](#species))
are expressed in the 3-dimensional Cartesian frame \((x,y,z)\).

Warning

The `"AMcylindrical"` geometry has some restrictions.
Boundary conditions must be set to `"remove"` for particles,
`"silver-muller"` for longitudinal EM boundaries and
`"buneman"` for transverse EM boundaries.
You can alternatively use `"PML"` for any EM boundary.
Collisions and
order-4 interpolation are not supported yet.

interpolation_order[¶](#interpolation_order)

Default:

`2`

Interpolation order, defines particle shape function:

-

`1`  : 2 points stencil in r with Ruyten correction, 3 points stencil in x. Supported only in AM geometry.

-

`2`  : 3 points stencil, supported in all configurations.

-

`4`  : 5 points stencil, not supported in vectorized 2D geometry.

The Ruyten correction is the scheme described bu equation 4.2 in [this paper](https://www.sciencedirect.com/science/article/abs/pii/S0021999183710703) .
It allows for a more accurate description on axis at the cost of a higher statistic noise so it often requires the use of more macro-particles.

interpolator[¶](#interpolator)

Default:

`"momentum-conserving"`

-

`"momentum-conserving"`

-

`"wt"`

The interpolation scheme to be used in the simulation.
`"wt"` is for the timestep dependent field interpolation scheme described in
[this paper](https://doi.org/10.1016/j.jcp.2020.109388) .

grid_length[¶](#grid_length)

number_of_cells[¶](#number_of_cells)

A list of numbers: size of the simulation box for each dimension of the simulation.

-

Either `grid_length`, the simulation length in each direction in units of \(L_r\),

-

or `number_of_cells`, the number of cells in each direction.

Note

In `AMcylindrical` geometry, the grid represents 2-dimensional fields.
The second dimension is the radius of the cylinder.

cell_length[¶](#cell_length)

A list of floats: sizes of one cell in each direction in units of \(L_r\).

simulation_time[¶](#simulation_time)

number_of_timesteps[¶](#number_of_timesteps)

Duration of the simulation.

-

Either `simulation_time`, the simulation duration in units of \(T_r\),

-

or `number_of_timesteps`, the total number of timesteps.

timestep[¶](#timestep)

timestep_over_CFL[¶](#timestep_over_CFL)

Duration of one timestep.

-

Either `timestep`, in units of \(T_r\),

-

or `timestep_over_CFL`, in units of the Courant–Friedrichs–Lewy (CFL) time.

gpu_computing[¶](#gpu_computing)

Default:

`False`

Activates GPU acceleration if set to True

number_of_patches[¶](#number_of_patches)

A list of integers: the number of patches in each direction.
Each integer must be a power of 2, and the total number of patches must be
greater or equal than the number of MPI processes.
It is also strongly advised to have more patches than the total number of openMP threads.
See [Parallelization basics](../Understand/parallelization.html).On the other hand, in case of GPU-acceleration it is recommended to use one patch per MPI-rank
(with one MPI-rank per GPU)

patch_arrangement[¶](#patch_arrangement)

Default:

`"hilbertian"`

Determines the ordering of patches and the way they are separated into the
various MPI processes. Options are:

-

`"hilbertian"`: following the Hilbert curve (see [this explanation](../Understand/parallelization.html#loadbalancingexplanation)).

-

`"linearized_XY"` in 2D or `"linearized_XYZ"` in 3D: following the
row-major (C-style) ordering.

-

`"linearized_YX"` in 2D or `"linearized_ZYX"` in 3D: following the
column-major (fortran-style) ordering. This prevents the usage of
[Fields diagnostics](#diagfields) (see [Parallelization basics](../Understand/parallelization.html)).

cluster_width[¶](#cluster_width)

Default:

set to minimize the memory footprint of the particles pusher, especially interpolation and projection processes

For advanced users. Integer specifying the cluster width along X direction in number of cells.
The “cluster” is a sub-patch structure in which particles are sorted for cache improvement.
`cluster_width` must divide the number of cells in one patch (in dimension X).
The finest sorting is achieved with `cluster_width=1` and no sorting with `cluster_width` equal to the full size of a patch along dimension X.
The cluster size in dimension Y and Z is always the full extent of the patch.

maxwell_solver[¶](#maxwell_solver)

Default:

‘Yee’

The solver for Maxwell’s equations.
Only `"Yee"` and `"M4"` are available for all geometries at the moment.
`"Cowan"`, `"Grassi"`, `"Lehe"` and `"Bouchard"` are available for `2DCartesian`.
`"Lehe"` and `"Bouchard"` are available for `3DCartesian`.
`"Lehe"` and `"Terzani"` are available for `AMcylindrical`.
The M4 solver is described in [this paper](https://doi.org/10.1016/j.jcp.2020.109388).
The Lehe solver is described in [this paper](https://journals.aps.org/prab/abstract/10.1103/PhysRevSTAB.16.021301).
The Bouchard solver is described in [this thesis p. 109](https://tel.archives-ouvertes.fr/tel-02967252).
The Terzani solver is described in [this paper](https://doi.org/10.1016/j.cpc.2019.04.007).

solve_poisson[¶](#solve_poisson)

Default:

True

Decides if Poisson correction must be applied or not initially.

poisson_max_iteration[¶](#poisson_max_iteration)

Default:

50000

Maximum number of iteration for the Poisson solver.

poisson_max_error[¶](#poisson_max_error)

Default:

1e-14

Maximum error for the Poisson solver.

solve_relativistic_poisson[¶](#solve_relativistic_poisson)

Default:

False

Decides if relativistic Poisson problem must be solved for at least one species.
See [Field initialization for relativistic species](../Understand/relativistic_fields_initialization.html) for more details.

relativistic_poisson_max_iteration[¶](#relativistic_poisson_max_iteration)

Default:

50000

Maximum number of iteration for the Poisson solver.

relativistic_poisson_max_error[¶](#relativistic_poisson_max_error)

Default:

1e-22

Maximum error for the Poisson solver.

EM_boundary_conditions[¶](#EM_boundary_conditions)

Type:

list of lists of strings

Default:

`[["periodic"]]`

The boundary conditions for the electromagnetic fields. Each boundary may have one of
the following conditions: `"periodic"`, `"silver-muller"`, `"reflective"`, `"ramp??"` or `"PML"`.

Syntax 1: `[[bc_all]]`, identical for all boundaries.
Syntax 2: `[[bc_X], [bc_Y], ...]`, different depending on x, y or z.
Syntax 3: `[[bc_Xmin, bc_Xmax], ...]`,  different on each boundary.

-

`"silver-muller"` is an open boundary condition.
The incident wave vector \(k_{inc}\) on each face is defined by
`"EM_boundary_conditions_k"`.
When using `"silver-muller"` as an injecting boundary,
make sure \(k_{inc}\) is aligned with the wave you are injecting.
When using `"silver-muller"` as an absorbing boundary,
the optimal wave absorption on a given face will be along \(k_{abs}\)
the specular reflection of \(k_{inc}\) on the considered face.

-

`"ramp??"` is a basic, open boundary condition designed
for the spectral solver in `AMcylindrical` geometry.
The `??` is an integer representing a number of cells
(smaller than the number of ghost cells).
Over the first half, the fields remain untouched.
Over the second half, all fields are progressively reduced down to zero.

-

`"PML"` stands for Perfectly Matched Layer. It is an open boundary condition.
The number of cells in the layer must be defined by `"number_of_pml_cells"`.
It supports laser injection as in `"silver-muller"`.
If not all boundary conditions are `PML`, make sure to set `number_of_pml_cells=0` on boundaries not using PML.

EM_boundary_conditions_k[¶](#EM_boundary_conditions_k)

Type:

list of lists of floats

Default:

`[[1.,0.],[-1.,0.],[0.,1.],[0.,-1.]]` in 2D

Default:

`[[1.,0.,0.],[-1.,0.,0.],[0.,1.,0.],[0.,-1.,0.],[0.,0.,1.],[0.,0.,-1.]]` in 3D

For `silver-muller` absorbing boundaries,
the x,y,z coordinates of the unit wave vector `k` incident on each face
(sequentially Xmin, Xmax, Ymin, Ymax, Zmin, Zmax).
The number of coordinates is equal to the dimension of the simulation.
The number of given vectors must be equal to 1 or to the number of faces
which is twice the dimension of the simulation. In cylindrical geometry,
`k` coordinates are given in the `xr` frame and only the Rmax face is affected.

Syntax 1: `[[1,0,0]]`, identical for all boundaries.
Syntax 2: `[[1,0,0],[-1,0,0], ...]`,  different on each boundary.

number_of_pml_cells[¶](#number_of_pml_cells)

Type:

List of lists of integers

Default:

`[[10,10],[10,10],[10,10]]`

Defines the number of cells in the `"PML"` layers using the same alternative syntaxes as `"EM_boundary_conditions"`.

pml_sigma[¶](#pml_sigma)

Type:

List of profiles

Default:

[lambda x : 20 * x**2]

Defines the sigma profiles across the transverse dimension of the PML for each dimension of the simulation.
It must be expressed as a list of profiles (1 per dimension).

If a single profile is given, it will be used for all dimensions.

For a given dimension, the same profile is applied to both sides of the domain.

The profile is given as a single variable function defined on the interval [0,1] where 0 is the inner bound of the PML and 1 is the outer bound of the PML.
Please refer to [Perfectly Matched Layers](../Understand/PML.html) if needed in AM geometry.

pml_kappa[¶](#pml_kappa)

Type:

List of profiles

Default:

[lambda x : 1 + 79 * x**4]

Defines the kappa profiles across the transverse dimension of the PML for each dimension of the simulation.
It must be expressed as a list of profiles (1 per dimension).

If a single profile is given, it will be used for all dimensions.

For a given dimension, the same profile is applied to both sides of the domain.

The profile is given as a single variable function defined on the interval [0,1] where 0 is the inner bound of the PML and 1 is the outer bound of the PML.
Please refer to [Perfectly Matched Layers](../Understand/PML.html) if needed in AM geometry.

time_fields_frozen[¶](#time_fields_frozen)

Default:

-

Time, at the beginning of the simulation, during which fields are frozen.

reference_angular_frequency_SI[¶](#reference_angular_frequency_SI)

The value of the reference angular frequency \(\omega_r\) in SI units,
only needed when collisions, ionization, radiation losses
or multiphoton Breit-Wheeler pair creation are requested.
This frequency is related to the normalization length according to \(L_r\omega_r = c\)
(see [Units](../Understand/units.html)).

print_every[¶](#print_every)

Number of timesteps between each info output on screen. By default, 10 outputs per
simulation.

print_expected_disk_usage[¶](#print_expected_disk_usage)

Default:

`True`

If `False`, the calculation of the expected disk usage, that is usually printed in the
standard output, is skipped. This might be useful in rare cases where this calculation
is costly.

random_seed[¶](#random_seed)

Default:

0

The value of the random seed. Each patch has its own random number generator, with a seed
equal to `random_seed` + the index of the patch.

number_of_AM[¶](#number_of_AM)

Type:

integer

Default:

2

The number of azimuthal modes used for the Fourier decomposition in `"AMcylindrical"` geometry.
The modes range from mode 0 to mode `"number_of_AM-1"`.

number_of_AM_classical_Poisson_solver[¶](#number_of_AM_classical_Poisson_solver)

Default:

1

The number of azimuthal modes used for the field initialization with non relativistic Poisson solver in `"AMcylindrical"` geometry.
Note that this number must be lower or equal to the number of modes of the simulation.

number_of_AM_relativistic_field_initialization[¶](#number_of_AM_relativistic_field_initialization)

Default:

1

The number of azimuthal modes used for the relativistic field initialization in `"AMcylindrical"` geometry.
Note that this number must be lower or equal to the number of modes of the simulation.

use_BTIS3_interpolation[¶](#use_BTIS3_interpolation)

Default:

`False`

If `True`, the B-translated interpolation scheme 3 (or B-TIS3) described in [PIC algorithms](../Understand/algorithms.html) is used.

custom_oversize[¶](#custom_oversize)

Type:

integer

Default:

2

The number of ghost-cell for each patches. The default value is set accordingly with
the `interpolation_order` value.
