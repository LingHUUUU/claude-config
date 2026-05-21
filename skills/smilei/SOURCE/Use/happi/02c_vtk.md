## Export 2D or 3D data to VTK[¶](#export-2d-or-3d-data-to-vtk "Link to this heading")

Field.toVTK(*numberOfPieces=1*)[¶](#Field.toVTK "Link to this definition")

Probe.toVTK(*numberOfPieces=1*)[¶](#Probe.toVTK "Link to this definition")

ParticleBinning.toVTK(*numberOfPieces=1*)[¶](#ParticleBinning.toVTK "Link to this definition")

Performances.toVTK(*numberOfPieces=1*)[¶](#Performances.toVTK "Link to this definition")

Screen.toVTK(*numberOfPieces=1*)[¶](#Screen.toVTK "Link to this definition")

TrackParticles.toVTK(*rendering='trajectory'*, *data\_format='xml'*)[¶](#TrackParticles.toVTK "Link to this definition")
:   Converts the data from a diagnostic object to the vtk format.
    Note the `export_dir` argument available for each diagnostic (see above).

    - `numberOfPieces`: the number of files into which the data will be split.
    - `rendering`: the type of output in the case of [`TrackParticles()`](#TrackParticles "TrackParticles"):

      - `"trajectory"`: show particle trajectories. One file is generated for all trajectories.
        This rendering requires the particles to be sorted.
      - `"cloud"`: show a cloud of particles. One file is generated for each iteration.
        This rendering can be used without sorting the particles.
    - `data_format`: the data formatting in the case of [`TrackParticles()`](#TrackParticles "TrackParticles"),
      either `"vtk"` or `"xml"`. The format `"vtk"` results in ascii.

    **Example for tracked particles**:

    ```
    S = happi.Open("path/to/my/results")
    tracked_particles = S.TrackParticles("electron", axes=["x","y","z","px","py","pz","Id"], timesteps=[1,10])
    # Create cloud of particles in separate files for each iteration
    tracked_particles.toVTK(rendering="cloud",data_format="xml");
    # Create trajectory in a single file
    tracked_particles.toVTK(rendering="trajectory",data_format="xml");
    ```

---

## Plot the data at one timestep[¶](#plot-the-data-at-one-timestep "Link to this heading")
