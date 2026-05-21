## Multiphoton Breit-Wheeler[¶](#multiphoton-breit-wheeler "Link to this heading")

The block `MultiphotonBreitWheeler` enables to tune parameters of the
multiphoton Breit-Wheeler process and particularly the table generation.
For more information on this physical mechanism, see [Multiphoton Breit-Wheeler pair creation](../Understand/multiphoton_Breit_Wheeler.html).

There are three tables used for the multiphoton Breit-Wheeler refers to as the
*integration\_dT\_dchi*, *min\_particle\_chi\_for\_xi* and *xi* table.

```
MultiphotonBreitWheeler(

  # Path to the tables
  table_path = "<path to the external table folder>",

)
```

table\_path[¶](#id72 "Link to this definition")
:   Default:
    :   `""`

    Path to the **directory** that contains external tables for the multiphoton Breit-Wheeler.
    If empty, the default tables are used.
    Default tables are embedded in the code.
    External tables can be generated using the external tool **smilei\_tables** (see [Generation of the external tables](tables.html)).

---
