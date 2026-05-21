## Other arguments for diagnostics[¶](#other-arguments-for-diagnostics "Link to this heading")

All diagnostics above can use additional keyword arguments (`kwargs`)
to manipulate the plotting options:

- `figure`: The figure number that is passed to matplotlib.
- `vmin`, `vmax`: data value limits.
- `vsym`: makes data limits symmetric about 0 (`vmin` and `vmax` are ignored),
  and sets the colormap to `smileiD`.

  - If `vsym = True`, autoscale symmetrically.
  - If `vsym` is a number, limits are set to [-`vsym`, `vsym`].
- `xmin`, `xmax`, `ymin`, `ymax`: axes limits.
- `xfactor`, `yfactor`: factors to rescale axes.
- `xoffset`, `yoffset`: numerical values to offset the
  coordinates. These values must be given in the original (normalized)
  units, i.e. not acounting for the factors above or for unit conversion.
- `title`: a string that replaces the plot title (or the y-label in a 1D plot).
  The current simulation time can be included with the placeholders `{time}` and
  `{time_units}`, together with formatting instructions conforming to
  [python’s string formatter](https://docs.python.org/3/library/string.html#format-string-syntax).
  For instance: `title = "Density @ $t = {time:.0f} {time_units}$"`.
- `side`: `"left"` (by default) or `"right"` puts the y-axis on the left-
  or the right-hand-side.
- `transparent`: `None` (by default), `"over"`, `"under"`, `"both"`, or a *function*.
  The colormap becomes transparent *over*, *under*, or *outside both* the boundaries
  set by `vmin` and `vmax`.
  This argument may be set instead to a function mapping the data value \(\in [0,1]\) to the
  transparency \(\in [0,1]\). For instance `lambda x: 1-x`.
- Other Matplotlib arguments listed in [Advanced plotting options](#advancedoptions).

---

## Obtain the data[¶](#obtain-the-data "Link to this heading")
