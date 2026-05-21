# Slurm Submission Flow

## Wrapper: `submit.sh`

自动创建 logs 目录后提交作业:

```bash
#!/bin/bash
SLURM_SCRIPT="submit_array.job"
LOG_DIR="logs"

if [ ! -d "$LOG_DIR" ]; then
    mkdir -p "$LOG_DIR"
fi

if [ ! -f "$SLURM_SCRIPT" ]; then
    echo "错误: 未找到作业脚本 $SLURM_SCRIPT"
    exit 1
fi

sbatch "$SLURM_SCRIPT"
echo "已提交。使用 squeue 查看状态，日志在 $LOG_DIR/"
```

## Cleanup: `clean.sh`

```bash
#!/bin/bash
LOG_DIR="logs"
if [ -d "$LOG_DIR" ]; then
    rm -f $LOG_DIR/*.out $LOG_DIR/*.err
    echo "清理完成。"
fi
```

## MPI Configuration

- 使用 `mpirun -np $SLURM_NTASKS`（不是 `srun`）
- OpenMPI 2.x 不稳定时加 `--mca btl ^vader`
- Smilei `number_of_patches` 应能被 MPI 进程数整除
- 每节点 `ntasks-per-node=2`, `cpus-per-task=28` → 充分利用 56 核
- Smilei GPU 版本需额外 binding script，联系管理员
