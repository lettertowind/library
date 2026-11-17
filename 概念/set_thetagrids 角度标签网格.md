---
term: set_thetagrids 角度标签网格
aliases: [thetagrids, plt.thetagrids, ax.set_thetagrids, 极坐标角度网格标签]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E22 · 雷达图"
order: 71
created: 2026-11-17
updated: 2026-11-17
---

# set_thetagrids 角度标签网格

> 别名：thetagrids、plt.thetagrids、ax.set_thetagrids、极坐标角度网格标签

**在极坐标图上按角度设置网格线与标签文字的方法。**

## 解释

极坐标图的圆周方向刻度默认是角度值，set_thetagrids 让你用自定义文案替换这些刻度，雷达图外圈的科目名就是靠它实现的。第一个参数是角度（必须是度数），第二个参数是对应的标签列表。

## 有什么用

- 雷达图外圈显示科目名
- 自定义极坐标圆周刻度标签

## 关键要点

- 第一个参数是度数列表，弧度要先经 np.degrees 转换
- 第二个参数是标签文字列表，长度需与角度数一致
- ax.set_thetagrids 与 plt.thetagrids 都可用
- 标签文字可再用 fontsize、颜色、加粗进一步修饰

## 边界与易混淆

传弧度进去标签位置会严重错位，因为它按度数解释；这是最常见的踩坑点。

## 关联

- [[np.degrees]] — 前置知识
- [[极坐标系（polar）]] — 上位概念
- [[雷达图]] — 组合使用

## 自测

调用 set_thetagrids 时直接把 np.linspace 的结果传进去会怎样？::位置会错乱，因为该参数按度数解释，弧度值远小于对应度数，必须先 np.degrees 转换。
标签列表比角度列表少一个，结果是什么？::标签与角度对不上，会缺少某个方向的科目标签或抛出长度不匹配问题。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p71 S03E22.雷达图](https://www.bilibili.com/video/BV1ji4y157uB?p=71) · 2026-11-17
