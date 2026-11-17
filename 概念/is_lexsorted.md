---
term: is_lexsorted
aliases: [index.is_lexsorted, 索引有序性检查]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 35
stage: "S02E20 · 多层索引与多层索引计算"
order: 35
---

# is_lexsorted

> 别名：index.is_lexsorted、索引有序性检查

**检查多层索引是否按字典序排好序的方法。**

## 解释

is_lexsorted 返回布尔值，用于判断 MultiIndex 是否处于有序状态。无序索引直接查询可能报错，因此查询前可用它检查，必要时先 sort_index 排序。

## 有什么用

- 查询前检查多层索引是否有序
- 判断是否需要先排序

## 关键要点

- 返回 True 表示索引已按字典序排列
- 无序索引直接查询可能报错
- 检查后可配合 sort_index 先排序再查询

## 边界与易混淆

不是所有无序查询都会报错，但为安全起见建议先排序。

## 关联

- [[分层索引]] — 组合使用
- [[sort_index]] — 组合使用

## 自测

is_lexsorted 返回 False 时应该怎么处理再查询？::先用 sort_index 对索引排序，再用 .loc 查询。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
