---
term: set_axis_off
aliases: [plt.gca().set_axis_off(), 关闭坐标轴, 隐藏坐标轴]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E30 · 玫瑰图"
order: 79
created: 2026-11-17
updated: 2026-11-17
---

# set_axis_off

> 别名：plt.gca().set_axis_off()、关闭坐标轴、隐藏坐标轴

**关闭坐标轴外框、刻度与网格等全部装饰的坐标轴方法。**

## 解释

极坐标图默认带外圈圆、刻度和网格线，视觉上很杂。调用 ax.set_axis_off() 后这些元素全部隐藏，只剩图形本身；代价是失去了坐标参照，必须另加数据标签说明每个部分代表什么。

## 有什么用

- 让玫瑰图/极坐标图只保留图形本身
- 制作演示或海报式简洁图表

## 关键要点

- 通常先 plt.gca() 取当前轴，再链式调用 set_axis_off()
- 关闭后须用 plt.text 补数据标签，否则读者无法识别类别
- 与单独隐藏刻度的做法相比，它是整体关闭

## 边界与易混淆

会一并隐藏数值刻度，需要精确读数的场景不应使用。

## 关联

- [[plt.gca 与 plt.gcf]] — 组合使用
- [[plt.text 数据标签]] — 组合使用

## 自测

为什么关闭坐标轴后必须加数据标签？::外圈与刻度都被隐藏，图形失去了任何类别和数值参照，只能用文本标签标出每根柱子对应的人或类别。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p79 S03E30.玫瑰图](https://www.bilibili.com/video/BV1ji4y157uB?p=79) · 2026-11-17
