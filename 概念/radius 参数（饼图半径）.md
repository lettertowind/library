---
term: radius 参数（饼图半径）
aliases: [radius, 饼图半径参数, radius=0.5]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E07 · 饼图"
order: 54
created: 2026-11-17
updated: 2026-11-17
---

# radius 参数（饼图半径）

> 别名：radius、饼图半径参数、radius=0.5

**设定饼图半径大小的参数，默认值为 1**

## 解释

radius 直接缩放整个饼图，大于 1 变大、小于 1 变小。它最大的用途不是单个饼图的大小，而是在同一坐标系里画半径不同的多个饼图，形成饼图套饼。

## 有什么用

- 放大或缩小饼图
- 在同一坐标系绘制内层小饼图

## 关键要点

- 默认 radius=1，radius=1.3 放大、0.5 缩小
- 同一坐标系重复调用 plt.pie 并用不同 radius 即可套饼
- 缩小半径后文字同样会挤，需要重新调 labeldistance、pctdistance

## 边界与易混淆

radius 是饼图专属参数，柱形图、折线图没有；缩放图形大小不等于调整画布尺寸。

## 关联

- [[饼图]] — 上位概念
- [[饼图套饼]] — 组合使用

## 自测

radius=0.5 的饼图叠在一个默认半径的饼图上，会是什么效果？::大饼内部出现一个同心小饼，即饼图套饼。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p54 S03E07.饼图](https://www.bilibili.com/video/BV1ji4y157uB?p=54) · 2026-11-17
