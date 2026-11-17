---
term: value_counts
aliases: [df['列'].value_counts, 频数统计, 出现次数统计]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# value_counts

> 别名：df['列'].value_counts、频数统计、出现次数统计

**统计 Series 中每个取值出现的次数并按频数排序。**

## 解释

value_counts() 对一列数据做频数统计，返回每个取值及其出现次数。它是重复值处理的基础统计方法，可快速看出哪些值重复、重复几次。

## 有什么用

- 统计每个人下了多少次订单
- 查看某列各取值的出现频次

## 关键要点

- 返回 Series，索引为取值、值为出现次数
- 默认按次数降序排列
- 常与 duplicated 配合先看频次再处理重复

## 边界与易混淆

只做统计不修改数据；需要按频数筛选或去重仍需 drop_duplicates 或布尔索引。

## 关联

- [[duplicated]] — 前置知识
- [[unique]] — 对比项

## 自测

有订单号和姓名两列，想统计每个人对应多少订单，用什么方法？::df['姓名'].value_counts()，统计姓名出现次数即订单数。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
