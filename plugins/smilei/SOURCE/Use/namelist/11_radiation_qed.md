# Radiation Reaction & Multiphoton Breit-Wheeler

## Block: RadiationReaction

### 概述
配置辐射损失参数和 Monte-Carlo 光子发射的截面表。若表已存在于模拟目录中，Smilei 直接读取；否则生成新表。默认表内嵌于代码中，外部表可用 `smilei_tables` 工具生成。

参考：[High-energy photon emission & radiation reaction](../Understand/radiation_loss.html), [External tables](tables.html)

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| minimum_chi_continuous | float | `1e-3` | 粒子量子参数 `particle_chi` 阈值。低于此值不考虑辐射反作用 |
| minimum_chi_discontinuous | float | `1e-2` | 连续与不连续辐射模型之间的 `particle_chi` 阈值 |
| table_path | str | `""` | 外部辐射损失表目录路径。空则使用内嵌默认表 |
| Niel_computation_method | str | `"table"` | Niel 等人的 h 函数计算方法（见下方） |

### `Niel_computation_method` 选项

| 值 | 说明 |
|----|------|
| `"table"` | 表查询（精度最高，但阻止完全向量化） |
| `"fit5"` | 5 阶多项式拟合。最大相对误差 0.02，\(\chi \in [10^{-3}, 10]\) |
| `"fit10"` | 10 阶多项式拟合。最大相对误差 0.0002，\(\chi \in [10^{-3}, 10]\) |
| `"ridgers"` | Ridgers et al., ArXiv 1708.04511 (2017) 的拟合 |

> **Note:** 表查询精度最高但性能较差（阻止向量化）；拟合方法可向量化。

### 代码示例
```python
RadiationReaction(
    minimum_chi_continuous = 1e-3,
    minimum_chi_discontinuous = 1e-2,
    table_path = "",
    Niel_computation_method = "table",
)
```

---

## Block: MultiphotonBreitWheeler

### 概述
配置多光子 Breit-Wheeler 对产生过程的参数和表生成。涉及三张表：`integration_dT_dchi`、`min_particle_chi_for_xi` 和 `xi`。

参考：[Multiphoton Breit-Wheeler pair creation](../Understand/multiphoton_Breit_Wheeler.html)

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| table_path | str | `""` | 外部 Breit-Wheeler 表目录路径。空则使用内嵌默认表 |

### 代码示例
```python
MultiphotonBreitWheeler(
    table_path = "",
)
```
