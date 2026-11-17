---
term: plt.polar
aliases: [polar, plt.polar(), 极坐标绘图函数, Matplotlib polar]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E21 · 极坐标"
order: 70
created: 2026-11-17
updated: 2026-11-17
---

# plt.polar

> 别名：polar、plt.polar()、极坐标绘图函数、Matplotlib polar

**Matplotlib 中创建极坐标轴并按极角、极径绘图的核心函数。**

## 解释

调用 plt.polar() 不带参数时只画出极坐标圆盘，传入 (theta, r) 会自动建立极坐标系并按极坐标定位数据点。它是散点、折线到雷达图的基础绘图入口。

## 有什么用

- 绘制极坐标散点图、折线图
- 搭建雷达图雏形（多点连线并闭合）

## 关键要点

- 签名 plt.polar(theta, r, fmt)：theta 为弧度极角，r 为极径
- 不带参数调用只显示圆盘，不绘制任何数据
- fmt 可组合标记与颜色，如 'o'、'ro'、'go'、'o-'、'ro-'
- 默认按数组顺序依次连点，不会自动把末点连回首点
- 常与 plt.ylim 配合限定极径范围

## 边界与易混淆

极角必须传弧度而非角度；它画的是极坐标（θ, r），不能像 plt.plot 那样直接理解成直角坐标 (x, y)。

## 关联

- [[极坐标系（polar）]] — 上位概念
- [[极角]] — 组合使用
- [[极径]] — 组合使用
- [[弧度制]] — 前置知识
- [[雷达图]] — 组合使用

## 自测

要画一个位于 45° 方向、极径为 20 的红色圆点，代码怎么写？::plt.polar(0.25 * np.pi, 20, 'ro')
只写 plt.polar() 和写 plt.polar(theta, r) 输出有什么差别？::前者只显示空的极坐标圆盘（无数据点），后者会自动建立极坐标系并绘制对应数据。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p70 S03E21.极坐标](https://www.bilibili.com/video/BV1ji4y157uB?p=70) · 2026-11-17
