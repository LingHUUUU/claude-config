# Units

Like many PIC codes, Smilei handles only **dimension-less variables**, normalized to *reference* quantities.

---

## Basic reference quantities

The speed of light, the elementary charge and the electron mass provide the basis of the normalizations:

- Reference electric charge: \(Q_r = e\) (the elementary charge)
- Reference mass: \(M_r = m_e\) (the electron mass)
- Reference velocity: \(V_r = c\) (the speed of light)

Derived from these:
- Reference energy: \(K_r = m_e c^2\)
- Reference momentum: \(P_r = m_e c\)

Smilei does NOT know the scale of the problem: it lacks a reference distance or time.

---

## Arbitrary reference quantities

The user chooses a **reference angular frequency** \(\omega_r\). Usually this is the laser frequency or electron plasma frequency. From \(\omega_r\):

- Reference time: \(T_r = 1/\omega_r\)
- Reference length: \(L_r = c/\omega_r\)
- Reference electric field: \(E_r = m_e c \omega_r / e\)
- Reference magnetic field: \(B_r = m_e \omega_r / e\)
- Reference particle density: \(N_r = \varepsilon_0 m_e \omega_r^2 /e^2\)
- Reference current: \(J_r = c e N_r\)

**Warning**: \(1/N_r\) is a volume, but it is NOT equal to \(L_r^{3}\).

### Normalized equations

All quantities normalized to these references convert Maxwell's equations to dimensionless form:

\[\nabla\cdot\mathbf{E} = \rho \qquad \nabla\cdot\mathbf{B} = 0\]
\[\nabla\times\mathbf{E} = -\partial_t\mathbf{B} \qquad \nabla\times\mathbf{B} = \mathbf{j} + \partial_t\mathbf{E}\]
\[\partial_t\mathbf{p} = Z\mathbf{E} + Z\mathbf{v}\times\mathbf{B}\]

---

## Tips for the namelist

All parameters in the namelist must be in reference units. The namelist is Python code — compute conversions easily:

```python
from math import pi
wavelength = 2. * pi          # reference wavelength = 2*pi*Lr
cell_length = [0.05 * wavelength]
grid_length  = [100. * wavelength]
```

## reference_angular_frequency_SI

Required when using: collisions, ionization, QED processes (radiation reaction, Breit-Wheeler).

```python
reference_angular_frequency_SI = 2. * pi * 3e8 / 1e-6  # Lr = 1um/(2*pi)
```

This is used ONLY in specific modules (collisions, ionization, QED), NOT in the main PIC algorithms. Outputs remain in reference units.

---

## Quantities integrated over the grid

### Spatially-integrated kinetic energy density

Units: \(K_r N_r L_r^D\) where \(D\) is the simulation dimension.

Appears in Scalar diagnostics as `Ukin` (and associated quantities).

### Spatially-integrated EM energy density

Same units: \(K_r N_r L_r^D\).

Appears as `Uelm` (and associated quantities).

### Space- & time-integrated Poynting flux

Same units: \(K_r N_r L_r^D\).

Appears as `Uelm_bnd`, `PoyXmin`, `PoyXminInst` (and associated quantities).

---

## Macro-particle weights

\[\textrm{weight} = \frac{\textrm{species density} \times \textrm{cell hypervolume}}{\textrm{number of macro-particles in cell}}\]

Units: \(N_r L_r^D\). Weights are independent of cell hypervolume — they can be reused in another simulation with same \(D\), \(L_r\), \(N_r\).
