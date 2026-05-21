## Load Balancing[¶](#load-balancing "Link to this heading")

Load balancing (explained [here](../Understand/parallelization.html#loadbalancingexplanation)) consists in exchanging
patches (domains of the simulation box) between MPI processes to reduce the
computational load imbalance.
The block `LoadBalancing` is optional. If you do not define it, load balancing will
occur every 150 iterations.

```
LoadBalancing(
    initial_balance = True,
    every = 150,
    cell_load = 1.,
    frozen_particle_load = 0.1
)
```

initial\_balance[¶](#initial_balance "Link to this definition")
:   Default:
    :   True

    Decides if the load must be balanced at initialization. If not, the same amount of
    patches will be attributed to each MPI rank.

every[¶](#every "Link to this definition")
:   Default:
    :   150

    Number of timesteps between each load balancing **or** a [time selection](#timeselections).
    The value `0` suppresses all load balancing.

cell\_load[¶](#cell_load "Link to this definition")
:   Default:

    Computational load of a single grid cell considered by the dynamic load balancing algorithm.
    This load is normalized to the load of a single particle.

frozen\_particle\_load[¶](#frozen_particle_load "Link to this definition")
:   Default:
    :   0.1

    Computational load of a single frozen particle considered by the dynamic load balancing algorithm.
    This load is normalized to the load of a single particle.

---

## Multiple decomposition of the domain[¶](#multiple-decomposition-of-the-domain "Link to this heading")

The block `MultipleDecomposition` is necessary for spectral solvers and optional in all other cases.
When present, it activates
the [Single-domain multiple decompositions](../Understand/SDMD.html) (SDMD) technique
which separates the decomposition of the field grids from that of the particles.
Fields are set on large sub-domain called *regions* (1 region per MPI process) while
particles are kept as small *patches* as in the standard decomposition (many patches per MPI process).
Benefits of this option are illustrated [in this paper](https://hal.archives-ouvertes.fr/hal-02973139).

```
MultipleDecomposition(
    region_ghost_cells = 2
)
```

region\_ghost\_cells[¶](#region_ghost_cells "Link to this definition")
:   Type:
    :   integer

    Default:
    :   2

    The number of ghost cells for each region.
    The default value is set accordingly with the `interpolation_order`.
    The same number of ghost cells is used in all dimensions except for spectral solver in AM geometry for which the number of radial ghost cells is always automatically set to be the same as patches.

---

## Vectorization[¶](#vectorization "Link to this heading")

The block `Vectorization` is optional.
It controls the SIMD operations that can enhance the performance of some computations.
The technique is detailed in Ref. [[Beck2019]](../Overview/material.html#beck2019) and summarized in [this doc](../Understand/vectorization.html).
It requires [additional compilation options](installation.html#vectorization-flags) to be actived.

```
Vectorization(
    mode = "adaptive",
    reconfigure_every = 20,
    initial_mode = "on"
)
```

mode[¶](#mode "Link to this definition")
:   Default:
    :   `"off"`

    - `"off"`: non-vectorized operators are used.
      Recommended when the number of particles per cell stays below 10.
    - `"on"`: vectorized operators are used.
      Recommended when the number of particles per cell stays above 10.
      Particles are sorted per cell.
    - `"adaptive"`: the best operators (scalar or vectorized)
      are determined and configured dynamically and locally
      (per patch and per species). For the moment this mode is only supported in `3Dcartesian` geometry.
      Particles are sorted per cell.

    In the `"adaptive"` mode, [`cluster_width`](#cluster_width "cluster_width") is set to the maximum.

reconfigure\_every[¶](#reconfigure_every "Link to this definition")
:   Default:
    :   20

    The number of timesteps between each dynamic reconfiguration of
    the vectorized operators, when using the `"adaptive"` vectorization mode.
    It may be set to a [time selection](#timeselections) as well.

initial\_mode[¶](#initial_mode "Link to this definition")
:   Default:
    :   `off`

    Default state when the `"adaptive"` mode is activated
    and no particle is present in the patch.

---
