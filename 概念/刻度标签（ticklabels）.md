---
term: 刻度标签（ticklabels）
aliases: [ticklabels, get_xticklabels, get_yticklabels, 刻度文字]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E18 · 坐标轴【上】"
order: 67
created: 2026-11-17
updated: 2026-11-17
---

# 刻度标签（ticklabels）

> 别名：ticklabels、get_xticklabels、get_yticklabels、刻度文字

**坐标轴上显示刻度数值的文字对象，用 get_xticklabels() 取到列表后可逐个改样式。**

## 解释

刻度标签是 Text 对象而不是刻度线，因此可以单独设颜色、字号来突出某个值。ax.get_xticklabels() 返回 x 轴刻度文字列表，按索引取一个后调用 set_color/set_fontsize，或用 plt.setp 一次设多个属性。

## 有什么用

- 把某个关键刻度值放大标红，让观众注意
- 批量统一刻度文字的字号与颜色

## 关键要点

- get_xticklabels() 取 x 轴、get_yticklabels() 取 y 轴，都返回列表
- Python 索引从 0 开始，「第二个标签」应写 [1] 而不是 [2]
- plt.setp(labels[1], color='red', fontsize=30) 可一次设多个属性
- 改的是文字外观；要隐藏刻度得用 plt.xticks([])

## 边界与易混淆

与 spines（边框线）、ticks（刻度刻线）是不同对象；突出某个数据点也可以用 annotate 注释实现。

## 关联

- [[ax.spines（坐标轴边框）]] — 对比项
- [[set_ticks_position（刻度位置设置）]] — 组合使用
- [[数值索引替代字符串类别轴]] — 对比项

## 自测

要突出显示 x 轴的第三个刻度标签，索引该写几？为什么？::写 labels[2]，因为列表索引从 0 开始，第三个元素下标是 2。
get_xticklabels() 改的是刻度线还是刻度文字？::改的是刻度文字（Text 对象），刻度刻线的位置由 set_ticks_position 等方法控制。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p67 S03E18.坐标轴【上】](https://www.bilibili.com/video/BV1ji4y157uB?p=67) · 2026-11-17
