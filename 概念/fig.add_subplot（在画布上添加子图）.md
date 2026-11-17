---
term: fig.add_subplot（在画布上添加子图）
aliases: [add_subplot, fig.add_subplot(221), 添加子图方法]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E10 · 画布和子图"
order: 58
created: 2026-11-17
updated: 2026-11-17
---

# fig.add_subplot（在画布上添加子图）

> 别名：add_subplot、fig.add_subplot(221)、添加子图方法

**在已经存在的 figure 对象上添加并返回一个子图 axes 的方法。**

## 解释

这是面向对象的写法：先有 fig，再 fig.add_subplot(行, 列, 位置) 往里加子图。它与 pyplot 风格下的 plt.subplot(221) 效果完全一样，区别只在调用入口是画布对象还是 plt 状态机。

## 有什么用

- 已经持有 fig 对象时，在其上逐个添加子图
- 阅读别人面向对象风格的绘图代码

## 关键要点

- 参数仍是行、列、位置三要素，如 add_subplot(221)
- 调用前必须先有 fig 对象
- 与 plt.subplot 等价，只是写法不同
- 子图多时可循环调用 add_subplot 批量添加

## 边界与易混淆

add_subplot 每次只加一个子图，要一次生成多个子图应改用 plt.subplots(行, 列)。

## 关联

- [[plt.subplot 子图布局]] — 对比项
- [[plt.figure（创建画布）]] — 前置知识
- [[figure 与 axes（画布与子图）]] — 上位概念

## 自测

fig.add_subplot(223) 和 plt.subplot(223) 画出来的位置一样吗？::完全一样，都是 2 行 2 列中的第 3 个位置，只是调用风格不同
为什么 add_subplot 必须先有 fig？::它是画布对象的方法，子图要挂在具体画布上，没有 fig 就没有调用对象


### 补充 · 2026-11-17

参数描述『几行几列第几个图』：三位数 221 即 2 行 2 列的第 1 个，也可写成逗号形式 fig.add_subplot(2, 2, 1)，两种写法等价。它既负责划分布局，也把该子图设为当前子图，返回的 ax 对象可用于后续面向对象绘图。

- 221 = 2 行 2 列中的第 1 个图；223 = 第 3 个
- 可写 fig.add_subplot(221)，也可写 (2, 2, 1)，等价
- 子图编号不必连续使用，可留空某些位置
布局为 3 行 3 列时，第 5 个位置的子图编号是多少？::335（3 行 3 列第 5 个），也可写 add_subplot(3, 3, 5)。
只想要 2×2 布局中的第 1、3、4 个图，需要为第 2 个位置写 add_subplot 吗？::不需要，不创建的位置就自然留白。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p58 S03E10.画布和子图](https://www.bilibili.com/video/BV1ji4y157uB?p=58) · 2026-11-17

add_subplot(nrows, ncols, index) 把画布切成规则网格，并按序号返回对应 Axes。它适合规则多图布局，与 add_axes 的自由矩形定位形成对比。

- index 从 1 开始，按行优先计数。
- 2,1,1 表示 2 行 1 列的第 1 个；2,2,4 表示 2 行 2 列的第 4 个。
- 返回 Axes 对象，可独立调用 bar、plot、set_title。
add_subplot(2, 1, 1) 表示什么布局？::把画布分成 2 行 1 列，取第 1 个子图，即上半部分。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p60 S03E12.新增子图或区域](https://www.bilibili.com/video/BV1ji4y157uB?p=60) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p59 S03E11.创建多个子图](https://www.bilibili.com/video/BV1ji4y157uB?p=59) · 2026-11-17
