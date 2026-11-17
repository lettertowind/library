---
term: MultipleLocator
aliases: [MultipleLocator, 倍数刻度定位器, 按倍数设置刻度]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E19 · 坐标轴【下】"
order: 68
created: 2026-11-17
updated: 2026-11-17
---

# MultipleLocator

> 别名：MultipleLocator、倍数刻度定位器、按倍数设置刻度

**让主刻度落在某个数的整数倍上的刻度定位器。**

## 解释

MultipleLocator(7) 表示刻度只出现在 7、14、21、28… 这些位置。它挂在轴的 set_major_locator 上使用，改参数即可换倍数。适合需要“整齐倍数刻度”的坐标轴。

## 有什么用

- x 轴按 7 的倍数显示刻度
- 需要固定步长刻度且不想手写刻度列表

## 关键要点

- MultipleLocator(7) 生成 7、14、21… 的刻度位置
- 导入方式：from matplotlib.ticker import MultipleLocator
- 用法：ax.xaxis.set_major_locator(MultipleLocator(7))
- 只决定位置不决定文字，数字格式另用格式器

## 边界与易混淆

刻度区间含负数时，常需先解决负号显示问题，否则负号可能变成方块甚至报错。

## 关联

- [[刻度定位器与格式器（Locator Formatter）]] — 上位概念
- [[FormatStrFormatter]] — 组合使用
- [[axes.unicode_minus（负号显示配置）]] — 组合使用

## 自测

要让 y 轴刻度都是 5 的倍数，写核心代码？::ax.yaxis.set_major_locator(MultipleLocator(5))
MultipleLocator 能决定刻度显示成几位小数吗？::不能，它只管位置，小数位由格式器决定。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p68 S03E19.坐标轴【下】](https://www.bilibili.com/video/BV1ji4y157uB?p=68) · 2026-11-17
