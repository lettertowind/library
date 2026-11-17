---
term: plt.rcParams
aliases: [rcParams, 全局参数设置, 运行时配置字典]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E01 · 柱状图"
order: 48
created: 2026-11-17
updated: 2026-11-17
---

# plt.rcParams

> 别名：rcParams、全局参数设置、运行时配置字典

**Matplotlib 的全局配置字典，统一控制字体、负号等默认显示行为。**

## 解释

绘图前通过 plt.rcParams['键'] = 值 修改全局默认值，对之后所有图生效，不用每张图单独设。中文字体（font.sans-serif）和负号（axes.unicode_minus）这两类显示问题都靠它解决。

## 有什么用

- 批量解决中文乱码、负号显示为方块
- 统一整个项目的字体、字号、配色风格

## 关键要点

- 写法：plt.rcParams['font.sans-serif'] = ['SimHei']
- 改的是全局默认值，一次设置后面所有图生效
- 键名对应 Matplotlib 配置文件 matplotlibrc
- 不同问题对应不同键，中文与负号要分别设

## 边界与易混淆

全局设置会污染后续图表；只想改单张图时应用具体函数的参数而非 rcParams。

## 关联

- [[Matplotlib 中文显示配置]] — 下位概念
- [[axes.unicode_minus（负号显示配置）]] — 下位概念
- [[Matplotlib]] — 上位概念

## 自测

设置中文字体后负号依然显示成方块，为什么？::中文字体和负号显示是 rcParams 里两个不同的键（font.sans-serif 与 axes.unicode_minus），必须分别设置。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p48 S03E01.柱状图](https://www.bilibili.com/video/BV1ji4y157uB?p=48) · 2026-11-17
