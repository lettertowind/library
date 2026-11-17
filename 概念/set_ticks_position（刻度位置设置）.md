---
term: set_ticks_position（刻度位置设置）
aliases: [set_ticks_position, xaxis.set_ticks_position, yaxis.set_ticks_position, 刻度位置]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E18 · 坐标轴【上】"
order: 67
created: 2026-11-17
updated: 2026-11-17
---

# set_ticks_position（刻度位置设置）

> 别名：set_ticks_position、xaxis.set_ticks_position、yaxis.set_ticks_position、刻度位置

**用 ax.xaxis.set_ticks_position('top') 一类调用，把刻度线移到指定的边框一侧。**

## 解释

它决定刻度刻线贴着哪条边框：x 轴可选 top 或 bottom，y 轴可选 left 或 right。注意它只移动刻度，不移动边框线，所以移完还要把原边框设为 'none'、目标边框设成可见颜色，否则刻度会悬浮或落在看不见的线上。

## 有什么用

- 把 x 轴刻度放到顶部、y 轴刻度放到右侧
- 做对照式布局，例如上下双刻度

## 关键要点

- x 轴可选 top/bottom，y 轴可选 left/right
- 移动刻度不改边框，底部旧红线需单独设为 'none'
- 目标侧边框要设可见颜色，否则刻度看起来悬空
- 刻度文字样式要用 get_xticklabels() 另一套方法调

## 边界与易混淆

只挪刻度刻线与标签的位置，不挪边框线本身；与 spines 的 set_color 是两件独立的事，必须配套改。

## 关联

- [[ax.spines（坐标轴边框）]] — 对比项
- [[刻度标签（ticklabels）]] — 组合使用

## 自测

把 x 轴刻度移到顶部后，图上却看不到刻度线，最可能漏了哪一步？::没把 top 边框设为可见颜色（它此前被设成了 'none'）。
set_ticks_position('right') 会把右边框线也一起画出来吗？::不会，它只移动刻度位置，边框线仍需用 spines 单独设置颜色。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p67 S03E18.坐标轴【上】](https://www.bilibili.com/video/BV1ji4y157uB?p=67) · 2026-11-17
