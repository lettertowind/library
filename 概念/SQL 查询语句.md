---
term: SQL 查询语句
aliases: [SQL, select 语句, 结构化查询语言]
kind: concept
domain: 数据分析/数据库
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
stage: "S02E03 · 读取Mysql文件"
order: 18
---

# SQL 查询语句

> 别名：SQL、select 语句、结构化查询语言

**用于从关系型数据库中检索和操作数据的通用语言，跨数据库产品通用。**

## 解释

SQL 是访问关系型数据库的标准语言，MySQL、SQL Server、SQLite 等都支持。数据分析中取数几乎都靠 SQL，因此它是读数据库的前置能力。

## 有什么用

- 从数据库表中筛选、聚合数据
- 作为 read_sql 的查询输入

## 关键要点

- SQL 语句在不同数据库间基本通用
- 最常用形式是 select * from 表名
- 是数据分析的必备基础能力
- 写进 read_sql 前需保证语法正确

## 边界与易混淆

各数据库方言存在差异，复杂函数不一定完全通用。

## 关联

- [[pd.read_sql]] — 前置知识
- [[pymysql]] — 组合使用

## 自测

为什么说学好 SQL 对数据分析是刚需？::数据大多存放在关系型数据库中，取数环节必须用 SQL，且它跨数据库通用。


### 补充 · 2026-11-17

Python 读库时必须告诉数据库「要哪些数据」，这就是 SQL 的职责。最常见的形如 select * from 表名，取全表数据；也可加条件、聚合后再交给 pandas。

- 基本结构：select 字段 from 表名（可加 where、group by）
- select * 表示取全部列
- 表名、字段名需按自己的数据库实际填写
为什么不宜总是 select * 取全表再在 pandas 里过滤？::会传输大量无用数据，速度慢；能在数据库内先过滤聚合就应该先做。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p18 S02E03.读取Mysql文件](https://www.bilibili.com/video/BV1ji4y157uB?p=18) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
