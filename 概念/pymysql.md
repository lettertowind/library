---
term: pymysql
aliases: [PyMySQL, pymysql 模块]
kind: tool
domain: 数据分析/Python
tags: [概念/tool, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
stage: "S02E03 · 读取Mysql文件"
order: 18
---

# pymysql

> 别名：PyMySQL、pymysql 模块

**纯 Python 实现的 MySQL 客户端库，用于在 Python 中连接和操作 MySQL 数据库。**

## 解释

pymysql 提供 connect() 方法建立到 MySQL 的连接对象，是 pandas 读取 MySQL 数据的前置依赖。它不需要安装 MySQL 的 C 客户端，安装简单，适合数据分析场景。

## 有什么用

- Python 连接 MySQL 数据库
- 为 pd.read_sql 提供连接对象

## 关键要点

- 需先 pip 安装并 import pymysql 才能使用
- 核心入口是 pymysql.connect() 返回连接对象
- 连接对象封装了主机、用户、密码、库名等信息
- 无法使用时通常是未安装该库

## 边界与易混淆

只负责连接与执行 SQL，不做数据分析；数据整理交给 pandas。

## 关联

- [[pd.read_sql]] — 组合使用
- [[pip]] — 前置知识

## 自测

为什么 pandas 读 MySQL 前要先装 pymysql？::pandas 本身不实现 MySQL 协议，需要 pymysql 提供连接对象传给 read_sql 的 con 参数。


### 补充 · 2026-11-17

pandas 自己不会说 MySQL 的协议，需要 pymysql 这类驱动站在中间做翻译：Python 代码 → 数据库连接 → SQL 执行。所以读库前必须先安装并 import 它。

- 属于第三方库，需先安装再 import
- import 报错通常意味着还没安装
- 必须与 pandas 一起导入，缺一不可
代码写了 import pymysql 却报错，最先该检查什么？::检查这个第三方库是否已经安装好。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p18 S02E03.读取Mysql文件](https://www.bilibili.com/video/BV1ji4y157uB?p=18) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
