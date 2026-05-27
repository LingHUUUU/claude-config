# Smilei Skill - Templates Index

> This file provides templates for creating new Smilei simulation projects. Referenced from SKILL.md when user requests project creation.

---

## Project Structure

| Template | File | Description |
|----------|------|-------------|
| Project Layout | [project_structure.md](project_structure.md) | Standard directory structure for Smilei projects |
| Input Namelist | [input_template.py](input_template.py) | Template for Smilei input.py |
| Post-processing | [post_template.ipynb](post_template.ipynb) | Template for post.ipynb with happi |
| Slurm Submit | [submit_template.sh](submit_template.sh) | Template for Slurm job submission |
| Design Outline | [design_outline_template.md](design_outline_template.md) | Template for design_outline.md |
| Report | [report_template.md](report_template.md) | Template for report.md |

---

## Usage

When user says "创建项目", "新建模拟", "项目模板", or "init project":

1. Show user the [project_structure.md](project_structure.md) to confirm layout
2. Create directories based on project_structure.md
3. Copy and customize templates as needed:
   - `input_template.py` → `data/input.py` (modify physics parameters)
   - `post_template.ipynb` → `post/post.ipynb` (modify diagnostic names)
   - `submit_template.sh` → `submit_array.job` (modify resource allocation)
   - `design_outline_template.md` → `design_outline.md` (fill in design details)
   - `report_template.md` → `report.md` (fill in results)

---

## Current Project Reference

For a working example, see `/public/home/jiayijie/Projs/26_sim/20260527_双色光快点火/`
