# Laser Propagation Preprocessing (LaserOffset)

In Smilei, Lasers are provided as oscillating fields at the box boundaries. But sometimes the laser field is only known analytically at some arbitrary plane that does not coincide with the box boundary (e.g., tightly-focused beams that cannot be described with paraxial approximation).

At initialization, Smilei can perform a laser **backwards propagation** from an arbitrary plane to the box boundary. The calculated field is then injected from the boundary like a normal laser.

---

## Theoretical background

The method is similar to the *angular spectrum method*. For a scalar field \(A\) satisfying the wave equation:

\[c^2 \Delta A(x,y,z,t) = \partial_t^2 A(x,y,z,t)\]

A Fourier transform in the transverse coordinates \((y,z)\) and time \(t\) gives:

\[(-\omega^2/c^2 + k_x^2 + k_y^2 + k_z^2) A(k_x,k_y,k_z,\omega) = 0\]

Leading to the dispersion relation:

\[k_x = \sqrt{\omega^2/c^2 - k_y^2 - k_z^2}\]

The field can be propagated backwards from the definition plane to the boundary by applying the appropriate phase factor in Fourier space.

---

## Usage

The `LaserOffset` block defines a laser at an arbitrary plane:

```python
LaserOffset(
    box_side = "xmin",
    offset = 10.0,              # distance from boundary to definition plane (in Lr)
    space_time_profile = [...], # [time_profile, y_profile, z_profile]
    fft_time_window = 80.0,     # time window for FFT (optional, >= pulse duration)
    fft_time_step = 0.5,        # time step for FFT (optional)
    keep_n_components = 1,      # number of frequency components to keep (optional)
)
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| `box_side` | Boundary from which the laser enters (`"xmin"`, `"xmax"`, `"ymin"`, `"ymax"`, `"zmin"`, `"zmax"`) |
| `offset` | Distance from the boundary to the definition plane |
| `space_time_profile` | List of profiles: `[profile_t, profile_y, profile_z]` (or `[profile_t, profile_y]` in 2D) |
| `fft_time_window` | Time window for FFT computation |
| `fft_time_step` | Time step for the FFT computation |
| `keep_n_components` | Number of frequency components to keep (1 = standard, more = higher accuracy/cost) |

### Reusing from a previous simulation

Since v4.7, LaserOffset can reuse a previously computed field. This avoids recomputing the propagation for the same setup:

```python
LaserOffset(
    box_side = "xmin",
    offset = 10.0,
    space_time_profile = [...],
    file = "./previous_results/LaserOffset0.h5",  # reuse from previous run
)
```

### Available boundaries

Since v4.7, LaserOffset is available from `ymin`, `ymax`, `zmin`, and `zmax` (not just `xmin`).

---

## Notes

- LaserOffset is NOT recomputed after a restart (since v4.4)
- The propagation adds computational cost at initialization
- For simple Gaussian beams near the boundary, use standard `LaserGaussian2D/3D` instead
- Tightly-focused beams benefit most from this feature
