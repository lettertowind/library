---
term: plt.barh
aliases: [barh, barh(), 水平条形图函数]
kind: tool
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E02 · 条形图"
order: 49
created: 2026-11-17
updated: 2026-11-17
---

# plt.barh

> 别名：barh、barh()、水平条形图函数

**Matplotlib 中绘制水平条形图的函数，参数为 y、width、height、left**

## 解释

它把 plt.bar 的 x/y 语义对调：纵轴放类别，横轴放数值。width 决定条带长度（数值大小），height 决定条带粗细，left 决定条带从横轴哪个位置开始画。多次调用并递增 left 就得到堆叠效果。

## 有什么用

- 绘制水平条形图或水平堆积条形图
- 类别名称较长、纵向排列更易读时

## 关键要点

- y=类别列，width=数值列，二者不可与 bar 的 x/height 混用
- height 控制条带粗细（如 0.5），不是数值大小
- left 控制起点，是实现堆叠的唯一手段
- 每加一层就先运行一次，确认堆叠位置再继续

## 边界与易混淆

barh 与 bar 的参数方向相反，把柱形图代码直接照搬会出现参数接反、标签错位。

## 关联

- [[叠加条形图]] — 组合使用
- [[柱形图]] — 对比项
- [[left 参数]] — 组合使用
- [[plt.text 数据标签]] — 组合使用

## 自测

plt.barh 中控制条带长度和粗细的分别是哪两个参数？::width 控制长度（数值），height 控制粗细。
把 plt.bar(x=姓名, height=语文) 改成条形图，参数应如何对应？::改为 plt.barh(y=姓名, width=语文)，类别给 y，数值给 width。


### 补充 · 2026-11-17

barh 相当于把柱形图旋转 90°：原来放在 x 轴的分类移到 y 轴，条的长短由 x 方向的数值决定。它不会继承 plt.bar 的行为，必须显式调用；否则 Matplotlib 会按默认柱形图处理，导致参数对不上或图形错误。

- 第一个参数是 y 轴位置（分类），第二个参数由 width 决定，代表条的长度和对应的数值
- height 控制条形粗细，常用 0.5 或 0.6，也可用默认值
- 起始位置参数决定条从 x 轴哪里开始画，基础图从 0 开始
用 plt.barh 画图时，条的长度由哪个参数决定？::由 width 参数决定，它对应数据里的数值列（如分数）。
为什么只把柱形图代码里的参数名改一改，运行就会出错？::因为 Matplotlib 默认画柱形图，必须显式调用 barh 才表示要画横向条形图，否则参数含义和图形类型都无法对应。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p49 S03E02.条形图](https://www.bilibili.com/video/BV1ji4y157uB?p=49) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p53 S03E06.叠加条形图](https://www.bilibili.com/video/BV1ji4y157uB?p=53) · 2026-11-17
