---
term: pymysql.connect()
aliases: [connect, 建立数据库连接, 连接对象]
kind: method
domain: 计算机/数据分析/Python
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
stage: "S02E03 · 读取Mysql文件"
order: 18
---

# pymysql.connect()

> 别名：connect、建立数据库连接、连接对象

**用一组连接参数创建 MySQL 连接对象的函数，是读取数据库的第一步。**

## 解释

connect() 接收 host、user、password、database、charset 等参数，返回的连接对象代表一次已登录的数据库会话。该对象随后作为 con 参数传给 pd.read_sql()。

## 有什么用

- 建立与 MySQL 的会话
- 为 read_sql 提供 con 参数

## 关键要点

- host 填主机地址，本机通常为 localhost
- user/password/database 按自己环境填写
- MySQL 编码写 charset='utf8'，不是 utf-8
- 连接对象已包含全部登录信息，无需重复传参

## 边界与易混淆

连接参数因环境而异，示例中的 root/1234/test 仅为演示值。

## 关联

- [[pymysql]] — 上位概念
- [[pd.read_sql]] — 组合使用

## 自测

charset 参数为什么写 utf8 而不是 utf-8？::MySQL 的字符集名称规范是 utf8，写成 utf-8 可能不被识别。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
