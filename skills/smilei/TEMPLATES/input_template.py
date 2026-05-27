#!/usr/bin/env python3
"""
{CASE_NAME}: {DESCRIPTION}
=============================================
Smilei namelist for {PROJECT_NAME}
"""

# ============================================================
# 1. Physical Constants & Normalization
# ============================================================
import math
import numpy as np

# SI Constants
c_SI = 299792458.0              # speed of light [m/s]
m_e_SI = 9.10938e-31            # electron mass [kg]
e_SI = 1.602176634e-19          # elementary charge [C]
epsilon_0_SI = 8.8541878128e-12 # vacuum permittivity [F/m]

# Reference laser parameters
lambda0 = 1.0e-6                # fundamental wavelength [m]
omega0 = 2.0 * math.pi * c_SI / lambda0  # reference angular frequency [rad/s]
T_omega = 2.0 * math.pi / omega0         # fundamental period [s]

# Smilei normalization units
Lr = c_SI / omega0              # length normalization = lambda0/(2*pi) [m]
Tr = 1.0 / omega0               # time normalization [s]

# Unit conversion factors
um = 1.0e-6 / Lr                # 1 µm in normalized units
fs = 1.0e-15 / Tr               # 1 fs in normalized units

# ============================================================
# 2. Grid & MPI/Patch Configuration
# ============================================================
# Physical domain size
Lx = {LX} * um                  # {LX} µm in x
Ly = {LY} * um                  # {LY} µm in y

# Target resolution
target_dx = {DX} * um           # {DX} µm

# MPI/Patch configuration (must be power of 2)
npx = {NPX}                     # patches in x
npy = {NPY}                     # patches in y

# Calculate exact grid points (ensure divisibility by patch count)
Nx = int(Lx / target_dx / npx) * npx
Ny = int(Ly / target_dx / npy) * npy

# Actual grid spacing (recalculate for precision)
dx = Lx / Nx                    # exact spacing in x
dy = Ly / Ny                    # exact spacing in y

# Time step (CFL condition for 2D: dt = 0.95 / sqrt(1/dx^2 + 1/dy^2))
dt = 0.95 / math.sqrt(1.0 / dx**2 + 1.0 / dy**2)

# Simulation duration
simulation_time = {SIM_TIME} * fs   # {SIM_TIME} fs

# ============================================================
# 3. Laser Parameters
# ============================================================
# Peak intensity
I0 = {I0}                       # [W/cm²]
I18 = I0 / 1.0e18               # normalized to 10^18 W/cm²

# Laser parameters
sigma = {SIGMA} * um            # waist radius (1/e field)
tau = {TAU} * fs                # pulse duration

# Convert intensity to normalized vector potential a0
# Formula: a0 = 0.855 * lambda[µm] * sqrt(I[W/cm²] / 1e18)
a0 = 0.855 * 1.0 * math.sqrt(I18)

# ============================================================
# 4. Plasma Target Parameters
# ============================================================
# Material: {MATERIAL} with Z={Z}
Z_ion = {Z}
mass_ion = {MASS} * 1836.0      # mass in units of electron mass

# Initial temperature
Te = {TE_eV} / 511.0e3          # {TE_eV} eV in m_e c^2 units
Ti = {TI_eV} / 511.0e3          # {TI_eV} eV in m_e c^2 units

# Density profile parameters
x0 = {X0} * um                  # plasma left boundary
L_scale = {L_SCALE} * um        # density scale length
x2 = {X2} * um                  # plateau end

n_min = {N_MIN}                 # minimum density [n_c]
n_max = {N_MAX}                 # maximum density [n_c]

# Calculate ramp end point
x1 = x0 + L_scale * math.log(n_max / n_min)

# Check if x1 > x2 (ramp truncated before reaching n_max)
if x1 > x2:
    n_max_actual = n_min * math.exp((x2 - x0) / L_scale)
    print(f"Note: Ramp truncated at x2={x2/Lr*1e6:.2f} µm, actual n_max={n_max_actual:.2f} n_c")
else:
    n_max_actual = n_max

# ============================================================
# 5. Density Profile Function
# ============================================================
def n0_profile(x, y):
    """Density profile: exponential ramp + plateau + vacuum"""
    result = np.zeros_like(x)
    m1 = (x > x0) & (x < x1)
    m2 = (x >= x1) & (x < x2)
    result[m1] = n_min * np.exp((x[m1] - x0) / L_scale)
    result[m2] = n_max_actual
    return result

# ============================================================
# 6. Laser Envelope Functions
# ============================================================
def By_profile(y, t):
    """By component for laser (p-polarization, Ey field)"""
    spatial = np.exp(-(y - Ly/2)**2 / (2 * sigma**2))
    temporal = np.sin(np.pi * t / tau)**2 * (t >= 0) * (t <= tau)
    return a0 * spatial * temporal

def Bz_profile(y, t):
    """Bz component = 0 for linear p-polarization"""
    return np.zeros_like(y)

# ============================================================
# 7. Smilei Main Configuration
# ============================================================
Main(
    geometry = "2Dcartesian",
    interpolation_order = 2,
    grid_length = [Lx, Ly],
    number_of_cells = [Nx, Ny],
    number_of_patches = [npx, npy],
    timestep = dt,
    simulation_time = simulation_time,
    EM_boundary_conditions = [
        ["silver-muller", "silver-muller"],
        ["silver-muller", "silver-muller"]
    ],
    random_seed = 0,
    reference_angular_frequency_SI = omega0,
    print_every = 100,
)

# ============================================================
# 8. Laser Injection
# ============================================================
Laser(
    box_side = "xmin",
    space_time_profile = [By_profile, Bz_profile],
)

# ============================================================
# 9. Species Definition
# ============================================================
# Electrons
Species(
    name = "electron",
    position_initialization = "regular",
    momentum_initialization = "maxwell-juettner",
    particles_per_cell = {PPC},
    mass = 1.0,
    charge = -1.0,
    number_density = n0_profile,
    temperature = [Te],
    boundary_conditions = [
        ["remove", "remove"],
        ["remove", "remove"]
    ]
)

# Ions
Species(
    name = "{ION_NAME}",
    position_initialization = "regular",
    momentum_initialization = "maxwell-juettner",
    particles_per_cell = {PPC},
    mass = mass_ion,
    charge = Z_ion,
    number_density = lambda x, y: n0_profile(x, y) / Z_ion,
    temperature = [Ti],
    boundary_conditions = [
        ["remove", "remove"],
        ["remove", "remove"]
    ]
)

# ============================================================
# 10. Diagnostics
# ============================================================
# Output frequency: every {DIAG_TIME} fs
diag_every = int({DIAG_TIME} * fs / dt)

# Field diagnostics
DiagFields(
    every = diag_every,
    fields = [{FIELDS}],
)

# Scalar diagnostics
DiagScalar(every = diag_every)

# Particle tracking (optional)
# DiagTrackParticles(
#     species = "electron",
#     every = diag_every,
#     attributes = ["x", "y", "px", "py", "w", "id"]
# )

print(f"=== {CASE_NAME} Configuration Summary ===")
print(f"Domain: {Lx/um:.1f} x {Ly/um:.1f} µm")
print(f"Grid: {Nx} x {Ny} cells")
print(f"Resolution: {dx/Lr*1e9:.2f} nm")
print(f"Time step: {dt/Tr*1e18:.4f} as")
print(f"Simulation time: {simulation_time/fs:.0f} fs")
print(f"Laser a0: {a0:.3f}")
print(f"Peak intensity: {I0:.2e} W/cm²")
