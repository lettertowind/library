---
term: fill_between
aliases: [plt.fill_between, 填充两条曲线间区域]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E20 · 叠加区域图"
order: 69
created: 2026-11-17
updated: 2026-11-17
---

# fill_between

> 别名：plt.fill_between、填充两条曲线间区域

**Matplotlib 中填充两条曲线之间区域的函数。**

## 解释

fill_between 接收 x、上下边界 y1/y2，并用 where 布尔条件决定哪些区间着色。它适合展示两条曲线之间的差值、置信区间或交叉区域。交叉填充需要按条件多次调用并分别指定颜色。

## 有什么用

- 绘制曲线间差值区域
- 绘制置信区间或阈值区间
- 实现交叉填充

## 关键要点

- 必须同时传入 y1、y2 两个边界
- where 用布尔数组控制参与填充的区间
- facecolor 或 color 指定填充颜色
- 交叉填充常分两次调用，条件互补
- 先 plot 曲线再 fill_between

## 边界与易混淆

where 只决定哪些点填充，不会自动把两种颜色分段；多色填充需多次调用。

## 关联

- [[交叉填充]] — 组合使用
- [[条件分段填充]] — 组合使用

## 自测

fill_between 中 where 参数的作用是什么？::用布尔条件筛选需要填充的 x 区间。
只传 y1 不传 y2 能否完成两条曲线间填充？::不能，必须给出上下两个边界。


### 补充 · 2026-11-17

调用形式为 plt.fill_between(x, y1, y2, ...)，y1 是填充下限、y2 是填充上限，下限设 0 即从 x 轴向上填充。它既能做叠加区域图的面积效果，也能做区间高亮、置信带。

- 参数顺序：x 数据、下限、上限；下限为 0 表示从 x 轴开始填充
- facecolor 指定填充颜色，alpha 控制透明度（如 0.3）
- 两层填充时，下层上限用下方折线数据，可避免与底部区域重叠
fill_between(x, 0, y) 与 fill_between(x, y1, y2) 的填充范围有什么差别？::前者填 x 轴（0）到曲线 y 之间；后者填两条曲线 y1 与 y2 之间。
两个 fill_between 都用 alpha=0.3 且范围重叠，重叠区会出现什么现象？::两种颜色叠加混合成中间色，类似两个半透明图层叠加。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p69 S03E20.叠加区域图](https://www.bilibili.com/video/BV1ji4y157uB?p=69) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p75 S03E26.交差及填充](https://www.bilibili.com/video/BV1ji4y157uB?p=75) · 2026-11-17
