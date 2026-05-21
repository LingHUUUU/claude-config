## Particle Merging[¶](#particle-merging "Link to this heading")

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

merging\_method[¶](#merging_method "Link to this definition")
:   Default:
    :   `"none"`

    The particle merging method to use:

    - `"none"`: no merging
    - `"vranic_cartesian"`: method of M. Vranic with a cartesian momentum-space decomposition
    - `"vranic_spherical"`: method of M. Vranic with a spherical momentum-space decomposition

merge\_every[¶](#merge_every "Link to this definition")
:   Default:
    :   `0`

    Number of timesteps between each merging event
    **or** a [time selection](#timeselections).

min\_particles\_per\_cell[¶](#min_particles_per_cell "Link to this definition")
:   Default:
    :   `4`

    The minimum number of particles per cell for the merging.

merge\_min\_packet\_size[¶](#merge_min_packet_size "Link to this definition")
:   Default:
    :   `4`

    The minimum number of particles per packet to merge. Must be greater or equal to 4.

merge\_max\_packet\_size[¶](#merge_max_packet_size "Link to this definition")
:   Default:
    :   `4`

    The maximum number of particles per packet to merge.

merge\_momentum\_cell\_size[¶](#merge_momentum_cell_size "Link to this definition")
:   Default:
    :   `[16,16,16]`

    A list of 3 integers defining the number of sub-groups in each direction
    for the momentum-space discretization.

merge\_discretization\_scale[¶](#merge_discretization_scale "Link to this definition")
:   Default:
    :   `"linear"`

    The momentum discretization scale:: `"linear"` or `"log"`.
    The `"log"` scale only works with the spherical discretization at the moment.

merge\_min\_momentum[¶](#merge_min_momentum "Link to this definition")
:   Default:
    :   `1e-5`

    [for experts] The minimum momentum value when the log scale
    is chosen (`merge_discretization_scale = log`).
    This avoids a potential 0 value in the log domain.

merge\_min\_momentum\_cell\_length[¶](#merge_min_momentum_cell_length "Link to this definition")
:   Default:
    :   `[1e-10,1e-10,1e-10]`

    [for experts] The minimum sub-group length for the momentum-space
    discretization (below which the number of sub-groups is set to 1).

merge\_accumulation\_correction[¶](#merge_accumulation_correction "Link to this definition")
:   Default:
    :   `True`

    [for experts] Activates the accumulation correction
    (see [Particle Merging](../Understand/particle_merging.html) for more information).
    The correction only works in linear scale.

---
