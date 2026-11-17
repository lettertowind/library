---
term: PercentFormatter
aliases: [mtick.PercentFormatter, ticker.PercentFormatter, 百分比格式器, xmax 参数]
kind: tool
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E13 · 组合图"
order: 62
created: 2026-11-17
updated: 2026-11-17
---

# PercentFormatter

> 别名：mtick.PercentFormatter、ticker.PercentFormatter、百分比格式器、xmax 参数

**Matplotlib 的百分比刻度格式器，按 xmax 把原始值换算成百分比显示。**

## 解释

属于 matplotlib.ticker 模块，通过 axis.set_major_formatter 挂到坐标轴上。它按“显示百分比 = y / xmax × 100%”做换算，并自动补百分号、控制小数位，专门处理原始数据是 0~1 小数的场景。和只加符号的 FormatStrFormatter 不同，它真的改变了数值的显示尺度。

## 有什么用

- 原始数据是 0.38 这类小数，希望坐标轴显示 38.00%
- 比率类副轴统一成百分比刻度

## 关键要点

- xmax 表示“100% 对应的原始数据值”，小数数据设为 1
- 默认 xmax=100，所以 0.38 用默认值会显示成 0.38%
- decimals 控制百分比保留几位小数
- 常与 set_ylim 配合：0~1 数据配 (0, 1)，百分数数值配 (0, 100)
- 数据最大值只到 20% 时也可把 xmax 设为 0.2

## 边界与易混淆

数据本身已是 38.25 这类百分数数值时必须改用 FormatStrFormatter，否则会被再除一次 xmax，显示成 0.38%。

## 关联

- [[FormatStrFormatter]] — 对比项
- [[matplotlib.ticker 模块]] — 上位概念
- [[刻度定位器与格式器（Locator Formatter）]] — 上位概念
- [[主次坐标轴]] — 组合使用

## 自测

毛利率数据是 0.6158，要让坐标轴显示 61.58%，PercentFormatter 该怎么设？::PercentFormatter(xmax=1, decimals=2)，并把 y 轴范围设为 (0, 1)。
同一份 0.6158 的数据，误用 PercentFormatter(xmax=100) 会显示成什么？::0.62%，因为换算时多除了一次 100。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p62 S03E13.组合图：柱形图+折线图](https://www.bilibili.com/video/BV1ji4y157uB?p=62) · 2026-11-17
