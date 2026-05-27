# Project Conventions

## Directory Layout

- Simulation data is stored in `../data` (relative to namelist)
- Post-processing output images go to `./result`
- Original data is typically read from `"../data"` folder

## Multi-frame GIF

When generating multi-frame GIFs:
1. Use multiprocessing for frame generation
2. Save each frame to a temporary folder under current directory
3. Combine all frames into a single GIF
4. Delete the temporary folder afterwards

## Server-side Post-processing

- Smilei happi cannot display plots or GIFs on the server
- Post-processing workflow: use happi to export raw data arrays, then write custom scripts for processing and visualization
- Do NOT use `matplotlib.use('Agg')` in scripts — handle backend externally

## Jupyter 路径规则

**在 Jupyter notebook 中，所有相对路径都是相对于 .ipynb 文件所在目录**（不是你的终端路径，也不是 kernel 的工作目录）。

例如 `post/post.ipynb` 中：
- `../data` → `post/../data` = 项目根目录 `data/` ✓
- `post/results/...` → `post/post/results/...` ✗ **错误！** 会创建多余子目录
- `results/...` → `post/results/...` ✓ 正确

**经验法则：** 站在 `.ipynb` 文件的位置写相对路径，不要前缀 notebook 所在的目录名。
