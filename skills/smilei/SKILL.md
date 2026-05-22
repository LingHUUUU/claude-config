---
name: smilei
description: "Use this skill when working with Smilei PIC (Particle-In-Cell) simulations for laser-plasma interaction. Covers writing namelists/input files, running simulations with MPI on Slurm clusters, post-processing with happi, and troubleshooting. Trigger when user mentions Smilei, PIC simulation, laser-plasma, namelist, happi, or references .py input files in simulation directories."
---

# Smilei PIC Simulation Skill

**Always read [notes_index.md](notes_index.md) for the latest project-specific conventions and accumulated experience.**

**For every simulation task, follow the 5-stage workflow in [workflow.md](workflow.md). Do not skip stages or proceed without user approval at each gate.**

## Quick Reference

| Task | Guide |
|------|-------|
| Write a namelist | Start from [SOURCE/Use/namelist/_index.md](SOURCE/Use/namelist/_index.md) — pick the block you need |
| Post-process data | Start from [SOURCE/Use/happi/_index.md](SOURCE/Use/happi/_index.md) — happi API by topic |
| Run a simulation | [SOURCE/Use/run.md](SOURCE/Use/run.md) |
| Install Smilei | [SOURCE/Use/installation.md](SOURCE/Use/installation.md) |
| Understand units | [SOURCE/Understand/units.md](SOURCE/Understand/units.md) |
| Define density profiles | [SOURCE/Use/profiles.md](SOURCE/Use/profiles.md) |
| Debug / Troubleshoot | [SOURCE/Use/troubleshoot.md](SOURCE/Use/troubleshoot.md) |
| Tutorials reference | [SOURCE/tutorials/](SOURCE/tutorials/) (basics, advanced, parallel computing) |
| Smilei algorithms | [SOURCE/Understand/algorithms.md](SOURCE/Understand/algorithms.md) |
| Physics modules | [SOURCE/Understand/physics_modules.md](SOURCE/Understand/physics_modules.md) |
| HPC & parallelization | [SOURCE/Understand/performances.md](SOURCE/Understand/performances.md) |
| Track particle IDs | [SOURCE/Use/ids.md](SOURCE/Use/ids.md) |
| Laser offset setup | [SOURCE/Use/laser_offset.md](SOURCE/Use/laser_offset.md) |
| Particle from file | [SOURCE/Use/particle_initialization.md](SOURCE/Use/particle_initialization.md) |
| Full site index | [SOURCE/site.md](SOURCE/site.md), [understand.md](SOURCE/understand.md), [use.md](SOURCE/use.md) |

**For complete official documentation, see [SMILEI_MANUAL_SOURCE/](../SMILEI_MANUAL_SOURCE/).**

---

## Namelist Blocks (split by topic)

| File | Content |
|------|---------|
| [_index.md](SOURCE/Use/namelist/_index.md) | Full index of all namelist blocks |
| [00_general.md](SOURCE/Use/namelist/00_general.md) | General rules, Python workflow |
| [01_main.md](SOURCE/Use/namelist/01_main.md) | Main variables (geometry, grid, timestep, BC, PML, output) |
| [02_load_balancing.md](SOURCE/Use/namelist/02_load_balancing.md) | Load Balancing, SDMD, Vectorization |
| [03_moving_window.md](SOURCE/Use/namelist/03_moving_window.md) | Moving window |
| [04_filtering.md](SOURCE/Use/namelist/04_filtering.md) | Current and Field filtering |
| [05_species.md](SOURCE/Use/namelist/05_species.md) | Species block (position, momentum, ionization, radiation) |
| [06_injector_merging.md](SOURCE/Use/namelist/06_injector_merging.md) | Particle Injector and Particle Merging |
| [07_lasers.md](SOURCE/Use/namelist/07_lasers.md) | Lasers (all types, parameters, time envelopes) |
| [08_envelope.md](SOURCE/Use/namelist/08_envelope.md) | Laser envelope model |
| [09_external_fields.md](SOURCE/Use/namelist/09_external_fields.md) | External/Prescribed fields, Antennas, Walls |
| [10_collisions.md](SOURCE/Use/namelist/10_collisions.md) | Collisions & reactions |
| [11_radiation_qed.md](SOURCE/Use/namelist/11_radiation_qed.md) | Radiation reaction, Multiphoton Breit-Wheeler |
| [12a_scalar.md](SOURCE/Use/namelist/12a_scalar.md) | Scalar diagnostics |
| [12b_fields.md](SOURCE/Use/namelist/12b_fields.md) | Fields diagnostics |
| [12c_probe.md](SOURCE/Use/namelist/12c_probe.md) | Probe diagnostics |
| [12d_particle_binning.md](SOURCE/Use/namelist/12d_particle_binning.md) | ParticleBinning diagnostics |
| [12e_screen_radiation.md](SOURCE/Use/namelist/12e_screen_radiation.md) | Screen and RadiationSpectrum diagnostics |
| [12f_track_perf.md](SOURCE/Use/namelist/12f_track_perf.md) | TrackParticles, NewParticles, Performances diagnostics |
| [13_time_checkpoint.md](SOURCE/Use/namelist/13_time_checkpoint.md) | Time selections, Checkpoints, Variables |

## Happi Blocks (split by topic)

| File | Content |
|------|---------|
| [_index.md](SOURCE/Use/happi/_index.md) | Full index of all happi topics |
| [00_open.md](SOURCE/Use/happi/00_open.md) | Opening simulations, namelist access |
| [01_diagnostics.md](SOURCE/Use/happi/01_diagnostics.md) | All diagnostic types (Scalar, Field, Probe, etc.) |
| [02_data_plot.md](SOURCE/Use/happi/02_data_plot.md) | Data retrieval, VTK export, plotting, animation |

---

## Namelist Format

Smilei supports Python-based input files. The namelist is composed of *blocks*:

### Modern `input.py` format (recommended)

```python
import math

# Reference frequency
c = 299792458.0
lambda0 = 1.0e-6
omega0 = 2.0 * math.pi * c / lambda0
Lr = c / omega0          # reference length
Tr = 1.0 / omega0        # reference time

Main(
    geometry = "2Dcartesian",
    reference_angular_frequency_SI = omega0,
    grid_length = [80.0 * Lr, 60.0 * Lr],
    cell_length = [0.05 * Lr, 0.05 * Lr],
    number_of_patches = [16, 16],
    timestep = 0.95 / math.sqrt(2) * 0.05 * Lr / c,
    simulation_time = 100.0 * Tr,
    print_every = 100,
)

Species(
    name = "electron",
    position_initialization = "random",
    momentum_initialization = "maxwell-juettner",
    particles_per_cell = 64,
    mass = 1.0,
    charge = -1.0,
    number_density = 0.01,
    temperature = [0.001],
    boundary_conditions = [["remove", "remove"], ["remove", "remove"]],
)

LaserGaussian2D(
    box_side = "xmin",
    a0 = 2.0,
    omega = 1.0,
    focus = [5.0 * Lr, 30.0 * Lr],
    waist = 5.0 * Lr,
    time_envelope = tgaussian(center=20.0*Tr, fwhm=10.0*Tr),
)

DiagScalar(every = 100)
DiagFields(every = 100, fields = ["Ex", "Ey", "Bz", "Rho_electron"])
DiagParticleBinning(
    every = 100,
    species = ["electron"],
    axes = [["x", 0, 80.0*Lr, 200], ["px", -5.0, 5.0, 200]],
)
```

### Command-line arguments

Any python instruction can be passed as a command-line argument:
```bash
mpirun -n 4 ./smilei input.py "Main.print_every=10"
```

---

## Key Conventions

### Units & Normalization
```python
c = 299792458.0; lambda0 = 1.0e-6
omega0 = 2.0 * math.pi * c / lambda0
Lr = c / omega0; Tr = 1.0 / omega0
```
- Frequencies in units of `omega0`, lengths in `Lr`, times in `Tr`
- Velocities in units of `c`, densities in units of `N_r = epsilon_0 * m_e * omega_r^2 / e^2`
- Reference mass `M_r = m_e`, reference charge `Q_r = e`
- For collisions/ionization/QED: `reference_angular_frequency_SI` is required
- **Outputs are always in reference units, not SI**

### Grid Setup
- `number_of_patches`: integer per direction (must divide `grid_length`)
- Round `cells_per_patch` up to multiples of 8 (SIMD vectorization)
- CFL in 2D: `dt = 0.95 / sqrt(1/dx^2 + 1/dy^2)`
- CFL in 3D: `dt = 0.95 / sqrt(1/dx^2 + 1/dy^2 + 1/dz^2)`

### Common Boundary Conditions
- EM fields: `silver-muller` (absorbing), `periodic`, `reflective`, `PML`
- Particles: `remove` (absorbing), `reflect`, `periodic`, `thermalization`
- Laser injection: `box_side = "xmin"` (or `xmax`, `ymin`, `ymax`)

### HPC (this project)
- Slurm `partition=cu`, 2x28 CPUs/node
- `mpirun -np $SLURM_NTASKS smilei input.py`
- Array jobs via `submit_array.job`
- OpenMP: `export OMP_NUM_THREADS=4`

---

## Geometries

| `geometry` | Description |
|------------|-------------|
| `1Dcartesian` | 1D Cartesian (x only) |
| `2Dcartesian` | 2D Cartesian (x, y) |
| `3Dcartesian` | 3D Cartesian (x, y, z) |
| `AMcylindrical` | Cylindrical with azimuthal Fourier decomposition |

AMcylindrical decomposes fields in azimuthal modes \(\exp(-im\theta)\). Reduces cost of 3D-like simulations by ~order of magnitude for near-cylindrically-symmetric problems (e.g., LWFA).

## Maxwell Solvers

| Solver | Description |
|--------|-------------|
| `Yee` (default) | Standard FDTD, 2nd order |
| `Bouchard` | 4th-order non-standard FDTD, 2D/3D |
| `M4` | 4th-order non-standard FDTD |
| `Lehe` | Available in AMcylindrical |
| `Terzani` | Low-dispersion, AMcylindrical |
| PSATD | Pseudo-spectral analytical time domain (experimental) |

## Particle Pushers

| Pusher | Description |
|--------|-------------|
| `Boris` (default) | Standard Boris pusher |
| `Vay` | Vay's pusher |
| `HigueraCary` | Higuera-Cary pusher |

## Interpolation

| Order | Description |
|-------|-------------|
| 2 (default) | Standard quadratic spline |
| 4 | Higher order, reduced self-heating |
| B-TIS3 (experimental) | Reduces Numerical Cherenkov Radiation |

---

## Post-processing (happi)

```python
import happi

# Open
S = happi.Open("path/to/results")

# Namelist info
print(S.namelist.Main.geometry)
print(S.namelist.Species)

# Diagnostics
diags = S.getDiags()          # list all diagnostics
scalars = S.getScalars()      # list scalar keys

# Scalar
sc = S.Scalar(0)
sc.plot()
data = sc.getData()

# Field
F = S.Field(0, timestep=1000)
F.plot()
F.animate()

# ParticleBinning
Pb = S.ParticleBinning(0)
Pb.slide()
Pb.plot()

# Multi-plot
happi.multiPlot(F1, F2)
```

---

## Troubleshooting Quick Reference

| Problem | Check |
|---------|-------|
| Not starting | Test mode: `./smilei_test input.py` (1 MPI process only) |
| Self-heating | Increase `interpolation_order` (2->4), increase ppc, reduce CFL |
| Boundary reflections | `silver-muller` + `remove` + PML layers |
| Load imbalance | `LoadBalancing(every=...)` block |
| OpenMPI unstable | `mpirun --mca btl ^vader` |
| Wrong physics results | Check `reference_angular_frequency_SI`, CFL, units normalization |
| NaN in profiles | Check Python-defined functions for NaN values |
| Simulation stops | Check `print_every` to isolate iteration; try coarser resolution |
| Performance issues | Adjust patch count/distribution, enable LoadBalancing, check vectorization compilation flags |
