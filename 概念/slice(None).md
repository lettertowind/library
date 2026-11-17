---
term: slice(None)
aliases: [slice(None), 全部切片, 任意所有行]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 35
stage: "S02E20 · 多层索引与多层索引计算"
order: 35
---

# slice(None)

> 别名：slice(None)、全部切片、任意所有行

**在多层索引查询中表示某一层取全部标签的切片写法。**

## 解释

多层索引用 .loc 查询时，若想选外层索引下的所有内层行，内层不能简单写冒号，而要用 slice(None) 表示“全部”。它等价于 Python 切片中的 [:] 语义。

## 有什么用

- 查询某个外层索引下的全部内层行
- 多层索引中表达“任意”标签

## 关键要点

- slice(None) 表示该层取全部
- 多层行索引中不能只用冒号表示全部内层
- 常与元组形式的行标签配合使用

## 边界与易混淆

只在多层索引的 .loc 元组查询中有此特殊要求，单层索引直接用冒号即可。

## 关联

- [[分层索引]] — 组合使用
- [[loc]] — 组合使用

## 自测

查询“一班”下所有学号的数据，行标签应该怎么写？::data.loc[('一班', slice(None)), :]

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
