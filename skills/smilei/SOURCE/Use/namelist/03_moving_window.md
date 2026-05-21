## Moving window[¶](#moving-window "Link to this heading")

The simulated domain can move relatively to its the initial position. The “moving window”
is (almost) periodically shifted in the `x_max` direction.
Each “shift” consists in removing a column of patches from the `x_min` border and
adding a new one after the `x_max` border, thus changing the physical domain that the
simulation represents but keeping the same box size. This is particularly useful to
*follow* waves or plasma moving at high speed.
The frequency of the shifts is adjusted so that the average displacement velocity
over many shifts matches the velocity given by the user.
The user may ask for a given number of additional shifts at a given time.
These additional shifts are not taken into account for the evaluation of the average
velocity of the moving window.

The block `MovingWindow` is optional. The window does not move it you do not define it.

Warning

When the window starts moving, all laser injections via Silver-Muller boundary conditions
are immediately stopped for physical correctness.

```
MovingWindow(
    time_start = 0.,
    velocity_x = 1.,
    number_of_additional_shifts = 0.,
    additional_shifts_time = 0.,
)
```

time\_start[¶](#time_start "Link to this definition")
:   Type:
    :   Float.

    Default:

    The time at which the window starts moving.

velocity\_x[¶](#velocity_x "Link to this definition")
:   Type:
    :   Float.

    Default:

    The average velocity of the moving window in the `x_max` direction. It muste be between 0 and 1.

number\_of\_additional\_shifts[¶](#number_of_additional_shifts "Link to this definition")
:   Type:
    :   Integer.

    Default:

    The number of additional shifts of the moving window.

additional\_shifts\_time[¶](#additional_shifts_time "Link to this definition")
:   Type:
    :   Float.

    Default:

    The time at which the additional shifts are done.

Note

The [particle binning diagnostics](#diagparticlebinning) accept an “axis” called `moving_x`
corresponding to the `x` coordinate corrected by the moving window’s current movement.

---
