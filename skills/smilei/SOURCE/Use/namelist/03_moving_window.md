# Moving Window

## Block: MovingWindow

### 概述
模拟窗口可跟随等离子体或波高速移动。通过在 `x_max` 方向周期性移除 `x_min` 边界处的 patch 并在 `x_max` 后添加新 patch，保持 box 大小不变但改变物理域。窗口移动频率自动调整以匹配用户指定的平均速度。

该 block 是可选的。不定义则窗口不移动。

> **Warning:** 窗口开始移动后，所有通过 Silver-Muller 边界条件的激光注入会立即停止，以保证物理正确性。

### 属性速查表

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| time_start | float | 必填 | 窗口开始移动的时间 (\(T_r\)) |
| velocity_x | float | 必填 | 窗口在 `x_max` 方向的平均速度，范围 [0, 1] (\(c\)) |
| number_of_additional_shifts | int | 必填 | 额外移动步数 |
| additional_shifts_time | float | 必填 | 执行额外移动的时间 (\(T_r\)) |

> **Note:** 额外移动不计入平均速度评估。ParticleBinning 诊断支持 `moving_x` 轴（x 坐标经移动窗口校正）。

### 代码示例
```python
MovingWindow(
    time_start = 0.,
    velocity_x = 1.,
    number_of_additional_shifts = 0,
    additional_shifts_time = 0.,
)
```
