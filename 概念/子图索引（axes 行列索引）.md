---
term: 子图索引（axes 行列索引）
aliases: [axes[0,0], axes 索引, 子图下标, 二维索引取子图]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E11 · 创建多个子图"
order: 59
created: 2026-11-17
updated: 2026-11-17
---

# 子图索引（axes 行列索引）

> 别名：axes[0,0]、axes 索引、子图下标、二维索引取子图

**plt.subplots 返回的 axes 是一个二维数组，用 [行, 列] 从 0 开始定位每一张子图。**

## 解释

2×2 布局对应 axes[0,0]、axes[0,1]、axes[1,0]、axes[1,1]。因为索引是规则的二维下标，所以可以套用 for 循环 + range 批量给所有子图画图。注意它与线性代数里 a11、a12 从 1 开始的写法不同。

## 有什么用

- 在指定位置画图：axes[1,0].bar(x, y)
- 循环批量绘图时按行列索引取子图

## 关键要点

- axes[行索引, 列索引]，行列都从 0 开始
- 2×2 布局：[0,0] [0,1] [1,0] [1,1]
- 取到的对象可直接调 .bar / .pie / .plot
- 索引规律是能用循环批量出图的前提

## 边界与易混淆

容易和数学里 a11、a12 的下标混淆，编程一律从 0 开始，所以第一张是 [0,0] 而不是 [1,1]。

## 关联

- [[plt.subplots]] — 上位概念
- [[Numpy 索引]] — 前置知识
- [[enumerate]] — 组合使用

## 自测

2 行 2 列布局里，第二行第一个子图用哪个索引取？::axes[1, 0]
为什么 axes 的索引方式让批量画图变容易？::因为行列索引是连续的整数二维坐标，可直接用双重 for 循环遍历取值

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p59 S03E11.创建多个子图](https://www.bilibili.com/video/BV1ji4y157uB?p=59) · 2026-11-17
