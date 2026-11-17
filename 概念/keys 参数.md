---
term: keys 参数
aliases: [keys, 层次索引标识, 来源标识]
kind: concept
domain: 计算机/数据分析/Pandas
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 24
stage: "S02E09 · 连接查询之concat"
order: 24
---

# keys 参数

> 别名：keys、层次索引标识、来源标识

**concat 中用于为每个连接对象添加层次索引标签的参数。**

## 解释

keys 参数接收一个列表，列表元素与传入 concat 的对象顺序一一对应，生成外层索引以标识数据来源。添加后可通过外层索引筛选特定来源的数据，也便于后续分组分析。

## 有什么用

- 合并多张表时标识每行数据来自哪张表
- 为后续按来源筛选或分组提供依据

## 关键要点

- keys 列表顺序与传入对象顺序对应
- 生成 MultiIndex 的外层索引
- 可用字典替代 keys 列表，字典 key 作为分组标识
- 便于按来源表筛选数据

## 边界与易混淆

keys 只增加索引层级，不改变数据内容；与 ignore_index=True 同时使用时，keys 仍会保留外层索引。

## 关联

- [[pd.concat]] — 组合使用
- [[分层索引]] — 组合使用

## 自测

pd.concat([df1, df2], keys=['x','y']) 后，如何取出 df2 对应的数据？::使用 loc 按外层索引 'y' 选取，如 result.loc['y']。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
