# Initialize Particles from an Array or a File

`position_initialization` and `momentum_initialization` may be set to a *numpy* array or an *HDF5* file containing particle data to be imported.

**Incompatibilities**:
- Position initialization from array/file is incompatible with `number_density`, `charge_density`, and `particles_per_cell`
- Momentum initialization from array/file is incompatible with `temperature` and `mean_velocity`
- Particles initialized outside the initial simulation domain will NOT be created

---

## From a numpy array

### Position initialization

Numpy array of shape `(Ndim+1, Npart)` where `Ndim` is the number of particle dimensions and `Npart` is the total number of particles:
- Columns 0 through Ndim-1: position components (x, y, z)
- Last column: weights

### Momentum initialization

Numpy array of shape `(3, Npart)`. Requires that `position_initialization` also be an array with the same `Npart`:
- Columns: px, py, pz

```python
import numpy as np

Npart = 100000
positions = np.zeros((4, Npart))  # 3 position + weight
positions[0,:] = np.random.uniform(0, 10.0, Npart)  # x
positions[1,:] = np.random.uniform(0, 5.0, Npart)   # y
positions[2,:] = 0.0                                  # z
positions[3,:] = 0.01                                 # weight

momenta = np.zeros((3, Npart))
momenta[0,:] = np.random.normal(0, 0.1, Npart)       # px

Species(
    name = "electron",
    position_initialization = positions,
    momentum_initialization = momenta,
    mass = 1.0,
    charge = -1.0,
    boundary_conditions = [["remove"]],
)
```

---

## From an HDF5 file

### Position initialization

Path to an HDF5 file or group containing datasets (all 1-dimensional of equal size):
- `position/x` — list of x coordinates
- `position/y` — list of y coordinates
- `position/z` — list of z coordinates
- `weight` — list of statistical weights

### Momentum initialization

Path to an HDF5 file or group containing datasets:
- `momentum/x` — list of px
- `momentum/y` — list of py
- `momentum/z` — list of pz

**Important**: This file structure is identical to the output of `DiagTrackParticles`, meaning you can directly pass the output of a previous simulation:

```python
Species(
    name = "electron",
    position_initialization = "path/to/results/TrackParticlesDisordered_myspecies.h5/data/0000003000/particles/myspecies",
    momentum_initialization = "path/to/results/TrackParticlesDisordered_myspecies.h5/data/0000003000/particles/myspecies",
    mass = 1.0,
    charge = -1.0,
    boundary_conditions = [["remove"]],
)
```

---

## Notes

- The HDF5 file path may include a path to a group inside the file: `"some_folder/some_data.h5/group1/group2"`
- This feature is particularly useful for:
  - Continuing a simulation with particle data from a previous run
  - Initializing complex particle distributions computed externally
  - Plasma Wakefield Acceleration studies where a relativistic beam must be injected
