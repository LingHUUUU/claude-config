## Update the plotting options[¶](#update-the-plotting-options "Link to this heading")

Scalar.set(*...*)[¶](#Scalar.set "Link to this definition")

Field.set(*...*)[¶](#Field.set "Link to this definition")

Probe.set(*...*)[¶](#Probe.set "Link to this definition")

ParticleBinning.set(*...*)[¶](#ParticleBinning.set "Link to this definition")

Screen.set(*...*)[¶](#Screen.set "Link to this definition")
:   **Example**:

    ```
    S = happi.Open("path/to/my/results")
    A = S.ParticleBinning(diagNumber=0, figure=1, vmax=1)
    A.plot( figure=2 )
    A.set( vmax=2 )
    A.plot()
    ```

---

## Other tools in `happi`[¶](#other-tools-in-happi "Link to this heading")

happi.openNamelist(*namelist*)[¶](#happi.openNamelist "Link to this definition")
:   Reads a namelist and stores all its content in the returned object.

    - `namelist`: the path to the namelist.

**Example**:

```
namelist = happi.openNamelist("path/no/my/namelist.py")
print namelist.Main.timestep
```
