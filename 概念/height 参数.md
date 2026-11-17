---
term: height 参数
aliases: [height, height=0.5, 条形高度, 条形粗细]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E02 · 条形图"
order: 49
created: 2026-11-17
updated: 2026-11-17
---

# height 参数

> 别名：height、height=0.5、条形高度、条形粗细

**在 barh 中控制条形粗细（纵向厚度）的参数，而非条的长度。**

## 解释

横向条形图里的条是横躺的，纵向的“高度”在视觉上就是条的粗细，而条的长短由 width 决定。该参数可省略，显式设为 0.5、0.6 能让条更细、更有留白。

## 有什么用

- 条形过粗互相贴在一起时调小
- 需要统一视觉风格或多系列并排时设定

## 关键要点

- 在 barh 中 height 表示粗细；在 bar 中 height 表示柱高，两者同名但含义不同
- 取值一般在 0~1 之间，越大条越粗
- 不写则使用 Matplotlib 默认值（约 0.8）

## 边界与易混淆

不要与 width 混淆：width 才承载数据大小，height 只影响视觉样式，不改变数值含义。

## 关联

- [[plt.barh]] — 组合使用
- [[柱形图]] — 对比项

## 自测

在 barh 中把 height 从 0.8 改成 0.3，图形会怎么变化？::条形变细（变窄），但每条的长度和对应数值不变。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p49 S03E02.条形图](https://www.bilibili.com/video/BV1ji4y157uB?p=49) · 2026-11-17
