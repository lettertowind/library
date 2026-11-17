---
term: on 参数
aliases: [on, 连接键参数, on=['k1','k2']]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 22
stage: "S02E07 · 连接查询之Merge"
---

# on 参数

> 别名：on、连接键参数、on=['k1','k2']

**merge 中指定用于对齐合并的同名列的参数。**

## 解释

on 告诉 merge 用哪一列（或多列）作为连接键，要求左右表都存在该列名。它相当于 Excel VLOOKUP 中用来匹配的那个共同字段。

## 有什么用

- 指定单列连接键
- 用多列列表做复合键连接

## 关键要点

- 左右表必须存在同名同义的列
- 支持单列字符串或多列列表
- 多列时按组合键整体匹配
- 列名不同时需改用 left_on/right_on
- join 的 on 语义不同，常是左表列对右表索引

## 边界与易混淆

on 只适用于同名列；join 的 on 是左表列匹配右表索引，两者不可混用。

## 关联

- [[DataFrame 合并]] — 上位概念
- [[how 参数]] — 组合使用
- [[suffixes 参数]] — 组合使用

## 自测

左右表连接字段名不同（左 k1、右 key1），还能用 on 吗？::不能，应改用 left_on='k1', right_on='key1'。
on=['k1','k2'] 表示什么？::用 k1 和 k2 两列的组合作为复合连接键。


### 补充 · 2026-11-17

当两个表的连接键列名相同时用 on 指定；传列表即多键连接，要求所有键同时相等才算匹配。列名不同则改用 left_on/right_on。

- on='姓名' 为单键连接
- on=['姓名','班级'] 为多键连接，需全部键相等
- 同名列存在时 Pandas 可自动识别，但显式写更清楚
两表都有姓名和班级列，只想「姓名+班级」同时相同才匹配，怎么写？::pd.merge(a, b, on=['姓名','班级'])。

在 merge 中，on 直接写出左右表共有的列名，可传列表做多键连接；列名必须两边都存在，否则报错。在 join 中，on 的含义不同：它指定左表的某一列，去匹配右表的索引。

- merge 的 on 必须是两表都存在的同名列
- 多键连接写成 on=['k1','k2']，只有两键同时相等才算匹配
- 列名不一致时不能靠 on 解决，需先 rename 或改用 left_on/right_on
左表列叫 user_id、右表列叫 id，用 on='user_id' 能连上吗？::不能，会报错说右表没有该列；应改用 left_on='user_id', right_on='id'。
on=['k1','k2'] 时，只要 k1 相等就算匹配吗？::不是，必须 k1 和 k2 同时相等才算匹配成功。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p23 S02E08.连接查询之join与Merge总结](https://www.bilibili.com/video/BV1ji4y157uB?p=23) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
