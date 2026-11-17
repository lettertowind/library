---
term: GROUP BY
aliases: [SQL 分组子句, GROUPBY, 分组查询]
kind: concept
domain: 数据分析/数据库
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# GROUP BY

> 别名：SQL 分组子句、GROUPBY、分组查询

**SQL 中按指定字段分组并对每组聚合的子句。**

## 解释

GROUP BY 把分组键相同的行归为一组，再配合 COUNT、SUM、AVG 等聚合函数得到每组汇总结果。Pandas 的 groupby 在思路上与它相近。

## 有什么用

- SQL 中的分组汇总
- 按维度统计数量、金额、均值等

## 关键要点

- 通常与 COUNT、SUM、AVG 等聚合函数连用
- SELECT 中的非聚合列一般必须出现在 GROUP BY 中
- 可写多个字段实现多级分组
- Pandas 用 groupby 对应其分组思路

## 边界与易混淆

GROUP BY 会把多行压缩为每组一行；窗口函数则保留明细行，两者不要混淆。

## 关联

- [[SQL 查询语句]] — 上位概念
- [[groupby]] — 对比项

## 自测

SQL 中 SELECT 里的非聚合列通常要满足什么条件？::必须出现在 GROUP BY 子句中，或由聚合函数包裹。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p41 S02E26.分组与聚合 groupby基础部分](https://www.bilibili.com/video/BV1ji4y157uB?p=41) · 2026-11-17
