---
term: 聚合函数 NA 忽略特性
aliases: [skipna, 聚合忽略缺失值, 非 NA 聚合]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 31
stage: "S02E16 · 处理缺失值"
---

# 聚合函数 NA 忽略特性

> 别名：skipna、聚合忽略缺失值、非 NA 聚合

**Pandas 聚合函数默认跳过 NA 值，只对非缺失值计算。**

## 解释

count、sum、mean、median、std、var、max、min、prod、first、last 等聚合默认忽略 NA。这意味着 count 统计的是非空个数，sum 不会因缺失而变 NaN，与空值传播的算术运算不同。

## 有什么用

- 分组聚合前评估缺失影响
- 理解 count 与 size 的差异
- 决定是否需要先 fillna

## 关键要点

- count 返回非 NA 个数，size 返回全部行数
- sum/mean 等默认 skipna=True，跳过缺失值
- first/last 取第一个/最后一个非 NA 值
- 聚合前应先检查数据是否存在 NA

## 边界与易混淆

与普通算术运算的 NaN 传播行为不同，容易混淆。

## 关联

- [[Pandas 数学统计函数]] — 上位概念
- [[空值传播]] — 对比项
- [[缺失值处理]] — 组合使用

## 自测

某组有 5 行、其中 2 个成绩为 NaN，count 和 size 分别返回多少？::count 返回 3，size 返回 5。
为什么 sum 遇到 NaN 不会返回 NaN？::聚合函数默认 skipna=True，跳过缺失值计算。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
