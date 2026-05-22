# Namelist Bootstrap

## 核心原则: 只写公式, 不硬编码数字

- **设计大纲和正式代码中, 所有数值必须通过公式导出, 严禁 magic numbers。**
- 唯一的例外: 物理学常数 (c, e, m_e, ε₀ 等) 和纯数学常数 (π)。
- 每个参数旁边用注释标注公式 → 数值, 例如: `dx = Lx / Nx  # = 251.33/1280 = 0.19635 Lr`
- 好处: 参数可追溯、可验证、修改一处自动传播。

## Standard Unit Conversion

```python
import math
import numpy as np

# --- 1. Basic physics parameters & unit conversion ---
lambda0 = 0.8e-6
c = 299792458.0
omega0 = 2.0 * math.pi * c / lambda0

# Smilei normalization references
Tr = 1.0 / omega0
Lr = c / omega0

# Unit conversion factors
um = 1.0e-6 / Lr
fs = 1.0e-15 / Tr
ps = 1.0e-12 / Tr
```

- Frequencies in units of omega0, lengths in Lr, times in Tr
- Velocities in units of c, densities in units of critical density nc
- `reference_angular_frequency_SI = omega0` must be set in Main()

## Variable Naming Convention

- Smilei has NO predefined convenience variables (unlike EPOCH's `micron`, `femto`, etc.)
- Define ALL quantities from first principles — use `um`, `fs`, `ps` conversion factors
- Define SI values first, then convert to Smilei normalized units

## Grid & Patch Alignment Workflow

**标准流程: 定义 target_dx → 计算精确 Nx/Ny → 用 `number_of_cells` 传入 Smilei。**

```python
# 1. 定义空间范围和目标分辨率
Lx = 40.0 * um           # 模拟盒长度
Ly = 32.0 * um
target_dx = (1.0/32.0) * um   # 目标格点尺寸

# 2. 定义 patch 数 (2 的幂)
npx, npy = 8, 8

# 3. 计算精确格点数 (整数部分, 保证整除 patch 数)
Nx = int(Lx / target_dx / npx) * npx
Ny = int(Ly / target_dx / npy) * npy

# 4. 反推精确格点尺寸和步长
dx = Lx / Nx
dy = Ly / Ny
```

**为什么用 `number_of_cells` 而不是 `cell_length`**:
- 传入 `cell_length` 时, Smilei 内部做 `cells = grid_length / cell_length`, 浮点精度可能导致格点数漂移 (如 1280.003 → 1281 → 对齐后变 1344)
- 传入 `number_of_cells` 直接锁死格点数, Smilei 据此反算 cell_length, 无漂移风险
- Main 块中同时传入 `grid_length` 和 `number_of_cells`, 不传 `cell_length`

```python
Main(
    grid_length     = [Lx, Ly],
    number_of_cells = [Nx, Ny],
    number_of_patches = [npx, npy],
    ...
)
```

### 约束条件
- `number_of_patches` 必须是 2 的幂
- `Nx % npx == 0` 且 `Ny % npy == 0` (由上述公式自动保证)
- CFL 公式 2D: `dt = 0.95 / sqrt(1/dx^2 + 1/dy^2)`

## Density Profiles

- Normalize to critical density `nc`
- Use Python functions for complex profiles (ramps, cones, masks)
- `number_density = my_profile` where profile is defined above Main()
- Common patterns: uniform slab, exponential ramp, cone mask with conditionals
