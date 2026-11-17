---
term: DATEDIF
aliases: [Excel 日期差函数, DATEDIF 公式]
kind: tool
domain: 计算机/办公软件/Excel
tags: [概念/tool, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# DATEDIF

> 别名：Excel 日期差函数、DATEDIF 公式

**Excel 中按指定单位计算两个日期之差的隐藏函数。**

## 解释

语法为 DATEDIF(起始日期, 结束日期, "d")，第三参数 d/m/y 决定返回天、月还是年。在 Excel 中需要手写全称且没有智能提示，而在 Pandas 里等价操作只是两列直接相减。

## 有什么用

- Excel 中算工龄、年龄、间隔天数
- 作为理解 Pandas 日期相减的对照

## 关键要点

- 第三参数 d/m/y 分别表示天、月、年
- 函数属于隐藏函数，输入时没有提示，需要记住全称
- Pandas 中不需要函数，日期列相减即可

## 边界与易混淆

起始日期大于结束日期时 Excel 会报错，而 Pandas 相减得到的是负的 Timedelta。

## 关联

- [[日期差计算]] — 对比项
- [[Timedelta]] — 对比项

## 自测

DATEDIF 返回的是日期还是数值？::数值（整数），单位由第三个参数 d/m/y 决定。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p26 S02E11.列与列之间的计算](https://www.bilibili.com/video/BV1ji4y157uB?p=26) · 2026-11-17
