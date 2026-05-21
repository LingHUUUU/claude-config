# Particle Position Initialization

## Initialization Modes (`position_initialization`)

| Mode | Behavior |
|------|----------|
| `"random"` | Macro-particles randomly distributed within each cell. **Recommended** — avoids artificial noise from regular spacing. |
| `"regular"` | Uniform spacing within each cell. Has mathematical constraints (see below). |
| `"centered"` | All particles at cell geometric center. NOT supported in AMcylindrical geometry. |

## "regular" Mode Constraints

When using `position_initialization = "regular"`, `particles_per_cell` must satisfy dimension-based power requirements:

- **2D**: must be a perfect square (1, 4, 9, 16, 25, ...)
- **3D**: must be a perfect cube (1, 8, 27, 64, ...)

Setting `particles_per_cell = 20` in 2D without per-direction specification will trigger `createPosition` error because 20 is not a square number.

## Flexible Regular Placement: `regular_number`

To use non-power particle counts (e.g., 20) with regular spacing, or different densities per direction:

```python
Species(
    position_initialization = "regular",
    regular_number = [4, 5],   # 4 in x, 5 in y → total = 20 in 2D
    ...
)
```

- An integer list with length matching simulation dimensions
- Coordinate order: `[Nx, Ny, Nz]` in Cartesian geometry

## TrackParticles "id" Attribute

When using the "id" attribute in TrackParticles diagnostics, check the manual carefully for when particle IDs are created/assigned — the timing matters for correct tracking.
