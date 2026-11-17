---
term: notna
aliases: [notnull, df.notna, 判断非缺失值]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# notna

> 别名：notnull、df.notna、判断非缺失值

**逐元素判断是否为非缺失值，返回布尔表，True 表示非空。**

## 解释

notna() 与 notnull() 等价，是 isna 的取反。用于保留有效数据、统计非空数量，或在填充前确认哪些位置需要处理。

## 有什么用

- 筛选出非空行
- 统计每列有效值数量

## 关键要点

- notna 与 notnull 是同一函数
- True 表示非缺失，与 isna 相反
- 常与 sum() 组合统计有效值数量
- 可用于布尔索引保留有效行

## 边界与易混淆

同样只识别空值形态的缺失。

## 关联

- [[isnull]] — 对比项
- [[缺失值处理]] — 上位概念

## 自测

想统计每列有效值个数，用哪个函数？::df.notna().sum()。
notna 与 notnull 有区别吗？::没有，是同一函数的别名。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
