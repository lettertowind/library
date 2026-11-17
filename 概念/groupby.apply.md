---
term: groupby.apply
aliases: [分组应用, groupby(...).apply(...)]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 41
stage: "S02E26 · 分组与聚合 groupby基础部分"
order: 41
---

# groupby.apply

> 别名：分组应用、groupby(...).apply(...)

**按分组对每个子表调用自定义函数并合并结果。**

## 解释

当每组需要多步操作（如组内排序后 shift 再算环比）时，用 groupby(...).apply(函数) 把整段逻辑封装进函数，对每个城市独立执行，避免跨组串行。

## 有什么用

- 多城市分别计算环比
- 每组需要多列多步处理的场景

## 关键要点

- 先 sort_values 排序再 groupby，保证组内顺序
- group_keys=False 可避免多出分组索引层
- 函数内先 copy() 避免修改原数据告警
- 适合组内多步逻辑，单步聚合用 agg 更快

## 边界与易混淆

性能低于向量化操作；仅当组内逻辑复杂时才用。

## 关联

- [[shift]] — 组合使用
- [[环比]] — 组合使用

## 自测

为什么多城市算环比要先排序再分组再 apply？::排序保证每个城市内部月份顺序正确，分组保证各城市独立 shift 不串行。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
