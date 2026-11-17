---
term: crosstab
aliases: [pd.crosstab, 交叉表]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# crosstab

> 别名：pd.crosstab、交叉表

**按行、列两个维度统计频数的交叉计数表。**

## 解释

crosstab 可以看作 pivot_table 的计数特例，默认就是计数，不需要指定 aggfunc。index 指定行分组条件（可传列表形成多层），columns 指定统计对象，margins=True 可加小计总计。适合统计记录条数、订单笔数、出现频次。

## 有什么用

- 统计每月每区域各部门的记录条数
- 频数分布、列联表分析

## 关键要点

- 核心记忆：交叉表就是计数
- index 传列表可实现多条件行分组
- columns 指定被计数的对象列
- 默认计数，无需写 aggfunc
- 结果数字是记录条数，不一定是人数

## 边界与易混淆

需要求和、平均等非计数聚合时应改用 pivot_table。

## 关联

- [[pivot_table]] — 上位概念
- [[dt 访问器]] — 组合使用

## 自测

要统计每个月份、每个区域下各部门出现多少条记录，用哪个方法最直接？::pd.crosstab，index 传 [月份, 区域]，columns 传部门。
crosstab 结果里的数字代表什么？::记录条数/频数，不是人数或金额。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
