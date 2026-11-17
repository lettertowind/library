---
term: set_axis_off（关闭坐标轴）
aliases: [plt.gca().set_axis_off(), 关闭坐标轴, 隐藏坐标轴, plt.axis('off'), axis('off')]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E29 · 树状图"
order: 78
created: 2026-11-17
updated: 2026-11-17
---

# set_axis_off（关闭坐标轴）

> 别名：plt.gca().set_axis_off()、关闭坐标轴、隐藏坐标轴、plt.axis('off')、axis('off')

**隐藏当前图形的坐标轴、刻度和边框，只保留图形主体。**

## 解释

树状图、饼图这类不需要坐标系的图，绘制后坐标轴刻度只会干扰画面。除了 plt.gca().set_axis_off()，更简短的写法是 plt.axis('off')，效果相同。

## 有什么用

- 绘制树状图、饼图后去掉坐标轴
- 做纯图形展示时保持画面干净

## 关键要点

- plt.axis('off') 是最简写法，等价于 gca().set_axis_off()
- 只隐藏坐标轴和边框，不删除数据也不删除图像
- 不关闭时图像周围会残留默认刻度和边框

## 边界与易混淆

只影响坐标轴显示，不影响坐标范围；需要控制范围仍要用 xlim/ylim。

## 关联

- [[Matplotlib]] — 上位概念
- [[树状图]] — 组合使用

## 自测

plt.axis('off') 之后图中数据会消失吗？::不会，它只隐藏坐标轴、刻度和边框，矩形块和文字照常显示。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p78 S03E29.树状图](https://www.bilibili.com/video/BV1ji4y157uB?p=78) · 2026-11-17
