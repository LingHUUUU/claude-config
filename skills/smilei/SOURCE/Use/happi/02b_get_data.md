## Obtain the data[¶](#obtain-the-data "Link to this heading")

Scalar.getData(*timestep=None*)[¶](#Scalar.getData "Link to this definition")

Field.getData(*timestep=None*)[¶](#Field.getData "Link to this definition")

Probe.getData(*timestep=None*)[¶](#Probe.getData "Link to this definition")

ParticleBinning.getData(*timestep=None*)[¶](#ParticleBinning.getData "Link to this definition")

Screen.getData(*timestep=None*)[¶](#Screen.getData "Link to this definition")

TrackParticles.getData(*timestep=None*)[¶](#TrackParticles.getData "Link to this definition")
:   Returns a list of the data arrays (one element for each timestep requested).
    In the case of `TrackParticles`, this method returns a dictionary containing one
    entry for each axis, and if `sort==False`, these entries are included inside an entry
    for each timestep.

    - `timestep`, if specified, is the only timestep number that is read and returned.

    **Example**:

    ```
    S = happi.Open("path/to/results") # Open the simulation
    Diag = S.Field(0, "Ex")       # Open Ex in the first Field diag
    result = Diag.getData()       # Get list of Ex arrays (one for each time)
    ```

Scalar.getTimesteps()[¶](#Scalar.getTimesteps "Link to this definition")

Field.getTimesteps()[¶](#Field.getTimesteps "Link to this definition")

Probe.getTimesteps()[¶](#Probe.getTimesteps "Link to this definition")

ParticleBinning.getTimesteps()[¶](#ParticleBinning.getTimesteps "Link to this definition")

Screen.getTimesteps()[¶](#Screen.getTimesteps "Link to this definition")

TrackParticles.getTimesteps()[¶](#TrackParticles.getTimesteps "Link to this definition")
:   Returns a list of the timesteps requested.

Scalar.getTimes()[¶](#Scalar.getTimes "Link to this definition")

Field.getTimes()[¶](#Field.getTimes "Link to this definition")

Probe.getTimes()[¶](#Probe.getTimes "Link to this definition")

ParticleBinning.getTimes()[¶](#ParticleBinning.getTimes "Link to this definition")

Screen.getTimes()[¶](#Screen.getTimes "Link to this definition")

TrackParticles.getTimes()[¶](#TrackParticles.getTimes "Link to this definition")
:   Returns the list of the times requested.
    By default, times are in the code’s units, but are converted to the diagnostic’s
    units defined by the `units` argument, if provided.

Scalar.getAxis(*axis*)[¶](#Scalar.getAxis "Link to this definition")

Field.getAxis(*axis*, *timestep*)[¶](#Field.getAxis "Link to this definition")

Probe.getAxis(*axis*)[¶](#Probe.getAxis "Link to this definition")

ParticleBinning.getAxis(*axis*, *timestep*)[¶](#ParticleBinning.getAxis "Link to this definition")

Screen.getAxis(*axis*, *timestep*)[¶](#Screen.getAxis "Link to this definition")
:   Returns the list of positions of the diagnostic data along the requested axis.
    If the axis is not available, returns an empty list.
    By default, axis positions are in the code’s units, but are converted to
    the diagnostic’s units defined by the `units` argument, if provided.

    - `axis`: the name of the requested axis.

      - For `Field`: this is `"x"`, `"y"` or `"z"`.
      - For `Probe`: this is `"axis1"`, `"axis2"` or `"axis3"`.
      - For `ParticleBinning` and `Screen`: this is the `type` of the [`axes`](namelist.html#id98 "axes")
        defined in the namelist. In case of a user defined axis, the name is `"user_function"`
        followed by the number of the function (starting from 0 for the first one).
        The names of the axes can be checked by printing the diagnostic.
    - `timestep`: The timestep at which the axis is obtained. Only matters in
      `ParticleBinning`, `Screen` and `RadiationSpectrum` when `auto` axis
      limits are requested; or in `Field` when `moving=True`.

TrackParticles.iterParticles(*timestep*, *chunksize=1*)[¶](#TrackParticles.iterParticles "Link to this definition")
:   This method, specific to the tracked particles, provides a fast iterator on chunks of particles
    for a given timestep. The argument `chunksize` is the number of particles in each chunk.
    Note that the data is *not ordered* by particle ID, meaning that particles are not ordered
    the same way from one timestep to another.

    The returned quantity for each iteration is a python dictionary containing key/value
    pairs `axis:array`, where `axis` is the name of the particle characteristic (`"x"`,
    `"px"`, etc.) and `array` contains the corresponding particle values.

    **Example**:

    ```
    S = happi.Open("path/to/my/results")        # Open the simulation
    Diag = S.TrackParticles("my_particles") # Open the tracked particles
    npart = 0
    sum_px = 0.
    # Loop particles of timestep 100 by chunks of 10000
    for particle_chunk in Diag.iterParticles(100, chunksize=10000):
        npart  += particle_chunk["px"].size
        sum_px += particle_chunk["px"].sum()
    # Calculate the average px
    mean_px = sum_px / npart
    ```

Field.getXmoved(*timestep*)[¶](#Field.getXmoved "Link to this definition")

Probe.getXmoved(*timestep*)[¶](#Probe.getXmoved "Link to this definition")

TrackParticles.getXmoved(*timestep*)[¶](#TrackParticles.getXmoved "Link to this definition")
:   This method returns the displacement of the moving
    window at the required `timestep`.

---

## Export 2D or 3D data to VTK[¶](#export-2d-or-3d-data-to-vtk "Link to this heading")
