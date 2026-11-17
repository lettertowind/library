---
term: to_sql
aliases: [DataFrame.to_sql, 写出到数据库]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 16
stage: "S02E01 · 数据类型与新建文件"
order: 16
---

# to_sql

> 别名：DataFrame.to_sql、写出到数据库

**把 DataFrame 写入 SQL 数据库表的 Pandas 方法。**

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
