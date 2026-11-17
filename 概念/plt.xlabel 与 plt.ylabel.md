---
term: plt.xlabel 与 plt.ylabel
aliases: [xlabel, ylabel, 轴标签, 坐标轴标签]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E02 · 条形图"
order: 49
created: 2026-11-17
updated: 2026-11-17
---

# plt.xlabel 与 plt.ylabel

> 别名：xlabel、ylabel、轴标签、坐标轴标签

**为当前子图的 x 轴、y 轴添加说明文字的函数对。**

## 解释

plt.xlabel 在轴下方、plt.ylabel 在轴左侧添加文字，用来告诉读者这条轴代表什么。它们的样式参数与 plt.title 相同，也可以传 bbox 字典给文字加背景框，让标签在图形背景上更醒目。

## 有什么用

- 标注坐标轴含义与单位
- 给标签加背景框以提升可读性

## 关键要点

- xlabel 显示在轴下方，ylabel 显示在轴左侧
- fontsize、color 等样式参数与 plt.title 用法一致
- 需要背景框时传 bbox=dict(...)，而不是单独的 facecolor 参数
- 同样只作用于当前选中的子图

## 边界与易混淆

轴标签是文字说明，不是刻度值；刻度文本要用 xticks/yticks 修改。

## 关联

- [[plt.title]] — 对比项
- [[bbox 文本边框]] — 组合使用

## 自测

想让 x 轴标签背后有一块半透明黄底，应该给 plt.xlabel 传什么参数？::bbox=dict(facecolor='yellow', alpha=0.2, pad=...)，底色和透明度都写在这个字典里。


### 补充 · 2026-11-17

轴标签告诉读者每个轴代表什么数据，通常配合 fontsize 设置字号。在横向条形图中，两个轴的语义与柱形图互换：x 轴是数值（分数），y 轴是分类（姓名），写反是最常见的低级错误。

- 条形图中 x 轴为分数、y 轴为姓名，与柱形图正好相反
- 无论图形如何旋转，画布下方永远是 x 轴、上方永远是 y 轴
- 可用 fontsize 调整字号，与标题保持一致风格
画横向条形图时，x 轴和 y 轴标签分别应该写什么？::x 轴写“分数”（数值），y 轴写“姓名”（分类）。
把柱形图改成条形图后，轴标签需要改吗？::需要。两个轴的语义互换了，不改会出现 x 轴标成姓名、y 轴标成分数的错误。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p49 S03E02.条形图](https://www.bilibili.com/video/BV1ji4y157uB?p=49) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p72 S03E23.标题及轴标签](https://www.bilibili.com/video/BV1ji4y157uB?p=72) · 2026-11-17
