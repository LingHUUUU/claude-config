# Smilei Simulation Workflow

> This file defines the standard 5-stage workflow for every Smilei simulation task.
> All stages must be followed in order. Each stage produces a deliverable and requires user approval before proceeding to the next stage.

---

## Language Convention

**All user-facing deliverables must be written in Chinese (中文).** This includes:
- `design_outline.md`, `report.md` — full document in Chinese
- `post.ipynb` — markdown cells and inline comments in Chinese
- All stage-gate summaries and checkpoints presented to the user

Technical content that stays in English: Python code (`input.py`), shell scripts (`submit_array.job`), happi API calls, variable names, and SOURCE/ reference documents.

---

## Stage 1: Design Outline

**Goal**: Agree on the complete simulation design before writing any code.

**Steps**:
1. Extract core physics requirements from user's description: geometry, laser, target/plasma, species, diagnostics
2. Cross-reference SOURCE/ docs to confirm parameter validity and constraints
3. Check NOTES/ for relevant prior experience
4. Produce `design_outline.md` containing:

   - **Physics setup**: geometry type, laser parameters (a0, waist, duration, incidence angle, polarization), target/plasma (density profile, species, temperature, ionization), boundary conditions
   - **Grid design**: target resolution (dx, dy) → number_of_patches → cells_per_patch → exact dx, dy, dt → total cells (nx, ny) → CFL timestep
   - **Resource estimate**: estimated node count × walltime, expected disk usage for diagnostics
   - **Diagnostics list**: which Diag types, output fields, every interval, time selection if any
   - **Post-processing plan**: which physical quantities to verify, what plots to generate

5. **Submit `design_outline.md` to user for review. Wait for approval.**

**Deliverable**: `design_outline.md`

---

## Stage 2: Write & Validate

**Goal**: Write the namelist and post-processing notebook, validate syntax.

**Steps**:
1. Write `data/input.py` following the approved design outline, strictly using the NOTES/bootstrap.md four-step grid workflow and no-magic-numbers convention
2. Write `post/post.ipynb` — at minimum: open simulation with happi, read namelist parameters, read one diagnostic to verify data access works
3. Run `smilei_test input.py` — fix any errors until it passes
4. **Submit `input.py` and `post.ipynb` to user for review. Wait for approval.**

**Deliverables**: `data/input.py`, `post/post.ipynb`

---

## Stage 3: Submit & Run

**Goal**: Submit the simulation to the cluster with appropriate resource configuration.

**Steps**:
1. Run `squeue` to check cluster load and available nodes
2. Adjust `#SBATCH` parameters (nodes, ntasks-per-node, time) based on resource estimate from Stage 1 and current cluster availability
3. Write `submit_array.job` (or `submit.sh` for a single run), following NOTES/slurm/ patterns
4. `sbatch submit_array.job` — record the job ID
5. **Exit the task.** Inform user of job ID and estimated completion time. The user will restart the conversation when the simulation is done.

**Deliverable**: `submit_array.job` (submitted), job ID recorded

---

## Stage 4: Post-process & Analyze

**Goal**: Analyze simulation output and verify physical results.

**Steps**:
1. Verify output file integrity in `data/`: Fields*.h5 present, check scalars.txt for energy conservation
2. Check simulation log for warnings or errors
3. Complete `post/post.ipynb`: add analysis cells for each verification item from the design outline, generate plots to `result/`
4. Run all cells and verify:
   - Key physical quantities match expectations (within reasonable tolerance)
   - No numerical artifacts (boundary reflections, self-heating, etc.)
5. If any issue is found, document it in the relevant NOTES/ file for future reference

**Deliverable**: `post/post.ipynb` (completed), plots in `result/`

---

## Stage 5: Simulation Report

**Goal**: Produce a comprehensive, standalone simulation report.

**Steps**:
1. Write `report.md` containing:
   - **Overview**: physics objective and key parameters table
   - **Grid & resources**: final grid dimensions, patch configuration, nodes used, walltime
   - **Results**: key diagnostic plots with physical interpretation
   - **Verification checklist**: each item from Stage 1 design outline, pass/fail status
   - **Issues & notes**: anomalies found, improvements for future runs
2. **Submit `report.md` to user for review.**

**Deliverable**: `report.md`

---

## Project Directory Convention

```
<simulation_name>/
├── design_outline.md       # Stage 1
├── data/
│   └── input.py            # Stage 2
├── post/
│   └── post.ipynb          # Stage 2 & 4
├── submit_array.job        # Stage 3
├── result/                 # Stage 4 output
└── report.md               # Stage 5
```

## Stage Gates

| Stage | Gate | Deliverable |
|-------|------|-------------|
| 1 → 2 | `design_outline.md` approved | `design_outline.md` |
| 2 → 3 | `input.py` + `post.ipynb` approved | `input.py`, `post.ipynb` |
| 3 → 4 | Job completes (user restarts) | `submit_array.job`, job ID |
| 4 → 5 | Analysis results reviewed | `post.ipynb` (completed) |
| 5 → done | `report.md` approved | `report.md` |
