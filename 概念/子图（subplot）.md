---
term: 子图（subplot）
aliases: [subplot, 网格子图, 多图布局]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E12 · 新增子图或区域"
order: 60
created: 2026-11-17
updated: 2026-11-17
---

# 子图（subplot）

> 别名：subplot、网格子图、多图布局

**把一张画布按行列网格切分成多个独立坐标轴区域。**

## 解释

子图是 Figure 上的多个 Axes，用行数、列数和序号定位，适合并排比较多个图表。它与“子区域/画中画”不同：子图按规则网格切分，彼此不重叠。

## 有什么用

- 一张画布展示多张图
- 对比不同数据系列或指标

## 关键要点

- 用 add_subplot(nrows, ncols, index) 添加，index 从 1 开始、按行优先计数。
- 例如 2,1,1 表示 2 行 1 列的第 1 个；2,2,4 表示 2 行 2 列的第 4 个。
- 每个子图返回独立 Axes，可分别绘图和设置标题。
- 子图之间不重叠，布局由行列网格决定。

## 边界与易混淆

与“子区域”易混：子图按网格切分，子区域是在已有 Axes 内再嵌套一个 Axes。

## 关联

- [[fig.add_subplot（在画布上添加子图）]] — 组合使用
- [[子区域（画中画）]] — 对比项
- [[figure 与 axes（画布与子图）]] — 上位概念

## 自测

add_subplot(2, 2, 4) 在 2×2 网格中定位到哪一格？::第二行第二列，即右下角。
子图和子区域的根本区别是什么？::子图按网格切分、彼此不重叠；子区域是在已有图内部再嵌套一个小图。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p60 S03E12.新增子图或区域](https://www.bilibili.com/video/BV1ji4y157uB?p=60) · 2026-11-17
