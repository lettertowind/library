---
term: connectionstyle 变形箭头
aliases: [connectionstyle, 连接样式, 拐弯箭头]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E27 · 文本注释"
order: 76
created: 2026-11-17
updated: 2026-11-17
---

# connectionstyle 变形箭头

> 别名：connectionstyle、连接样式、拐弯箭头

**arrowprops 中控制箭头连接路径形状的键，可画出折线、弧线、条形箭头。**

## 解释

默认箭头是从文字到目标点的直线，遇到文字与目标点之间夹着别的图形时不好看。connectionstyle 改变的是箭头走过的路径形状，常用取值 angle（拐弯）、arc（弧线）、bar（条形），使箭头能绕开干扰元素。

## 有什么用

- 文字与目标点之间有其他数据点时绕行
- 让注释箭头更有设计感、层级更清楚

## 关键要点

- 取值写在 arrowprops=dict(connectionstyle='angle') 里
- angle 为折线拐弯，arc 为弧线，bar 为条形连接
- 它只改路径形状，不改变 xy 指向和 xytext 文字位置
- 讲师资料中列出全部可用样式，直接复制名称即可

## 边界与易混淆

改动的是视觉路径，不会自动避让其他图元，复杂图上仍需手动调 xytext 决定绕行起点。

## 关联

- [[arrowprops]] — 上位概念
- [[plt.annotate 文本注释]] — 组合使用

## 自测

设置 connectionstyle='arc' 后，箭头指向的点会变化吗？::不会。指向点仍由 xy 决定，connectionstyle 只改变连接路径的形状。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p76 S03E27.文本注释](https://www.bilibili.com/video/BV1ji4y157uB?p=76) · 2026-11-17
