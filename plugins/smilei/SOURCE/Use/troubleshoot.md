# Troubleshoot

If you encounter issues, ask in the Smilei chat room or publish an `Issue` on GitHub. Most issues can be found by performing basic checks below.

---

## Simulation not starting / Error running

- Check the `smilei` executable is called correctly and present in the namelist folder
- Check `smilei` runs with a benchmark namelist
- Use `smilei_test` on your namelist — does it show errors or warnings?
- Check your Profiles — avoid `NaN` values from files or Python functions
- Try `git pull`, `make clean` and compile again. Also run `make happi` for postprocessing
- Change numerical parameters (resolution, timestep, ppc, patches) — does the error persist?
- Change MPI process / OpenMP thread count. Do benchmarks run with 1 MPI/thread?
- Check MPI and OpenMP configuration with parallel Hello World tests
- Try a reduced simulation (fewer ppc, coarser resolution)
- Try on a different machine
- If the simulation stops, does the error occur at the same iteration? Use `print_every` to track

---

## New simulation does not run (old ones did)

- Use a working namelist and progressively change it toward the new simulation. At each step, check what breaks
- Try the new simulation with the same `smilei` executable used for a working simulation

---

## Postprocessing error

- Run `git pull` and `make happi` in the installation folder. Restart your Python interface afterward
- Check if you can open results from a benchmark simulation
- Carefully read the documentation for the post-process method you're using

---

## Physical error in results

- Read the doc on the physical methods you use — are the underlying assumptions satisfied?
- Check that units are properly normalized
- Check `reference_angular_frequency_SI` is provided in the `Main` block (required for collisions, ionization)
- Check the CFL condition
- Check Scalar diagnostics: do `Ukin` or `Uelm` show strange behavior (e.g., exponential growth)?
- Verify overall physical consistency (e.g., only immobile particles with Poisson solver)
- Check if a Poisson solver is needed for initial fields
- Run with different numerical parameters (resolution, timestep) to check for numerical effects
- In AMcylindrical geometry: check axis origins align with the documentation

---

## Performance issues

- Change MPI process and OpenMP thread count
- Change number of patches and/or their distribution per direction
- Enable `LoadBalancing` if the physical setup permits
- Check vectorization compilation flags were correctly used
