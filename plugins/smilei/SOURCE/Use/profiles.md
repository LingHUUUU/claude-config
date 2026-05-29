# Profiles

Several quantities require profiles: particle charge, density, external fields, etc. Profiles can be *spatial* or *temporal*.

---

## Constant profiles

```python
Species(..., charge = -3., ...)                     # charge Z* = 3
Species(..., number_density = 10., ...)             # density = 10 Nr (use number_density OR charge_density)
Species(..., mean_velocity = [0.05, 0., 0.], ...)   # drift velocity vx = 0.05c over whole box
Species(..., temperature = [1e-5], ...)             # temperature T = 1e-5 m_e c^2 (isotropic)
Species(..., temperature = [1e-5, 2e-5, 2e-5], ...) # anisotropic temperature
Species(..., particles_per_cell = 10., ...)         # 10 particles per cell
ExternalField(field="Bx", profile=0.1)              # constant Bx = 0.1 Br
```

---

## Python function profiles

Any Python function of spatial coordinates and/or time can be a profile:

```python
# 1D spatial profile
def n_profile(x):
    if x < 10.0: return 1.0
    else: return 0.0

Species(..., number_density = n_profile, ...)
```

```python
# 2D spatial profile
def density(x, y):
    return 1.0 * (y > 10.0) * (y < 30.0)

Species(..., number_density = density, ...)
```

```python
# 3D spatial + temporal profile
def n(x, y, z, t):
    return 1.0 * (x < 10.0 + 0.01*t)

Species(..., number_density = n, ...)
```

```python
# Laser profile with transverse coordinates
def transverse_profile(y, z):
    return exp(-(y**2 + z**2) / waist**2)
```

### Profile functions in ExternalField
```python
def By_profile(x, y):
    return 0.01 * cos(x)

ExternalField(field="By", profile=By_profile)
```

---

## Predefined analytical profiles

Several analytical profiles are available:

```python
# Gaussian density profile
Species(..., number_density = gaussian(x0=10.0, amplitude=1.0, length=2.0), ...)

# Trapezoidal density profile
Species(..., number_density = trapezoidal(x_start=5.0, x_end=15.0, amplitude=1.0), ...)

# Polynomial density profile
Species(..., number_density = polygonal(x_points=[0.0,10.0,20.0], y_values=[0.0,1.0,0.0]), ...)
```

---

## Profile dimensions

Profiles accept different numbers of arguments depending on geometry:
- 1Dcartesian: `f(x)` or `f(x, t)`
- 2Dcartesian: `f(x, y)` or `f(x, y, t)`
- 3Dcartesian: `f(x, y, z)` or `f(x, y, z, t)`
- AMcylindrical: `f(x, r)` or `f(x, r, t)`

If fewer arguments are given, Smilei does not pass extra dimensions.

---

## Profiles from files

Some profiles can be imported from an external file (available since v4.6). This is useful for complex density distributions computed externally.

---

## Important notes

- `number_density` and `charge_density` are mutually exclusive
- Negative profile values are set to 0 for density
- Position initialization `"random"` is incompatible with density profiles that are 0 at some locations (use `"centered"` or `"regular"` instead)
- Avoid `NaN` values in your Python profile functions
