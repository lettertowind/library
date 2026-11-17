---
term: plt.colorbar
aliases: [颜色条, colorbar, 颜色图例]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E16 · 散点图"
order: 65
created: 2026-11-17
updated: 2026-11-17
---

# plt.colorbar

> 别名：颜色条、colorbar、颜色图例

**为数值颜色映射添加一条“颜色—数值”对照条的方法。**

## 解释

当 c 传入的是数值数组时，颜色本身就成了一种数据表达，必须有颜色条告诉读者深色代表小值还是大值。调用非常简单：绘图后紧跟 plt.colorbar() 即可，它会把当前色标范围渲染到图旁。

## 有什么用

- 任何使用了数值颜色映射的图（散点图、热力图等）
- 需要在图旁标注颜色对应数值范围的场景

## 关键要点

- 在 plt.scatter(...) 之后、plt.show() 之前调用
- 只对数值映射有意义，固定颜色时不需要
- 颜色条一端代表最小值，另一端代表最大值

## 边界与易混淆

它只是图例工具，不改变数据也不改变配色，配色方案仍由 c 的数值和色板决定。

## 关联

- [[颜色映射]] — 前置知识
- [[散点图]] — 组合使用

## 自测

一张散点图的所有点都是红色，还需要调用 colorbar 吗？::不需要，颜色没有编码数值，颜色条没有可对照的信息。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p65 S03E16.散点图](https://www.bilibili.com/video/BV1ji4y157uB?p=65) · 2026-11-17
