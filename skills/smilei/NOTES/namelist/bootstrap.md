# Namelist Bootstrap

## Standard Unit Conversion

```python
import math
import numpy as np

# --- 1. Basic physics parameters & unit conversion ---
lambda0 = 0.8e-6
c = 299792458.0
omega0 = 2.0 * math.pi * c / lambda0

# Smilei normalization references
Tr = 1.0 / omega0
Lr = c / omega0

# Unit conversion factors
um = 1.0e-6 / Lr
fs = 1.0e-15 / Tr
ps = 1.0e-12 / Tr
```

- Frequencies in units of omega0, lengths in Lr, times in Tr
- Velocities in units of c, densities in units of critical density nc
- `reference_angular_frequency_SI = omega0` must be set in Main()

## Variable Naming Convention

- Smilei has NO predefined convenience variables (unlike EPOCH's `micron`, `femto`, etc.)
- Define ALL quantities from first principles — use `um`, `fs`, `ps` conversion factors
- **No magic numbers**: every physical value should be computable from Python math operations
- Define SI values first, then convert to Smilei normalized units

## Grid & Patch Alignment Workflow

**Must follow this definition order** to ensure total cells are divisible by patch count:

```python
# 1. Define spatial extent and target resolution
Lx = 100.0 * um
pre_defined_dx = 0.1 * um

# 2. Define patch count per dimension (must be power of 2)
number_of_patches = [8]

# 3. Calculate cells per patch (round up to fit)
cells_per_patch = int(Lx / pre_defined_dx / number_of_patches[0]) + 1

# 4. Auto-compute exact cell size and timestep
dx = Lx / number_of_patches[0] / cells_per_patch
```

Benefits:
- Guarantees `Nx % Px == 0` (Smilei hard requirement)
- Easy to match MPI process count (total patches ≥ MPI ranks)
- GPU mode: set large `cells_per_patch`, `number_of_patches` = MPI count

### Patch Constraints
- `number_of_patches` must be power of 2
- Round `cells_per_patch` up to multiples of 8 for SIMD vectorization
- Alternative: use `timestep_over_CFL = 0.95` to auto-calculate dt
- CFL formula for 2D: `dt = 0.95 / sqrt(1/dx^2 + 1/dy^2)`

## Density Profiles

- Normalize to critical density `nc`
- Use Python functions for complex profiles (ramps, cones, masks)
- `number_density = my_profile` where profile is defined above Main()
- Common patterns: uniform slab, exponential ramp, cone mask with conditionals
