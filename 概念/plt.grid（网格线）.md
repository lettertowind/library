---
term: plt.grid（网格线）
aliases: [grid, plt.grid(), 网格线, Matplotlib 网格线函数]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E28 · 瀑布图"
order: 77
created: 2026-11-17
updated: 2026-11-17
---

# plt.grid（网格线）

> 别名：grid、plt.grid()、网格线、Matplotlib 网格线函数

**Matplotlib 中开启并设置图表背景网格线的函数。**

## 解释

plt.grid() 在绘图区叠加与刻度对齐的参考线，帮助读图时对齐数值。它本身不产生新图形，只影响已有坐标轴的背景线，样式通过 axis、color、linestyle、linewidth 等参数统一控制。

## 有什么用

- 折线图、散点图中辅助读数
- 需要按 x 或 y 单方向加参考线时

## 关键要点

- 不想要网格线就不调用 plt.grid()，不必特意传 False 关闭
- axis='x' 控制竖直网格线，axis='y' 控制横向网格线，省略则两个方向一起生效
- color、linestyle、linewidth 可同时传入，一次设置颜色、线型、线宽
- 线宽过大会显笨重，linewidth=3 左右视觉较协调
- 网格线方向按所属轴命名，不是按视觉方向命名

## 边界与易混淆

与 plt.plot 等绘图函数的 linestyle/linewidth 同名但作用对象不同：plt.grid 的参数只影响网格线，不影响数据曲线。

## 关联

- [[plt.plot]] — 组合使用
- [[axis 参数]] — 组合使用
- [[linestyle 线型参数]] — 组合使用
- [[linewidth 线宽参数]] — 组合使用
- [[折线图]] — 组合使用

## 自测

只想保留横向网格线并设为红色虚线，代码怎么写？::plt.grid(axis='y', color='red', linestyle=':')
为什么 axis='x' 得到的是竖直网格线？::这些线从 x 轴上各刻度位置向上延伸，按所属轴归属命名，与视觉方向无关。


### 补充 · 2026-11-17

plt.grid(True) 一键开启全图网格，但有时只需横向参考线——这时通过 plt.gca() 拿到坐标轴对象，调用 ax.yaxis.grid(...) 只对 y 轴生效，参数可设虚线、颜色、透明度。

- 只画 y 轴网格：ax = plt.gca(); ax.yaxis.grid(True, linestyle='--', color='gray', alpha=0.5)
- linestyle='--' 虚线比实线更不抢眼
- alpha 控制透明度，常用于弱化网格
只想要横向虚线网格，最简写法是什么？::ax = plt.gca(); ax.yaxis.grid(True, linestyle='--')。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p77 S03E28.瀑布图](https://www.bilibili.com/video/BV1ji4y157uB?p=77) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p64 S03E15.网格线](https://www.bilibili.com/video/BV1ji4y157uB?p=64) · 2026-11-17
