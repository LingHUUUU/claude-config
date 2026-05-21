# Initialize particles from an array or a file[¶](#initialize-particles-from-an-array-or-a-file "Link to this heading")

In the namelist, [`position_initialization`](namelist.html#id11 "position_initialization") and [`momentum_initialization`](namelist.html#id12 "momentum_initialization")
may be set to a *numpy* array or to an *HDF5* file containing particle data to be imported.

The position initialization is incompatible with [`number_density`](namelist.html#id16 "number_density"),
[`charge_density`](namelist.html#id17 "charge_density") and [`particles_per_cell`](namelist.html#id15 "particles_per_cell").
Particles initialized outside of the initial simulation domain will not be created.

The momentum initialization is incompatible with [`temperature`](namelist.html#id14 "temperature")
and [`mean_velocity`](namelist.html#id13 "mean_velocity").

---

## From a numpy array[¶](#from-a-numpy-array "Link to this heading")

The [`position_initialization`](namelist.html#id11 "position_initialization") may be a *numpy* array of shape `(Ndim+1, Npart)`
where `Ndim` is the number of particle dimensions,
and `Npart` is the total number of particles.
Positions components x, y, z are given along the first `Ndim` columns
and the weights are given in the last column of the array.

The [`momentum_initialization`](namelist.html#id12 "momentum_initialization") may be a *numpy* array of shape `(3, Npart)`.
It requires that [`position_initialization`](namelist.html#id11 "position_initialization") also be an array
with the same number of particles `Npart`.
Momentum components px, py, pz are given in successive columns.

---

## From an *HDF5* file[¶](#from-an-hdf5-file "Link to this heading")

The [`position_initialization`](namelist.html#id11 "position_initialization") may be a path to an *HDF5* file containing the
appropriate data structure. The path may point to a file,
such as `"some_folder/some_data.h5"`, but it may also contain the path
to a group inside the file, such as `"some_folder/some_data.h5/group1/group2"`.

The *HDF5* location must contain the following datasets, all 1-dimensional of equal size:

- `position/x`, list of x coordinates
- `position/y`, list of y coordinates
- `position/z`, list of z coordinates
- `weight`, list of statistical weights

The [`momentum_initialization`](namelist.html#id12 "momentum_initialization") works the same way. It must be an *HDF5* location
containing the following datasets, all 1-dimensional of equal size:

- `momentum/x`, list of px
- `momentum/y`, list of py
- `momentum/z`, list of pz

Note

This file structure is identical to that obtained from the [TrackParticles diagnostics](namelist.html#diagtrackparticles),
meaning that you can directly pass the output of a previous simulation, for instance
`"path/to/results/TrackParticlesDisordered_myspecies.h5/data/0000003000/particles/myspecies"`.