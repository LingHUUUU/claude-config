# Slurm Array Job

## Standard Template

```bash
#!/bin/bash
#SBATCH --job-name=yjjia
#SBATCH --partition=cu              # 集群分区
#SBATCH --nodes=6                   # 节点数
#SBATCH --ntasks-per-node=2         # 每节点 MPI 进程数 (2 tasks × 28 cores)
#SBATCH --cpus-per-task=28          # 每进程 OpenMP 线程数
#SBATCH --time=7-24:00:00           # D-HH:MM:SS, 长任务给足时间
#SBATCH --array=0-4                 # 数组: 0..4 共 5 个 task
#SBATCH --output=logs/array_%A_%a.out
#SBATCH --error=logs/array_%A_%a.err

SMILEI_EXE=smilei
export OMP_SCHEDULE=dynamic

DIRS=(
    "/path/to/sim1/data"
    "/path/to/sim2/data"
    # ... 按索引与 array task ID 一一对应
)

TARGET_DIR=${DIRS[$SLURM_ARRAY_TASK_ID]}

if [ -d "$TARGET_DIR" ]; then
    cd "$TARGET_DIR"
    mpirun -np $SLURM_NTASKS $SMILEI_EXE input.py
else
    echo "Directory $TARGET_DIR does not exist."
    exit 1
fi
```

## Key Techniques

1. **Array job 参数扫描**: `--array=0-4` 对应 `DIRS` 中 5 个目录
2. **单任务模式**: `--array=0` 配合只含一个元素的 `DIRS`
3. **资源配比**: `nodes × ntasks-per-node = 总MPI进程`, `ntasks-per-node × cpus-per-task ≤ 每节点核心数 (56)`
4. **排除问题节点**: `--exclude=cu[02]` 跳过 cu02
5. **OpenMP 调度**: `export OMP_SCHEDULE=dynamic` 避免线程竞争
6. **日志命名**: `%A` = 主 job ID, `%a` = array task ID
7. **长任务**: `--time=7-24:00:00` 表示 7 天 24 小时，确保不被提前 kill
8. **Smilei patch 约束**: `number_of_patches` 必须能被 MPI 进程数整除
