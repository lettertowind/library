---
term: linewidth 线宽参数
aliases: [linewidth, lw, 线宽, 线条粗细]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E15 · 网格线"
order: 64
created: 2026-11-17
updated: 2026-11-17
---

# linewidth 线宽参数

> 别名：linewidth、lw、线宽、线条粗细

**Matplotlib 中控制线条粗细的参数，取值越大线越粗。**

## 解释

linewidth 以点为单位设定线条粗细，默认约 1。它在 plt.plot、plt.grid、边框等接口通用，可简写 lw。讲课示例先把网格线设成 10 发现过于笨重，改成 3 才协调。

## 有什么用

- 突出主体曲线或弱化辅助线
- 调整网格线、边框的视觉轻重

## 关键要点

- 可简写为 lw，如 lw=3
- 默认值约 1，属于细线
- 取值过大（如 10）会压过数据曲线，3 左右较合适
- 对网格线、折线、图形边框均生效

## 关联

- [[linestyle 线型参数]] — 对比项
- [[plt.grid（网格线）]] — 组合使用
- [[plt.plot]] — 组合使用

## 自测

把网格线 linewidth 设成 10 有什么问题？::线过粗，视觉上压过数据曲线、显得笨重，一般取 1~3 更协调。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p64 S03E15.网格线](https://www.bilibili.com/video/BV1ji4y157uB?p=64) · 2026-11-17
