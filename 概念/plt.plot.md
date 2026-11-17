---
term: plt.plot
aliases: [plot, plt.plot(), Matplotlib 折线绘图函数]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E09 · 平均线"
order: 57
created: 2026-11-17
updated: 2026-11-17
---

# plt.plot

> 别名：plot、plt.plot()、Matplotlib 折线绘图函数

**Matplotlib 中绘制折线图、同时设置线色与数据点样式的核心函数。**

## 解释

传入两组等长的 x、y 数据即可画出折线，默认只有线段、不显示数据点。通过参数可以一次性设定线的颜色、点的形状和点的大小，多次调用则在同一个坐标系里叠加多条线。

## 有什么用

- 绘制单系列或多系列的折线趋势图
- 快速调整线色和点标记以区分类别

## 关键要点

- 基本形式 plt.plot(x, y)，x、y 需等长且顺序对应
- c 参数设置线色，如 c='red'
- marker 参数设置数据点形状，常用 *、o、v 等符号
- ms 参数设置数据点大小（如 ms=10），与数值无关
- 多次调用 plt.plot 会在同一坐标系叠加多线，需配色与标记区分

## 边界与易混淆

marker 默认为空，所以初版折线往往只有线没有点，容易误以为数据点画不出来。

## 关联

- [[折线图]] — 组合使用
- [[plt.text 数据标签]] — 组合使用

## 自测

用 plt.plot 画出的初版图只有线看不到具体月份的点，原因和改法？::默认 marker 为空，需指定 marker（如 '*'、'o'）并用 ms 调大小才显示数据点。
在一张图上画四条线，代码上怎么写、区分上要注意什么？::连续调用四次 plt.plot，每次换 y 数据；同时用不同 c 颜色和 marker 形状区分系列。


### 补充 · 2026-11-17

plt.plot 接收 x、y 数据并连线，线条范围由传入的数据点决定。它画的是数据系列，不是坐标轴参考线，因此与 axhline 的语义和覆盖范围不同。

- 必须同时提供 x 和 y 数据
- 线条范围受数据点限制，不自动横贯图表
- 画平均线优先用 axhline，而不是 plot
plt.plot 画出的线条范围由什么决定？::由传入的数据点范围决定，通常只连接第一个到最后一个数据点
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p57 S03E09.平均线](https://www.bilibili.com/video/BV1ji4y157uB?p=57) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p56 S03E08.折线图](https://www.bilibili.com/video/BV1ji4y157uB?p=56) · 2026-11-17
