EM\_boundary\_conditions[¶](#EM_boundary_conditions "Link to this definition")
:   Type:
    :   list of lists of strings

    Default:
    :   `[["periodic"]]`

    The boundary conditions for the electromagnetic fields. Each boundary may have one of
    the following conditions: `"periodic"`, `"silver-muller"`, `"reflective"`, `"ramp??"` or `"PML"`.

    **Syntax 1:** `[[bc_all]]`, identical for all boundaries.

    **Syntax 2:** `[[bc_X], [bc_Y], ...]`, different depending on x, y or z.

    **Syntax 3:** `[[bc_Xmin, bc_Xmax], ...]`, different on each boundary.

    - `"silver-muller"` is an open boundary condition.
      The incident wave vector \(k\_{inc}\) on each face is defined by
      `"EM_boundary_conditions_k"`.
      When using `"silver-muller"` as an injecting boundary,
      make sure \(k\_{inc}\) is aligned with the wave you are injecting.
      When using `"silver-muller"` as an absorbing boundary,
      the optimal wave absorption on a given face will be along \(k\_{abs}\)
      the specular reflection of \(k\_{inc}\) on the considered face.
    - `"ramp??"` is a basic, open boundary condition designed
      for the spectral solver in `AMcylindrical` geometry.
      The `??` is an integer representing a number of cells
      (smaller than the number of ghost cells).
      Over the first half, the fields remain untouched.
      Over the second half, all fields are progressively reduced down to zero.
    - `"PML"` stands for Perfectly Matched Layer. It is an open boundary condition.
      The number of cells in the layer must be defined by `"number_of_pml_cells"`.
      It supports laser injection as in `"silver-muller"`.
      If not all boundary conditions are `PML`, make sure to set `number_of_pml_cells=0` on boundaries not using PML.

EM\_boundary\_conditions\_k[¶](#EM_boundary_conditions_k "Link to this definition")
:   Type:
    :   list of lists of floats

    Default:
    :   `[[1.,0.],[-1.,0.],[0.,1.],[0.,-1.]]` in 2D

    Default:
    :   `[[1.,0.,0.],[-1.,0.,0.],[0.,1.,0.],[0.,-1.,0.],[0.,0.,1.],[0.,0.,-1.]]` in 3D

    For `silver-muller` absorbing boundaries,
    the *x,y,z* coordinates of the unit wave vector `k` incident on each face
    (sequentially Xmin, Xmax, Ymin, Ymax, Zmin, Zmax).
    The number of coordinates is equal to the dimension of the simulation.
    The number of given vectors must be equal to 1 or to the number of faces
    which is twice the dimension of the simulation. In cylindrical geometry,
    `k` coordinates are given in the `xr` frame and only the Rmax face is affected.

    **Syntax 1:** `[[1,0,0]]`, identical for all boundaries.

    **Syntax 2:** `[[1,0,0],[-1,0,0], ...]`, different on each boundary.

number\_of\_pml\_cells[¶](#number_of_pml_cells "Link to this definition")
:   Type:
    :   List of lists of integers

    Default:
    :   `[[10,10],[10,10],[10,10]]`

    Defines the number of cells in the `"PML"` layers using the same alternative syntaxes as `"EM_boundary_conditions"`.

pml\_sigma[¶](#pml_sigma "Link to this definition")
:   Type:
    :   List of profiles

    Default:
    :   [lambda x : 20 \* x\*\*2]

    Defines the sigma profiles across the transverse dimension of the PML for each dimension of the simulation.
    It must be expressed as a list of profiles (1 per dimension).

    If a single profile is given, it will be used for all dimensions.

    For a given dimension, the same profile is applied to both sides of the domain.

    The profile is given as a single variable function defined on the interval [0,1] where 0 is the inner bound of the PML and 1 is the outer bound of the PML.
    Please refer to [Perfectly Matched Layers](../Understand/PML.html) if needed in AM geometry.

pml\_kappa[¶](#pml_kappa "Link to this definition")
:   Type:
    :   List of profiles

    Default:
    :   [lambda x : 1 + 79 \* x\*\*4]

    Defines the kappa profiles across the transverse dimension of the PML for each dimension of the simulation.
    It must be expressed as a list of profiles (1 per dimension).

    If a single profile is given, it will be used for all dimensions.

    For a given dimension, the same profile is applied to both sides of the domain.

    The profile is given as a single variable function defined on the interval [0,1] where 0 is the inner bound of the PML and 1 is the outer bound of the PML.
    Please refer to [Perfectly Matched Layers](../Understand/PML.html) if needed in AM geometry.

time\_fields\_frozen[¶](#time_fields_frozen "Link to this definition")
