number\_of\_patches[¶](#number_of_patches "Link to this definition")
:   A list of integers: the number of patches in each direction.
    Each integer must be a power of 2, and the total number of patches must be
    greater or equal than the number of MPI processes.
    It is also strongly advised to have more patches than the total number of openMP threads.
    See [Parallelization basics](../Understand/parallelization.html).On the other hand, in case of GPU-acceleration it is recommended to use one patch per MPI-rank
    (with one MPI-rank per GPU)

patch\_arrangement[¶](#patch_arrangement "Link to this definition")
:   Default:
    :   `"hilbertian"`

    Determines the ordering of patches and the way they are separated into the
    various MPI processes. Options are:

    - `"hilbertian"`: following the Hilbert curve (see [this explanation](../Understand/parallelization.html#loadbalancingexplanation)).
    - `"linearized_XY"` in 2D or `"linearized_XYZ"` in 3D: following the
      row-major (C-style) ordering.
    - `"linearized_YX"` in 2D or `"linearized_ZYX"` in 3D: following the
      column-major (fortran-style) ordering. This prevents the usage of
      [Fields diagnostics](#diagfields) (see [Parallelization basics](../Understand/parallelization.html)).

cluster\_width[¶](#cluster_width "Link to this definition")
:   Default:
    :   set to minimize the memory footprint of the particles pusher, especially interpolation and projection processes

    For advanced users. Integer specifying the cluster width along X direction in number of cells.
    The “cluster” is a sub-patch structure in which particles are sorted for cache improvement.
    `cluster_width` must divide the number of cells in one patch (in dimension X).
    The finest sorting is achieved with `cluster_width=1` and no sorting with `cluster_width` equal to the full size of a patch along dimension X.
    The cluster size in dimension Y and Z is always the full extent of the patch.

maxwell\_solver[¶](#maxwell_solver "Link to this definition")
:   Default:
    :   ‘Yee’

    The solver for Maxwell’s equations.
    Only `"Yee"` and `"M4"` are available for all geometries at the moment.
    `"Cowan"`, `"Grassi"`, `"Lehe"` and `"Bouchard"` are available for `2DCartesian`.
    `"Lehe"` and `"Bouchard"` are available for `3DCartesian`.
    `"Lehe"` and `"Terzani"` are available for `AMcylindrical`.
    The M4 solver is described in [this paper](https://doi.org/10.1016/j.jcp.2020.109388).
    The Lehe solver is described in [this paper](https://journals.aps.org/prab/abstract/10.1103/PhysRevSTAB.16.021301).
    The Bouchard solver is described in [this thesis p. 109](https://tel.archives-ouvertes.fr/tel-02967252).
    The Terzani solver is described in [this paper](https://doi.org/10.1016/j.cpc.2019.04.007).

solve\_poisson[¶](#solve_poisson "Link to this definition")
:   Default:
    :   True

    Decides if Poisson correction must be applied or not initially.

poisson\_max\_iteration[¶](#poisson_max_iteration "Link to this definition")
:   Default:
    :   50000

    Maximum number of iteration for the Poisson solver.

poisson\_max\_error[¶](#poisson_max_error "Link to this definition")
:   Default:
    :   1e-14

    Maximum error for the Poisson solver.

solve\_relativistic\_poisson[¶](#solve_relativistic_poisson "Link to this definition")
:   Default:
    :   False

    Decides if relativistic Poisson problem must be solved for at least one species.
    See [Field initialization for relativistic species](../Understand/relativistic_fields_initialization.html) for more details.

relativistic\_poisson\_max\_iteration[¶](#relativistic_poisson_max_iteration "Link to this definition")
:   Default:
    :   50000

    Maximum number of iteration for the Poisson solver.

relativistic\_poisson\_max\_error[¶](#relativistic_poisson_max_error "Link to this definition")
:   Default:
    :   1e-22

    Maximum error for the Poisson solver.

EM\_boundary\_conditions[¶](#EM_boundary_conditions "Link to this definition")
