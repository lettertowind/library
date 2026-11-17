---
term: figsize（画布尺寸）
aliases: [figsize, figsize=(12,13), 画布宽高, 图幅尺寸]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E11 · 创建多个子图"
order: 59
created: 2026-11-17
updated: 2026-11-17
---

# figsize（画布尺寸）

> 别名：figsize、figsize=(12,13)、画布宽高、图幅尺寸

**figure 中用来设定画布宽和高的参数，单位是英寸。**

## 解释

figsize 接收 (宽, 高) 元组，宽是水平方向、高是竖直方向。英寸是欧美常用单位，国内习惯厘米/米，需要自行换算（1 英寸≈2.54 厘米）。子图行列越多，画布就要相应放大，否则每个子图会被挤得很小。

## 有什么用

- 子图数量多时放大画布，避免每张图挤成一团
- 需要固定出图尺寸放进报告或 PPT

## 关键要点

- 元组形式传入，如 figsize=(12, 13)
- 单位为英寸，1 英寸约等于 2.54 厘米
- 与 dpi 共同决定最终像素：像素 ≈ figsize × dpi
- 4×4 这类密集布局必须同步调大 figsize

## 边界与易混淆

figsize 管画布的物理尺寸，dpi 管每英寸多少像素，只调 dpi 不调 figsize 时字号比例不会变。

## 关联

- [[plt.figure（创建画布）]] — 组合使用
- [[dpi（图像分辨率）]] — 对比项

## 自测

figsize=(12,13) 里的 12 和 13 分别指什么、什么单位？::宽 12、高 13，单位是英寸
在 4×4 子图布局下只调 dpi 不调 figsize，会有什么问题？::每个子图仍被挤得很小，图内文字标签放不下，需要同步放大 figsize

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p59 S03E11.创建多个子图](https://www.bilibili.com/video/BV1ji4y157uB?p=59) · 2026-11-17
