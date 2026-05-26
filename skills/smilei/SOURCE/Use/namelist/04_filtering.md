# Filtering

## Block: CurrentFilter

### 概述
对电流密度应用多通二项式滤波器，减少 PIC 模拟中的高频数值噪声。

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| model | str | `"binomial"` | 滤波模型: `"binomial"` 或 `"customFIR"` |
| passes | list[int] | `[0]` | 每个维度的滤波通数。若列表长度为 1，所有维度使用相同值 |
| kernelFIR | list[float] | `[0.25, 0.5, 0.25]` | 仅 `"customFIR"` 模型。FIR 核系数，数量须小于 `custom_oversize` 指定的 ghost cell 数的两倍 |

### 代码示例
```python
CurrentFilter(
    model = "binomial",
    passes = [0],
    kernelFIR = [0.25, 0.5, 0.25]
)
```

---

## Block: FieldFilter

### 概述
对电磁场应用时间滤波。目前仅支持 Friedman 电场时间滤波方法。

参考：[E-field filter 算法](../Understand/algorithms.html#efieldfilter)

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| model | str | `"Friedman"` | 场滤波模型。目前仅可用 `"Friedman"` |
| theta | float | `0.` | Friedman 方法的 \(\theta\) 参数，取值范围 [0, 1] |

### 代码示例
```python
FieldFilter(
    model = "Friedman",
    theta = 0.,
)
```
