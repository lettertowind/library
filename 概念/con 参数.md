---
term: con 参数
aliases: [con, read_sql 的 con, 连接参数]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# con 参数

> 别名：con、read_sql 的 con、连接参数

**pd.read_sql 中用来传入数据库连接对象的关键字参数。**

## 用法
**语法**：`pd.read_sql(sql, con, index_col=None, params=None, parse_dates=None, chunksize=None)`
**参数**：
- `sql`：要执行的查询语句字符串，说明“查什么”
- `con`：数据库连接对象，即 `pymysql.connect()` 或 `sqlite3.connect()` 的返回值；它说明“连哪里”，必须用关键字传入
- `index_col`：指定某一列作为结果 DataFrame 的索引，默认 `None`
- `params`：配合 SQL 占位符传入的参数，可以是列表、元组或字典
- `parse_dates`：需要解析成日期类型的列名或列名列表
- `chunksize`：设定每块的行数，返回可迭代对象，适合大表分块读取
**示例**：
```python
import pandas as pd
import sqlite3  # 用 sqlite 演示，con 的用法与 pymysql.connect() 完全一致

conn = sqlite3.connect(":memory:")                      # 连接对象自带库信息
pd.DataFrame({"name": ["Tom", "Amy"], "score": [90, 85]}).to_sql("score", conn, index=False)

df = pd.read_sql("SELECT * FROM score", con=conn)       # con 传连接对象，不是表名
print(df)
#   name  score
# 0  Tom     90
# 1  Amy     85

df2 = pd.read_sql("SELECT * FROM score WHERE score > ?", con=conn, params=[88])  # 同一 conn 可复用
print(len(df2))   # 1
conn.close()
```

## 解释

read_sql 需要知道去哪里取数，con 就是那条通道——把 pymysql.connect() 建好的连接对象交给它。连接对象里已含主机、用户名、密码、库名，所以传入 con 就等于完成了登录，不必再重复写账号信息。

## 有什么用

- 用 pandas 从 MySQL 读取数据时传入连接对象
- 把查询结果转成 DataFrame 后继续做分析

## 关键要点

- 写法固定为 pd.read_sql(sql, con=conn)，con 必须用关键字传
- con 接收的是连接对象，不是表名、不是 SQL 语句
- 连接对象自带登录信息，故 con 内部无需再写账号密码
- 同一个 conn 可复用多次查询，避免反复建立连接

## 边界与易混淆

con 与第一个参数 sql 分工明确：sql 说明查什么，con 说明连哪里，两者不可互换。

## 关联

- [[pd.read_sql]] — 组合使用
- [[pymysql.connect()]] — 前置知识

## 自测

read_sql 的 con 参数如果误传成表名字符串，会发生什么？::无法建立连接，因为 con 需要的是带登录信息的连接对象，不是表名。
为什么 con=conn 里不需要再写用户名和密码？::因为 conn 这个连接对象在创建时已经封装了 host、user、password、database 等信息。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p18 S02E03.读取Mysql文件](https://www.bilibili.com/video/BV1ji4y157uB?p=18) · 2026-11-17
