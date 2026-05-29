# Opening Simulations

## `happi.Open()`

```python
happi.Open(results_path='.', reference_angular_frequency_SI=None,
           show=True, verbose=True, scan=True, pint=True)
```

Open one or more Smilei simulations. Multiple simulations can be opened at once if they are restarts of the same simulation.

**Returns:** An object `S` providing access to namelist, diagnostic information, and diagnostic constructors.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `results_path` | str / list[str] | `"."` | Path(s) to simulation result directories. Supports wildcards (`*`, `?`). |
| `reference_angular_frequency_SI` | float | None | Overrides the simulation's `reference_angular_frequency_SI` for unit rescaling. |
| `show` | bool | `True` | If `False`, figures do not display on screen. |
| `verbose` | bool | `True` | If `False`, suppress printed information during post-processing. |
| `scan` | bool | `True` | If `False`, skip HDF5 file scan and namelist reading. |
| `pint` | bool | `True` | If `True`, attempt to load Pint for unit management. |

### Example
```python
S = happi.Open("path/to/my/results")
```

---

## Namelist Access

Access any namelist variable via `S.namelist`:

```python
S = happi.Open("path/to/my/results")
print(S.namelist.Main.timestep)    # timestep value
print(S.namelist.Main.geometry)    # simulation geometry
```

### Iterating over multi-instance blocks

Blocks like `Species`, `ExternalField`, `DiagProbe` can have multiple instances:

```python
# Iterate all species
for species in S.namelist.Species:
    print("species " + species.name + " has mass " + str(species.mass))

# Access by index
F = S.namelist.ExternalField[0]

# Access species by name
species = S.namelist.Species["electron1"]
```

---

## Diagnostic Information Methods

### `S.getDiags(diagType)`

Returns list of available diagnostics of the given type.

| Parameter | Type | Description |
|-----------|------|-------------|
| `diagType` | str | Diagnostic type: `"Field"`, `"Probe"`, `"ParticleBinning"`, `"Screen"`, `"RadiationSpectrum"`, `"TrackParticles"`, `"Performances"` |

### `S.getScalars()`

Returns list of available scalar names.

### `S.getTrackSpecies()`

Returns list of available tracked-particle species names.

### `S.fieldInfo(diag)`

| Parameter | Type | Description |
|-----------|------|-------------|
| `diag` | int/str | Field diagnostic number or name |

Returns dict with keys: `"diagNumber"`, `"diagName"`, `"fields"` (list of available fields; in AMcylindrical, a dict with modes per field).

### `S.probeInfo(diag)`

| Parameter | Type | Description |
|-----------|------|-------------|
| `diag` | int/str | Probe diagnostic number or name |

Returns dict with keys: `"probeNumber"`, `"probeName"`, `"fields"`.

### `S.performanceInfo()`

Returns dict with keys: `"quantities_uint"`, `"quantities_double"`, `"patch_arrangement"`, `"timesteps"`.

---

## Direct Diagnostic Access

Calling `S.Scalar`, `S.Field`, `S.Probe` (etc.) without arguments prints general information about available diagnostics of that type.

For full diagnostic constructor reference, see [Diagnostics Reference](02_diagnostics.md).

---

## `happi.openNamelist(namelist)`

Read a namelist file without opening a simulation:

```python
namelist = happi.openNamelist("path/to/my/namelist.py")
print(namelist.Main.timestep)
```
