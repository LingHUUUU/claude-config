# Units[¶](#units "Link to this heading")

Like many PIC codes, **Smilei** handles only **dimension-less variables**,
normalized to *reference* quantities.

---

## Basic reference quantities[¶](#basic-reference-quantities "Link to this heading")

The speed of light, the elementary charge and the electron mass provide the basis
of the normalizations in **Smilei**:

- Reference electric charge \(Q\_r = e\) (the elementary charge)
- Reference mass \(M\_r = m\_e\) (the electron mass)
- Reference velocity \(V\_r = c\) (the speed of light)

We can derive from these:

- a reference energy \(K\_r = m\_e c^2\)
- a reference momentum \(P\_r = m\_e c\)

Even with these normalizations, **Smilei** **does not know the scale of the problem**:
it lacks a reference distance, or equivalently, a reference time.

---

## Arbitrary reference quantities[¶](#arbitrary-reference-quantities "Link to this heading")

Instead of choosing a physical constant (for example, the electron radius) as a reference,
the scale of the problem is not decided *a priori*, and the user is free to scale the result
of the simulation to any value.
In fact, quantities are proportional an *unknown* reference frequency
\(\omega\_r\), which can be scaled by the user *a posteriori*.

Usually, \(\omega\_r\) will be an important frequency of the problem.
For example, if there is a laser, it could be the laser frequency.
Or it could be the electron plasma frequency.

From this reference frequency \(\omega\_r\), we define:

- a reference time \(T\_r = 1/\omega\_r\)
- a reference length \(L\_r = c/\omega\_r\)
- a reference electric field \(E\_r = m\_e c \omega\_r / e\)
- a reference magnetic field \(B\_r = m\_e \omega\_r / e\)
- a reference particle density \(N\_r = \varepsilon\_0 m\_e \omega\_r^2 /e^2\)
- a reference current \(J\_r = c\, e\, N\_r\)

Warning

\(1/N\_r\) is a volume, but counter-intuitively, it is **not equal** to \(L\_r^{3}\).

Normalizing all quantities to these references is convenient for resolving Maxwell’s equations,
and the charges equation of motion, as it converts them into a dimension-less set of equations:

\[ \begin{align}\begin{aligned}\begin{split}\mathbf{\nabla}\cdot\mathbf{E} = \rho
\quad\quad
\nabla\cdot\mathbf{B} & = 0 \\\end{split}\\\nabla\times\mathbf{E} = - \partial\_t \mathbf{B}
\quad\quad
\nabla\times\mathbf{B} = & \; \mathbf{j} + \partial\_t \mathbf{E}\end{aligned}\end{align} \]

\[\partial\_t \mathbf{p} = Z \mathbf{E} + Z \mathbf{v}\times\mathbf{B}\]

where \(\mathbf{E}\), \(\mathbf{B}\), \(\mathbf{j}\) and \(\mathbf{\rho}\)
are the electric field, magnetic field, current density and charge density, normalized to
\(E\_r\), \(B\_r\), \(J\_r\) and \(Q\_r N\_r\), respectively. \(Z\) and
\(\mathbf p\) are a particle’s charge and momentum, normalized to \(Q\_r\) and
\(P\_r\), respectively. Note that the temporal and spatial derivatives are also
normalized to \(T\_r\) and \(L\_r\), respectively.

---

## Tips for the namelist[¶](#tips-for-the-namelist "Link to this heading")

In the [namelist](../Use/namelist.html), the user must provide all parameters in units of \(Q\_r\),
\(M\_r\), \(V\_r\), \(K\_r\), \(P\_r\), \(T\_r\), \(L\_r\), \(E\_r\),
\(B\_r\), \(N\_r\) or \(J\_r\).

This may be cumbersome if you know your input data in other units.
However, the namelist is actually a *python* code that can compute conversions easily.

For example, let us assume that you know your problem size in units of the wavelength.
Knowing that the reference wavelength is \(2\pi L\_r\), you can multiply all your
lengths by \(2\pi\):

```
from math import pi
wavelength = 2. * pi
cell_length = [0.05 * wavelength]
grid_length  = [100. * wavelength]
```

---

## Problems requiring explicit units[¶](#problems-requiring-explicit-units "Link to this heading")

Sometimes, **Smilei** may be requested to compute other things than Maxwell’s
equations. That is the case, for example, for computing [collisions](collisions.html) or ionization.
In these situations, equations cannot be normalized to dimension-less terms, and
the code must know the value of \(\omega\_r\) in physical units. This requires
defining an [extra parameter in the namelist](../Use/namelist.html#reference-angular-frequency-si).

For instance, `reference_angular_frequency_SI = 2.*pi*3e8/1e-6` means that
\(L\_r = 1\,\mathrm{\mu m} /(2\pi)\).
This information will be used only in some specific parts of the code (collisions, ionization, …)
but not in the main PIC algorithms.

Warning

The outputs of the code are not converted to SI.
They are all kept in the reference units listed above.

---

## Quantities integrated over the grid[¶](#quantities-integrated-over-the-grid "Link to this heading")

Special care must be taken when considering local quantities that are spatially
integrated.

1. The spatially-integrated kinetic energy density

The particle kinetic energy density is naturally in units of \(K\_r N\_r\).
Integrating over space give different results depending on the simulation dimension.
In 1D, this space is a length, with units \(L\_r\); in 2D, it is a surface, with units
\(L\_r^2\); and in 3D, it is a volume, with units \(L\_r^3\).
Overall, the integrated energy has the units \(K\_r N\_r L\_r^D\)
where \(D\) is the simulation dimension. Note that we could expect
to obtain, in 3D, an energy with units \(K\_r\), but counter-intuitively
it has the units \(K\_r N\_r L\_r^3\).

These kinetic energies appear, for instance, in the [Scalar diagnostics](../Use/namelist.html#diagscalar) as
`Ukin` (and associated quantities).

2. The spatially-integrated electromagnetic energy density

The electromagnetic energy density has the units \(E\_r^2/\varepsilon\_0 = K\_r N\_r\).
Consequently, the spatially-integrated electromagnetic energy density has
the units \(K\_r N\_r L\_r^D\); the same as the integrated kinetic energy density above.

These electromagnetic energies appear, for instance, in the [Scalar diagnostics](../Use/namelist.html#diagscalar) as
`Uelm` (and associated quantities).

3. The space- & time-integrated Poynting flux

The Poynting flux has the units \(E\_r B\_r / \mu\_0 = V\_r K\_r N\_r\).
Consequently, the flux integrated over a boundary, and over time, has the units
\(V\_r K\_r N\_r L\_r^{D-1} T\_r = K\_r N\_r L\_r^D\), which is the same as the
integrated energy densities above.

This integrated Poynting flux appears, for instance, in the [Scalar diagnostics](../Use/namelist.html#diagscalar) as
`Uelm_bnd`, `PoyXmin`, `PoyXminInst` (and associated quantities).

---

## Macro-particle weights[¶](#macro-particle-weights "Link to this heading")

Macro-particles are assigned a *statistical weight* which measures
their contribution to the plasma distribution function.
In **Smilei**, this weight is defined for each particle at the moment of its creation
(usually at the beginning of the simulation),
and is never modified afterwards. Its definition reads:

\[\textrm{macro-particle weight} = \frac
{\textrm{species density} \times \textrm{cell hypervolume}}
{\textrm{number of macro-particles in cell}}\]

As the density is in units of \(N\_r\) and the cell hypervolume in
units of \(L\_r^D\) (where \(D\) is the simulation dimension),
then the units of weights is \(N\_r L\_r^D\).

This definition of weights ensures that they do not depend on the
cell hypervolume, i.e. they can be reused in another simulation, as long as
\(D\), \(L\_r\) and \(N\_r\) are unchanged.