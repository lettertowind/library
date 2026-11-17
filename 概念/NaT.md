---
term: NaT
aliases: [Not a Time, 时间空值]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# NaT

> 别名：Not a Time、时间空值

**Pandas 中日期时间类型的缺失值标记，地位等同数值列的 NaN。**

## 解释

日期时间列不能用 NaN 表示缺失，Pandas 专门用 NaT（Not a Time）占位。它会在时间运算、排序、筛选时被自动跳过，但直接参与计算仍会传染成 NaT。想把 NaT 显示成空字符串需专门转换。

## 关键要点

- 只在 datetime 类型列中出现，对应数值列的 NaN
- 与 NaN 混用会导致整列类型异常
- 时间运算遇到 NaT 结果仍为 NaT
- 转成空文本需要额外处理，不能直接 replace

## 边界与易混淆

不要与字符串 'NaT'、None 混为一谈，判空应使用 isna()。

## 关联

- [[NaN]] — 对比项
- [[DatetimeIndex]] — 组合使用
- [[缺失值处理]] — 上位概念

## 自测

时间列里的空值显示成什么？和数值列空值有什么区别？::显示为 NaT；数值列空值是 NaN，两者只在各自类型下出现

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p38 S02E23.字符串操作（上）](https://www.bilibili.com/video/BV1ji4y157uB?p=38) · 2026-11-17
