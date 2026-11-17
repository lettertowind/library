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
order: 32
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

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
