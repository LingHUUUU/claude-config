# Write a namelist[¶](#write-a-namelist "Link to this heading")

Before you run **Smilei**, you need a *namelist* (an input file). The namelist
is written in the *python* language. It is thus recommended to know the basics of *python*.

We suggest you copy one existing namelist from the folder *benchmarks*.
All namelists have the extension `.py`.

---

## General rules[¶](#general-rules "Link to this heading")

- **Smilei** requires a few *blocks* to be defined, such as:

  ```
  Main(
      # ...
      timestep = 0.01,         # defines the timestep value
      grid_length = [10., 20.], # defines the 2D box dimensions
      # ...
  )
  ```

  Outside blocks, you can calculate anything you require.
  Inside a block, you must only define variables for **Smilei**.
- The *python* syntax requires special indentation of each line.
  You begin with no indentation, but you have to **add four spaces at the
  beginning of lines inside a group**, and so on.
  For instance:

  ```
  if a == 0:
      timestep = 0.1
      if b == 1:
          timestep = 0.2
  else:
      timestep = 0.3
  ```
- You will need to use [lists](https://docs.python.org/2/tutorial/introduction.html#lists),
  which are series of things in *python*,
  defined between brackets `[]` and separated by commas.
  For example, `mean_velocity = [0., 1.1, 3.]`.
- You are free to import any installed *python* package into the namelist.
  For instance, you may obtain \(\pi\) using `from math import pi`.
- All quantities are normalized to arbitrary values: see [Units](../Understand/units.html).

---

## Python workflow[¶](#python-workflow "Link to this heading")

*Python* is started at the beginning of the simulation (one *python* interpreter
for each MPI process). The following steps are executed:

1. A few variables from **Smilei** are passed to *python* so that they are
   available to the user:

   - The rank of the current MPI process as [`smilei_mpi_rank`](#smilei_mpi_rank "smilei_mpi_rank").
   - The total number of MPI processes as [`smilei_mpi_size`](#smilei_mpi_size "smilei_mpi_size").
   - The number of OpenMP threads per MPI [`smilei_omp_threads`](#smilei_omp_threads "smilei_omp_threads").
   - The total number of cores [`smilei_total_cores`](#smilei_total_cores "smilei_total_cores").
2. The namelist(s) is executed.
3. *Python* runs `preprocess()` if the user has defined it.
   This is a good place to calculate things that are not needed for
   post-processing with **happi**.
4. The simulation is initialized (including field and particle arrays).
5. *Python* runs `cleanup()` if the user has defined it.
   This is a good place to delete unused heavy variables.
6. *Python* checks whether the *python* interpreter is needed during the simulation
   (e.g. the user has defined a temporal [profile](profiles.html) which requires *python*
   to calculate it every timestep). Otherwise, *python* is stopped.

All these instructions are summarized in a file `smilei.py`,
so that the user can directly run `python -i smilei.py` for post-processing purposes.

---
