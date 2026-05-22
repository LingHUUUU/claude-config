# Smilei Synopsis

Smilei is a collaborative, open-source, user-friendly, high-performance and multi-purpose electromagnetic Particle-In-Cell (PIC) code for plasma simulation.

The code is developed in C++ based on an object-oriented architecture. To face diverse community needs, it offers modularity:

- **Geometries**: Cartesian 1D, 2D, 3D or cylindrical with azimuthal Fourier decomposition (AMcylindrical)
- **Arbitrary laser or plasma profiles** (any Python function)
- **Various Maxwell solvers**: Yee (FDTD), Bouchard (4th-order), M4, Lehe, Terzani (low-dispersion), PSATD (experimental)
- **Particle pushers**: Boris (standard), Vay, Higuera-Cary
- **Interpolators/projectors**: Orders 2 and 4, B-TIS3 (experimental, reduces NCR)
- **Laser envelope model**, including in cylindrical geometry
- **Advanced boundary conditions**: Silver-Muller, PML, periodic, reflective

The user-friendly interface consists of input files written in Python, with run-time diagnostics (HDF5 output) and Python post-processing tools (happi).

## Performance

Co-developed by HPC specialists and physicists, Smilei is designed for high performance on massively-parallel supercomputers:
- Hybrid MPI/OpenMP parallelization
- Dynamic load balancing
- SIMD vectorization (2-3x speedup above ~10 ppc)
- GPU acceleration (Nvidia or AMD, supports 1D/2D/3D Cartesian with Moving Window)

## Physics modules

- Field ionization (tunnel ionization, ADK/PPT/BSI models)
- Binary Coulomb collisions and impact ionization
- QED processes: high-energy photon emission, radiation reaction (multiple models)
- Multiphoton Breit-Wheeler pair production
- Nuclear reactions (experimental)

## Reference publication

> J. Derouillat et al., SMILEI: a collaborative, open-source, multi-purpose particle-in-cell code for plasma simulation, Comput. Phys. Commun. 222, 351-373 (2018), doi:10.1016/j.cpc.2017.09.024
