# Probe Diagnostics

## Block: DiagProbe

### 概述
在任意位置（非 PIC 网格点）插值获取场数据。支持 0-D（单点）、1-D（线）、2-D 或 3-D 网格。Probe 使用粒子插值器计算场，因此磁场相比 Fields 诊断有半个 timestep 的偏移。

> **Note:** Probe 跟随移动窗口。如需获取等离子体中固定位置的场，创建冷、无电荷物种并 [追踪其粒子](#diagtrackparticles)。

> **Note:** AMcylindrical 中 Probe 定义为 3D Cartesian 坐标，不能按 mode 分离。使用 Field 诊断获取柱坐标和按 mode 的信息。

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| name | str | None | 诊断名称（仅后处理用） |
| every | int / time selection | 必填 | 输出间隔（timestep） |
| flush_every | int / time selection | `1` | 文件刷新间隔。刷新过频繁会严重拖慢模拟 |
| origin | list[float] | 必填 | Probe 网格原点坐标（长度 = 模拟维度） |
| corners | list[list[float]] | 与 `vectors` 二选一 | 绝对坐标定义的 probe 网格角点 |
| vectors | list[list[float]] | 与 `corners` 二选一 | 相对于 `origin` 的坐标定义 probe 网格 |
| number | list[int] | 0-D probe 不定义 | 每个 probe 轴的采样点数（每个维度一个整数） |
| fields | list[str] | `[]`（= 全部 10 个默认场） | 输出场列表（见下方） |
| time_integral | bool | `False` | 若 `True`，输出对时间积分。会强制每个 timestep 插值，建议减少 probe 点数 |
| datatype | str | `"double"` | 数据类型: `"double"` (8 bytes) 或 `"float"` (4 bytes) |

### 可用 `fields`

默认（`[]`）输出全部: `"Ex"`, `"Ey"`, `"Ez"`, `"Bx"`, `"By"`, `"Bz"`, `"Jx"`, `"Jy"`, `"Jz"`, `"Rho"`

额外可选:
- `"PoyX"`, `"PoyY"`, `"PoyZ"` — Poynting 矢量分量
- `"Jx_abc"`, `"Jy_abc"`, `"Jz_abc"`, `"Rho_abc"` — 物种 "abc" 的电流/电荷密度
- Envelope 模型: `"Env_Chi"`, `"Env_A_abs"`, `"Env_E_abs"`, `"Env_Ex_abs"`
- B-TIS3: `"ByBTIS3"`, `"BzBTIS3"`

### 示例

**0-D probe（1D 模拟）：**
```python
DiagProbe(every=1, origin=[1.2])
```

**1-D probe（1D 模拟）：**
```python
DiagProbe(every=1, origin=[1.2], corners=[[5.6]], number=[100])
```

**1-D probe（2D 模拟）：**
```python
DiagProbe(every=1, origin=[1.2, 4.], corners=[[5.6, 4.]], number=[100])
```

**2-D probe（2D 模拟）：**
```python
DiagProbe(every=1, origin=[0., 0.], corners=[[10.,0.], [0.,10.]], number=[100, 100])
```

### 代码示例
```python
DiagProbe(
    every = 10,
    origin = [1., 1.],
    corners = [[1.,10.], [10.,1.]],
    number = [100, 100],
    fields = ["Ex", "Ey", "Ez"]
)
```
