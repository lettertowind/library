---
term: MySQL
aliases: [MySQL 数据库, 关系型数据库]
kind: tool
domain: 数据分析/数据库
tags: [概念/tool, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# MySQL

> 别名：MySQL 数据库、关系型数据库

**用 SQL 语句管理数据表的主流开源关系型数据库。**

## 解释

数据以表的形式存在，通过 SQL 语句增删改查。Python 无法直接操作它，需要借助 pymysql 这类驱动先建立连接，再由 pandas 把查询结果取成 DataFrame 分析。

## 有什么用

- 业务数据、日志数据的持久化存储
- 数据分析时作为取数源，配合 SQL 查询

## 关键要点

- 属于关系型数据库，数据组织为二维表
- 客户端操作依赖连接信息：主机、用户、密码、库名、编码
- SQL 语句在 MySQL、SQL Server、SQLite 间基本通用
- Python 侧连接依赖第三方驱动 pymysql

## 边界与易混淆

MySQL 只是数据库的一种；SQL 语法通用但不完全等价，不同数据库的方言存在差异。

## 关联

- [[SQL 查询语句]] — 组合使用
- [[pymysql]] — 前置知识
- [[pd.read_sql]] — 组合使用

## 自测

为什么说学会了 SQL 不等于只会在 MySQL 上用？::因为 SQL 是通用查询语言，SQL Server、SQLite 等数据库也支持基本相同的查询语句。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p18 S02E03.读取Mysql文件](https://www.bilibili.com/video/BV1ji4y157uB?p=18) · 2026-11-17
