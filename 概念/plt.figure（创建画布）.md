---
term: plt.figure（创建画布）
aliases: [plt.figure(), figure(), 创建画布, 画布参数]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E10 · 画布和子图"
order: 58
created: 2026-11-17
updated: 2026-11-17
---

# plt.figure（创建画布）

> 别名：plt.figure()、figure()、创建画布、画布参数

**创建一块承载所有子图的画布，并同时设定它的名称、尺寸、分辨率与底色。**

## 解释

画布（figure）是绘图的底层容器，子图都挂在这块画布上。调用 plt.figure() 时不带参数就用默认配置新建一块空白画布；带参数则一次性确定窗口标题、宽高、清晰度和背景色，避免出图后再改。

## 有什么用

- 需要在同一窗口布局多张子图之前先建画布
- 统一调整输出图片的尺寸、清晰度与背景色

## 关键要点

- num 设置窗口名称，如 plt.figure(num='孙兴华')
- figsize 用元组设宽高，单位为英寸
- dpi 控制分辨率，实战建议不低于 200
- facecolor 设背景色，可写 'blue'、'b' 或十六进制
- edgecolor 设边框色，一般看不出来，不必设置

## 边界与易混淆

plt.figure() 负责建画布但不建子图；fig, axes = plt.subplots(2,2) 则把画布与子图一次建好，两者是替代关系。

## 关联

- [[figure 与 axes（画布与子图）]] — 上位概念
- [[figsize（画布尺寸）]] — 组合使用
- [[dpi（图像分辨率）]] — 组合使用
- [[plt.subplots]] — 对比项

## 自测

想让绘图窗口顶部的标题显示成“销售分析”，应该调哪个参数？::plt.figure(num='销售分析') 中的 num 参数
plt.figure(facecolor='b') 和 plt.figure(edgecolor='b') 改的是同一处颜色吗？::不是，前者改画布背景色，后者改画布边框色


### 补充 · 2026-11-17

必须先有画布，才能在上面添加子图和绘图，否则 plt 会隐式创建一张默认画布。显式写成 fig = plt.figure() 的好处是拿到 fig 变量，之后用 fig.add_subplot 精确地把子图挂在这张画布上。

- 返回 Figure 对象，通常用 fig 变量接收
- 刚创建时是空白画布，不含任何图形
- 所有子图都通过 fig.add_subplot 挂到这张画布上
不写 plt.figure() 直接 plt.plot() 会怎样？::Matplotlib 自动创建一张默认画布并画上去，但你就拿不到 fig，不便继续做多子图布局。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p58 S03E10.画布和子图](https://www.bilibili.com/video/BV1ji4y157uB?p=58) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p59 S03E11.创建多个子图](https://www.bilibili.com/video/BV1ji4y157uB?p=59) · 2026-11-17
