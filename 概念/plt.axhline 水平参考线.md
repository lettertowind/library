---
term: plt.axhline 水平参考线
aliases: [axhline, plt.axhline(), 水平参考线, 水平线函数]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E25 · 填充"
order: 74
created: 2026-11-17
updated: 2026-11-17
---

# plt.axhline 水平参考线

> 别名：axhline、plt.axhline()、水平参考线、水平线函数

**在指定 y 值处绘制横贯整个坐标轴的水平线。**

## 解释

plt.axhline 是 Matplotlib 的坐标轴水平参考线函数，只需给定 y 轴位置即可画一条贯穿图表的水平线。常用于平均线、阈值线、目标线等参考语义，不依赖具体数据点的 x 范围。

## 有什么用

- 给柱形图或折线图添加平均线
- 标注阈值、目标值、警戒线

## 关键要点

- 核心参数 y 指定水平线所在的纵坐标
- color 设颜色，linestyle=':' 画虚线更符合参考线语义
- 线条横贯整个坐标轴，不受数据点范围限制
- 平均线应传 np.mean 计算结果，不要写死数值

## 边界与易混淆

与 plt.plot 画水平线不同：axhline 不接收 x 数据，线条范围跟图表走而非跟数据走。

## 关联

- [[平均线]] — 组合使用
- [[plt.plot]] — 对比项
- [[np.mean]] — 前置知识
- [[柱形图]] — 组合使用

## 自测

要给柱形图加一条表示销量均值的蓝色虚线，应调用哪个函数？::plt.axhline(y=均值, color='blue', linestyle=':')
axhline 的线条长度由什么决定？::由坐标轴范围决定，横贯整个图表，不需要传 x 数据


### 补充 · 2026-11-17

axhline(y=...) 用 y 定位，线在 x 方向贯穿全图；若同时给出 xmin、xmax，则只在指定横向区间内显示，变成一条水平线段。它常用于把平均值、阈值画成贯穿全图的参考线。

- 用 y 指定横线位置，如 plt.axhline(y=0.2)
- 用 xmin、xmax 控制横向显示区间，如 xmin=0.2, xmax=0.6 可画线段
- 线宽用 linewidth，注意拼写完整
axhline 中 xmin 和 xmax 控制什么？::控制横线在 x 轴上的显示区间；只显示这一段时就是线段。
要画一条 y=0.5、只在 x=0.2 到 0.6 显示的水平线段，怎么写？::plt.axhline(y=0.5, xmin=0.2, xmax=0.6)。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p74 S03E25.填充](https://www.bilibili.com/video/BV1ji4y157uB?p=74) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p57 S03E09.平均线](https://www.bilibili.com/video/BV1ji4y157uB?p=57) · 2026-11-17
