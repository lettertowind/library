---
term: plt.gca 与 plt.gcf
aliases: [gca, gcf, get current axes, get current figure, 当前坐标轴, 当前图形对象]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E18 · 坐标轴【上】"
order: 67
created: 2026-11-17
updated: 2026-11-17
---

# plt.gca 与 plt.gcf

> 别名：gca、gcf、get current axes、get current figure、当前坐标轴、当前图形对象

**分别获取当前 Axes 轴对象和当前 Figure 图形对象，用于更精细的面向对象设置。**

## 解释

pyplot 是状态机式的简写接口，很多细节设置做不到；先取到轴对象或图对象，再调用它们的方法（如 set_xticklabels、subplots_adjust）就能精细控制。

## 有什么用

- 设置刻度标签的旋转角度与对齐方式
- 调整整张图的边距和子图布局

## 关键要点

- plt.gca() 返回当前轴，可调 set_xticklabels、set_xlabel 等
- plt.gcf() 返回当前图，可调 subplots_adjust 改整体边距
- 单轴设置用 gca，整图边距用 gcf，各管一层
- 这是从 pyplot 简写过渡到面向对象接口的入口

## 边界与易混淆

存在多个子图时 gca() 只返回当前激活的轴，需用 axes[i] 或返回值精确指定目标轴。

## 关联

- [[plt.subplots_adjust]] — 组合使用
- [[刻度标签旋转]] — 组合使用
- [[plt.subplot 子图布局]] — 组合使用

## 自测

要给刻度标签设置旋转，为什么必须先 plt.gca()？::旋转与对齐是轴对象的方法（set_xticklabels），pyplot 层面没有对应简写。
调整整张图左边距应该用 gca 还是 gcf？::用 gcf 取到图形对象再 subplots_adjust，边距属于整图属性而非单个轴。


### 补充 · 2026-11-17

用 plt.plot() 这类快捷函数画图后，往往没有 ax 变量，此时 plt.gca() 就能拿回当前坐标轴对象，再在其上做边框、刻度、翻转等设置。它也可以链式调用，如 plt.gca().invert_yaxis()。

- gca = get current axes（当前子图），gcf = get current figure（当前画布）
- ax = plt.gca() 后可继续 spines、xaxis、yaxis 等操作
- 支持链式写法：plt.gca().invert_yaxis() 省去中间变量
代码里只有 plt.plot(...) 没有 ax 变量，要改边框该怎么做？::用 ax = plt.gca() 取到当前坐标轴，再操作 ax.spines。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p67 S03E18.坐标轴【上】](https://www.bilibili.com/video/BV1ji4y157uB?p=67) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p50 S03E03.分组柱状图](https://www.bilibili.com/video/BV1ji4y157uB?p=50) · 2026-11-17
