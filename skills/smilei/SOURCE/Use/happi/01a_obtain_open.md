## Obtain diagnostic information[¶](#obtain-diagnostic-information "Link to this heading")

Print available diagnostics

Commands `S.Scalar`, `S.Field`, `S.Probe` (etc.) will display general information
about the corresponding diagnostics in the simulation.

List available diagnostics

getDiags(*diagType*)[¶](#getDiags "Link to this definition")
:   Returns a list of available diagnostics of the given type

    - `diagType`: The diagnostic type (`"Field"`, `"Probe"`, etc.)

Information on specific diagnostics

getScalars()[¶](#getScalars "Link to this definition")
:   Returns a list of available scalars.

getTrackSpecies()[¶](#getTrackSpecies "Link to this definition")
:   Returns a list of available tracked species.

fieldInfo(*diag*)[¶](#fieldInfo "Link to this definition")
:   - `diag`: the number or name of a Field diagnostic

    Returns a dictionnary containing:

    - `"diagNumber"`: the diagnostic number
    - `"diagName"`: the diagnostic name
    - `"fields"`: list of the available fields in this diagnostic. In the case of
      `AMcylindrical` geometry, this is a dictionnary with a list of modes for each field.

probeInfo(*diag*)[¶](#probeInfo "Link to this definition")
:   - `diag`: the number or name of a Probe diagnostic

    Returns a dictionnary containing:

    - `"probeNumber"`: the diagnostic number
    - `"probeName"`: the diagnostic name
    - `"fields"`: list of the available fields in this diagnostic

performanceInfo()[¶](#performanceInfo "Link to this definition")
:   Returns a dictionnary containing:

    - `"quantities_uint"`: a list of the available integer quantities
    - `"quantities_double"`: a list of the available float quantities
    - `"patch_arrangement"`: the type of patch arrangement
    - `"timesteps"`: the list of timesteps

---

## Open a Scalar diagnostic[¶](#open-a-scalar-diagnostic "Link to this heading")
