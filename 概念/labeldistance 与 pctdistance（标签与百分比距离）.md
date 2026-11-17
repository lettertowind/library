---
term: labeldistance 与 pctdistance（标签与百分比距离）
aliases: [labeldistance, pctdistance, 标签距离, 百分比距离]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E07 · 饼图"
order: 54
created: 2026-11-17
updated: 2026-11-17
---

# labeldistance 与 pctdistance（标签与百分比距离）

> 别名：labeldistance、pctdistance、标签距离、百分比距离

**分别控制扇区标签与百分比数字到圆心距离倍数的一对饼图参数**

## 解释

两个参数都按半径倍数定位文字：labeldistance 管姓名之类的扇区标签，默认约 1.1；pctdistance 管 autopct 生成的百分比数字，默认 0.6。数值越小越靠圆心，小于 1 就进入饼图内部。

## 有什么用

- 标签与饼图重叠、或文字压到内层图形时做微调
- 把百分比数字放到扇区内部或外侧

## 关键要点

- labeldistance 默认约 1.1，调到 0.8 标签就落进饼图内部
- pctdistance 默认 0.6，调小则百分比向圆心移动
- 两者的区别是控制的文字对象不同，不是方向不同
- 饼图套饼时常用调大 labeldistance 避免与外层文字重叠

## 边界与易混淆

radius 改的是饼图本身的半径，这两个参数只移动文字，不要混淆。

## 关联

- [[autopct（饼图百分比显示）]] — 组合使用
- [[radius 参数（饼图半径）]] — 对比项

## 自测

百分比数字挤在圆心附近，想让它往外走该调哪个参数？::把 pctdistance 调大，默认是 0.6。
labeldistance=0.8 会有什么效果？::扇区标签移到饼图内部。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p54 S03E07.饼图](https://www.bilibili.com/video/BV1ji4y157uB?p=54) · 2026-11-17
