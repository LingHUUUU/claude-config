## *ParticleBinning* diagnostics[¶](#particlebinning-diagnostics "Link to this heading")

A *particle binning diagnostic* collects data from the macro-particles and processes them during runtime.
It does not provide information on individual particles: instead, it produces
**averaged quantities** like the particle density, currents, etc.
The raw data and how it is post-processed by happi is described [here](binning_units.html).

The data is discretized inside a “grid” chosen by the user. This grid may be of any dimension.

Examples:

- 1-dimensional grid along the position \(x\) (gives density variation along \(x\))
- 2-dimensional grid along positions \(x\) and \(y\) (gives density map)
- 1-dimensional grid along the velocity \(v\_x\) (gives the velocity distribution)
- 2-dimensional grid along position \(x\) and momentum \(p\_x\) (gives the phase-space)
- 1-dimensional grid along the kinetic energy \(E\_\mathrm{kin}\) (gives the energy distribution)
- 3-dimensional grid along \(x\), \(y\) and \(E\_\mathrm{kin}\) (gives the density map for several energies)
- 1-dimensional grid along the charge \(Z^\star\) (gives the charge distribution)
- 0-dimensional grid (simply gives the total integrated particle density)

Each dimension of the grid is called “axis”.

You can add a particle binning diagnostic by including a block `DiagParticleBinning()` in the namelist,
for instance:

```
DiagParticleBinning(
    #name = "my binning",
    deposited_quantity = "weight",
    every = 5,
    time_average = 1,
    species = ["electrons1", "electrons2"],
    axes = [
        ["x", 0., 10, 100],
        ["ekin", 0.1, 100, 1000, "logscale", "edge_inclusive"]
    ]
)
```

name[¶](#id81 "Link to this definition")
:   Optional name of the diagnostic. Used only for post-processing purposes.

deposited\_quantity[¶](#deposited_quantity "Link to this definition")
:   The type of data that is summed in each cell of the grid.
    Consider reading [this](../Understand/units.html#weights) to understand the meaning of the `weight`.

    - `"weight"` results in a number density.
    - `"weight_charge"` results in a charge density.
    - `"weight_charge_vx"` results in the \(j\_x\) current density (same with \(y\) and \(z\)).
    - `"weight_p"` results in the momentum density (same with \(p\_x\), \(p\_y\) and \(p\_z\)).
    - `"weight_ekin"` results in the energy density.
    - `"weight_vx_px"` results in the `xx` pressure (same with yy, zz, xy, yz and xz).
    - `"weight_chi"` results in the quantum parameter density (only for species with radiation losses).
    - with a user-defined python function, an arbitrary quantity can be calculated (the *numpy*
      module is necessary). This function should take one argument, for instance
      `particles`, which contains the attributes `x`, `y`, `z`, `px`, `py`,
      `pz`, `charge`, `weight`, `chi` and `id` (additionally, it may also have the
      attributes `Ex`, `Bx`, `Ey`, and so on, depending on [`keep_interpolated_fields`](#keep_interpolated_fields "keep_interpolated_fields")).
      Each of these attributes is a *numpy* array
      containing the data of all particles in one patch. The function must return a *numpy*
      array of the same shape, containing the desired deposition of each particle. For example,
      defining the following function:

      ```
      def stuff(particles):
          return particles.weight * particles.px
      ```

      passed as `deposited_quantity=stuff`, the diagnostic will sum the weights
      \(\times\; p\_x\).

      You may also pass directly an implicit (*lambda*) function using:

      ```
      deposited_quantity = lambda p: p.weight * p.px
      ```

every[¶](#id82 "Link to this definition")
:   The number of time-steps between each output, **or** a [time selection](#timeselections).

flush\_every[¶](#id83 "Link to this definition")
:   Default:
    :   1

    Number of timesteps **or** a [time selection](#timeselections).

    When `flush_every` coincides with `every`, the output
    file is actually written (“flushed” from the buffer). Flushing
    too often can *dramatically* slow down the simulation.

time\_average[¶](#id84 "Link to this definition")
:   Default:
    :   1

    The number of time-steps during which the data is averaged. The data is averaged over time\_average consecutive iterations after the selected time.
