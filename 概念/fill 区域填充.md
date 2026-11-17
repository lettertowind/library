---
term: fill 区域填充
aliases: [fill, plt.fill, ax.fill, 填充区域, 多边形填充]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E22 · 雷达图"
order: 71
created: 2026-11-17
updated: 2026-11-17
---

# fill 区域填充

> 别名：fill、plt.fill、ax.fill、填充区域、多边形填充

**用颜色填充折线或多边形所围区域的 Matplotlib 方法。**

## 解释

fill 接收一组 x 和 y 坐标，把它们围成的区域上色，常用于雷达图、面积图这类需要强调面积的图形。填充色由第三个位置参数或 color 指定，透明度由 alpha 控制。

## 有什么用

- 雷达图填充对象区域
- 面积图、区域强调
- 多层数据对比时用半透明色叠加

## 关键要点

- 前两个位置参数是 x（角度）与 y（分数）数据
- 第三个位置参数是颜色，不是 marker，容易混
- alpha 一般取 0.25 左右，避免遮挡其他对象
- ax.fill 与 plt.fill 功能等价，面向对象写法更推荐

## 边界与易混淆

填充色不透明度叠加时颜色会混浊，对象超过 3 个基本无法分辨，所以雷达图填充只适合少量对象。

## 关联

- [[雷达图]] — 组合使用
- [[alpha 透明度]] — 组合使用
- [[面向对象绘图接口（Axes 方法）]] — 组合使用

## 自测

plt.fill(angles, a01, 'red', alpha=0.25) 里的 'red' 起什么作用？::指定填充颜色，它是第三个位置参数；不是标记样式。
为什么两个对象的填充都设 alpha=0.25 而不是 1？::让两层颜色半透明叠加，既能看到重叠区域又能分辨各自的轮廓。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p71 S03E22.雷达图](https://www.bilibili.com/video/BV1ji4y157uB?p=71) · 2026-11-17
