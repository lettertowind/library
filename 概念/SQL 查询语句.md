---
term: SQL 查询语句
aliases: [SQL, select 语句, 结构化查询语言]
kind: concept
domain: 计算机/数据分析/数据库
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
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

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
