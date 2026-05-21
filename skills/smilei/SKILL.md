---
name: smilei
description: "Use this skill when working with Smilei PIC (Particle-In-Cell) simulations for laser-plasma interaction. Covers writing namelists/input files, running simulations with MPI on Slurm clusters, post-processing with happi, and troubleshooting. Trigger when user mentions Smilei, PIC simulation, laser-plasma, namelist, happi, or references .py input files in simulation directories."
---

# Smilei PIC Simulation Skill

**Always read [notes_index.md](notes_index.md) for the latest project-specific conventions and accumulated experience.**

## Quick Reference

| Task | Guide |
|------|-------|
| Write a namelist | Start from [SOURCE/Use/namelist/_index.md](SOURCE/Use/namelist/_index.md) — pick the block you need |
| Post-process data | Start from [SOURCE/Use/happi/_index.md](SOURCE/Use/happi/_index.md) — happi API by topic |
| Run a simulation | [SOURCE/Use/run.md](SOURCE/Use/run.md) |
| Install Smilei | [SOURCE/Use/installation.md](SOURCE/Use/installation.md) |
| Understand units | [SOURCE/Understand/units.md](SOURCE/Understand/units.md) |
| Define density profiles | [SOURCE/Use/profiles.md](SOURCE/Use/profiles.md) |
| Troubleshoot | [SOURCE/Use/troubleshoot.md](SOURCE/Use/troubleshoot.md) |
| Tutorials | [SOURCE/tutorials/](SOURCE/tutorials/) |

### Namelist blocks (split by topic — read only what you need)

| File | Content |
|------|---------|
| [SOURCE/Use/namelist/_index.md](SOURCE/Use/namelist/_index.md) | Full index of all namelist blocks |
| [00_general.md](SOURCE/Use/namelist/00_general.md) | General rules, Python workflow |
| [01_main.md](SOURCE/Use/namelist/01_main.md) | Main variables (geometry, grid, BC, PML, etc.) |
| [05_species.md](SOURCE/Use/namelist/05_species.md) | Species block |
| [08_lasers.md](SOURCE/Use/namelist/08_lasers.md) | Lasers block |
| [12_diagnostics.md](SOURCE/Use/namelist/12_diagnostics.md) | Scalar, Field, Probe, ParticleBinning, Screen, RadiationSpectrum |
| [14_checkpoints.md](SOURCE/Use/namelist/14_checkpoints.md) | Checkpoints, restart, time selections |

### Happi blocks (split by topic)

| File | Content |
|------|---------|
| [SOURCE/Use/happi/_index.md](SOURCE/Use/happi/_index.md) | Full index of all happi topics |
| [00_open.md](SOURCE/Use/happi/00_open.md) | Opening simulations, namelist access |
| [01_diagnostics.md](SOURCE/Use/happi/01_diagnostics.md) | All diagnostic types |
| [02_data_plot.md](SOURCE/Use/happi/02_data_plot.md) | Data retrieval, VTK export, plotting |

---

## Namelist Format

Smilei supports two input formats:

### Modern `input.py` format (recommended)
```python
Main(
    geometry = "2Dcartesian",
    grid_length = [Lx, Ly],
    cell_length = [dx, dy],
    number_of_patches = [16, 16],
    timestep = dt,
    simulation_time = T_max,
    reference_angular_frequency_SI = omega0,
)

Species(
    name = "electron",
    position_initialization = "random",
    momentum_initialization = "maxwell-juettner",
    particles_per_cell = 64,
    mass = 1.0,
    charge = -1.0,
    number_density = n_profile,
    boundary_conditions = [["remove"]],
)

LaserGaussian2D(
    box_side = "xmin", a0 = 2.0, omega = 1.0,
    focus = [x_focus, y_focus], waist = w0,
    time_envelope = tgaussian(...),
)

DiagFields(every = 100, fields = ["Ex", "Ey", "Bz", "Rho_electron"])
```

---

## Key Conventions

### Units & Normalization
```python
c = 299792458.0; lambda0 = 1.0e-6
omega0 = 2.0 * math.pi * c / lambda0
Lr = c / omega0; Tr = 1.0 / omega0
```
- Frequencies in units of omega0, lengths in Lr, times in Tr
- Velocities in units of c, densities in units of nc

### Grid Setup
- `number_of_patches` must be powers of 2
- Round `cells_per_patch` up to multiples of 8 (SIMD vectorization)
- CFL: `dt = 0.95 / sqrt(1/dx^2 + 1/dy^2)` for 2D

### Common BCs
- EM: `silver-muller` (absorbing), `periodic`, `reflective`
- Particles: `remove` (absorbing), `reflect`, `periodic`
- Laser: `box_side = "xmin"` (or `xmax`, `ymin`, `ymax`)

### HPC (this project)
- Slurm `partition=cu`, 2x28 CPUs/node
- `mpirun -np $SLURM_NTASKS smilei input.py`
- Array jobs via `submit_array.job`

---

## Post-processing (happi)

```python
import happi
S = happi.Open("path/to/results")
F = S.Field(0, timestep=1000); F.plot(); F.animate()
sc = S.Scalar(0); sc.plot(); sc.getData()
Pb = S.ParticleBinning(0); Pb.slide()
happi.multiPlot(F1, F2)
```

---

## Troubleshooting

| Problem | Check |
|---------|-------|
| Not starting | Test mode: `./smilei_test input.py` |
| Self-heating | Increase `interpolation_order` (2→4), increase ppc, reduce CFL |
| Boundary reflections | `silver-muller` + `remove` + PML |
| Load imbalance | `LoadBalancing(every=...)` block |
| OpenMPI unstable | `mpirun --mca btl ^vader` |
