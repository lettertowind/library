---
term: np.degrees
aliases: [degrees, 弧度转角度, rad2deg]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# np.degrees

> 别名：degrees、弧度转角度、rad2deg

**把弧度值按比例换算成角度值的 NumPy 函数。**

## 用法
**语法**：`np.degrees(x, /, out=None, *, where=True)`
**参数**：
- `x`：输入弧度值，可以是标量或数组（array_like），会按元素逐个换算
- `out`：可选，指定用于存放结果的数组；指定后就地写入，并返回该数组
- `where`：可选，布尔数组或条件，为 True 的位置才参与计算

**示例**：
```python
import numpy as np

# 标量：π/2 弧度 = 90 度
print(np.degrees(np.pi / 2))        # 90.0

# 数组：批量换算，无需循环
angles = np.linspace(0, 2 * np.pi, 5)
print(np.degrees(angles))           # [  0.  90. 180. 270. 360.]

# 与 np.radians 互为逆运算
print(np.radians(np.degrees(angles)))  # [0.  1.5708 3.1416 4.7124 6.2832]
```

## 解释

NumPy 三角函数与极坐标相关参数都以弧度为单位，而人类展示和部分 API（如 thetagrids）按度数工作。np.degrees 就是做 rad × 180/π 的向量化换算，与 np.radians 互为逆运算。

## 有什么用

- 雷达图设置角度标签前转换单位
- 任何需要把弧度结果展示成度数的场景

## 关键要点

- 换算公式：degrees = rad × 180 / π
- np.pi 对应 180°，2*np.pi 对应 360°
- 对数组成批换算，不需写循环
- 与 np.radians 互为逆运算

## 边界与易混淆

只做单位换算，不改变数据本身含义；混淆弧度和度数导致刻度错位是最常见错误。

## 关联

- [[np.linspace]] — 前置知识
- [[set_thetagrids 角度标签网格]] — 组合使用

## 自测

np.degrees(np.pi/2) 结果是多少？::90，因为 π/2 弧度即 90 度。
为什么不直接用角度生成 linspace 而要先弧度后转换？::Matplotlib 极坐标内部按弧度计算位置，绘图必须传弧度；只在设置标签文字时才转成度数。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p71 S03E22.雷达图](https://www.bilibili.com/video/BV1ji4y157uB?p=71) · 2026-11-17
