## Open a NewParticles diagnostic[¶](#open-a-newparticles-diagnostic "Link to this heading")

NewParticles(*species=None*, *select=''*, *axes=[]*, *units=['']*, *\*\*kwargs*)[¶](#NewParticles "Link to this definition")
:   - `units`: same as before.
    - `species`: same as for `TrackParticles`
    - `axes`: same as for `TrackParticles`, with the addition of another axis `t`
      that represents the time when the particle was born.
    - `select`: Instructions for selecting particles among those available.
      It must be a condition on particles properties `axes`, for instance `px>0`.
      It is possible to make logical operations: `+` is *OR*; `*` is *AND*; `~` is *NOT*.

      **Example:** `select="(x>1)*(x<2)"`

      It is also possible to select directly a list of IDs.

      **Example:** `select=[ID1, ID2, ...]`

---

## Open a Performances diagnostic[¶](#open-a-performances-diagnostic "Link to this heading")

The post-processing of the *performances* diagnostic may be achieved in three different
modes: `raw`, `map`, or `histogram`, described further below. You must choose one
and only one mode between those three.

Performances(*raw=None*, *map=None*, *histogram=None*, *timesteps=None*, *units=['']*, *data\_log=False*, *data\_transform=None*, *species=None*, *cumulative=True*, *\*\*kwargs*)[¶](#Performances "Link to this definition")
:   - `timesteps`, `units`, `data_log`, `data_transform`, `export_dir`: same as before.
    - `raw`: The name of a quantity, or an operation between them (see quantities below).
      The requested quantity is listed for each process.
    - `map`: The name of a quantity, or an operation between them (see quantities below).
      The requested quantity is mapped vs. space coordinates (1D and 2D only).
    - `histogram`: the list `["quantity", min, max, nsteps]`.
      Makes a histogram of the requested quantity between `min` an `max`, with `nsteps` bins.
      The `"quantity"` may be an operation between the quantities listed further below.
    - `cumulative`: may be `True` for timers accumulated for the duration of the simulation,
      or `False` for timers reset to 0 at each output.
    - See also [Other arguments for diagnostics](#otherkwargs)

**Quantities at the MPI-process level** (contain many patches):

> - `hindex` : the starting index of each proc in the hilbert curve
> - `number_of_cells` : the number of cells in each proc
> - `number_of_particles` : the total number of non-frozen macro-particles in each proc (includes all species)
> - `number_of_frozen_particles` : the number of frozen particles in each proc
> - `total_load` : the load of each proc (number of macro-particles and cells weighted by cell\_load coefficients)
> - `timer_global` : global simulation time (only available for proc 0)
> - `timer_particles` : time spent computing particles by each proc
> - `timer_maxwell` : time spent solving maxwell by each proc
> - `timer_envelope` : time spent solving the envelope propagation by each proc
> - `timer_densities` : time spent projecting densities by each proc
> - `timer_collisions` : time spent computing collisions by each proc
> - `timer_movWindow` : time spent handling the moving window by each proc
> - `timer_loadBal` : time spent balancing the load by each proc
> - `timer_partMerging` : time spent merging particles by each proc
> - `timer_syncPart` : time spent synchronzing particles by each proc
> - `timer_syncField` : time spent synchronzing fields by each proc
> - `timer_syncDens` : time spent synchronzing densities by each proc
> - `timer_syncSusceptibility` : time spent synchronzing susceptibility by each proc
> - `timer_diags` : time spent by each proc calculating and writing diagnostics
> - `timer_total` : the sum of all timers above (except timer\_global)
> - `memory_total` : the total memory (RSS) used by the process in GB
> - `memory_peak` : the peak memory (peak RSS) used by the process in GB
>
> **WARNING**: The timers `loadBal` and `diags` include *global* communications.
> This means they might contain time doing nothing, waiting for other processes.
> The `sync***` timers contain *proc-to-proc* communications, which also represents
> some waiting time.

**Quantities at the patch level**:

> This requires [`patch_information`](namelist.html#patch_information "patch_information") in the namelist.
>
> - `mpi_rank` : the MPI rank that contains the current patch
> - `vecto` : the mode of the specified species in the current patch
>   (vectorized of scalar) when the adaptive mode is activated. Here the `species` argument has to be specified.
>
> **WARNING**: The patch quantities are only compatible with the `raw` mode
> and only in `3Dcartesian` [`geometry`](namelist.html#geometry "geometry"). The result is a patch matrix with the
> quantity on each patch.

**Example**: performance diagnostic at the MPI level:

```
S = happi.Open("path/to/my/results")
Diag = S.Performances(map="total_load")
```

**Example**: performance diagnostic at the patch level:

```
S = happi.Open("path/to/my/results")
Diag = S.Performances(raw="vecto", species="electron")
```

---

## Specifying units[¶](#specifying-units "Link to this heading")
