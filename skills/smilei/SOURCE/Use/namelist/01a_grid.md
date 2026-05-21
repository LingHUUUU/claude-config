## Main variables[¶](#main-variables "Link to this heading")

The block `Main` is **mandatory** and has the following syntax:

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

geometry[¶](#geometry "Link to this definition")
:   The geometry of the simulation:

    - `"1Dcartesian"`
    - `"2Dcartesian"`
    - `"3Dcartesian"`
    - `"AMcylindrical"`: cylindrical geometry with [Azimuthal modes decomposition](../Understand/azimuthal_modes_decomposition.html).

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

interpolation\_order[¶](#interpolation_order "Link to this definition")
:   Default:
    :   `2`

    Interpolation order, defines particle shape function:

    - `1` : 2 points stencil in r with Ruyten correction, 3 points stencil in x. Supported only in AM geometry.
    - `2` : 3 points stencil, supported in all configurations.
    - `4` : 5 points stencil, not supported in vectorized 2D geometry.

    The Ruyten correction is the scheme described bu equation 4.2 in [this paper](https://www.sciencedirect.com/science/article/abs/pii/S0021999183710703) .
    It allows for a more accurate description on axis at the cost of a higher statistic noise so it often requires the use of more macro-particles.

interpolator[¶](#interpolator "Link to this definition")
:   Default:
    :   `"momentum-conserving"`

    - `"momentum-conserving"`
    - `"wt"`

    The interpolation scheme to be used in the simulation.
    `"wt"` is for the timestep dependent field interpolation scheme described in
    [this paper](https://doi.org/10.1016/j.jcp.2020.109388) .

grid\_length[¶](#grid_length "Link to this definition")

number\_of\_cells[¶](#number_of_cells "Link to this definition")
:   A list of numbers: size of the simulation box for each dimension of the simulation.

    - Either `grid_length`, the simulation length in each direction in units of \(L\_r\),
    - or `number_of_cells`, the number of cells in each direction.

    Note

    In `AMcylindrical` geometry, the grid represents 2-dimensional fields.
    The second dimension is the **radius** of the cylinder.

cell\_length[¶](#cell_length "Link to this definition")
:   A list of floats: sizes of one cell in each direction in units of \(L\_r\).

simulation\_time[¶](#simulation_time "Link to this definition")

number\_of\_timesteps[¶](#number_of_timesteps "Link to this definition")
:   Duration of the simulation.

    - Either `simulation_time`, the simulation duration in units of \(T\_r\),
    - or `number_of_timesteps`, the total number of timesteps.

timestep[¶](#timestep "Link to this definition")

timestep\_over\_CFL[¶](#timestep_over_CFL "Link to this definition")
:   Duration of one timestep.

    - Either `timestep`, in units of \(T\_r\),
    - or `timestep_over_CFL`, in units of the *Courant–Friedrichs–Lewy* (CFL) time.

gpu\_computing[¶](#gpu_computing "Link to this definition")
:   Default:
    :   `False`

    Activates GPU acceleration if set to True

number\_of\_patches[¶](#number_of_patches "Link to this definition")
