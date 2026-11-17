---
term: matplotlib.ticker 模块
aliases: [mtick, ticker, import matplotlib.ticker as mtick]
kind: tool
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E13 · 组合图"
order: 62
created: 2026-11-17
updated: 2026-11-17
---

# matplotlib.ticker 模块

> 别名：mtick、ticker、import matplotlib.ticker as mtick

**Matplotlib 中集中提供刻度定位器与刻度格式器的子模块，常简写为 mtick。**

## 解释

通过 import matplotlib.ticker as mtick 引入，模块内含 MultipleLocator、FormatStrFormatter、PercentFormatter、DateFormatter 等类。它把“刻度放哪里”和“刻度显示成什么样”拆成两类可插拔对象，配合 set_major_locator / set_major_formatter 挂到具体坐标轴上。

## 有什么用

- 需要自定义坐标轴刻度间隔或显示格式时
- 把日期、百分比、金额等刻度统一成特定样式

## 关键要点

- 常用别名有 mtick 和 ticker，两种写法等价
- 定位器管刻度位置，格式器管刻度文字
- 通过 axis.set_major_locator() / set_major_formatter() 应用到轴上
- 纯显示层工具，不改变底层数据

## 关联

- [[刻度定位器与格式器（Locator Formatter）]] — 下位概念
- [[FormatStrFormatter]] — 下位概念
- [[PercentFormatter]] — 下位概念
- [[MultipleLocator]] — 下位概念

## 自测

定位器和格式器分别负责什么？::定位器决定刻度出现在哪些位置，格式器决定刻度标签显示成什么样子。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p62 S03E13.组合图：柱形图+折线图](https://www.bilibili.com/video/BV1ji4y157uB?p=62) · 2026-11-17
