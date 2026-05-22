# PIC Algorithms

This document describes the theoretical basis of Smilei's plasma simulation. All quantities are expressed in reference units.

---

## The Maxwell-Vlasov model

The kinetic description of a collisionless plasma relies on the Vlasov-Maxwell system. Species \(s\) (charge \(q_s\), mass \(m_s\)) are described by distribution functions \(f_s(t,\mathbf{x},\mathbf{p})\) satisfying Vlasov's equation:

\[\left(\partial_t + \frac{\mathbf{p}}{m_s \gamma} \cdot \nabla + \mathbf{F}_L \cdot \nabla_{\mathbf{p}} \right) f_s = 0\]

where \(\mathbf{F}_L = q_s(\mathbf{E} + \mathbf{v}\times\mathbf{B})\) is the Lorentz force and \(\gamma = \sqrt{1 + p^2}\) is the Lorentz factor.

The electromagnetic fields satisfy Maxwell's equations with sources (charge density \(\rho\) and current density \(\mathbf{j}\)) computed from the distribution functions:

\[\rho = \sum_s q_s \int f_s d\mathbf{p} \qquad \mathbf{j} = \sum_s q_s \int \mathbf{v} f_s d\mathbf{p}\]

---

## The PIC method

The PIC method approximates the continuous distribution function by a collection of *macro-particles*:

\[f_s(t,\mathbf{x},\mathbf{p}) \approx \sum_{k=1}^{N_s} w_k S(\mathbf{x} - \mathbf{x}_k) \delta(\mathbf{p} - \mathbf{p}_k)\]

where \(w_k\) is the statistical weight, \(\mathbf{x}_k\) the position, \(\mathbf{p}_k\) the momentum, and \(S\) the shape function (spline of chosen order).

### The PIC cycle (4 steps)

1. **Field interpolation**: Interpolate EM fields from grid to particle positions using shape function \(S\)
2. **Particle push**: Update particle momenta and positions using the equation of motion
3. **Current projection (deposition)**: Project particle currents onto the grid (charge-conserving scheme)
4. **Maxwell solver**: Advance EM fields using Maxwell's equations on the grid

---

## Maxwell solvers

### FDTD (Yee) solver

The standard FDTD method places E and B fields on a staggered Yee mesh:
- E fields at cell edges, B fields at cell faces
- E and B are staggered in time by half a timestep
- Second-order accurate in space and time

The CFL condition restricts the timestep:

\[\Delta t < \frac{1}{\sqrt{\frac{1}{\Delta x^2} + \frac{1}{\Delta y^2} + \frac{1}{\Delta z^2}}}\]

### Non-standard FDTD solvers

Smilei provides 4th-order non-standard FDTD solvers (`Bouchard`, `M4`) that use modified coefficients and larger stencils for improved dispersion properties.

### PSATD (experimental)

Pseudo-Spectral Analytical Time Domain solver uses spectral methods for spatial derivatives, eliminating numerical dispersion.

---

## Particle pushers

### Boris pusher (default)

The standard Boris algorithm splits the Lorentz force update into:
1. Half electric acceleration
2. Magnetic rotation
3. Half electric acceleration

Properties: time-reversible, volume-preserving in phase space, good long-term energy conservation.

### Vay's pusher

An improved relativistic pusher with better conservation properties at high Lorentz factors.

### Higuera-Cary pusher

A volume-preserving relativistic pusher combining advantages of Boris and Vay methods.

---

## Current projection

Smilei uses a charge-conserving current deposition scheme (Esirkepov method). This ensures that \(\nabla\cdot\mathbf{E} = \rho\) is maintained at machine precision throughout the simulation.

---

## Shape functions (interpolation orders)

The shape function \(S\) controls how macro-particles interact with the grid:

| Order | Support | Description |
|-------|---------|-------------|
| 1 | 1 cell | Nearest-grid-point (NGP), noisy |
| 2 | 2 cells | Quadratic spline (default), good balance |
| 3 | 3 cells | Cubic spline |
| 4 | 4 cells | Quartic spline, reduced self-heating, best for relativistic problems |

Higher order = smoother fields, less self-heating, but more computation.

---

## Initial fields

### Poisson solver

If net charge exists at initialization, the electrostatic field is solved from Poisson's equation:

\[\nabla^2 \phi = -\rho \qquad \mathbf{E} = -\nabla\phi\]

Available solvers: standard Poisson, relativistic Poisson (for fast-moving species).

### Field initialization for relativistic beams

For relativistic species, the full electromagnetic fields are solved using a modified Poisson's equation accounting for the beam velocity.

---

## The timestep

The CFL condition must be satisfied for numerical stability:

- 1D: \(\Delta t < \Delta x\)
- 2D: \(\Delta t < 1 / \sqrt{1/\Delta x^2 + 1/\Delta y^2}\)
- 3D: \(\Delta t < 1 / \sqrt{1/\Delta x^2 + 1/\Delta y^2 + 1/\Delta z^2}\)

In practice, use `timestep_over_CFL` (default 0.95) to set the safety factor:

```python
Main(timestep_over_CFL = 0.95, ...)
```
