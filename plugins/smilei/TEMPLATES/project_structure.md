# Smilei Project Directory Structure

## Standard Layout

```
<project_name>/
├── Claude.md                    # 项目物理参数规范（可选）
├── <case_name>/                 # 工况目录（可多个）
│   ├── data/
│   │   └── input.py             # Smilei namelist
│   ├── post/
│   │   ├── post.ipynb           # 后处理 notebook
│   │   └── result/              # 后处理输出图片
├── article/                     # 参考文献
├── submit/
│   ├── submit_array.job         # Slurm 提交脚本
│   └── logs/                    # 作业日志
└── reminder/
    ├── logs.md                  # 运行日志
    └── reminder.md              # 提醒事项
```

## Naming Convention

- **Project directory**: `YYYYMMDD_topic` (e.g., `20260527_双色光快点火`)
- **Case directories**: descriptive names (e.g., `I1_100`, `I1_30_I2_65`)
- Use underscore `_` as separator, avoid spaces

## Directory Purposes

| Directory | Purpose |
|-----------|---------|
| `data/` | Contains `input.py` namelist, simulation input files |
| `post/` | Contains `post.ipynb` for analysis, `result/` for output plots |
| `article/` | Reference papers and literature |
| `submit/` | Slurm job scripts, submission logs |
| `reminder/` | Project notes, running logs, reminders |

## Example: Two-Case Study

```
dual_laser_study/
├── case_fundamental/
│   ├── data/
│   │   └── input.py
│   └── post/
│       ├── post.ipynb
│       └── result/
├── case_dual_color/
│   ├── data/
│   │   └── input.py
│   └── post/
│       ├── post.ipynb
│       └── result/
├── submit/
│   └── submit_array.job
└── reminder/
    └── logs.md
```
