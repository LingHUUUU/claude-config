# Common Gotchas

## Python Interpreter Overhead

- Smilei starts one Python interpreter per MPI rank
- Large namelist imports can be expensive — avoid unnecessary `import` statements
- Use `cleanup()` to delete large variables and free memory after initialization

## Test Mode (`smilei_test`)

- Only initializes, does NOT run the PIC loop — checks namelist consistency
- Must run on 1 MPI process
- Can specify expected MPI/OpenMP config: `./smilei_test 1024 12 namelist.py`

## preprocess() / cleanup() Hooks

- `preprocess()`: runs before main loop, good for copying shared data
- `cleanup()`: runs after main loop, good for freeing Python memory

## Post-processing

- `python -i smilei.py` restores namelist variables into interactive Python
- happi does NOT support multiple `%matplotlib` calls — restart Python when switching simulations

## OpenMPI

- Use `--mca btl ^vader` to disable vader protocol instability
- Cluster may require `module load mpi/openmpi`

## Boundary Conditions

- `silver-muller` EM BC + `remove` particle BC = most stable combination
- PML absorbs better than silver-muller but costs more computation
