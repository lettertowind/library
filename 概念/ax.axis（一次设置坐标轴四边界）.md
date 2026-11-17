---
term: ax.axis（一次设置坐标轴四边界）
aliases: [ax.axis, axis([xmin, xmax, ymin, ymax]), 一次设置坐标轴范围, Matplotlib axis]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E25 · 填充"
order: 74
created: 2026-11-17
updated: 2026-11-17
---

# ax.axis（一次设置坐标轴四边界）

> 别名：ax.axis、axis([xmin, xmax, ymin, ymax])、一次设置坐标轴范围、Matplotlib axis

**用 [xmin, xmax, ymin, ymax] 一个列表同时设定 x、y 轴显示范围的 Axes 方法。**

## 解释

它等价于分别调用 set_xlim 与 set_ylim，只是写成一行。参数顺序严格固定为 x 最小、x 最大、y 最小、y 最大，写反会导致图形显示异常。需先通过 plt.gca() 拿到轴对象。

## 有什么用

- 一次性锁定画布可视区域
- 想省掉两次 set_xlim/set_ylim 调用

## 关键要点

- 顺序必须是 [xmin, xmax, ymin, ymax]，不能颠倒
- 等价于 set_xlim(xmin, xmax) + set_ylim(ymin, ymax)
- 是轴对象方法，先 ax = plt.gca() 再调用
- 与 NumPy/Pandas 的 axis 参数含义完全无关

## 边界与易混淆

同名不同义：NumPy/Pandas 的 axis 指运算沿哪个方向，Matplotlib 的 ax.axis 指坐标轴显示范围。

## 关联

- [[axis 参数]] — 对比项
- [[axis 参数]] — 对比项
- [[plt.gca 与 plt.gcf]] — 组合使用
- [[坐标轴边界参数（bottomtopleftright）]] — 组合使用

## 自测

想让 x 轴 0~10、y 轴 0~20，用一行 ax.axis 怎么写？::ax.axis([0, 10, 0, 20])
ax.axis 的四个数写反了会怎样？::显示范围错乱，最小值大于最大值时轴会翻转或图形不可见。


### 补充 · 2026-11-17

axis([xmin, xmax, ymin, ymax]) 按顺序给出 x 轴最小/最大和 y 轴最小/最大；pyplot 层写作 plt.axis(...)，Axes 对象层写作 ax.axis(...)。设置范围可确保参考线和填充区域落在可视区域内。

- 参数顺序为 xmin, xmax, ymin, ymax
- plt.axis([-1, 2, -1, 2]) 将 x、y 范围都设为 -1 到 2
- 填充/参考线超出范围时会看不见，需先调范围
plt.axis([-1, 2, -1, 2]) 中第二个 2 表示什么？::x 轴的最大值（xmax）。
为什么要先设置坐标轴范围再画填充？::避免填充区域超出当前视野而看不到。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p74 S03E25.填充](https://www.bilibili.com/video/BV1ji4y157uB?p=74) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p68 S03E19.坐标轴【下】](https://www.bilibili.com/video/BV1ji4y157uB?p=68) · 2026-11-17
