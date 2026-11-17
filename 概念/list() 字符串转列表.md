---
term: list() 字符串转列表
aliases: [list('xyz'), 字符串拆成列表, str to list]
kind: method
domain: 数据分析/Python
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# list() 字符串转列表

> 别名：list('xyz')、字符串拆成列表、str to list

**用 list() 把字符串按字符拆成列表，省去手写引号和逗号。**

## 解释

list('xyz') 得到 ['x','y','z']。建 DataFrame 时写 columns=list('xyz')、index=list('abc') 就能快速给出列名和行索引，列一多时代码明显更短更干净。

## 有什么用

- 建表时快速生成列名、行索引列表
- 批量造短字符串列表

## 关键要点

- 按字符逐个拆，空格标点也会成为元素
- 等价于列表推导 [c for c in 'xyz']
- columns 与 index 都是关键字参数，先后顺序无关

## 边界与易混淆

只适合单字符的短名字；列名是多字符单词时必须手写列表

## 关联

- [[DataFrame 构造]] — 组合使用

## 自测

list('abc') 的结果是什么？::['a','b','c']，按字符拆开的列表。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p26 S02E11.列与列之间的计算](https://www.bilibili.com/video/BV1ji4y157uB?p=26) · 2026-11-17
