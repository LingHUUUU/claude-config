## Specifying units[¶](#specifying-units "Link to this heading")

By default, all the diagnostics data is in code units (see [Units](../Understand/units.html)).

To change the units, all the methods [`Scalar()`](#Scalar "Scalar"),
[`Field()`](#Field "Field"), [`Probe()`](#Probe "Probe"),
[`ParticleBinning()`](#ParticleBinning "ParticleBinning") and
[`TrackParticles()`](#TrackParticles "TrackParticles") support a `units` argument.
It has three different syntaxes:

1. **A list**, for example `units = ["um/ns", "feet", "W/cm^2"]`

   In this case, any quantity found to be of the same dimension as one of these units
   will be converted.
2. **A dictionary**, for example `units = {"x":"um", "y":"um", "v":"Joule"}`

   In this case, we specify the units separately for axes `x` and `y`, and for the
   data values `v`.
3. **A** `Units` **object**, for example `units = happi.Units("um/ns", "feet", x="um")`

   This version combines the two previous ones.

Requirements for changing units

- The [Pint module](https://pypi.python.org/pypi/Pint/).
- To obtain units in a non-normalized system (e.g. SI), the simulation must have the
  parameter [`reference_angular_frequency_SI`](namelist.html#reference_angular_frequency_SI "reference_angular_frequency_SI") set to a finite value.
  Otherwise, this parameter can be set during post-processing as an argument to the
  [`happi.Open()`](#happi.Open "happi.Open") function.

---
