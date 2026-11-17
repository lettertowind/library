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
---

# pd.read_sql

> 别名：read_sql、读取 SQL 数据、pandas 读数据库

**执行 SQL 查询并把结果直接转成 DataFrame 的 pandas 函数。**

## 用法
**语法**：`pd.read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)`
**参数**：
- `sql`：SQL 查询语句字符串，执行结果就是返回的 DataFrame
- `con`：数据库连接对象，如 `sqlite3.Connection` 或 SQLAlchemy 的 Engine（`pymysql.connect()` 连接 MySQL）
- `index_col`：把结果集中某一列设为 DataFrame 的索引
- `columns`：只读取指定列名的列表（配合 sql 里的 SELECT 使用）
- `parse_dates`：需要解析成 datetime 的列名或列名列表
- `chunksize`：设置后返回可迭代的读取器，按块处理大结果集
**示例**：
```python
import pandas as pd
import sqlite3

con = sqlite3.connect(":memory:")  # 内存库代替 MySQL，模式完全一致
pd.DataFrame({"姓名": ["小明", "小红"], "分数": [90, 85]}).to_sql("score", con, index=False)

df = pd.read_sql("SELECT * FROM score", con)
print(df)
#    姓名  分数
# 0  小明  90
# 1  小红  85

df2 = pd.read_sql("SELECT * FROM score", con, index_col="姓名")
print(df2)
#       分数
# 姓名
# 小明   90
# 小红   85
```

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


### 补充 · 2026-11-17

它省去了「先取游标再逐行取值再拼表」的繁琐流程，一条查询就能拿到结构化表。第一个位置参数放 SQL 语句说明查什么，con 参数放连接对象说明连哪里。

- 第一个参数是 SQL 字符串，第二个是 con=连接对象
- 返回结果本身就是 DataFrame，可直接套用后续 pandas 方法
- 与读文件的 read_csv 用法相似，索引类参数思路一致
read_sql 返回的是游标还是 DataFrame？::DataFrame，可直接继续用 pandas 方法处理。
同一份数据，用 read_csv 和 read_sql 读，主要差别在哪？::数据来源和连接方式不同：前者读本地文件，后者需要 SQL 语句加数据库连接对象。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p18 S02E03.读取Mysql文件](https://www.bilibili.com/video/BV1ji4y157uB?p=18) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
