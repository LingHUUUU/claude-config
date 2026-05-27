#!/bin/bash
#SBATCH --job-name={JOB_NAME}
#SBATCH --partition=cu
#SBATCH --nodes={NODES}
#SBATCH --ntasks-per-node={NTASKS}
#SBATCH --time={WALLTIME}
#SBATCH --output=logs/%j.out
#SBATCH --error=logs/%j.err

# Load environment
module purge
source activate pic

# MPI configuration
export OMP_NUM_THREADS={OMP_THREADS}

# Run simulation
cd $SLURM_SUBMIT_DIR/../{CASE_DIR}/data
mpirun -np $SLURM_NTASKS smilei input.py

echo "Job completed at $(date)"
