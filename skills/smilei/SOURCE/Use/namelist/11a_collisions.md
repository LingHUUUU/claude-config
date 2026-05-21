## Collisions & reactions[¶](#collisions-reactions "Link to this heading")

[Binary collisions & reactions](../Understand/collisions.html) account for short-range Coulomb interactions of particles (shorter than the
cell size), but also include other effects such as impact ionization and nuclear reactions.
These are gathered under this section because they are treated as *binary processes* (meaning
they happen during the encounter of two macro-particles).

They are specified by one or several `Collisions` blocks:

```
Collisions(
    species1 = ["electrons1",  "electrons2"],
    species2 = ["ions1"],
    debug_every = 1000,
    coulomb_log = 0.,
    coulomb_log_factor = 1.,
    ionizing = False,
#      nuclear_reaction = [],
)
```

Note

The screening from bound electrons, which is important when
the atom is neutral or partially ionized, is accounted for only in the
case of e-i collisions. To activate it, atom species **must have**
their [`atomic_number`](#atomic_number "atomic_number") defined and non-zero.

species1[¶](#species1 "Link to this definition")

species2[¶](#species2 "Link to this definition")
:   Lists of species’ [`name`](#id93 "name").

    The collisions and reactions will occur between all species under the group `species1`
    and all species under the group `species2`. For example, to collide all
    electrons with ions:

    ```
    species1 = ["electrons1", "electrons2"], species2 = ["ions"]
    ```

    Warning

    This does not make `electrons1` collide with `electrons2`.

    The two groups of species have to be *completely different* OR *exactly equal*.
    In other words, if `species1` is not equal to `species2`,
    then they cannot have any common species.
    If the two groups are exactly equal, we call this situation **intra-collisions**.

    Note

    If both lists `species1` and `species2` contain only one species,
    the algorithm is potentially faster than the situation with several
    species in one or the other list. This is especially true if the
    machine accepts SIMD vectorization.

every[¶](#id70 "Link to this definition")
:   Default:
    :   1

    Number of timesteps between each computation of the collisions or reactions.
    Use a number higher than 1 only if you know the collision frequency is low
    with respect to the inverse of the timestep.

debug\_every[¶](#debug_every "Link to this definition")
:   Default:
    :   0

    Number of timesteps between each output of information about collisions or reactions.
    If 0, there will be no outputs.

time\_frozen[¶](#id71 "Link to this definition")
:   Default:

    The time during which no collisions or reactions happen, in units of \(T\_r\).

coulomb\_log[¶](#coulomb_log "Link to this definition")
:   Default:

    The Coulomb logarithm.

    - If \(= 0\), the Coulomb logarithm is automatically computed for each collision.
    - If \(> 0\), the Coulomb logarithm is equal to this value.
    - If \(< 0\), collisions are not treated (but other reactions may happen).

coulomb\_log\_factor[¶](#coulomb_log_factor "Link to this definition")
:   Default:

    A constant, strictly positive factor that multiplies the Coulomb logarithm, regardless
    of [`coulomb_log`](#coulomb_log "coulomb_log") being automatically computed or set to a constant value.
    This can help, for example, to compensate artificially-reduced ion masses.

ionizing[¶](#ionizing "Link to this definition")
:   Default:
    :   `False`

    [Collisional ionization](../Understand/collisions.html#collionization) is set when this parameter is not `False`.
    It can either be set to the name of a pre-existing electron species (where the ionized
    electrons are created), or to `True` (the first electron species in [`species1`](#species1 "species1")
    or [`species2`](#species2 "species2") is then chosen for ionized electrons).

    One of the species groups must be all electrons ([`mass`](#mass "mass") = 1), and the other
    one all ions of the same [`atomic_number`](#atomic_number "atomic_number").

nuclear\_reaction[¶](#nuclear_reaction "Link to this definition")
:   Type:
    :   a list of strings

    Default:
    :   `None` (no nuclear reaction)

    A list of the species names for the products of [Nuclear reactions](../Understand/collisions.html#collnuclearreactions)
    that may occur during collisions. You may omit product species if they are not necessary
    for the simulation.

    All members of [`species1`](#species1 "species1") must be the same type of atoms, which is automatically
    recognized by their [`mass`](#mass "mass") and [`atomic_number`](#atomic_number "atomic_number"). The same applies for
    all members of [`species2`](#species2 "species2").

    In the current version, only the reaction D(d,n)He³ is available.

nuclear\_reaction\_multiplier[¶](#nuclear_reaction_multiplier "Link to this definition")
:   Type:
    :   a float

    Default:
    :   0. (automatically adjusted)

    The rate multiplier for nuclear reactions. It is a positive number that artificially
    increases the occurence of reactions so that a good statistics is obtained. The number
    of actual reaction products is adjusted by changing their weights in order to provide
    a physically correct number of reactions. Leave this number to `0.` for an automatic
    rate multiplier: the final number of produced macro-particles will be of the same order
    as that of reactants.

---

## Radiation reaction[¶](#radiation-reaction "Link to this heading")
