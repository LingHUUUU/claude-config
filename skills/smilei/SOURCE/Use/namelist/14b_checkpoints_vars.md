## Checkpoints[¶](#checkpoints "Link to this heading")

The simulation state can be saved (*dumped*) at given times (*checkpoints*)
in order to be later *restarted* at that point.

A few things are important to know when you need dumps and restarts.

- Do not restart the simulation in the same directory as the previous one. Files will be
  overwritten, and errors may occur. Create a new directory for your restarted simulation.
- Manage your disk space: each MPI process dumps one file, and the total can be significant.
- The restarted runs must have the same namelist as the initial simulation, except the
  [Checkpoints](#checkpoints) block, which can be modified.

```
Checkpoints(
    # restart_dir = "dump1",
    dump_step = 10000,
    dump_minutes = 240.,
    exit_after_dump = True,
    keep_n_dumps = 2,
)
```

**Parameters to save the state of the current simulation**

> dump\_step[¶](#dump_step "Link to this definition")
> :   Default:
>     :   `0`
>
>     The number of timesteps between each dump.
>     If `0`, no dump is done.
>
> dump\_minutes[¶](#dump_minutes "Link to this definition")
> :   Default:
>     :   `0.`
>
>     The number of minutes between each dump.
>     If `0.`, no dump is done.
>
>     May be used in combination with [`dump_step`](#dump_step "dump_step").
>
> exit\_after\_dump[¶](#exit_after_dump "Link to this definition")
> :   Default:
>     :   `True`
>
>     If `True`, the code stops after the first dump. If `False`, the simulation continues.
>
> keep\_n\_dumps[¶](#keep_n_dumps "Link to this definition")
> :   Default:
>     :   `2`
>
>     This tells **Smilei** to keep, in the current run, only the last `n` dumps.
>     Older dumps will be overwritten.
>
>     The default value, `2`, saves one extra dump in case of a crash during the next dump.
>
> file\_grouping[¶](#file_grouping "Link to this definition")
> :   Default:
>     :   `0` (no grouping)
>
>     The maximum number of checkpoint files that can be stored in one directory.
>     Subdirectories are created to accomodate for all files.
>     This is useful on filesystem with a limited number of files per directory.
>
> dump\_deflate[¶](#dump_deflate "Link to this definition")
> :   to do

**Parameters to restart from a previous simulation**

> restart\_dir[¶](#restart_dir "Link to this definition")
> :   Default:
>     :   `None`
>
>     The directory of a previous run from which **Smilei** should restart.
>     For the first run, do not specify this parameter.
>
>     **This path must either absolute or be relative to the current directory.**
>
>     Note
>
>     In many situations, the restarted runs will have the exact same namelist as the initial
>     simulation, except this `restart_dir` parameter, which points to the previous simulation
>     folder.
>     You can use the same namelist file, and simply add an extra argument when you launch the
>     restart:
>
>     `mpirun ... ./smilei mynamelist.py "Checkpoints.restart_dir='/path/to/previous/run'"`
>
> restart\_number[¶](#restart_number "Link to this definition")
> :   Default:
>     :   `None`
>
>     The number of the dump (in the previous run) that should be used for the restart.
>     For the first run, do not specify this parameter.
>
>     In a previous run, the simulation state may have been dumped several times.
>     These dumps are numbered 0, 1, 2, etc. until the number [`keep_n_dumps`](#keep_n_dumps "keep_n_dumps").
>     In case multiple dumps are kept, the newest one will overwrite the oldest one.
>     To restart the simulation from the most advanced point, specify the dump number
>     corresponding to the newest that was created.

---

## Variables defined by Smilei[¶](#variables-defined-by-smilei "Link to this heading")

**Smilei** passes the following variables to the python interpreter for use in the
namelist. They should not be re-defined by the user!

smilei\_mpi\_rank[¶](#smilei_mpi_rank "Link to this definition")
:   The MPI rank of the current process.

smilei\_mpi\_size[¶](#smilei_mpi_size "Link to this definition")
:   The total number of MPI processes.

smilei\_omp\_threads[¶](#smilei_omp_threads "Link to this definition")
:   The number of OpenMP threads per MPI.

smilei\_total\_cores[¶](#smilei_total_cores "Link to this definition")
:   The total number of cores.

Note

These variables can be access during `happi` post-processing, e.g.
`S.namelist.smilei_mpi_size`.
