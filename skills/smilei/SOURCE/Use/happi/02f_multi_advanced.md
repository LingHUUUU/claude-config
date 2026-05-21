## Simultaneous plotting of multiple diagnostics[¶](#simultaneous-plotting-of-multiple-diagnostics "Link to this heading")

happi.multiPlot(*diag1*, *diag2*, *...*, *\*\*kwargs*)[¶](#happi.multiPlot "Link to this definition")
:   Makes an animated figure containing several plots (one for each diagnostic).
    If all diagnostics are of similar type, they may be overlayed on only one plot.

    - `diag1`, `diag2`, etc.
      :   Diagnostics prepared by `Scalar()`, `Field()`, `Probe()`, etc.

    Keyword-arguments `kwargs` are:

    - `figure`: The figure number that is passed to matplotlib (default is 1).
    - `shape`: The arrangement of plots inside the figure. For instance, `[2, 1]`
      makes two plots stacked vertically, and `[1, 2]` makes two plots stacked horizontally.
      If absent, stacks plots vertically.
    - `legend_font`: dictionnary to set the legend’s font properties,
      such as `{'size':15, 'weight':'bold', 'family':'serif', 'color':'k'}`.
    - `movie` : filename to create a movie.
    - `fps` : frames per second for the movie.
    - `dpi` : resolution of the `movie` or `saveAs`.
    - `saveAs`: name of a directory where to save each frame as figures.
      You can even specify a filename such as `mydir/prefix.png` and it will automatically
      make successive files showing the timestep: `mydir/prefix0.png`, `mydir/prefix1.png`, etc.
    - `skipAnimation` : if True, plots only the last frame.
    - `timesteps`: same as the `timesteps` argument of the [`plot()`](#plot "plot") method.

happi.multiSlide(*diag1*, *diag2*, *...*, *\*\*kwargs*)[¶](#happi.multiSlide "Link to this definition")
:   Identical to `happi.multiPlot` but uses a time slider instead of an animation.

    - `diag1`, `diag2`, etc.
      :   Diagnostics prepared by `Scalar()`, `Field()`, `Probe()`, etc.
    - `figure`, `shape`, and `legend_font`: same as in `happi.multiPlot`.

**Example**:

```
S = happi.Open("path/to/my/results")
A = S.Probe(probeNumber=0, field="Ex")
B = S.ParticleBinning(diagNumber=1)
happi.multiPlot( A, B, figure=1 )
```

> This plots a Probe and a ParticleBinning on the same figure, and makes an animation for all available timesteps.

Note

To plot several quantities on the same graph, you can try `shape=[1,1]`.
One diagnostic may have the option `side="right"` to use the right-hand-side axis.

---

## Advanced plotting options[¶](#advanced-plotting-options "Link to this heading")

In addition to `figure`, `vmin`, `vmax`, `xmin`, `xmax`, `ymin` and `ymax`,
there are many more optional arguments. They are directly passed to the *matplotlib* package.

For the figure: `figsize`, `dpi`, `facecolor`, `edgecolor`

> Please refer to
> [matplotlib’s figure options](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html).

For the axes frame: `aspect`, `axis_facecolor`, `frame_on`, `position`,
`visible`, `xlabel`, `xscale`, `xticklabels`, `xticks`,
`ylabel`, `yscale`, `yticklabels`, `yticks`, `zorder`

> Please refer to matplotlib’s axes options: the same as functions starting
> with `set_` listed [here](http://matplotlib.org/stable/api/axes_api.html).

For the lines: `color`, `dashes`, `drawstyle`, `fillstyle`,
`label`, `linestyle`, `linewidth`,
`marker`, `markeredgecolor`, `markeredgewidth`,
`markerfacecolor`, `markerfacecoloralt`, `markersize`, `markevery`,
`visible`, `zorder`

> Please refer to
> [matplotlib’s line options](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html).

For the image: `cmap`, `aspect`, `interpolation`, `norm`

> Please refer to
> [matplotlib’s image options](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html).

For the colorbar: `cbaspect`, `orientation`, `fraction`, `pad`,
`shrink`, `anchor`, `panchor`, `extend`, `extendfrac`, `extendrect`,
`spacing`, `ticks`, `format`, `drawedges`, `size`, `clabel`

> Please refer to
> [matplotlib’s colorbar options](https://matplotlib.org/stable/api/colorbar_api.html).

For the tick number format: `style_x`, `scilimits_x`, `useOffset_x`,
`style_y`, `scilimits_y`, `useOffset_y`

> Please refer to
> [matplotlib’s tick label format](http://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ticklabel_format.html).

For fonts: `title_font`, `xlabel_font`, `xticklabels_font`,
`ylabel_font`, `yticklabels_font`, `colorbar_font`

> These options are dictionnaries that may contain the entries available in
> [matplotlib’s font properties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties),
> for instance:
>
> ```
> title_font = {'size': 15, 'weight': 'bold', 'family':'serif', 'color': 'k'}
> ```

**Example**:

> To choose a gray colormap of the image, use `cmap="gray"`:
>
> ```
> S = happi.Open("path/to/my/results")
> S.ParticleBinning(0, figure=1, cmap="gray") .plot()
> ```

> Many colormaps are available from the *matplotlib* package. With `cmap=""`, you will get a list of available colormaps.
> Smilei’s default colormaps are: `smilei`, `smilei_r`, `smileiD` and `smileiD_r`.

---

## Update the plotting options[¶](#update-the-plotting-options "Link to this heading")
