---
term: groupby
aliases: [分组, DataFrame.groupby, 分组聚合]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 41
stage: "S02E26 · 分组与聚合 groupby基础部分"
order: 41
---

# groupby

> 别名：分组、DataFrame.groupby、分组聚合

**按指定键把数据拆成若干组，再对每组分别计算并合并结果。**

## 解释

groupby 是 Pandas 的核心分组机制，思想是「拆分—应用—合并」：先按一列或多列（或索引层级、函数、字典）把行分组，再对每组应用聚合函数，最后把各组结果拼回一张表。它对应 SQL 的 GROUP BY 和 Excel 的 SUMIF，但聚合方式远不止求和。

## 有什么用

- 按维度汇总数据，如按城市/区域统计人数与金额
- 为后续 agg、transform、apply 提供分组对象
- 替代手工 for 循环逐组计算

## 关键要点

- 语法：df.groupby(按谁分组)[对谁聚合].聚合函数()
- 单个分组键写字符串，多个分组键写列表
- 建议统一写成列表套列表 [["人数"]]，避免格式出错
- 只做一种聚合可直接接 .sum()；多种聚合先保存分组对象复用
- Pandas 中应尽量避免 for 循环遍历分组

## 边界与易混淆

groupby 本身只完成分组，不计算；必须接聚合函数或 agg 才有结果。按索引层级分组需先用 set_index 提升层级。

## 关联

- [[agg]] — 组合使用
- [[set_index]] — 前置知识
- [[分层索引]] — 组合使用
- [[pivot_table]] — 对比项

## 自测

groupby 之后不加聚合函数，得到的是什么？::一个 DataFrameGroupBy 分组对象，尚未产生计算结果。
为什么建议把聚合列写成 [["人数"]] 而不是 ["人数"]？::列表套列表保证结果仍是 DataFrame，分组键增多时也不易写错格式。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
