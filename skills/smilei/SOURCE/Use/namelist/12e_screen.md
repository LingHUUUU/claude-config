## *Screen* diagnostics[¶](#screen-diagnostics "Link to this heading")

A *screen* collects data from the macro-particles when they cross a surface.
It processes this data similarly to the [particle binning diagnostics](#diagparticlebinning)
as it makes a histogram of the macro-particle properties. There are two differences:

- the histogram is made only by the particles that cross the surface
- the data is accumulated for all timesteps.

You can add a screen by including a block `DiagScreen()` in the namelist,
for instance:

```
DiagScreen(
    #name = "my screen",
    shape = "plane",
    point = [5., 10.],
    vector = [1., 0.],
    direction = "canceling",
    deposited_quantity = "weight",
    species = ["electron"],
    axes = [["a", -10.*l0, 10.*l0, 40],
            ["px", 0., 3., 30]],
    every = 10
)
```

name[¶](#id86 "Link to this definition")
:   Optional name of the diagnostic. Used only for post-processing purposes.

shape[¶](#shape "Link to this definition")
:   The shape of the screen surface: `"plane"`, `"sphere"`, or `"cylinder"`.

point[¶](#point "Link to this definition")
:   Type:
    :   A list of floats `[X]` in 1D, `[X,Y]` in 2D, `[X,Y,Z]` in 3D

    The coordinates of a point that defines the screen surface:
    a point of the `"plane"`, the center of the `"sphere"`,
    or a point on the `"cylinder"` axis.

vector[¶](#vector "Link to this definition")
:   Type:
    :   A list of floats `[X]` in 1D, `[X,Y]` in 2D, `[X,Y,Z]` in 3D

    The coordinates of a vector that defines the screen surface:
    the normal to the `"plane"`, a radius of the `"sphere"`.
    or the axis of the `"cylinder"` (in the latter case, the vector
    norm defines the cylinder radius).

direction[¶](#id87 "Link to this definition")
:   Default:
    :   `"both"`

    Determines how particles are counted depending on which side of the screen they come from.

    - `"both"` to account for both sides.
    - `"forward"` for only the ones in the direction of the `vector`.
    - `"backward"` for only the ones in the opposite direction.
    - `"canceling"` to count negatively the ones in the opposite direction.

deposited\_quantity[¶](#id88 "Link to this definition")
:   Identical to the `deposited_quantity` of [particle binning diagnostics](#diagparticlebinning).

every[¶](#id89 "Link to this definition")
:   The number of time-steps between each output, **or** a [time selection](#timeselections).

flush\_every[¶](#id90 "Link to this definition")
:   Default:
    :   1

    Number of timesteps **or** a [time selection](#timeselections).

    When `flush_every` coincides with `every`, the output
    file is actually written (“flushed” from the buffer). Flushing
    too often can *dramatically* slow down the simulation.

species[¶](#id91 "Link to this definition")
:   A list of one or several species’ [`name`](#id93 "name").
    All these species are combined into the same diagnostic.

axes[¶](#id92 "Link to this definition")
:   A list of “axes” that define the grid of the histogram.
    It is identical to that of [particle binning diagnostics](#diagparticlebinning), with the
    addition of four types of axes:

    - If `shape="plane"`, then `"a"` and `"b"` are the axes perpendicular to the `vector`.
    - If `shape="sphere"`, then `"theta"` and `"phi"` are the angles with respect to the `vector`.
    - If `shape="cylinder"`, then `"a"` is along the cylinder axis and `"phi"` is the angle around it.

---

## *RadiationSpectrum* diagnostics[¶](#radiationspectrum-diagnostics "Link to this heading")
