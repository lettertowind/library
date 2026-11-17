---
term: 当前子图（current axes）
aliases: [current axes, 当前坐标轴, 隐式当前子图]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E10 · 画布和子图"
order: 58
created: 2026-11-17
updated: 2026-11-17
---

# 当前子图（current axes）

> 别名：current axes、当前坐标轴、隐式当前子图

**plt 系列绘图函数默认作用的那一块子图区域。**

## 解释

调用 fig.add_subplot(...) 创建子图时，Matplotlib 会把它设为『当前子图』，之后的 plt.plot、plt.bar 等不带 ax 参数的调用都画在这块区域上。所以『在哪个 add_subplot 下面写绘图代码，图就落在哪个子图里』。理解这一点，才能在多子图排版时不把图形画错位置。

## 有什么用

- 多子图排版时决定每个图形画到哪里
- 排查『图画到了不该出现的子图』这类问题

## 关键要点

- 每次执行 add_subplot 都会切换一次当前子图
- plt.plot / plt.bar 等作用于最近一次创建的当前子图
- 写成 ax.plot(...) 的面向对象方式则不受当前子图影响
- 绘图代码顺序写错，图形会落到意外子图中

## 边界与易混淆

只有 plt.* 这种隐式接口依赖当前子图；用 ax.* 显式调用时与该机制无关。

## 关联

- [[fig.add_subplot（在画布上添加子图）]] — 组合使用
- [[figure 与 axes（画布与子图）]] — 上位概念
- [[plt.subplots]] — 对比项

## 自测

先 add_subplot(221)，画一个折线图；再 add_subplot(222)，画一个柱形图。两张图分别出现在哪？::折线图在第 1 个子图，柱形图在第 2 个子图，因为每次 add_subplot 都切换了当前子图。
为什么用 ax.plot() 写法就基本不会出现图形错位的问题？::因为它显式指定了目标 axes 对象，不依赖『当前子图』这个隐式状态。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p58 S03E10.画布和子图](https://www.bilibili.com/video/BV1ji4y157uB?p=58) · 2026-11-17
