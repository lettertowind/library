---
term: to_sql
aliases: [DataFrame.to_sql, 写出到数据库]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 16
stage: "S02E01 · 数据类型与新建文件"
---

# to_sql

> 别名：DataFrame.to_sql、写出到数据库

**把 DataFrame 写入 SQL 数据库表的 Pandas 方法。**

## 用法
**语法**：`DataFrame.to_sql(name, con, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None)`
**参数**：
- `name`：目标数据库表名（字符串）
- `con`：数据库连接对象，可以是 `sqlite3.Connection`，也可以是 SQLAlchemy 的 engine
- `if_exists`：表已存在时的处理方式，`'fail'` 表示报错（默认）、`'replace'` 表示先删表重建、`'append'` 表示追加写入
- `index`：是否把行索引也写成一列，默认 `True`；只写数据列时传 `False`
- `index_label`：索引列写进表后的列名
- `chunksize`：分批写入时每批的行数，数据量大时用来控制内存
- `dtype`：用字典指定某些列的数据库类型，如 `{'score': sqlalchemy.types.Integer}`
**示例**：
```python
import pandas as pd
import sqlite3

df = pd.DataFrame({'name': ['张三', '李四'], 'score': [90, 85]})
con = sqlite3.connect(':memory:')                      # 内存数据库，无需额外驱动配置
df.to_sql('score', con, if_exists='replace', index=False)   # index=False 不把行号写进表

print(pd.read_sql('SELECT * FROM score', con).to_dict('records'))
# [{'name': '张三', 'score': 90}, {'name': '李四', 'score': 85}]
df.to_sql('score', con, if_exists='append', index=False)    # 追加一行数据
print(pd.read_sql('SELECT COUNT(*) AS n FROM score', con)['n'].tolist())
# [4]
```

## 解释

to_sql 用于将内存中的二维表数据写入关系型数据库，需要先建立数据库连接。它与 to_csv、to_excel 同属写出方法家族，只是目标从文件变成数据库表。

## 有什么用

- 把分析结果落库供其他系统查询
- 将批量数据导入数据库表

## 关键要点

- 调用形式是 data.to_sql(...)，需传入连接对象
- 与 to_csv、to_excel 并列为三大常用写出方法
- 视频转录中的乱码实为 to_sql 的识别误差
- 掌握这三种写出方法基本够用

## 边界与易混淆

需要数据库驱动和连接配置，不是纯文件操作。

## 关联

- [[DataFrame.to_excel]] — 对比项
- [[to_csv]] — 对比项
- [[DataFrame]] — 上位概念

## 自测

to_sql 和 to_csv 的核心区别是什么？::to_sql 写入数据库表，需要连接对象；to_csv 写入本地纯文本文件，只需路径。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
