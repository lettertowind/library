---
term: plt.subplots
aliases: [subplots, fig, ax = plt.subplots(), 创建画布与子图]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E18 · 坐标轴【上】"
order: 67
created: 2026-11-17
updated: 2026-11-17
---

# plt.subplots

> 别名：subplots、fig, ax = plt.subplots()、创建画布与子图

**一次性创建 figure 画布与 axes 子图并返回 (fig, ax) 的函数。**

## 解释

相比 plt.plot() 这种画在「当前坐标轴」上的快捷写法，plt.subplots() 直接给出画布和子图对象，后续用 ax.plot()、ax.spines 在指定子图上操作，不会画错位置。做多子图时它返回 axes 数组，可逐个访问。

## 有什么用

- 任何需要精细控制边框、刻度的图
- 一画多图的多子图布局

## 关键要点

- plt.subplots(1, 1) 建一行一列单子图，此时 ax 是单个对象
- 返回元组 (fig, ax)，绘图与设置都在 ax 上做
- 配 ax.plot() 使用，与 plt.plot() 的隐式当前轴相对
- 建立多子图时 ax 变成数组，用 ax[0]、ax[1] 分别操作

## 边界与易混淆

与 plt.subplot(221) 不同：subplots 一次建好画布和全部子图并返回对象，subplot 是按位置逐个激活。

## 关联

- [[figure 与 axes（画布与子图）]] — 组合使用
- [[plt.gca 与 plt.gcf]] — 对比项

## 自测

用了 plt.subplots() 之后，为什么建议改用 ax.plot()？::plt.plot() 画在「当前坐标轴」上，多子图时容易画错子图；ax.plot() 明确指定目标。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p67 S03E18.坐标轴【上】](https://www.bilibili.com/video/BV1ji4y157uB?p=67) · 2026-11-17
