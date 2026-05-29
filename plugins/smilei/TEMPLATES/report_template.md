# {PROJECT_NAME} 模拟报告

## 1. 概述

### 物理目标

{PHYSICS_OBJECTIVE}

### 关键参数

| 参数 | 值 |
|------|-----|
| 模拟区域 | {LX} × {LY} µm |
| 分辨率 | {DX} µm |
| 模拟时长 | {SIM_TIME} fs |
| 激光强度 | {I0} W/cm² |
| 靶材 | {MATERIAL}, Z={Z} |

## 2. 网格与资源

| 参数 | 值 |
|------|-----|
| 网格数 | {NX} × {NY} |
| Patch数 | {NPX} × {NPY} |
| 节点数 | {NODES} |
| 运行时间 | {WALLTIME} |

## 3. 结果

### 3.1 场分布

{FIELD_RESULTS}

### 3.2 粒子动力学

{PARTICLE_RESULTS}

### 3.3 能量守恒

{ENERGY_RESULTS}

## 4. 验证清单

| 验证项目 | 状态 | 说明 |
|----------|------|------|
| 能量守恒 | {STATUS} | |
| 动量守恒 | {STATUS} | |
| 激光传播 | {STATUS} | |
| 密度分布 | {STATUS} | |
| 粒子加速 | {STATUS} | |

## 5. 问题与改进

{ISSUES_AND_IMPROVEMENTS}
