---
term: isna
aliases: [isnull, df.isna, 判断缺失值]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# isna

> 别名：isnull、df.isna、判断缺失值

**逐元素判断是否为缺失值，返回同形状的布尔表。**

## 解释

isna() 与 isnull() 完全等价，返回 True 表示该位置缺失、False 表示非空。它是查看缺失值分布的基础工具，结果可直接用于筛选或计数。

## 有什么用

- 快速定位空值位置
- 配合 sum 统计每列缺失数量

## 关键要点

- isna 与 isnull 是同一函数的两个名字
- 返回布尔 DataFrame/Series，True 代表缺失
- 常与 sum() 组合统计各列缺失数
- 与 notna/notnull 互为取反

## 边界与易混淆

只判断空值形态的缺失，不识别占位符等隐性缺失。

## 关联

- [[notnull]] — 对比项
- [[缺失值处理]] — 上位概念
- [[布尔索引筛选]] — 组合使用

## 自测

df.isna().sum() 得到的是什么？::每一列缺失值的数量。
isna 和 notna 的结果是什么关系？::逻辑取反关系，同一位置结果相反。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
