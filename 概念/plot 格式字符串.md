---
term: plot 格式字符串
aliases: [fmt, 'ro-', 'ro', 'o', 颜色标记线型简写]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E23 · 标题及轴标签"
order: 72
created: 2026-11-17
updated: 2026-11-17
---

# plot 格式字符串

> 别名：fmt、'ro-'、'ro'、'o'、颜色标记线型简写

**用 'ro-' 这类短字符串同时指定颜色、标记点和线型的简写写法。**

## 解释

plt.plot(x, y, 'ro-') 中的每个字符各管一件事：r 是红色，o 是圆点标记，- 是实线连接。它等价于分别写 color='red'、marker='o'、linestyle='-'，但更紧凑，是快速出图时最常用的写法。

## 有什么用

- 快速指定点的颜色和标记形状
- 把散点和连线一次性画出来

## 关键要点

- 颜色字符如 r/g/b，标记字符如 o/s/^，线型字符如 -、--、:
- 只写 'o' 时不画连线，相当于只画散点
- 'ro' 与 'or' 解析结果相同，惯例顺序是颜色→标记→线型
- 线宽、标记大小等细节仍需 linewidth、markersize 单独设置

## 边界与易混淆

格式字符串只能表达颜色/标记/线型三类，与关键字参数同时出现时关键字参数优先。

## 关联

- [[plt.plot]] — 上位概念
- [[linestyle 线型参数]] — 对比项
- [[linewidth 线宽参数]] — 对比项

## 自测

plt.plot(x, y, 'ro-') 和 plt.plot(x, y, 'o') 画出来的图有什么区别？::前者是红色圆点并用线连起来，后者只画点不连线。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p72 S03E23.标题及轴标签](https://www.bilibili.com/video/BV1ji4y157uB?p=72) · 2026-11-17
