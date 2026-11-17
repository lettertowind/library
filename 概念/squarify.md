---
term: squarify
aliases: [squarify 库, Python 树状图库]
kind: tool
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E29 · 树状图"
order: 78
created: 2026-11-17
updated: 2026-11-17
---

# squarify

> 别名：squarify 库、Python 树状图库

**Python 第三方库，专门计算并绘制树状图的矩形布局。**

## 解释

squarify 会按 squarified treemap 算法把一组数值切成面积成比例的矩形，并调用 Matplotlib 完成绘制。它只负责矩形划分与块上标注，画布、坐标轴、标题、字体等样式仍由 matplotlib 控制。

## 有什么用

- 在 Python 中快速绘制静态树状图
- 为分类占比数据生成矩形布局

## 关键要点

- 安装命令为 pip3 install squarify，用 import squarify 验证
- 绘图入口是 squarify.plot()，不是 matplotlib 的 plot
- matplotlib 是通用可视化库，squarify 才是树状图专用模块
- 只产出静态图，不支持 Power BI 那样的交互下钻

## 边界与易混淆

只能做单层矩形划分；需要多层级下钻或交互时应改用支持交互的可视化工具。

## 关联

- [[树状图]] — 上位概念
- [[Matplotlib]] — 组合使用
- [[pip]] — 前置知识

## 自测

squarify 和 matplotlib 在画树状图时各自负责什么？::squarify 计算矩形面积布局并画矩形块和标注，matplotlib 提供画布、坐标轴、标题和字体等样式控制。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p78 S03E29.树状图](https://www.bilibili.com/video/BV1ji4y157uB?p=78) · 2026-11-17
