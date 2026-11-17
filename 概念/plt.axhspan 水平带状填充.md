---
term: plt.axhspan 水平带状填充
aliases: [axhspan, plt.axhspan(), 水平区域填充, 水平带状填充]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E25 · 填充"
order: 74
created: 2026-11-17
updated: 2026-11-17
---

# plt.axhspan 水平带状填充

> 别名：axhspan、plt.axhspan()、水平区域填充、水平带状填充

**在 y 轴指定区间内填充一条贯穿 x 方向的水平带状区域。**

## 解释

axhspan(ymin, ymax) 接收 y 轴起止值，在两者之间铺一层色带，x 方向默认覆盖整个绘图区；h 代表 horizontal。常用于突出某个 y 值区间，如阈值带、置信区间或目标范围。

## 有什么用

- 突出显示 y 轴上的某个数值区间
- 绘制阈值带、置信区间、目标范围

## 关键要点

- 参数为 ymin、ymax，填充的是 y 轴范围
- 用 facecolor 指定填充色，如 facecolor='yellow'
- 用 alpha 控制透明度，如 alpha=0.5
- 需先设置 plt.axis 范围，否则填充区可能不在视野内
- h 表示水平，与 axvspan 的垂直填充相对

## 边界与易混淆

填充范围由 y 轴起止值决定，不是 x 轴；别与 axvspan 混淆。

## 关联

- [[plt.axvspan 垂直带状填充]] — 对比项
- [[alpha 透明度]] — 组合使用
- [[ax.axis（一次设置坐标轴四边界）]] — 组合使用

## 自测

plt.axhspan(1, 1.3) 填充的是哪个轴的范围？::y 轴，从 y=1 到 y=1.3。
如何让 axhspan 的填充区域半透明？::设置 alpha 参数，例如 alpha=0.5。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p74 S03E25.填充](https://www.bilibili.com/video/BV1ji4y157uB?p=74) · 2026-11-17
