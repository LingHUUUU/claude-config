# Namelist Reference - Index

Complete namelist parameter reference. Read only the file(s) relevant to the current task. Each file contains the full official documentation for that topic.

The complete raw namelist page is available at `SMILEI_MANUAL_SOURCE/Use/namelist.md` (6882 lines).

| File | Content | Sections |
|------|---------|----------|
| [00_general.md](00_general.md) | General rules, Python workflow | How to structure a namelist, Smilei blocks, Python variables |
| [01_main.md](01_main.md) | Main variables | `geometry`, `grid_length`, `cell_length`, `number_of_patches`, `timestep`, `simulation_time`, `reference_angular_frequency_SI`, `print_every`, `interpolation_order`, `number_of_pml_cells`, `EM_boundary_conditions`, `random_seed`, `timestep_over_CFL`, `solve_poisson`, `poisson_solver`, `keep_interpolated_fields`, `file_grouping`, `print_expected_disk_usage` |
| [02_load_balancing.md](02_load_balancing.md) | Load Balancing, SDMD, Vectorization | Dynamic load balancing, multiple domain decomposition, SIMD vectorization |
| [03_moving_window.md](03_moving_window.md) | Moving window | `number_of_moving_patches`, `time_start`, `velocity_x`, `dir` |
| [04_filtering.md](04_filtering.md) | Current and Field filtering | Binomial filter, Friedman filter, FIR filter, number of passes |
| [05_species.md](05_species.md) | Species block | `name`, `mass`, `charge`, `position_initialization`, `momentum_initialization`, `particles_per_cell`, `number_density`, `charge_density`, `temperature`, `mean_velocity`, `boundary_conditions`, `ionization_model`, `radiation_model`, `radiation_quantum_parameter`, `number_of_additional_arguments` |
| [06_injector_merging.md](06_injector_merging.md) | Particle Injector and Merging | Injector parameters, Vranic merging algorithm, cartesian/spherical momentum discretization |
| [07_lasers.md](07_lasers.md) | Lasers | `LaserGaussian2D`, `LaserGaussian3D`, `LaserGaussianAM`, `LaserPlaneWave`, `LaserOffset`, time envelopes (`tgaussian`, `tsine`, `ttrapezoidal`, `tcustom`), `box_side`, `a0`, `omega`, `focus`, `waist`, `incidence_angle`, `phase_offset`, `ellipticity` |
| [08_envelope.md](08_envelope.md) | Laser envelope model | `LaserEnvelope`, envelope equation, ponderomotive force, susceptibility |
| [09_external_fields.md](09_external_fields.md) | External/Prescribed fields, Antennas, Walls | `ExternalField`, `PrescribedField`, `Antenna`, `Wall` |
| [10_collisions.md](10_collisions.md) | Collisions & reactions | `Collisions`, `coulomb_log`, `screened_coulomb_log`, collisional ionization, nuclear reactions, `time_frozen` |
| [11_radiation_qed.md](11_radiation_qed.md) | Radiation reaction, Multiphoton Breit-Wheeler | Niel, Monte-Carlo, Landau-Lifshitz models; `MultiphotonBreitWheeler` |
| [12a_scalar.md](12a_scalar.md) | Scalar diagnostics | `DiagScalar`, `Ukin`, `Uelm`, `Ubal`, `Urad`, `PoyXmin`, `PoyXminInst`, all scalar quantities |
| [12b_fields.md](12b_fields.md) | Fields diagnostics | `DiagFields`, `fields`, `every`, `time_average`, `subgrid`, `datatype`, `flush_every` |
| [12c_probe.md](12c_probe.md) | Probe diagnostics | `DiagProbe`, `fields`, `origin`, `corners`, `number`, `time_integrate`, `PoyX`/`PoyY`/`PoyZ`, `changeField` |
| [12d_particle_binning.md](12d_particle_binning.md) | ParticleBinning diagnostics | `DiagParticleBinning`, `species`, `axes`, `deposited_quantity`, `average`, `auto` axis limits |
| [12e_screen_radiation.md](12e_screen_radiation.md) | Screen and RadiationSpectrum | `DiagScreen`, `shape` (`sphere`/`cylinder`), `direction`, `DiagRadiationSpectrum`, `photon_energy_axis` |
| [12f_track_perf.md](12f_track_perf.md) | TrackParticles, NewParticles, Performances | `DiagTrackParticles`, `filter`, `keep_interpolated_fields`; `DiagNewParticles`; `DiagPerformances`, `cumulative` |
| [13_time_checkpoint.md](13_time_checkpoint.md) | Time selections, Checkpoints, Variables | `time_selector`, `dump_minutes`, `restart_number`, `restart_files`, Smilei-defined variables (`smilei_omp_threads`, `smilei_total_cores`, `smilei_mpi_rank`, etc.) |
