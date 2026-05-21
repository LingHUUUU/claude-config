## Animated plot[¶](#animated-plot "Link to this heading")

This third plotting method animates the data over time.

Scalar.animate(*...*)[¶](#Scalar.animate "Link to this definition")

Field.animate(*...*)[¶](#Field.animate "Link to this definition")

Probe.animate(*...*)[¶](#Probe.animate "Link to this definition")

ParticleBinning.animate(*...*)[¶](#ParticleBinning.animate "Link to this definition")

TrackParticles.animate(*...*)[¶](#TrackParticles.animate "Link to this definition")

Screen.animate(*...*)[¶](#Screen.animate "Link to this definition")
:   All these methods have the same arguments described below.

animate(*movie=''*, *fps=15*, *dpi=200*, *saveAs=None*, *axes=None*, *\*\*kwargs*)[¶](#animate "Link to this definition")
:   All arguments are identical to those of `streak`, with the addition of:

    - `movie`: name of a file to create a movie, such as `"movie.avi"` or `"movie.gif"`.
      If `movie=""` no movie is created.
    - `fps`: number of frames per second (only if movie requested).
    - `dpi`: number of dots per inch for both `movie` and `saveAs`

**Example**:

```
S = happi.Open("path/to/my/results")
S.ParticleBinning(1).animate()
```

---

## Plot with a slider[¶](#plot-with-a-slider "Link to this heading")

This methods provides an interactive slider to change the time.

Scalar.slide(*...*)[¶](#Scalar.slide "Link to this definition")

Field.slide(*...*)[¶](#Field.slide "Link to this definition")

Probe.slide(*...*)[¶](#Probe.slide "Link to this definition")

ParticleBinning.slide(*...*)[¶](#ParticleBinning.slide "Link to this definition")

TrackParticles.slide(*...*)[¶](#TrackParticles.slide "Link to this definition")

Screen.slide(*...*)[¶](#Screen.slide "Link to this definition")
:   All these methods have the same arguments described below.

slide(*axes=None*, *\*\*kwargs*)[¶](#slide "Link to this definition")
:   See `plot` for the description of the arguments.

**Example**:

```
S = happi.Open("path/to/my/results")
S.ParticleBinning(1).slide(vmin=0)
```

---

## Simultaneous plotting of multiple diagnostics[¶](#simultaneous-plotting-of-multiple-diagnostics "Link to this heading")
