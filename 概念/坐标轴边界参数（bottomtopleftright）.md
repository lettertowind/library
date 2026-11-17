---
term: 坐标轴边界参数（bottomtopleftright）
aliases: [bottom, top, left, right, set_ylim(bottom=), 轴边界具名参数]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E19 · 坐标轴【下】"
order: 68
created: 2026-11-17
updated: 2026-11-17
---

# 坐标轴边界参数（bottomtopleftright）

> 别名：bottom、top、left、right、set_ylim(bottom=)、轴边界具名参数

**set_xlim/set_ylim 中用于单独指定某一侧边界的四个具名参数。**

## 解释

不想同时给上下限时，可用 bottom（y 轴下限）、top（y 轴上限）、left（x 轴左界）、right（x 轴右界）只设一侧，另一侧保持自动。y 轴用 bottom/top，x 轴用 left/right，不能混用。

## 有什么用

- 只把 y 轴下探到 -10 而不动上限
- 把 x 轴起点从 0 改为 5

## 关键要点

- y 轴：bottom 为下限、top 为上限
- x 轴：left 为左界、right 为右界
- 可只设一侧，如 ax.set_ylim(bottom=-10)
- 与位置参数写法 ax.set_xlim(0, 10) 可混用

## 边界与易混淆

易错：set_ylim 没有 left/right，set_xlim 没有 bottom/top，写错会抛 TypeError。

## 关联

- [[plt.ylim（y 轴显示范围）]] — 上位概念
- [[ax.axis（一次设置坐标轴四边界）]] — 组合使用

## 自测

只想让 y 轴从 -10 开始、上限保持自动，怎么写？::ax.set_ylim(bottom=-10)
ax.set_xlim(bottom=0) 会怎样？::报错，x 轴没有 bottom 参数，应使用 left/right。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p68 S03E19.坐标轴【下】](https://www.bilibili.com/video/BV1ji4y157uB?p=68) · 2026-11-17
