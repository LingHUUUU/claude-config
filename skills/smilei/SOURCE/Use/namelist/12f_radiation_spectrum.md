## *RadiationSpectrum* diagnostics[¶](#radiationspectrum-diagnostics "Link to this heading")

A *radiation spectrum diagnostic* computes (at a given time) the instantaneous
power spectrum following from the incoherent emission of high-energy
photons by accelerated charge (see [High-energy photon emission & radiation reaction](../Understand/radiation_loss.html) for more details
on the emission process and its implementation in **Smilei**).

It is similar to the [particle binning diagnostics](#diagparticlebinning),
with an extra axis of binning: the emitted photon energy.
The other axes remain available to the user.

A radiation spectrum diagnostic is defined by a block `RadiationSpectrum()`:

```
DiagRadiationSpectrum(
    #name = "my radiation spectrum",
    every = 5,
    flush_every = 1,
    time_average = 1,
    species = ["electrons1", "electrons2"],
    photon_energy_axis = [0., 1000., 100, 'logscale'],
    axes = []
)
```

name[¶](#id93 "Link to this definition")
:   Optional name of the diagnostic. Used only for post-processing purposes.

every[¶](#id94 "Link to this definition")
:   The number of time-steps between each output, **or** a [time selection](#timeselections).

flush\_every[¶](#id95 "Link to this definition")
:   Default:
    :   1

    Number of timesteps **or** a [time selection](#timeselections).

    When `flush_every` coincides with `every`, the output
    file is actually written (“flushed” from the buffer). Flushing
    too often can *dramatically* slow down the simulation.

time\_average[¶](#id96 "Link to this definition")
:   Default:
    :   1

    The number of time-steps during which the data is averaged before output.

species[¶](#id97 "Link to this definition")
:   A list of one or several species’ [`name`](#id93 "name") that emit the radiation.
    All these species are combined into the same diagnostic.

photon\_energy\_axis[¶](#photon_energy_axis "Link to this definition")
:   The axis of photon energies (in units of \(m\_e c^2\)).
    The syntax is similar to that of
    [particle binning diagnostics](#diagparticlebinning).

    Syntax: `[min, max, nsteps, "logscale"]`

axes[¶](#id98 "Link to this definition")
:   An additional list of “axes” that define the grid.
    There may be as many axes as wanted (there may be zero axes).
    Their syntax is the same that for “axes” of a
    [particle binning diagnostics](#diagparticlebinning).

**Examples of radiation spectrum diagnostics**

- Time-integrated over the full duration of the simulation:

  ```
  DiagRadiationSpectrum(
      every = Nt,
      time_average = Nt,
      species = ["electrons"],
      photon_energy_axis = [0., 1000., 100, 'logscale'],
      axes = []
  )
  ```
- Angularly-resolved instantaneous radiation spectrum.
  The diagnostic considers that all electrons emit radiation in
  the direction of their velocity:

  ```
  from numpy import arctan2, pi

  def angle(p):
      return arctan2(p.py,p.px)

  DiagRadiationSpectrum(
      every = 10,
      species = ["electrons"],
      photon_energy_axis = [0., 1000., 100, 'logscale'],
      axes = [
          [angle,-pi,pi,90]
      ]
  )
  ```

---
