# Smilei Skill - Notes Index

> This file is read every time the skill is loaded. It provides quick reference and points to detailed notes organized by topic.

---

## Project Quick Reference

- **HPC**: Slurm partition `cu`, 2×28 CPUs/node
- **MPI**: `mpirun -np $SLURM_NTASKS smilei input.py`
- **Conda**: `conda activate pic`
- **Submit**: `submit_array.job` for array jobs, `submit.sh` for single
- **Data dir**: simulation data in `../data`, output images in `./result`

---

## Notes Index

### Namelist

| Topic | File | Content |
|-------|------|---------|
| Bootstrap & grid | [namelist/bootstrap.md](NOTES/namelist/bootstrap.md) | Unit conversion, grid/patch workflow, variable naming, density profiles |
| Particle init | [namelist/particle_init.md](NOTES/namelist/particle_init.md) | position_initialization modes, regular_number, square-number constraint |

### Slurm

| Topic | File | Content |
|-------|------|---------|
| Array job | [slurm/array_job.md](NOTES/slurm/array_job.md) | Array job template, parameter sweep, key techniques |
| Submission flow | [slurm/submit_flow.md](NOTES/slurm/submit_flow.md) | submit.sh, clean.sh, MPI configuration |

### Post-processing

| Topic | File | Content |
|-------|------|---------|
| Project conventions | [postprocessing/conventions.md](NOTES/postprocessing/conventions.md) | Directory layout, GIF workflow, server-side rendering |
| Happi tips | [postprocessing/happi_tips.md](NOTES/postprocessing/happi_tips.md) | Timestep lookup, Rho sign, getTimes/units, array indexing, transpose |
| TrackParticles | [postprocessing/track_particles.md](NOTES/postprocessing/track_particles.md) | Physical time → step conversion, sort=False fast read, nested dict structure |

### Gotchas

| Topic | File | Content |
|-------|------|---------|
| Common pitfalls | [gotchas/common.md](NOTES/gotchas/common.md) | Python overhead, test mode, hooks, BC tips |

---

## Skill Modification Rules

**Before modifying any file in this skill (SKILL.md, NOTES/, SOURCE/):**
1. Discuss the proposed change with the user first
2. Explain what you plan to add, modify, or delete and why
3. Wait for user approval before making changes
4. Do NOT unilaterally add or delete content — especially conclusions about physics or numerical behavior

---

## How to Add Notes

1. Find the right directory under `NOTES/` (or create a new one)
2. Write a markdown file with `# Title`
3. Add an entry to the index table above
4. Keep files focused: one topic per file. Files can be as long as needed to cover the topic thoroughly — do not artificially limit length at the cost of information loss.
