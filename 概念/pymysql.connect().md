---
term: pymysql.connect()
aliases: [connect, 建立数据库连接, 连接对象]
kind: method
domain: 数据分析/Python
tags: [概念/method, 领域/数据分析]
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


### 补充 · 2026-11-17

它相当于「登录数据库」这一步，返回的连接对象内部封装了主机、用户名、密码、库名和编码。之后把该对象交给 pd.read_sql，就能执行查询。

- 五大参数：host、user、password、database、charset
- host='localhost' 表示连接本机数据库
- 参数必须换成本机环境的值，不能照搬示例账号密码
别人用你写的 host='localhost', user='root' 能在自己电脑上连上你的库吗？::不能，localhost 指本机，连接参数必须按各自的实际环境填写。
连接对象和读取到的数据表是同一个东西吗？::不是，连接对象只承载登录信息，数据要通过查询语句经它取回。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p18 S02E03.读取Mysql文件](https://www.bilibili.com/video/BV1ji4y157uB?p=18) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
