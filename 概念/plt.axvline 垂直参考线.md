---
term: plt.axvline 垂直参考线
aliases: [axvline, plt.axvline(), 垂直参考线, 竖线函数]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E25 · 填充"
order: 74
created: 2026-11-17
updated: 2026-11-17
---

# plt.axvline 垂直参考线

> 别名：axvline、plt.axvline()、垂直参考线、竖线函数

**在指定 x 坐标处绘制一条贯穿绘图区的垂直参考线。**

## 解释

axvline 与 axhline 成对使用，h 表示 horizontal、v 表示 vertical；调用时只需给出 x 轴位置，线在 y 方向自动贯穿整个绘图区。它常用来标记阈值、时间点或分类分界。

## 有什么用

- 标记某个 x 值对应的阈值、事件时间点
- 在图中添加垂直分界线或参考线

## 关键要点

- 用 x 参数指定竖线位置，如 plt.axvline(x=0.4)
- 命名与 axhline 对应：h 横线、v 竖线
- 支持 linewidth、color 等线条样式参数
- 默认贯穿整个绘图区，不是局部线段

## 边界与易混淆

竖线位置看 x 轴；不要和 axhline 的 y 参数混淆。

## 关联

- [[plt.axhline 水平参考线]] — 对比项
- [[linewidth 线宽参数]] — 组合使用
- [[Matplotlib 颜色简写]] — 组合使用

## 自测

axvline 需要指定哪个坐标参数？::x 轴坐标，例如 x=0.4。
如果要在 y=0.2 处画横线，应该用 axvline 还是 axhline？::axhline，因为横线由 y 定位。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p74 S03E25.填充](https://www.bilibili.com/video/BV1ji4y157uB?p=74) · 2026-11-17
