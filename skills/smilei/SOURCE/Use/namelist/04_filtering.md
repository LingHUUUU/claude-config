## Current filtering[¶](#current-filtering "Link to this heading")

The present version of **Smilei** provides a
[multi-pass binomial filter](../Understand/algorithms.html#multipassbinomialfilter) on the current densities,
which parameters are controlled in the following block:

```
CurrentFilter(
    model = "binomial",
    passes = [0],
    kernelFIR = [0.25,0.5,0.25]
)
```

model[¶](#model "Link to this definition")
:   Default:
    :   `"binomial"`

    The model for current filtering.

    - `"binomial"` for a binomial filter.
    - `"customFIR"` for a custom FIR kernel.

passes[¶](#passes "Link to this definition")
:   Type:
    :   A python list of integers.

    Default:
    :   `[0]`

    The number of passes (at each timestep) given for each dimension.
    If the list is of length 1, the same number of passes is assumed for all dimensions.

kernelFIR[¶](#kernelFIR "Link to this definition")
:   Default:
    :   `"[0.25,0.5,0.25]"`

    The FIR kernel for the `"customFIR"` model. The number of coefficients
    must be less than twice the number of ghost cells
    (adjusted using [`custom_oversize`](#custom_oversize "custom_oversize")).

---

## Field filtering[¶](#field-filtering "Link to this heading")

The present version of **Smilei** provides a method for field filtering
(at the moment, only the [Friedman electric field time-filter](../Understand/algorithms.html#efieldfilter) is available)
which parameters are controlled in the following block:

```
FieldFilter(
    model = "Friedman",
    theta = 0.,
)
```

model[¶](#id0 "Link to this definition")
:   Default:
    :   `"Friedman"`

    The model for field filtering. Presently, only `"Friedman"` field filtering is available.

theta[¶](#theta "Link to this definition")
:   Default:
    :   `0.`

    The \(\theta\) parameter (between 0 and 1) of Friedman’s method.

---
