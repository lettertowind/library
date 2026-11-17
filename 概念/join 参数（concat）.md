---
term: join 参数（concat）
aliases: [join, join='inner', join='outer']
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 24
stage: "S02E09 · 连接查询之concat"
---

# join 参数（concat）

> 别名：join、join='inner'、join='outer'

**concat 中控制索引对齐方式的参数，可选 inner 或 outer。**

## 解释

当 concat 沿 axis=1 横向拼接时，join 参数决定保留哪些行索引。inner 取交集，只保留所有对象共有的索引；outer 取并集，保留所有索引，缺失处填 NaN。默认值为 outer。

## 有什么用

- 横向拼接时控制保留共同索引还是全部索引
- 需要严格对齐时使用 inner，需要完整保留时使用 outer

## 关键要点

- join='inner' 取交集，只保留共同索引
- join='outer' 取并集，缺失填 NaN（默认）
- 仅影响索引对齐，不改变列字段对齐规则
- 不要与 DataFrame.join 方法混淆

## 边界与易混淆

join 参数仅在 concat 中生效，且主要影响 axis=1 时的行索引对齐；axis=0 时 join 参数作用有限。

## 关联

- [[pd.concat]] — 组合使用
- [[索引对齐]] — 前置知识

## 自测

pd.concat([df1, df4], axis=1, join='inner') 的结果行索引是什么？::df1 和 df4 行索引的交集。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
