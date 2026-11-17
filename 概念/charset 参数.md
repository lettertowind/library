---
term: charset 参数
aliases: [charset, charset='utf8', MySQL 编码参数]
kind: method
domain: 数据分析/数据库
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# charset 参数

> 别名：charset、charset='utf8'、MySQL 编码参数

**建立 MySQL 连接时指定字符编码的参数，取值写 utf8。**

## 解释

它决定 Python 与 MySQL 之间传输文本使用的字符集，写错会出现中文乱码或写入失败。最容易踩的坑是照搬 Python 习惯写成 utf-8——在 MySQL 语境里要写 utf8。

## 有什么用

- pymysql.connect() 中设置客户端字符集
- 读取含中文的表时防止乱码

## 关键要点

- MySQL 中写 charset='utf8'，不要写 'utf-8'
- 与 pandas 读文件的 encoding='utf-8' 是两套写法，别混
- 通常与数据库建库时的字符集保持一致

## 边界与易混淆

charset 属于数据库连接参数，只作用于 pymysql.connect()；pandas 读写本地文件的编码由 encoding 参数控制。

## 关联

- [[pymysql.connect()]] — 组合使用
- [[encoding 参数]] — 对比项

## 自测

为什么 pymysql.connect() 里写 charset='utf-8' 可能出问题？::MySQL 的字符集名是 utf8 而非 utf-8，写错会导致连接报错或中文乱码。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p18 S02E03.读取Mysql文件](https://www.bilibili.com/video/BV1ji4y157uB?p=18) · 2026-11-17
