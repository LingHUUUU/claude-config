# Run Smilei

Before launching Smilei, write a namelist file containing all simulation information (grid shape, particles, lasers, diagnostics, etc.). You can start from examples in the `benchmarks` directory.

---

## The `smilei` executable

After compiling, the executable `smilei` is in the source directory:

```
smilei arg1 arg2 arg3 ...
```

Command-line arguments can be:
- Path to a namelist
- Any Python instruction to execute during namelist reading

**Run with MPI**:
```bash
mpirun -n 4 ./smilei my_namelist.py
```

**Pass extra instructions**:
```bash
./smilei my_namelist.py "Main.print_every=10"
```

**With OpenMP threads** (set before mpirun):
```bash
export OMP_NUM_THREADS=4
```

When running, the output log will show how many MPI processes and OpenMP threads are in use.

---

## Test mode

A second executable `smilei_test` is available:

```bash
./smilei_test my_namelist.py
```

Test mode does the same initialization as normal mode, but:
- Only loads the first patch of the full simulation
- Does NOT compute the PIC loop — exits after initialization
- **Requires 1 MPI process only**

To test a namelist intended for N MPI processes × M OpenMP threads:
```bash
./smilei_test 1024 12 my_namelist.py
```

---

## Directory management

Smilei writes output to the current directory. Recommended workflow:

```bash
mkdir ~/my_simulation                     # New directory for results
cp ~/my_namelist.py ~/my_simulation       # Copy namelist
cd ~/my_simulation                        # Go there
mpirun -n 4 ~/Smilei/smilei my_namelist   # Run with 4 MPI processes
```

### Using the provided script

```bash
./smilei.sh 4 my_namelist.py
```
Creates a directory with results next to the namelist. The number (4) is the MPI process count.

---

## Running on GPU-equiped nodes

With Nvidia GPUs:
```bash
srun bind_gpu.sh ./smilei input.py
```

With AMD GPUs using cray on Adastra:
```bash
srun --cpu-bind=none --mem-bind=none --mpi=cray_shasta --kill-on-bad-exit=1 -- ./bind ./smilei input.py
```

Binding scripts are architecture-dependent — contact your admin support team.

---

## Debugging

Compile with debugging flags and internal checks:
```bash
make config=debug
```

In debug mode these C++ macros are activated:
- `DEBUG("some text" [<< other streamable])`
- `HEREIAM("some text" [<< other streamable])`

To check only a particular file: first compile with `make`, then modify the file, and recompile in debug mode.

---

## Known issues

**OpenMPI 2.* instability**: The vader protocol interferes with Smilei's memory management. Disable it:
```bash
mpirun --mca btl ^vader -n 4 ~/Smilei/smilei my_namelist
```
