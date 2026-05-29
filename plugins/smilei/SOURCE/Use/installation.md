# Install Smilei

---

## Dependencies

**Required**:
- A C++11 compiler, optionally implementing OpenMP version > 4.5
- An MPI library (recommended: IntelMPI or OpenMPI supporting `MPI_THREAD_MULTIPLE`)
- Parallel HDF5 library compiled with your versions of C++ and MPI
- Python 3+ with header files

**For GPU compilation**:
- GPU-aware C++ compiler (e.g., `nvc++` for NVIDIA or `clang` for AMD)
- CUDA or HIP compiler (e.g., `nvcc` for NVIDIA or `hipcc` for AMD)

**Optional**:
- Git for version control
- Python modules for post-processing: `sphinx`, `h5py`, `numpy`, `matplotlib`, `pint`
- FFmpeg for converting animations to videos

---

## Download Smilei

```bash
cd /path/of/your/choice/
git clone https://github.com/SmileiPIC/Smilei.git
```

---

## Compile

After downloading, compile with:

```bash
cd Smilei
make
```

### Compile options

- `make config=debug` — compile with debugging flags (slower)
- `make -j N` — use N parallel compilation jobs
- `make happi` — prepare the post-processing library

### Environment variables

Key environment variables for compilation:
- `CXX` — C++ compiler
- `CXXFLAGS` — compiler flags for optimization/vectorization
- `HDF5_ROOT` — path to HDF5 installation

### Machine-specific compilation

Smilei provides machine files for specific architectures. For example, for Skylake with Intel compiler, the `skylake` machine file sets:

```
-xCOMMON-AVX512 -ip -ipo -inline-factor=1000 -D__INTEL_SKYLAKE_8168 -fno-alias
```

### GPU compilation

For GPU-equipped clusters, specific compilation instructions are available. See `SMILEI_MANUAL_SOURCE/Use/install_linux_GPU.md` for details.

---

## Platform-specific installation

Detailed installation guides are available for:
- **Linux**: See `SMILEI_MANUAL_SOURCE/Use/install_linux.md`
- **macOS**: See `SMILEI_MANUAL_SOURCE/Use/install_macos.md`
- **Supercomputers**: See `SMILEI_MANUAL_SOURCE/Use/install_supercomputer.md`
- **Linux with GPU**: See `SMILEI_MANUAL_SOURCE/Use/install_linux_GPU.md`

---

## Post-installation

After compilation, verify your installation:

```bash
# Test with a benchmark
cd benchmarks
mpirun -n 1 ../smilei_test some_benchmark.py

# Build happi for post-processing
make happi
```
