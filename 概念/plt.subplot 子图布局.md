---
term: plt.subplot 子图布局
aliases: [subplot, 221, 2×2 子图, 子图网格]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E11 · 创建多个子图"
order: 59
created: 2026-11-17
updated: 2026-11-17
---

# plt.subplot 子图布局

> 别名：subplot、221、2×2 子图、子图网格

**用行列编号把同一画布切分为多个区域，并激活其中一个用于绘图。**

## 解释

plt.subplot(221) 一次性表达了「2 行 2 列、选第 1 个」两件事。调用后该区域成为当前 Axes，后续所有 plot、title、xlabel 都只作用在它上面，直到再次调用 subplot 切换到别的区域。

## 有什么用

- 一张图上并排对比多个图表
- 分面展示不同类别的数据

## 关键要点

- 三位数字依次表示行数、列数、子图序号
- 每次调用都会激活对应子图，绘图函数只落在激活的子图上
- 切换子图后需重新设置标题和轴标签
- 子图多时标题与标签容易重叠，配合 tight_layout 使用

## 边界与易混淆

数字写法的序号不能超过行×列；面向对象的 fig, axes = plt.subplots() 是另一种更灵活的等价写法。

## 关联

- [[plt.title]] — 组合使用
- [[plt.tight_layout]] — 组合使用

## 自测

已经调用 plt.subplot(221) 画完图，再想往第 4 个区域画东西，先要做什么？::先调用 plt.subplot(224) 激活第 4 个子图，再执行绘图和标签设置。


### 补充 · 2026-11-17

plt.subplot(221) 表示把画布分成 2 行 2 列并选中第 1 个位置。每次调用都会切换当前激活的子图，因此后面紧跟的 plt.bar、plt.pie、plt.plot 才会画到对应位置。它与面向对象的 fig.add_subplot(221) 效果一致。

- 三位数编号 221 = 2 行 2 列第 1 个
- 与 fig.add_subplot(221) 效果相同，写法不同
- 可只用部分位置，如跳过 222 则第二格留白
先 plt.subplot(223) 再 plt.plot(...)，折线画在哪一格？::2 行 2 列布局中的第 3 格（左下）
如果想在 2×2 布局里只画第 1、3、4 格，需要特殊处理吗？::不需要，正常调用 221、223、224 即可，222 位置自然留空
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p59 S03E11.创建多个子图](https://www.bilibili.com/video/BV1ji4y157uB?p=59) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p72 S03E23.标题及轴标签](https://www.bilibili.com/video/BV1ji4y157uB?p=72) · 2026-11-17
