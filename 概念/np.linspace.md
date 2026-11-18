---
term: np.linspace
aliases: [linspace, 等间距生成, 线性等分]
kind: method
domain: Numpy
tags: [概念/method, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
---

# np.linspace

> 别名：linspace、等间距生成、线性等分

**在指定区间内按等间距生成指定个数数值的 NumPy 函数。**

## 用法

**语法**：`np.linspace(start, stop, num=50, endpoint=True)`
**参数**：
- `start`：区间起点，作为第一个输出值
- `stop`：区间终点；`endpoint=True` 时，这个值会作为最后一个输出值
- `num`：生成的元素个数，默认为 50；在需要与数据条数一一对应时，务必显式传入 `len(数据)`
- `endpoint`：是否包含终点，默认为 `True`；设为 `False` 时，步长为 `(stop-start)/num`，并且不包含 `stop`，因此常用来生成极坐标角度，避免 0 与 2π 重合
**示例**：
```python
import numpy as np

# endpoint=False：4 个角度均分一整圈，不含 2π
angles = np.linspace(0, 2*np.pi, 4, endpoint=False)
print(angles.round(3))   # [0.    1.571 3.142 4.712]
print(len(angles))       # 4

# endpoint=True（默认）：包含终点
print(np.linspace(0, 1, 5))   # [0.   0.25 0.5  0.75 1.  ]
```

## 解释

np.linspace(start, stop, num, endpoint) 返回 num 个均匀分布的点。绘图时常用来把一整圈 2π 均分成若干角度，让每个分类占据一个位置。

## 有什么用

- 为极坐标图生成均匀角度
- 生成等距的坐标刻度或采样点

## 关键要点

- 三个核心参数：起点、终点、个数
- endpoint=False 表示不包含终点，为后续补首值闭合留位置
- 与 np.arange 区别：linspace 指定个数，arange 指定步长
- 个数通常取数据条数，保证角度与数据一一对应

## 边界与易混淆

endpoint 默认 True，画极坐标闭合图时必须显式改为 False，否则首尾角度会重复。

## 关联

- [[玫瑰图]] — 组合使用
- [[首尾闭合（封口）]] — 组合使用
- [[Numpy 切片]] — 对比项

## 自测

np.linspace(0, 2*np.pi, 20, False) 生成多少个角度、为什么不含终点？::生成 20 个角度，从 0 开始但不取 2π；终点位置留给补上来的第一个值，保证首尾重合。


### 补充 · 2026-11-17

linspace(start, stop, num) 返回 num 个均匀分布的点，常用于生成坐标轴刻度或极坐标角度。用 endpoint 控制是否包含终点，避免圆周首尾角度重复。

- 雷达图写法：np.linspace(0, 2*np.pi, len(科目), endpoint=False)
- 必须显式给 num，否则默认 50 个点，角度会远多于数据点
- endpoint=False 排除终点，防止 0 与 2π 两个角度重合
生成雷达图角度时漏写 len(科目) 会发生什么？::默认生成 50 个角度，与 5 个维度的数据长度不匹配，图形完全错乱。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p71 S03E22.雷达图](https://www.bilibili.com/video/BV1ji4y157uB?p=71) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p79 S03E30.玫瑰图](https://www.bilibili.com/video/BV1ji4y157uB?p=79) · 2026-11-17
