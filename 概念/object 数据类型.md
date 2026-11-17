---
term: object 数据类型
aliases: [object dtype, 字符型, 字符串类型列]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# object 数据类型

> 别名：object dtype、字符型、字符串类型列

**Pandas 中存放任意 Python 对象的列类型，含文本的列通常显示为 object。**

## 解释

Pandas 没有独立的字符串 dtype（旧版本），文本列一律存成 object，可以理解为「字符型」。它的代价是无法向量化计算，做数值运算前必须先 astype 转成数值类型。

## 关键要点

- 含字符串、混合类型的列常显示为 object
- 可粗略理解为字符串型/字符型
- object 列不能直接做数值运算
- 判断类型用 df.dtypes 或 type() 查看具体值

## 边界与易混淆

object 不只是字符串，任何 Python 对象（列表、字典）放进去也是 object，不能默认当成文本。

## 关联

- [[astype(str)]] — 组合使用
- [[整数列被提升为 float64]] — 对比项
- [[Series]] — 上位概念

## 自测

一列里混着字符串和数字，dtypes 会显示什么？::object

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p38 S02E23.字符串操作（上）](https://www.bilibili.com/video/BV1ji4y157uB?p=38) · 2026-11-17
