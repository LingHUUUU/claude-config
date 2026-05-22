## Time selections[¶](#time-selections)

Several components (mainly diagnostics) may require a selection of timesteps to
be chosen by the user. When one of these timesteps is reached, the diagnostics will
output data. A time selection is given through the parameter `every` and is a list
of several numbers.

You may chose between five different syntaxes:

```
every = [               period                    ] # Syntax 1
every = [       start,  period                    ] # Syntax 2
every = [ start,  end,  period                    ] # Syntax 3
every = [ start,  end,  period,  repeat           ] # Syntax 4
every = [ start,  end,  period,  repeat,  spacing ] # Syntax 5

```

where

-

`start` is the first timestep of the selection (defaults to 0);

-

`end` is the last timestep of the selection (defaults to ∞);

-

`period` is the separation between outputs (defaults to 1);

-

`repeat` indicates how many outputs to do at each period (defaults to 1);

-

`spacing` is the separation between each repeat (defaults to 1).

For more clarity, this graph illustrates the five syntaxes for time selections:

[](../_images/TimeSelections.png)

Tips

-

The syntax `every = period` is also accepted.

-

Any value set to `0` will be replaced by the default value.

-

Special case: `every=0` means no output.

-

The numbers may be non-integers (apart from `repeat`). The closest timesteps are chosen.

## Profiles[¶](#profiles)

Some of the quantities described in the previous sections can be profiles that depend on
space and/or time. See the [documentation on profiles](profiles.html) for detailed
instructions.

## Checkpoints[¶](#checkpoints)

The simulation state can be saved (dumped) at given times (checkpoints)
in order to be later restarted at that point.

A few things are important to know when you need dumps and restarts.

-

Do not restart the simulation in the same directory as the previous one. Files will be
overwritten, and errors may occur. Create a new directory for your restarted simulation.

-

Manage your disk space: each MPI process dumps one file, and the total can be significant.

-

The restarted runs must have the same namelist as the initial simulation, except the
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

Parameters to save the state of the current simulation

dump_step[¶](#dump_step)

Default:

`0`

The number of timesteps between each dump.
If `0`, no dump is done.

dump_minutes[¶](#dump_minutes)

Default:

`0.`

The number of minutes between each dump.
If `0.`, no dump is done.

May be used in combination with [`dump_step`](#dump_step).

exit_after_dump[¶](#exit_after_dump)

Default:

`True`

If `True`, the code stops after the first dump. If `False`, the simulation continues.

keep_n_dumps[¶](#keep_n_dumps)

Default:

`2`

This tells Smilei to keep, in the current run,  only the last `n` dumps.
Older dumps will be overwritten.

The default value, `2`, saves one extra dump in case of a crash during the next dump.

file_grouping[¶](#file_grouping)

Default:

`0` (no grouping)

The maximum number of checkpoint files that can be stored in one directory.
Subdirectories are created to accomodate for all files.
This is useful on filesystem with a limited number of files per directory.

dump_deflate[¶](#dump_deflate)

to do

Parameters to restart from a previous simulation

restart_dir[¶](#restart_dir)

Default:

`None`

The directory of a previous run from which Smilei should restart.
For the first run, do not specify this parameter.

This path must either absolute or be relative to the current directory.

Note

In many situations, the restarted runs will have the exact same namelist as the initial
simulation, except this `restart_dir` parameter, which points to the previous simulation
folder.
You can use the same namelist file, and simply add an extra argument when you launch the
restart:

`mpirun ... ./smilei mynamelist.py "Checkpoints.restart_dir='/path/to/previous/run'"`

restart_number[¶](#restart_number)

Default:

`None`

The number of the dump (in the previous run) that should be used for the restart.
For the first run, do not specify this parameter.

In a previous run, the simulation state may have been dumped several times.
These dumps are numbered 0, 1, 2, etc. until the number [`keep_n_dumps`](#keep_n_dumps).
In case multiple dumps are kept, the newest one will overwrite the oldest one.
To restart the simulation from the most advanced point, specify the dump number
corresponding to the newest that was created.

## Variables defined by Smilei[¶](#variables-defined-by-smilei)

Smilei passes the following variables to the python interpreter for use in the
namelist. They should not be re-defined by the user!

smilei_mpi_rank[¶](#smilei_mpi_rank)

The MPI rank of the current process.

smilei_mpi_size[¶](#smilei_mpi_size)

The total number of MPI processes.

smilei_omp_threads[¶](#smilei_omp_threads)

The number of OpenMP threads per MPI.

smilei_total_cores[¶](#smilei_total_cores)

The total number of cores.

Note

These variables can be access during `happi` post-processing, e.g.
`S.namelist.smilei_mpi_size`.

[Site index](site.html)

Last updated on Mar 16, 2026

Powered by [Sphinx 7.2.6](http://sphinx-doc.org/)
