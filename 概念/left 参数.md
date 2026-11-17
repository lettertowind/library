---
term: left 参数
aliases: [left, 堆积起点, left=累计值]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E06 · 叠加条形图"
order: 53
created: 2026-11-17
updated: 2026-11-17
---

# left 参数

> 别名：left、堆积起点、left=累计值

**barh 中指定条带起始横坐标的参数，是横向堆叠的控制开关**

## 解释

默认所有条带都从 0 开始，会互相覆盖；显式设置 left 让后一层从前一层的末端继续延伸。它接受 Series，因此可以直接写 left=data.语文 + data.数学 做逐元素累加。

## 有什么用

- 绘制堆叠条形图时确定每层起点
- 需要让条形不从 0 起始（如作区间图）时

## 关键要点

- 第一层 left=0，第二层 left=第一层数值，第三层 left=前两层之和
- 起点用 Series 表达式，做到每人各自累计而非全局累加
- 漏设 left 的表现是各层从同一起点重叠，看不出堆叠
- 柱形图中对应的是 bottom 参数，方向不同名字不同

## 边界与易混淆

left 只在堆积类图中有意义；单层条形图传非 0 值会让长度失去“占比”的直观含义。

## 关联

- [[plt.barh]] — 组合使用
- [[叠加条形图]] — 组合使用
- [[plt.text 数据标签]] — 前置知识

## 自测

如果第二层的 left 仍写成 0，图上会看到什么？::两层条带都从 0 起画、互相覆盖，长度不累加。
为什么 left 可以直接写 data.语文 + data.数学 而不需要循环？::left 接受 Series，Pandas 的加法按行逐元素对齐计算，天然得到每人各自的累计起点。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p53 S03E06.叠加条形图](https://www.bilibili.com/video/BV1ji4y157uB?p=53) · 2026-11-17
