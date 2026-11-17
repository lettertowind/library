---
term: pd.read_sql
aliases: [read_sql, 读取 SQL 数据, pandas 读数据库]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 18
stage: "S02E03 · 读取Mysql文件"
order: 18
---

# pd.read_sql

> 别名：read_sql、读取 SQL 数据、pandas 读数据库

**执行 SQL 查询并把结果直接转成 DataFrame 的 pandas 函数。**

## 解释

read_sql(sql, con) 把 SQL 语句交给连接对象执行，返回结果集并自动整理为 DataFrame，省去手工建表的步骤。它是 read_csv 的数据库版本，用法结构高度相似。

## 有什么用

- 从 MySQL 等数据库直接取数进 DataFrame
- 替代导出 CSV 再读取的中间步骤

## 关键要点

- 第一个参数 sql 是查询语句字符串
- 第二个参数 con 是数据库连接对象
- 支持索引相关等参数，与 read_csv 思路相近
- 核心模式：连接对象 + SQL + read_sql

## 边界与易混淆

只负责取数，复杂清洗仍需后续 pandas 操作；SQL 写错会在执行时报错。

## 关联

- [[pd.read_csv]] — 对比项
- [[pymysql.connect()]] — 组合使用
- [[DataFrame]] — 下位概念

## 自测

read_sql 和 read_csv 在用法结构上最大的共同点是什么？::都是 pd.read_xxx(数据源) 的形式，返回 DataFrame，后续处理完全一致。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
