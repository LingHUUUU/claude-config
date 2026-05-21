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
