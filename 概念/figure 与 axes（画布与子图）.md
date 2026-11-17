---
term: figure 与 axes（画布与子图）
aliases: [figure, axes, fig, ax, 画布与坐标轴对象]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E10 · 画布和子图"
order: 58
created: 2026-11-17
updated: 2026-11-17
---

# figure 与 axes（画布与子图）

> 别名：figure、axes、fig、ax、画布与坐标轴对象

**figure 是承载整张图的画布，axes 是其中真正绘图、带坐标轴的区域。**

## 解释

Matplotlib 的对象分两层：figure 管画布级属性（尺寸、dpi、保存），axes 管具体绘图区（坐标轴、刻度、线条、文字）。几乎所有坐标轴设置都作用在 axes 上，所以先拿到 ax 是第一步。

## 有什么用

- 理解 Matplotlib 面向对象的绘图层次
- 判断某个设置该写给 fig 还是 ax

## 关键要点

- figure 管画布级属性：figsize、dpi、savefig
- axes 管绘图区：spines、ticks、ticklabels、plot 线条
- 一个 figure 可以包含多个 axes（即多子图）
- fig, ax = plt.subplots() 是同时拿到两者的标准写法

## 边界与易混淆

口语里的「坐标轴」常混指整个 axes；严格说 xaxis/yaxis 才是单条轴，spines 只是边框线。

## 关联

- [[plt.subplots]] — 组合使用
- [[plt.gca 与 plt.gcf]] — 组合使用

## 自测

设置图片 200dpi 和隐藏上边框，分别作用在哪一层对象上？::dpi 属于 figure（画布）；隐藏上边框属于 axes 的 spines。


### 补充 · 2026-11-17

可以类比为『一张纸』和『纸上的一个个图框』：paper 只有一张，图框可以有很多个。每块 axes 有自己独立的坐标轴、标题和图例，互不干扰。所有绘图函数最终都是往某个 axes 上画东西。

- 一个 figure 可以包含多个 axes
- axes 各自拥有独立坐标轴、图例与标题
- plt.figure() 建 figure，add_subplot() 建 axes
一个 figure 里有 4 个 axes，它们的 x 轴刻度必须一样吗？::不必，每个 axes 的坐标轴设置彼此独立。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p58 S03E10.画布和子图](https://www.bilibili.com/video/BV1ji4y157uB?p=58) · 2026-11-17

一个 Figure 可以包含多个 Axes；子图、子区域本质上都是 Axes。add_subplot 和 add_axes 都返回 Axes 对象，绘图时应明确在哪个 Axes 上操作。

- Figure 管整张画布，Axes 管具体坐标系和绘图内容。
- 一个 Figure 可有多个 Axes，也可嵌套小 Axes。
- add_subplot、add_axes 的返回值都是 Axes。
一个 Figure 上可以有多个 Axes 吗？::可以，子图布局和画中画都是在同一 Figure 上放置多个 Axes。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p60 S03E12.新增子图或区域](https://www.bilibili.com/video/BV1ji4y157uB?p=60) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p67 S03E18.坐标轴【上】](https://www.bilibili.com/video/BV1ji4y157uB?p=67) · 2026-11-17
