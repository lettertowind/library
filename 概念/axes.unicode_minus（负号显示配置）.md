---
term: axes.unicode_minus（负号显示配置）
aliases: [unicode_minus, 负号显示为方块, 负号乱码, axes.unicode_minus=False]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E19 · 坐标轴【下】"
order: 68
created: 2026-11-17
updated: 2026-11-17
---

# axes.unicode_minus（负号显示配置）

> 别名：unicode_minus、负号显示为方块、负号乱码、axes.unicode_minus=False

**控制 Matplotlib 是否使用 Unicode 减号的 rcParams 开关，关闭后负数才能正常显示。**

## 解释

默认 True 时负号用 Unicode 减号，中文字体常缺这个字形，于是负数刻度显示成方块甚至抛错。设 plt.rcParams['axes.unicode_minus'] = False 改用 ASCII 连字符即可恢复正常。

## 有什么用

- 刻度或数据含负数时出现方块或报错
- 中文绘图环境的初始化配置

## 关键要点

- 写法：plt.rcParams['axes.unicode_minus'] = False
- 典型现象：-4、-17 的负号变成方块或报错
- 需在绘图前设置，且与中文字体配置常成对出现
- 只修负号字形，不解决中文乱码

## 边界与易混淆

与 font.sans-serif 中文字体设置是两件独立的事，中文乱码要靠后者解决。

## 关联

- [[Matplotlib 中文显示配置]] — 组合使用
- [[MultipleLocator]] — 组合使用

## 自测

图上负数刻度显示成小方块，改哪一行配置？::plt.rcParams['axes.unicode_minus'] = False
设了 unicode_minus=False 中文标题还是乱码，说明什么？::中文乱码由字体配置决定，需另设 font.sans-serif 等中文字体。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p68 S03E19.坐标轴【下】](https://www.bilibili.com/video/BV1ji4y157uB?p=68) · 2026-11-17
