---
term: drawstyle 折线连接样式
aliases: [drawstyle, 折线连接样式, 阶梯线, steps, drawstyle='steps']
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E24 · 样式"
order: 73
created: 2026-11-17
updated: 2026-11-17
---

# drawstyle 折线连接样式

> 别名：drawstyle、折线连接样式、阶梯线、steps、drawstyle='steps'

**plt.plot 中控制相邻数据点之间如何连线（直线或阶梯）的参数。**

## 解释

默认情况下折线用直线把相邻数据点直接连起来；给 drawstyle 赋值后，点与点之间改成水平加垂直的阶梯式走线。它表达的是「数值在一段区间内保持不变、只在特定位置跳变」这一含义，适合阶梯电价、累计计数、状态切换这类离散变化。

## 有什么用

- 画阶梯状变化趋势（如价格分段、库存台阶式变化）
- 强调数值在某区间内恒定、在指定点跳变

## 关键要点

- 共五个取值：default、steps、steps-pre、steps-mid、steps-post
- default 即默认直线连接，等同不写该参数
- steps-pre / mid / post 的差别是水平段相对数据点偏左、居中还是偏右
- 与 linestyle 不是一回事：drawstyle 管连线的走法，linestyle 管线条的虚实
- 样式只改变连线路径，不改变数据点本身的坐标值

## 边界与易混淆

只影响点与点之间的连接路径，不改变坐标数值，也不影响线条颜色、粗细和标记点；数据点很密集时阶梯效果在视觉上几乎看不出来。

## 关联

- [[plt.plot]] — 组合使用
- [[linestyle 线型参数]] — 对比项
- [[折线图]] — 上位概念

## 自测

steps-pre、steps-mid、steps-post 三者的区别是什么？::阶梯中水平段相对两个数据点的位置不同：pre 让水平段从数据点向左（前置）保持恒定，post 向右（后置）保持恒定，mid 在两点中间转折。
想画阶梯线，应该改 drawstyle 还是 linestyle？::drawstyle。linestyle 只控制线条是实线、虚线还是点划线。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p73 S03E24.样式](https://www.bilibili.com/video/BV1ji4y157uB?p=73) · 2026-11-17
