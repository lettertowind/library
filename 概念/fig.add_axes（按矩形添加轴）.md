---
term: fig.add_axes（按矩形添加轴）
aliases: [add_axes, fig.add_axes(), add_axes 四元组, 按矩形添加轴]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E12 · 新增子图或区域"
order: 60
created: 2026-11-17
updated: 2026-11-17
---

# fig.add_axes（按矩形添加轴）

> 别名：add_axes、fig.add_axes()、add_axes 四元组、按矩形添加轴

**按 [left, bottom, width, height] 矩形位置在画布上添加一个坐标轴。**

## 解释

add_axes 用相对画布的 0–1 比例定位新 Axes，可精确控制位置和大小，是制作子区域/画中画的核心方法。它与 add_subplot 的网格定位不同，不会自动避让其他轴。

## 有什么用

- 创建画中画
- 自由布局多个重叠或非网格图

## 关键要点

- 参数是一个列表或元组：left 左、bottom 下、width 宽、height 高。
- 数值是相对画布的比例，0 是左/下边缘，1 是右/上边缘。
- 返回 Axes 对象，后续用 ax.bar、ax.plot、ax.set_title 绘图。
- 内部小图的四元组没有默认值，必须显式指定。
- 位置可以反复运行、凭视觉微调。

## 边界与易混淆

与 add_subplot 区分：add_axes 按矩形自由定位，add_subplot 按行列网格定位；add_axes 不自动避让其他轴。

## 关联

- [[子区域（画中画）]] — 组合使用
- [[子图（subplot）]] — 对比项
- [[fig.add_subplot（在画布上添加子图）]] — 对比项
- [[figure 与 axes（画布与子图）]] — 上位概念
- [[面向对象绘图接口（Axes 方法）]] — 组合使用

## 自测

add_axes([0.65, 0.65, 0.2, 0.2]) 的小图大致在画布什么位置？::偏右上的位置，宽度和高度各占画布的 20%。
add_axes 的坐标是像素值还是比例值？::相对画布的比例值，范围通常是 0 到 1。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p60 S03E12.新增子图或区域](https://www.bilibili.com/video/BV1ji4y157uB?p=60) · 2026-11-17
