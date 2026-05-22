## Other arguments for diagnostics[¶](#other-arguments-for-diagnostics "Link to this heading")

All diagnostics above can use additional keyword arguments (`kwargs`) to manipulate the plotting options:

* `figure`: The figure number that is passed to matplotlib.
* `vmin`, `vmax`: data value limits.
* `vsym`: makes data limits symmetric about 0 (`vmin` and `vmax` are ignored), and sets the colormap to `smileiD`.  
   * If `vsym = True`, autoscale symmetrically.  
   * If `vsym` is a number, limits are set to \[-`vsym`, `vsym`\].
* `xmin`, `xmax`, `ymin`, `ymax`: axes limits.
* `xfactor`, `yfactor`: factors to rescale axes.
* `xoffset`, `yoffset`: numerical values to offset the coordinates. These values must be given in the original (normalized) units, i.e. not acounting for the factors above or for unit conversion.
* `title`: a string that replaces the plot title (or the y-label in a 1D plot). The current simulation time can be included with the placeholders `{time}` and`{time_units}`, together with formatting instructions conforming to[python’s string formatter](https://docs.python.org/3/library/string.html#format-string-syntax). For instance: `title = "Density @ $t = {time:.0f} {time_units}$"`.
* `side`: `"left"` (by default) or `"right"` puts the y-axis on the left- or the right-hand-side.
* `transparent`: `None` (by default), `"over"`, `"under"`, `"both"`, or a _function_. The colormap becomes transparent _over_, _under_, or _outside both_ the boundaries set by `vmin` and `vmax`. This argument may be set instead to a function mapping the data value \\(\\in \[0,1\]\\) to the transparency \\(\\in \[0,1\]\\). For instance `lambda x: 1-x`.
* Other Matplotlib arguments listed in [Advanced plotting options](#advancedoptions).

---

## Obtain the data[¶](#obtain-the-data "Link to this heading")

Scalar.getData(_timestep\=None_)[¶](#Scalar.getData "Link to this definition")

Field.getData(_timestep\=None_)[¶](#Field.getData "Link to this definition")

Probe.getData(_timestep\=None_)[¶](#Probe.getData "Link to this definition")

ParticleBinning.getData(_timestep\=None_)[¶](#ParticleBinning.getData "Link to this definition")

Screen.getData(_timestep\=None_)[¶](#Screen.getData "Link to this definition")

TrackParticles.getData(_timestep\=None_)[¶](#TrackParticles.getData "Link to this definition")

Returns a list of the data arrays (one element for each timestep requested). In the case of `TrackParticles`, this method returns a dictionary containing one entry for each axis, and if `sort==False`, these entries are included inside an entry for each timestep.

* `timestep`, if specified, is the only timestep number that is read and returned.

**Example**:

S = happi.Open("path/to/results") # Open the simulation
Diag = S.Field(0, "Ex")       # Open Ex in the first Field diag
result = Diag.getData()       # Get list of Ex arrays (one for each time)

Scalar.getTimesteps()[¶](#Scalar.getTimesteps "Link to this definition")

Field.getTimesteps()[¶](#Field.getTimesteps "Link to this definition")

Probe.getTimesteps()[¶](#Probe.getTimesteps "Link to this definition")

ParticleBinning.getTimesteps()[¶](#ParticleBinning.getTimesteps "Link to this definition")

Screen.getTimesteps()[¶](#Screen.getTimesteps "Link to this definition")

TrackParticles.getTimesteps()[¶](#TrackParticles.getTimesteps "Link to this definition")

Returns a list of the timesteps requested.

Scalar.getTimes()[¶](#Scalar.getTimes "Link to this definition")

Field.getTimes()[¶](#Field.getTimes "Link to this definition")

Probe.getTimes()[¶](#Probe.getTimes "Link to this definition")

ParticleBinning.getTimes()[¶](#ParticleBinning.getTimes "Link to this definition")

Screen.getTimes()[¶](#Screen.getTimes "Link to this definition")

TrackParticles.getTimes()[¶](#TrackParticles.getTimes "Link to this definition")

Returns the list of the times requested. By default, times are in the code’s units, but are converted to the diagnostic’s units defined by the `units` argument, if provided.

Scalar.getAxis(_axis_)[¶](#Scalar.getAxis "Link to this definition")

Field.getAxis(_axis_, _timestep_)[¶](#Field.getAxis "Link to this definition")

Probe.getAxis(_axis_)[¶](#Probe.getAxis "Link to this definition")

ParticleBinning.getAxis(_axis_, _timestep_)[¶](#ParticleBinning.getAxis "Link to this definition")

Screen.getAxis(_axis_, _timestep_)[¶](#Screen.getAxis "Link to this definition")

Returns the list of positions of the diagnostic data along the requested axis. If the axis is not available, returns an empty list. By default, axis positions are in the code’s units, but are converted to the diagnostic’s units defined by the `units` argument, if provided.

* `axis`: the name of the requested axis.  
   * For `Field`: this is `"x"`, `"y"` or `"z"`.  
   * For `Probe`: this is `"axis1"`, `"axis2"` or `"axis3"`.  
   * For `ParticleBinning` and `Screen`: this is the `type` of the [axes](namelist.html#id98 "axes")defined in the namelist. In case of a user defined axis, the name is `"user_function"`followed by the number of the function (starting from 0 for the first one). The names of the axes can be checked by printing the diagnostic.
* `timestep`: The timestep at which the axis is obtained. Only matters in`ParticleBinning`, `Screen` and `RadiationSpectrum` when `auto` axis limits are requested; or in `Field` when `moving=True`.

TrackParticles.iterParticles(_timestep_, _chunksize\=1_)[¶](#TrackParticles.iterParticles "Link to this definition")

This method, specific to the tracked particles, provides a fast iterator on chunks of particles for a given timestep. The argument `chunksize` is the number of particles in each chunk. Note that the data is _not ordered_ by particle ID, meaning that particles are not ordered the same way from one timestep to another.

The returned quantity for each iteration is a python dictionary containing key/value pairs `axis:array`, where `axis` is the name of the particle characteristic (`"x"`,`"px"`, etc.) and `array` contains the corresponding particle values.

**Example**:

S = happi.Open("path/to/my/results")        # Open the simulation
Diag = S.TrackParticles("my_particles") # Open the tracked particles
npart = 0
sum_px = 0.
# Loop particles of timestep 100 by chunks of 10000
for particle_chunk in Diag.iterParticles(100, chunksize=10000):
    npart  += particle_chunk["px"].size
    sum_px += particle_chunk["px"].sum()
# Calculate the average px
mean_px = sum_px / npart

Field.getXmoved(_timestep_)[¶](#Field.getXmoved "Link to this definition")

Probe.getXmoved(_timestep_)[¶](#Probe.getXmoved "Link to this definition")

TrackParticles.getXmoved(_timestep_)[¶](#TrackParticles.getXmoved "Link to this definition")

This method returns the displacement of the moving window at the required `timestep`.

---

## Export 2D or 3D data to VTK[¶](#export-2d-or-3d-data-to-vtk "Link to this heading")

Field.toVTK(_numberOfPieces\=1_)[¶](#Field.toVTK "Link to this definition")

Probe.toVTK(_numberOfPieces\=1_)[¶](#Probe.toVTK "Link to this definition")

ParticleBinning.toVTK(_numberOfPieces\=1_)[¶](#ParticleBinning.toVTK "Link to this definition")

Performances.toVTK(_numberOfPieces\=1_)[¶](#Performances.toVTK "Link to this definition")

Screen.toVTK(_numberOfPieces\=1_)[¶](#Screen.toVTK "Link to this definition")

TrackParticles.toVTK(_rendering\='trajectory'_, _data\_format\='xml'_)[¶](#TrackParticles.toVTK "Link to this definition")

Converts the data from a diagnostic object to the vtk format. Note the `export_dir` argument available for each diagnostic (see above).

* `numberOfPieces`: the number of files into which the data will be split.
* `rendering`: the type of output in the case of [TrackParticles()](#TrackParticles "TrackParticles"):  
   * `"trajectory"`: show particle trajectories. One file is generated for all trajectories. This rendering requires the particles to be sorted.  
   * `"cloud"`: show a cloud of particles. One file is generated for each iteration. This rendering can be used without sorting the particles.
* `data_format`: the data formatting in the case of [TrackParticles()](#TrackParticles "TrackParticles"), either `"vtk"` or `"xml"`. The format `"vtk"` results in ascii.

**Example for tracked particles**:

S = happi.Open("path/to/my/results")
tracked_particles = S.TrackParticles("electron", axes=["x","y","z","px","py","pz","Id"], timesteps=[1,10])
# Create cloud of particles in separate files for each iteration
tracked_particles.toVTK(rendering="cloud",data_format="xml");
# Create trajectory in a single file
tracked_particles.toVTK(rendering="trajectory",data_format="xml");

---

## Plot the data at one timestep[¶](#plot-the-data-at-one-timestep "Link to this heading")

This is the first method to plot the data. It produces a static image of the data at one given timestep.

Scalar.plot(_..._)[¶](#Scalar.plot "Link to this definition")

Field.plot(_..._)[¶](#Field.plot "Link to this definition")

Probe.plot(_..._)[¶](#Probe.plot "Link to this definition")

ParticleBinning.plot(_..._)[¶](#ParticleBinning.plot "Link to this definition")

TrackParticles.plot(_..._)[¶](#TrackParticles.plot "Link to this definition")

Screen.plot(_..._)[¶](#Screen.plot "Link to this definition")

All these methods have the same arguments described below.

plot(_timestep\=None_, _saveAs\=None_, _axes\=None_, _dpi\=200_, _\*\*kwargs_)[¶](#plot "Link to this definition")

If the data is 1D, it is plotted as a **curve**.

If the data is 2D, it is plotted as a **map**.

If the data is 0D, it is plotted as a **curve** as function of time.

* `timestep`: The iteration number at which to plot the data.
* `saveAs`: name of a directory where to save each frame as figures. You can even specify a filename such as `mydir/prefix.png` and it will automatically make successive files showing the timestep: `mydir/prefix0.png`, `mydir/prefix1.png`, etc.
* `axes`: Matplotlib’s axes handle on which to plot. If None, make new axes.
* `dpi`: the number of dots per inch for `saveAs`.

You may also have keyword-arguments (`kwargs`) described in [Other arguments for diagnostics](#otherkwargs).

**Example**:

S = happi.Open("path/to/my/results")
S.ParticleBinning(1).plot(timestep=40, vmin=0, vmax=1e14)

---

## Plot the data streaked over time[¶](#plot-the-data-streaked-over-time "Link to this heading")

This second type of plot works only for 1D data. All available timesteps are streaked to produce a 2D image where the second axis is time.

Scalar.streak(_..._)[¶](#Scalar.streak "Link to this definition")

Field.streak(_..._)[¶](#Field.streak "Link to this definition")

Probe.streak(_..._)[¶](#Probe.streak "Link to this definition")

ParticleBinning.streak(_..._)[¶](#ParticleBinning.streak "Link to this definition")

TrackParticles.streak(_..._)[¶](#TrackParticles.streak "Link to this definition")

Screen.streak(_..._)[¶](#Screen.streak "Link to this definition")

All these methods have the same arguments described below.

streak(_saveAs\=None_, _axes\=None_, _\*\*kwargs_)[¶](#streak "Link to this definition")

All arguments are identical to those of `plot`, with the exception of `timestep`.

**Example**:

S = happi.Open("path/to/my/results")
S.ParticleBinning(1).streak()

---

## Animated plot[¶](#animated-plot "Link to this heading")

This third plotting method animates the data over time.

Scalar.animate(_..._)[¶](#Scalar.animate "Link to this definition")

Field.animate(_..._)[¶](#Field.animate "Link to this definition")

Probe.animate(_..._)[¶](#Probe.animate "Link to this definition")

ParticleBinning.animate(_..._)[¶](#ParticleBinning.animate "Link to this definition")

TrackParticles.animate(_..._)[¶](#TrackParticles.animate "Link to this definition")

Screen.animate(_..._)[¶](#Screen.animate "Link to this definition")

All these methods have the same arguments described below.

animate(_movie\=''_, _fps\=15_, _dpi\=200_, _saveAs\=None_, _axes\=None_, _\*\*kwargs_)[¶](#animate "Link to this definition")

All arguments are identical to those of `streak`, with the addition of:

* `movie`: name of a file to create a movie, such as `"movie.avi"` or `"movie.gif"`. If `movie=""` no movie is created.
* `fps`: number of frames per second (only if movie requested).
* `dpi`: number of dots per inch for both `movie` and `saveAs`

**Example**:

S = happi.Open("path/to/my/results")
S.ParticleBinning(1).animate()

---

## Plot with a slider[¶](#plot-with-a-slider "Link to this heading")

This methods provides an interactive slider to change the time.

Scalar.slide(_..._)[¶](#Scalar.slide "Link to this definition")

Field.slide(_..._)[¶](#Field.slide "Link to this definition")

Probe.slide(_..._)[¶](#Probe.slide "Link to this definition")

ParticleBinning.slide(_..._)[¶](#ParticleBinning.slide "Link to this definition")

TrackParticles.slide(_..._)[¶](#TrackParticles.slide "Link to this definition")

Screen.slide(_..._)[¶](#Screen.slide "Link to this definition")

All these methods have the same arguments described below.

slide(_axes\=None_, _\*\*kwargs_)[¶](#slide "Link to this definition")

See `plot` for the description of the arguments.

**Example**:

S = happi.Open("path/to/my/results")
S.ParticleBinning(1).slide(vmin=0)

---

## Simultaneous plotting of multiple diagnostics[¶](#simultaneous-plotting-of-multiple-diagnostics "Link to this heading")

happi.multiPlot(_diag1_, _diag2_, _..._, _\*\*kwargs_)[¶](#happi.multiPlot "Link to this definition")

Makes an animated figure containing several plots (one for each diagnostic). If all diagnostics are of similar type, they may be overlayed on only one plot.

* `diag1`, `diag2`, etc.  
Diagnostics prepared by `Scalar()`, `Field()`, `Probe()`, etc.

Keyword-arguments `kwargs` are:

* `figure`: The figure number that is passed to matplotlib (default is 1).
* `shape`: The arrangement of plots inside the figure. For instance, `[2, 1]`makes two plots stacked vertically, and `[1, 2]` makes two plots stacked horizontally. If absent, stacks plots vertically.
* `legend_font`: dictionnary to set the legend’s font properties, such as `{'size':15, 'weight':'bold', 'family':'serif', 'color':'k'}`.
* `movie` : filename to create a movie.
* `fps` : frames per second for the movie.
* `dpi` : resolution of the `movie` or `saveAs`.
* `saveAs`: name of a directory where to save each frame as figures. You can even specify a filename such as `mydir/prefix.png` and it will automatically make successive files showing the timestep: `mydir/prefix0.png`, `mydir/prefix1.png`, etc.
* `skipAnimation` : if True, plots only the last frame.
* `timesteps`: same as the `timesteps` argument of the [plot()](#plot "plot") method.

happi.multiSlide(_diag1_, _diag2_, _..._, _\*\*kwargs_)[¶](#happi.multiSlide "Link to this definition")

Identical to `happi.multiPlot` but uses a time slider instead of an animation.

* `diag1`, `diag2`, etc.  
Diagnostics prepared by `Scalar()`, `Field()`, `Probe()`, etc.
* `figure`, `shape`, and `legend_font`: same as in `happi.multiPlot`.

**Example**:

S = happi.Open("path/to/my/results")
A = S.Probe(probeNumber=0, field="Ex")
B = S.ParticleBinning(diagNumber=1)
happi.multiPlot( A, B, figure=1 )

> This plots a Probe and a ParticleBinning on the same figure, and makes an animation for all available timesteps.

Note

To plot several quantities on the same graph, you can try `shape=[1,1]`. One diagnostic may have the option `side="right"` to use the right-hand-side axis.

---

## Advanced plotting options[¶](#advanced-plotting-options "Link to this heading")

In addition to `figure`, `vmin`, `vmax`, `xmin`, `xmax`, `ymin` and `ymax`, there are many more optional arguments. They are directly passed to the _matplotlib_ package.

For the figure: `figsize`, `dpi`, `facecolor`, `edgecolor`

> Please refer to[matplotlib’s figure options](https://matplotlib.org/stable/api/%5Fas%5Fgen/matplotlib.pyplot.figure.html).

For the axes frame: `aspect`, `axis_facecolor`, `frame_on`, `position`,`visible`, `xlabel`, `xscale`, `xticklabels`, `xticks`,`ylabel`, `yscale`, `yticklabels`, `yticks`, `zorder`

> Please refer to matplotlib’s axes options: the same as functions starting with `set_` listed [here](http://matplotlib.org/stable/api/axes%5Fapi.html).

For the lines: `color`, `dashes`, `drawstyle`, `fillstyle`,`label`, `linestyle`, `linewidth`,`marker`, `markeredgecolor`, `markeredgewidth`,`markerfacecolor`, `markerfacecoloralt`, `markersize`, `markevery`,`visible`, `zorder`

> Please refer to[matplotlib’s line options](https://matplotlib.org/stable/api/%5Fas%5Fgen/matplotlib.lines.Line2D.html).

For the image: `cmap`, `aspect`, `interpolation`, `norm`

> Please refer to[matplotlib’s image options](https://matplotlib.org/stable/api/%5Fas%5Fgen/matplotlib.pyplot.imshow.html).

For the colorbar: `cbaspect`, `orientation`, `fraction`, `pad`,`shrink`, `anchor`, `panchor`, `extend`, `extendfrac`, `extendrect`,`spacing`, `ticks`, `format`, `drawedges`, `size`, `clabel`

> Please refer to[matplotlib’s colorbar options](https://matplotlib.org/stable/api/colorbar%5Fapi.html).

For the tick number format: `style_x`, `scilimits_x`, `useOffset_x`,`style_y`, `scilimits_y`, `useOffset_y`

> Please refer to[matplotlib’s tick label format](http://matplotlib.org/stable/api/%5Fas%5Fgen/matplotlib.axes.Axes.ticklabel%5Fformat.html).

For fonts: `title_font`, `xlabel_font`, `xticklabels_font`,`ylabel_font`, `yticklabels_font`, `colorbar_font`

> These options are dictionnaries that may contain the entries available in[matplotlib’s font properties](https://matplotlib.org/stable/api/font%5Fmanager%5Fapi.html#matplotlib.font%5Fmanager.FontProperties), for instance:
> 
> title_font = {'size': 15, 'weight': 'bold', 'family':'serif', 'color': 'k'}

**Example**:

> To choose a gray colormap of the image, use `cmap="gray"`:
> 
> S = happi.Open("path/to/my/results")
> S.ParticleBinning(0, figure=1, cmap="gray") .plot()

> Many colormaps are available from the _matplotlib_ package. With `cmap=""`, you will get a list of available colormaps. Smilei’s default colormaps are: `smilei`, `smilei_r`, `smileiD` and `smileiD_r`.

---

## Update the plotting options[¶](#update-the-plotting-options "Link to this heading")

Scalar.set(_..._)[¶](#Scalar.set "Link to this definition")

Field.set(_..._)[¶](#Field.set "Link to this definition")

Probe.set(_..._)[¶](#Probe.set "Link to this definition")

ParticleBinning.set(_..._)[¶](#ParticleBinning.set "Link to this definition")

Screen.set(_..._)[¶](#Screen.set "Link to this definition")

**Example**:

S = happi.Open("path/to/my/results")
A = S.ParticleBinning(diagNumber=0, figure=1, vmax=1)
A.plot( figure=2 )
A.set( vmax=2 )
A.plot()

---

## Other tools in `happi`[¶](#other-tools-in-happi "Link to this heading")

happi.openNamelist(_namelist_)[¶](#happi.openNamelist "Link to this definition")

Reads a namelist and stores all its content in the returned object.

* `namelist`: the path to the namelist.

**Example**:

namelist = happi.openNamelist("path/no/my/namelist.py")
print namelist.Main.timestep

[Site index](site.html) 

 Last updated on Mar 16, 2026

 Powered by [Sphinx 7.2.6](http://sphinx-doc.org/)
