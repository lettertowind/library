---
term: startangle 与 counterclock（起始角度与绘制方向）
aliases: [startangle, counterclock, 起始角度参数, 绘制方向参数]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E07 · 饼图"
order: 54
created: 2026-11-17
updated: 2026-11-17
---

# startangle 与 counterclock（起始角度与绘制方向）

> 别名：startangle、counterclock、起始角度参数、绘制方向参数

**两个配合使用的饼图参数，分别决定从哪个角度起画、按顺时针还是逆时针排列**

## 解释

startangle 设定第一个扇区从哪个角度开始绘制，默认从 0 度（水平方向）起步；counterclock 决定接下来是按逆时针还是顺时针推进。二者一起决定各扇区在圆上的落位顺序。

## 有什么用

- 把某个扇区摆到正上方、使版式更顺眼
- 调整数据排列顺序的视觉方向

## 关键要点

- startangle=90 相当于从 y 轴正方向开始绘制
- startangle 只改起点，不改变绘制方向
- counterclock 默认 True，即逆时针
- counterclock=False 变为顺时针，数据顺序整体镜像

## 边界与易混淆

startangle 改起点、counterclock 改方向，两者独立，不要以为是同一个参数的正负效果。

## 关联

- [[饼图]] — 上位概念

## 自测

同时设 startangle=90、counterclock=False，饼图会怎么画？::从 y 轴正方向起，按顺时针依次排布数据。
只调 startangle 会让扇区顺序反转吗？::不会，顺序不变，只是整体旋转了起始位置。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p54 S03E07.饼图](https://www.bilibili.com/video/BV1ji4y157uB?p=54) · 2026-11-17
