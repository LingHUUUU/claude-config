# Load Balancing, SDMD & Vectorization

## Block: LoadBalancing

### 概述
动态负载均衡：在 MPI 进程间交换 patch 以减少计算负载不平衡。该 block 是可选的；不定义则默认每 150 个 timestep 执行一次负载均衡。

参考：[Load balancing algorithm](../Understand/parallelization.html#loadbalancingexplanation)

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| initial_balance | bool | `True` | 初始化时是否均衡负载。若 `False`，每个 MPI rank 分配相同数量的 patch |
| every | int / time selection | `150` | 两次负载均衡之间的 timestep 数。`0` 表示禁用所有负载均衡 |
| cell_load | float | 必填 | 单个网格单元的计算负载权重（归一化到单个粒子的负载） |
| frozen_particle_load | float | `0.1` | 单个冻结粒子的计算负载权重（归一化到单个粒子的负载） |

### 代码示例
```python
LoadBalancing(
    initial_balance = True,
    every = 150,
    cell_load = 1.,
    frozen_particle_load = 0.1
)
```

---

## Block: MultipleDecomposition

### 概述
Single-domain Multiple Decompositions (SDMD) 技术：将场网格的分解与粒子的分解分离。场分配在大子域（region，每个 MPI 进程 1 个），粒子保持在标准分解的小 patch 中（每个 MPI 进程多个 patch）。谱求解器必需，其他情况可选。

参考：[SDMD paper](https://hal.archives-ouvertes.fr/hal-02973139)

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| region_ghost_cells | int | `2`（根据 `interpolation_order` 自动设置） | 每个 region 的 ghost cell 数。所有维度使用相同数量（AM 几何谱求解器除外：径向 ghost cell 数始终自动等于 patch 大小） |

### 代码示例
```python
MultipleDecomposition(
    region_ghost_cells = 2
)
```

---

## Block: Vectorization

### 概述
控制 SIMD 向量化操作以提升计算性能。需要额外的编译选项。超过 ~10 ppc 时推荐使用。

参考：[Vectorization technique](../Understand/vectorization.html), [[Beck2019]](../Overview/material.html#beck2019)

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| mode | str | `"off"` | `"off"`: 标量操作（ppc < 10 推荐）。`"on"`: 向量化操作（ppc > 10 推荐，粒子按 cell 排序）。`"adaptive"`: 动态选择最佳模式（仅 `3Dcartesian`，粒子按 cell 排序）。自适应模式自动将 `cluster_width` 设为最大值 |
| reconfigure_every | int / time selection | `20` | 自适应模式下重新配置向量化算子的 timestep 间隔 |
| initial_mode | str | `"off"` | 自适应模式激活且 patch 中无粒子时的默认状态 |

### 代码示例
```python
Vectorization(
    mode = "adaptive",
    reconfigure_every = 20,
    initial_mode = "on"
)
```
