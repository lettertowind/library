---
term: set_theta_zero_location
aliases: [set_theta_zero_location('N'), 零度位置设置, 极坐标起始方向]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E30 · 玫瑰图"
order: 79
created: 2026-11-17
updated: 2026-11-17
---

# set_theta_zero_location

> 别名：set_theta_zero_location('N')、零度位置设置、极坐标起始方向

**设置极坐标中 0 度（θ=0）指向哪个方位的坐标轴方法。**

## 解释

默认 0 度在右侧，图形看起来歪斜；传入 'N' 可让 0 度指向正上方，像指南针上端永远是 N 一样，图形就变得端正。与之配套的 set_theta_direction 可控制角度是顺时针还是逆时针增长。

## 有什么用

- 让玫瑰图/雷达图的起始柱位于正上方
- 调整极坐标图的整体旋转方向

## 关键要点

- 参数可选 'N'（上）、'E'（右）、'S'（下）、'W'（左）
- 只影响起始角度，不改变各柱之间的相对角度
- 配合 set_theta_direction 可得到顺/逆时针布局

## 边界与易混淆

只对极坐标轴有效，普通笛卡尔坐标轴调用无意义。

## 关联

- [[极坐标系（polar）]] — 组合使用
- [[玫瑰图]] — 组合使用

## 自测

不加 set_theta_zero_location('N') 时玫瑰图会有什么观感问题？::0 度位于右侧水平方向，整圈柱子像是“趴着”，起始位置不正，视觉上不端正。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p79 S03E30.玫瑰图](https://www.bilibili.com/video/BV1ji4y157uB?p=79) · 2026-11-17
