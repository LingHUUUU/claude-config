## Time selections[¶](#time-selections "Link to this heading")

Several components (mainly diagnostics) may require a selection of timesteps to
be chosen by the user. When one of these timesteps is reached, the diagnostics will
output data. A time selection is given through the parameter `every` and is a list
of several numbers.

You may chose between five different syntaxes:

```
every = [               period                    ] # Syntax 1
every = [       start,  period                    ] # Syntax 2
every = [ start,  end,  period                    ] # Syntax 3
every = [ start,  end,  period,  repeat           ] # Syntax 4
every = [ start,  end,  period,  repeat,  spacing ] # Syntax 5
```

where

- `start` is the first timestep of the selection (defaults to 0);
- `end` is the last timestep of the selection (defaults to ∞);
- `period` is the separation between outputs (defaults to 1);
- `repeat` indicates how many outputs to do at each period (defaults to 1);
- `spacing` is the separation between each repeat (defaults to 1).

For more clarity, this graph illustrates the five syntaxes for time selections:

[![../_images/TimeSelections.png](../_images/TimeSelections.png)](../_images/TimeSelections.png)

Tips

- The syntax `every = period` is also accepted.
- Any value set to `0` will be replaced by the default value.
- Special case: `every=0` means no output.
- The numbers may be non-integers (apart from `repeat`). The closest timesteps are chosen.

---

## Profiles[¶](#profiles "Link to this heading")

Some of the quantities described in the previous sections can be profiles that depend on
space and/or time. See the [documentation on profiles](profiles.html) for detailed
instructions.

---

## Checkpoints[¶](#checkpoints "Link to this heading")
