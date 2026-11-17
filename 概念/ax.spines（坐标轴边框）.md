---
term: ax.spines（坐标轴边框）
aliases: [spines, ax.spines, spine, 坐标轴边框集合]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E18 · 坐标轴【上】"
order: 67
created: 2026-11-17
updated: 2026-11-17
---

# ax.spines（坐标轴边框）

> 别名：spines、ax.spines、spine、坐标轴边框集合

**Axes 上按 top/right/left/bottom 索引的四条边框线集合，可单独设色或隐藏。**

## 解释

绘图区四周的线不是坐标轴本身，而是 spines 边框，因此可逐条控制。用 ax.spines['top'].set_color('none') 即可隐藏某条边框，用其他颜色则更换样式。最常见的用法是去掉上、右边框，只留下、左两条，使统计图更简洁。

## 有什么用

- 隐藏上/右边框，做出简洁的趋势图、统计图
- 给某条边框换颜色，配合刻度位置的调整

## 关键要点

- 四个键 top/right/left/bottom 分别对应上右下左四条边框
- set_color('none') 才是真正隐藏；设成白色在彩色背景下仍可见
- 隐藏边框不等于隐藏刻度，刻度要另用 plt.xticks([])/plt.yticks([])
- 移动刻度位置后必须同步改边框颜色，否则刻度落在被隐藏的线上

## 边界与易混淆

spines 只控制边框线，不管刻度刻线、刻度文字和轴标签；'none' 是无颜色，不是白色也不是透明填充。

## 关联

- [[set_ticks_position（刻度位置设置）]] — 对比项
- [[刻度标签（ticklabels）]] — 对比项
- [[plt.gca 与 plt.gcf]] — 组合使用

## 自测

想把上边框去掉，把颜色设成 'white' 能达到目的吗？::不能，白色只是把线画成背景色，背景一换就露出来，应设为 'none'。
已经隐藏了左、下边框，为什么图上还有刻度？::spines 只管边框线，刻度由 ticks 控制，需要另外调用 plt.xticks([]) / plt.yticks([])。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p67 S03E18.坐标轴【上】](https://www.bilibili.com/video/BV1ji4y157uB?p=67) · 2026-11-17
