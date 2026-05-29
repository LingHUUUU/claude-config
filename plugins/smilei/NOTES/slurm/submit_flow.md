# Slurm Submission Flow

## 目录规范

- Slurm 脚本放在 `项目/submit/` 目录下
- **日志目录必须先于提交创建**: `mkdir -p 项目/submit/logs/`
- 原因: Slurm 在 `sbatch` 提交时解析 `--output/--error` 路径, 目录不存在则日志写入失败, 作业静默 FAILED (exit code 1:0, 无任何输出)
- 脚本中 `--output/--error` 路径写为 `submit/logs/...` (相对于项目根目录)

## 目录结构

```
project/
├── submit/
│   ├── logs/              # mkdir -p 先创建, 再 sbatch
│   └── submit_array.job
├── case1/
├── case2/
└── ...
```

## Array Job 模板

```bash
#!/bin/bash
#SBATCH --job-name=job_name
#SBATCH --partition=cu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=28
#SBATCH --time=5:00:00
#SBATCH --array=0-3
#SBATCH --output=submit/logs/array_%A_%a.out
#SBATCH --error=submit/logs/array_%A_%a.err

SMILEI_EXE=smilei
export OMP_SCHEDULE=dynamic
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

CASES=("S1" "S2" "D1" "D2")
DIRS=("case1" "case2" "case3" "case4")
CASE=${CASES[$SLURM_ARRAY_TASK_ID]}
TARGET_DIR=${DIRS[$SLURM_ARRAY_TASK_ID]}
BASE_DIR=/path/to/project

if [ -d "$BASE_DIR/$TARGET_DIR" ]; then
    cd "$BASE_DIR/$TARGET_DIR"
    echo "=== Case: $CASE ==="
    echo "Start: $(date)"
    mpirun -np $SLURM_NTASKS $SMILEI_EXE input.py "case='$CASE'"
    echo "Done: $(date)"
else
    echo "Directory $BASE_DIR/$TARGET_DIR does not exist."
    exit 1
fi
```

## MPI 配置

- 使用 `mpirun -np $SLURM_NTASKS` (**不是 `srun`**)
- OpenMPI 2.x 不稳定时加 `--mca btl ^vader`
- Smilei `number_of_patches` 应能被 MPI 进程数整除
- 每节点 `ntasks-per-node=2`, `cpus-per-task=28` → 充分利用 56 核
- Smilei GPU 版本需额外 binding script, 联系管理员
