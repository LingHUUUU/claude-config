species[¶](#id85 "Link to this definition")
:   A list of one or several species’ [`name`](#id93 "name").
    All these species are combined into the same diagnostic.

axes[¶](#axes "Link to this definition")
:   A list of *axes* that define the grid.
    There may be as many axes as wanted (there may be zero axes).

    Syntax of one axis: `[type, min, max, nsteps, "logscale", "edge_inclusive"]`

    - `type` is one of:

      - `"x"`, `"y"`, `"z"`: spatial coordinates (`"moving_x"` with a [moving window](#movingwindow))
      - `"px"`, `"py"`, `"pz"`, `"p"`: momenta
      - `"vx"`, `"vy"`, `"vz"`, `"v"`: velocities
      - `"gamma"`, `"ekin"`: energies
      - `"chi"`: quantum parameter
      - `"charge"`: the particles’ electric charge
      - or a *python function* with the same syntax as the `deposited_quantity`.
        Namely, this function must accept one argument only, for instance `particles`,
        which holds the attributes `x`, `y`, `z`, `px`, `py`, `pz`, `charge`,
        `weight` and `id`. Each of these attributes is a *numpy* array containing the
        data of all particles in one patch. The function must return a *numpy* array of
        the same shape, containing the desired quantity of each particle that will decide
        its location in the histogram binning.
    - The axis is discretized for `type` from `min` to `max` in `nsteps` bins.
    - The `min` and `max` may be set to `"auto"` so that they are automatically
      computed from all the particles in the simulation. This option can be bad for performances.
    - The optional keyword `logscale` sets the axis scale to logarithmic instead of linear
      (bins become uneven).
    - The optional keyword `edge_inclusive` includes the particles outside the range
      [`min`, `max`] into the extrema bins.

**Examples of particle binning diagnostics**

- Variation of the density of species `electron1`
  from \(x=0\) to 1, every 5 time-steps, without time-averaging

  ```
  DiagParticleBinning(
      deposited_quantity = "weight",
      every = 5,
      time_average = 1,
      species = ["electron1"],
      axes = [ ["x",    0.,    1.,    30] ]
  )
  ```
- Density map from \(x=0\) to 1, \(y=0\) to 1

  ```
  DiagParticleBinning(
      deposited_quantity = "weight",
      every = 5,
      time_average = 1,
      species = ["electron1"],
      axes = [ ["x",    0.,    1.,    30],
               ["y",    0.,    1.,    30] ]
  )
  ```
- Velocity distribution from \(v\_x = -0.1\) to \(0.1\)

  ```
  DiagParticleBinning(
      deposited_quantity = "weight",
      every = 5,
      time_average = 1,
      species = ["electron1"],
      axes = [ ["vx",   -0.1,    0.1,    100] ]
  )
  ```
- Phase space from \(x=0\) to 1 and from \(px=-1\) to 1

  ```
  DiagParticleBinning(
      deposited_quantity = "weight",
      every = 5,
      time_average = 1,
      species = ["electron1"],
      axes = [ ["x",    0.,    1.,    30],
               ["px",   -1.,   1.,    100] ]
  )
  ```
- Energy distribution from 0.01 to 1 MeV in logarithmic scale.
  Note that the input units are \(m\_ec^2 \sim 0.5\) MeV

  ```
  DiagParticleBinning(
      deposited_quantity = "weight",
      every = 5,
      time_average = 1,
      species = ["electron1"],
      axes = [ ["ekin",    0.02,    2.,   100, "logscale"] ]
  )
  ```
- \(x\)-\(y\) density maps for three bands of energy: \([0,1]\), \([1,2]\), \([2,\infty]\).
  Note the use of `edge_inclusive` to reach energies up to \(\infty\)

  ```
  DiagParticleBinning(
      deposited_quantity = "weight",
      every = 5,
      time_average = 1,
      species = ["electron1"],
      axes = [ ["x",    0.,    1.,    30],
               ["y",    0.,    1.,    30],
               ["ekin", 0.,    6.,    3,  "edge_inclusive"] ]
  )
  ```
- Charge distribution from \(Z^\star =0\) to 10

  ```
  DiagParticleBinning(
      deposited_quantity = "weight",
      every = 5,
      time_average = 1,
      species = ["electron1"],
      axes = [ ["charge",    -0.5,   10.5,   11] ]
  )
  ```

---

## *Screen* diagnostics[¶](#screen-diagnostics "Link to this heading")
