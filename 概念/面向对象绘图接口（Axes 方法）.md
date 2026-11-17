---
term: 面向对象绘图接口（Axes 方法）
aliases: [面向对象接口, Axes 绘图方法, ax.bar, ax.plot, OOP 接口]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E12 · 新增子图或区域"
order: 60
created: 2026-11-17
updated: 2026-11-17
---

# 面向对象绘图接口（Axes 方法）

> 别名：面向对象接口、Axes 绘图方法、ax.bar、ax.plot、OOP 接口

**通过 Figure/Axes 对象的方法绘图，而不是调用 pyplot 全局函数。**

## 解释

Matplotlib 有两套接口：pyplot 状态机式（如 plt.plot）和面向对象式（如 ax.plot）。在多子图、子区域场景中，明确指定在哪个 Axes 上绘图更可靠。

## 有什么用

- 多图布局
- 在子图或子区域中分别绘图和设置标题

## 关键要点

- 常见方法：ax.bar、ax.plot、ax.set_title、ax.set_xlabel。
- 每个 Axes 独立管理自己的图形元素和标题。
- 与 plt.bar、plt.plot 对应，但作用于指定轴。
- 复杂布局中优先用面向对象接口，避免“画错轴”。

## 边界与易混淆

简单单图可用 plt.* 快速绘制；多图时混用两套接口容易搞混“当前轴”。

## 关联

- [[figure 与 axes（画布与子图）]] — 上位概念
- [[子区域（画中画）]] — 组合使用
- [[plt.plot]] — 对比项
- [[柱形图]] — 对比项

## 自测

图一.bar(...) 和 plt.bar(...) 有什么区别？::前者在指定的 Axes 对象上绘图，后者在“当前轴”上绘图。
多子图场景中为什么更推荐 ax.set_title 而不是 plt.title？::因为 ax.set_title 明确作用于指定子图，不会把标题设到错误的当前轴上。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p60 S03E12.新增子图或区域](https://www.bilibili.com/video/BV1ji4y157uB?p=60) · 2026-11-17
