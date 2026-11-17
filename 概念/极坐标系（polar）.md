---
term: 极坐标系（polar）
aliases: [polar, plt.axes(polar=True), 极坐标轴]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E22 · 雷达图"
order: 71
created: 2026-11-17
updated: 2026-11-17
---

# 极坐标系（polar）

> 别名：polar、plt.axes(polar=True)、极坐标轴

**用角度和半径定位点的坐标系，Matplotlib 中以 plt.axes(polar=True) 创建。**

## 解释

在极坐标轴里，x 被解释为角度 θ、y 被解释为半径 r，因此 plt.bar 画出来的柱子会沿圆周排布、从圆心向外延伸。它是玫瑰图、雷达图、饼图类图形的共同底座。

## 有什么用

- 绘制玫瑰图、雷达图、极坐标柱图
- 需要按圆周分布表达分类时

## 关键要点

- plt.axes(polar=True) 返回极坐标轴对象，而非常规笛卡尔轴
- 极坐标中 x=角度、y=半径，绘图函数语义随之改变
- 先 plt.show() 可看到一个空圆盘，验证坐标系已建立

## 边界与易混淆

极坐标轴默认 0 度在右侧水平方向，直接用图会显得“趴着”，需要调整零度位置。

## 关联

- [[玫瑰图]] — 组合使用
- [[set_theta_zero_location]] — 组合使用
- [[雷达图]] — 组合使用

## 自测

在极坐标轴里调用 plt.bar，x 和 y 分别代表什么？::x 代表该柱子所在的角度位置，y 代表柱子从圆心向外的长度（数值大小）。


### 补充 · 2026-11-17

普通直角坐标用 x、y 定位，极坐标用角度定方向、半径定大小。在 Matplotlib 中通过 add_subplot(..., polar=True) 或 plt.axes(polar=True) 开启，绘图时第一个数据序列被解释为角度、第二个为半径。

- 开启方式：fig.add_subplot(111, polar=True)
- 111 表示一行一列的第一个子图，polar=True 切换为极坐标
- 角度传弧度，半径传数值（如分数）
在极坐标轴上调用 ax.plot(angles, scores) 时，两个参数分别代表什么？::angles 是每个点的极角（弧度），scores 是对应的半径长度。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p71 S03E22.雷达图](https://www.bilibili.com/video/BV1ji4y157uB?p=71) · 2026-11-17

极坐标系由四要素构成：极点是圆心原点，极轴是从极点指向 0° 方向的基准射线，极角是相对极轴的逆时针旋转角，极径是到极点的距离。Matplotlib 通过 plt.polar 或 plt.axes(polar=True) 创建该坐标系。

- 四要素：极点、极轴、极角 θ、极径 r，缺一无法定位
- 极轴是 0° 方向基准线，不是极径
- 极点等价于直角坐标的原点，径向零点在此
极轴和极径的区别是什么？::极轴是从极点出发、指向 0° 方向的固定基准射线；极径是极点到某个具体点的距离，随点变化。
在极坐标圆盘上，怎样定位一个唯一的点？::同时给出极角（方向）和极径（距离），两条信息缺一不可。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p70 S03E21.极坐标](https://www.bilibili.com/video/BV1ji4y157uB?p=70) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p79 S03E30.玫瑰图](https://www.bilibili.com/video/BV1ji4y157uB?p=79) · 2026-11-17
