---
term: join_axes 参数
aliases: [join_axes, join_axis, 对齐基准轴]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 24
stage: "S02E09 · 连接查询之concat"
order: 24
---

# join_axes 参数

> 别名：join_axes、join_axis、对齐基准轴

**旧版 Pandas 中 concat 的参数，指定以某个对象的索引为对齐基准。**

## 解释

join_axes 用于横向拼接时，以指定对象的索引为基准，将其他对象的数据按该索引匹配过来，效果类似 Excel 的 VLOOKUP。该参数在新版 Pandas 中已被移除，可用 merge 或 reindex 替代。

## 有什么用

- 需要以某张表的索引为基准进行横向对齐时
- 旧版 Pandas 代码维护

## 关键要点

- 以指定索引为基准，保留基准索引，匹配其他表数据
- 效果类似 VLOOKUP：基准表有的索引保留，没有的不保留
- 新版 Pandas 已弃用，建议用 merge 或 reindex 替代

## 边界与易混淆

仅适用于旧版 Pandas；新版应使用 merge(how='left') 或 reindex 实现相同效果。

## 关联

- [[pd.concat]] — 组合使用
- [[索引对齐]] — 前置知识

## 自测

join_axes=df1.index 在横向拼接时起什么作用？::以 df1 的索引为基准，只保留 df1 中存在的索引，其他表按此索引匹配数据。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
