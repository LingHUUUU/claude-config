# Happi Reference Index

Complete happi (post-processing) reference. Structured for AI reading — shared parameters defined once, diagnostics reference them. Original source: `SMILEI_MANUAL_SOURCE/Use/happi/post-processing.md` (1122 lines).

| File | Content |
|------|---------|
| [00_open.md](00_open.md) | `happi.Open()`, `.namelist` access, `.getDiags()`, `.getScalars()`, `.getTrackSpecies()`, `.fieldInfo()`, `.probeInfo()`, `.performanceInfo()`, `happi.openNamelist()` |
| [01_shared_parameters.md](01_shared_parameters.md) | Shared parameters defined once: timesteps, units, subset, average, data_log, data_transform, export_dir, **kwargs |
| [02_diagnostics.md](02_diagnostics.md) | Diagnostic constructors with unique parameters: Scalar, Field, Probe, ParticleBinning, Screen, RadiationSpectrum, TrackParticles, NewParticles, Performances |
| [03_data_methods.md](03_data_methods.md) | Data retrieval: getData, getTimesteps, getTimes, getAxis, getXmoved, iterParticles, toVTK |
| [04_plotting.md](04_plotting.md) | Plotting: plot, streak, animate, slide, multiPlot, multiSlide, set, advanced matplotlib options |
