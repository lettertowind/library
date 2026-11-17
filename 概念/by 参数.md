---
term: by 参数
aliases: [by, 排序字段参数, 排序键]
kind: concept
domain: 计算机/数据分析/Pandas
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 27
stage: "S02E12 · 数据排序【已修证】"
order: 27
---

# by 参数

> 别名：by、排序字段参数、排序键

**sort_values 中指定按哪个字段或哪些字段排序的参数。**

## 解释

by 决定排序依据。单字段传字符串，多字段传列表，列表顺序就是排序优先级。按行排序时 by 填行索引名。

## 有什么用

- 指定单列排序
- 指定多列组合排序
- 按行索引对列排序

## 关键要点

- 单字段：by='语文'
- 多字段：by=['语文','数学','英语']，顺序即优先级
- 按行排序时 by 写行索引名，并配合 axis=1
- 多字段时 ascending 列表长度需与 by 对应

## 边界与易混淆

by 写错字段名会直接报 KeyError；多字段列表与 ascending 列表长度不一致会报错。

## 关联

- [[sort_values]] — 上位概念
- [[ascending 参数]] — 组合使用

## 自测

by=['语文','数学'] 表示什么排序逻辑？::先按语文排，语文相同的再按数学排

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
