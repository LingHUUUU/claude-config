## Open a simulation[¶](#open-a-simulation "Link to this heading")

In a _python_ command line (or script), call the following function to open your **Smilei** simulation. Note that several simulations can be opened at once, as long as they correspond to several [restarts](namelist.html#checkpoints) of the same simulation.

happi.Open(_results\_path\='.'_, _reference\_angular\_frequency\_SI\=None_, _show\=True_, _verbose\=True_, _scan\=True_, _pint\=True_)[¶](#happi.Open "Link to this definition")

* `results_path`: path or list of paths to the directory-ies where the results of the simulation-s are stored. It can also contain wildcards, such as `*` and `?` in order to include several simulations at once.
* `reference_angular_frequency_SI`: overrides the value of the simulation parameter[reference\_angular\_frequency\_SI](namelist.html#reference%5Fangular%5Ffrequency%5FSI "reference_angular_frequency_SI"), in order to re-scale units.
* `show`: if `False`, figures will not plot on screen. Make sure that you have not loaded another simulation or the matplotlib package. You may need to restart python.
* `verbose`: if `False`, less information is printed while post-processing.
* `scan`: if `False`, HDF5 output files are not scanned initially, and the namelist is not read.
* `pint`: if `True`, _happi_ attempts to load the _Pint_ package and to use it for managing units.

**Returns:** An object containing various methods to extract and manipulate the simulation

outputs, as described below.

**Example**:

S = happi.Open("path/to/my/results")

Once a simulation is opened, several methods are available to find information on the namelist or open various diagnostics. Checkout the namelist documentation to find out which diagnostics are included in Smilei: [scalars](namelist.html#diagscalar),[fields](namelist.html#diagfields), [probes](namelist.html#diagprobe),[particle binning](namelist.html#diagparticlebinning), [trajectories](namelist.html#diagtrackparticles)and [performances](namelist.html#diagperformances).

---

## Extract namelist information[¶](#extract-namelist-information "Link to this heading")

Once a simulation is opened as shown above, you can access the content of the namelist using the attribute `namelist`:

S = happi.Open("path/to/my/results") # Open a simulation
print(S.namelist.Main.timestep)   # print the timestep
print(S.namelist.Main.geometry)   # print the simulation dimensions

All the variables defined in the original namelist are copied into this variable.

Concerning components like [Species](namelist.html#species), [External fields](namelist.html#externalfield) or [Probe diagnostics](namelist.html#diagprobe), of which several instances may exist, you can directly iterate over them:

for species in S.namelist.Species:
    print("species "+species.name+" has mass "+str(species.mass))

You can also access to a specific component by referencing its number:

F = S.namelist.ExternalField[0]  # get the first external field
print("An external field "+F.field+" was applied")

In the case of the species, you can also obtain a given species by its name:

species = S.namelist.Species["electron1"]
print("species "+species.name+" has mass "+str(species.mass))

---

## Obtain diagnostic information[¶](#obtain-diagnostic-information "Link to this heading")

Print available diagnostics

Commands `S.Scalar`, `S.Field`, `S.Probe` (etc.) will display general information about the corresponding diagnostics in the simulation.

List available diagnostics

getDiags(_diagType_)[¶](#getDiags "Link to this definition")

Returns a list of available diagnostics of the given type

* `diagType`: The diagnostic type (`"Field"`, `"Probe"`, etc.)

Information on specific diagnostics

getScalars()[¶](#getScalars "Link to this definition")

Returns a list of available scalars.

getTrackSpecies()[¶](#getTrackSpecies "Link to this definition")

Returns a list of available tracked species.

fieldInfo(_diag_)[¶](#fieldInfo "Link to this definition")

* `diag`: the number or name of a Field diagnostic

Returns a dictionnary containing:

* `"diagNumber"`: the diagnostic number
* `"diagName"`: the diagnostic name
* `"fields"`: list of the available fields in this diagnostic. In the case of`AMcylindrical` geometry, this is a dictionnary with a list of modes for each field.

probeInfo(_diag_)[¶](#probeInfo "Link to this definition")

* `diag`: the number or name of a Probe diagnostic

Returns a dictionnary containing:

* `"probeNumber"`: the diagnostic number
* `"probeName"`: the diagnostic name
* `"fields"`: list of the available fields in this diagnostic

performanceInfo()[¶](#performanceInfo "Link to this definition")

Returns a dictionnary containing:

* `"quantities_uint"`: a list of the available integer quantities
* `"quantities_double"`: a list of the available float quantities
* `"patch_arrangement"`: the type of patch arrangement
* `"timesteps"`: the list of timesteps

---
