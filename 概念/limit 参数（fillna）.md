---
term: limit 参数（fillna）
aliases: [limit, 填充数量限制, fillna limit]
kind: concept
domain: 计算机/数据分析/Pandas
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# limit 参数（fillna）

> 别名：limit、填充数量限制、fillna limit

**fillna 中限制每个填充方向最多填充的缺失值个数。**

## 解释

limit=n 表示沿填充方向最多只填 n 个空值，之后的空值保持原样。常用于只补最近几个空缺、避免过度填充的场景。

## 有什么用

- 只补少量连续空缺
- 控制填充范围避免失真

## 关键要点

- limit 控制的是填充个数
- 超出 limit 的空值保持为空
- 需与 method 或方向配合使用
- 可类比 MySQL 中 limit 控制条数

## 边界与易混淆

limit 不指定方向时依赖 method/axis 的默认行为。

## 关联

- [[fillna]] — 上位概念
- [[method 参数（fillna）]] — 组合使用

## 自测

fillna(method='ffill', limit=2) 的效果是什么？::每个连续空缺段最多向下填 2 个值，其余保持为空。
limit 限制的是填充方向还是填充总数？::限制每个填充方向上的填充个数。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
