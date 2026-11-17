---
term: ascending 参数
aliases: [ascending, 升序降序参数, 排序方向]
kind: concept
domain: 计算机/数据分析/Pandas
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# ascending 参数

> 别名：ascending、升序降序参数、排序方向

**控制排序方向是升序还是降序的布尔参数。**

## 解释

ascending=True 为升序（默认），False 为降序。多字段排序时可传列表，为每个字段分别指定方向。

## 有什么用

- 单字段控制升降序
- 多字段为每列分别指定方向

## 关键要点

- 默认 True，即升序
- False 表示降序
- 多字段时写列表，与 by 顺序一一对应
- sort_index 也支持该参数

## 边界与易混淆

多字段时若只写单个布尔值，会对所有字段统一生效，而非分别指定。

## 关联

- [[sort_values]] — 上位概念
- [[by 参数]] — 组合使用

## 自测

ascending=[False, True] 配合 by=['语文','数学'] 是什么效果？::语文降序，语文相同时数学升序

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
