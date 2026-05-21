## Plot the data at one timestep[¶](#plot-the-data-at-one-timestep "Link to this heading")

This is the first method to plot the data. It produces a static image of the data
at one given timestep.

Scalar.plot(*...*)[¶](#Scalar.plot "Link to this definition")

Field.plot(*...*)[¶](#Field.plot "Link to this definition")

Probe.plot(*...*)[¶](#Probe.plot "Link to this definition")

ParticleBinning.plot(*...*)[¶](#ParticleBinning.plot "Link to this definition")

TrackParticles.plot(*...*)[¶](#TrackParticles.plot "Link to this definition")

Screen.plot(*...*)[¶](#Screen.plot "Link to this definition")
:   All these methods have the same arguments described below.

plot(*timestep=None*, *saveAs=None*, *axes=None*, *dpi=200*, *\*\*kwargs*)[¶](#plot "Link to this definition")
:   If the data is 1D, it is plotted as a **curve**.

    If the data is 2D, it is plotted as a **map**.

    If the data is 0D, it is plotted as a **curve** as function of time.

    - `timestep`: The iteration number at which to plot the data.
    - `saveAs`: name of a directory where to save each frame as figures.
      You can even specify a filename such as `mydir/prefix.png` and it will automatically
      make successive files showing the timestep: `mydir/prefix0.png`, `mydir/prefix1.png`,
      etc.
    - `axes`: Matplotlib’s axes handle on which to plot. If None, make new axes.
    - `dpi`: the number of dots per inch for `saveAs`.

    You may also have keyword-arguments (`kwargs`) described in [Other arguments for diagnostics](#otherkwargs).

**Example**:

```
S = happi.Open("path/to/my/results")
S.ParticleBinning(1).plot(timestep=40, vmin=0, vmax=1e14)
```

---

## Plot the data streaked over time[¶](#plot-the-data-streaked-over-time "Link to this heading")

This second type of plot works only for 1D data. All available timesteps
are streaked to produce a 2D image where the second axis is time.

Scalar.streak(*...*)[¶](#Scalar.streak "Link to this definition")

Field.streak(*...*)[¶](#Field.streak "Link to this definition")

Probe.streak(*...*)[¶](#Probe.streak "Link to this definition")

ParticleBinning.streak(*...*)[¶](#ParticleBinning.streak "Link to this definition")

TrackParticles.streak(*...*)[¶](#TrackParticles.streak "Link to this definition")

Screen.streak(*...*)[¶](#Screen.streak "Link to this definition")
:   All these methods have the same arguments described below.

streak(*saveAs=None*, *axes=None*, *\*\*kwargs*)[¶](#streak "Link to this definition")
:   All arguments are identical to those of `plot`, with the exception of `timestep`.

**Example**:

```
S = happi.Open("path/to/my/results")
S.ParticleBinning(1).streak()
```

---

## Animated plot[¶](#animated-plot "Link to this heading")
