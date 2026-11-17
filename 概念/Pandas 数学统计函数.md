---
term: Pandas 数学统计函数
aliases: [统计函数家族, count/sum/mean/median/min/max/mode/prod/var/std/quantile/cummax/cummin/cov/corr]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 32
stage: "S02E17 · 数学统计函数"
---

# Pandas 数学统计函数

> 别名：统计函数家族、count/sum/mean/median/min/max/mode/prod/var/std/quantile/cummax/cummin/cov/corr

**DataFrame/Series 上点调用的一组内置统计方法，覆盖计数到相关分析。**

## 解释

Pandas 把常用统计量做成对象方法，统一用“对象.函数名()”调用。记住 describe() 即可覆盖大部分场景，其余按需查表。

## 有什么用

- 对某列快速求均值、最大值等单项统计
- 按需组合多个统计量做分析

## 关键要点

- 统一用法：df['列'].函数名()
- 平均值用 mean 不是 average
- cummax/cummin 是累积统计
- cov/corr 用于两列关系分析
- 不必全记，会查表即可

## 边界与易混淆

默认跳过非数值列；分类列统计需用 value_counts。

## 关联

- [[describe()]] — 下位概念
- [[Series]] — 组合使用
- [[DataFrame]] — 组合使用

## 自测

想求某列平均值，Pandas 中应调用哪个方法？::mean()，不是 Excel 里的 average。
cummax 和 max 有什么区别？::max 返回整列最大值，cummax 返回逐行的累积最大值序列。


### 补充 · 2026-11-17

这些函数既能在整表/整列上直接调用，也能接在 groupby 后面按组计算。它们默认跳过 NA 值，因此 count 统计的是非空数量而非行数，first/last 取的是第一个/最后一个非 NA 值。

- 常用：count、sum、mean、median、std、var、max、min、prod。
- first / last 返回第一个 / 最后一个非 NA 值。
- 所有函数默认跳过 NA，结果可能与行数不符。
某组共 5 行但有 2 个 NA，count 和 sum 分别怎么处理？::count 返回 3（非 NA 计数），sum 对这 3 个非 NA 值求和。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p42 S02E27.分组对象和创建](https://www.bilibili.com/video/BV1ji4y157uB?p=42) · 2026-11-17

这组方法覆盖计数、求和、平均、中位数、众数、乘积、方差、标准差、分位数、累积极值、协方差和相关系数。用法高度统一：对整个表写 df.mean()，对单列写 df['语文'].mean()，对多列先选列再调用。不需要全部背下来，记住函数名和用途、需要时查表即可。

- 平均数的函数名是 mean，不是 Excel 里的 average
- 调用形式统一为「对象.函数名()」，方差写 var()、标准差写 std()
- cummax/cummin 返回与原数据等长的累积序列，不是单个值
想求语文成绩的平均数，写 df['语文'].average() 为什么报错？::Pandas 中平均数方法名是 mean，average 是 Excel 的叫法。
cummax() 和 max() 的结果有什么区别？::max() 返回一个最大值标量；cummax() 返回与原数据等长的序列，每个位置是到此为止的累积最大值。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p32 S02E17.数学统计函数](https://www.bilibili.com/video/BV1ji4y157uB?p=32) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
