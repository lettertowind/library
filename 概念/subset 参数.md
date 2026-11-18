---
term: subset 参数
aliases: [subset, 按列去重参数, 判断重复的列]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 33
stage: "S02E18 · 删除重复和提取重复"
---

# subset 参数

> 别名：subset、按列去重参数、判断重复的列

**指定按哪些列判断重复的参数，单列传字符串、多列传列表。**

## 解释

subset 是 drop_duplicates 和 duplicated 共有的关键参数，决定重复判断的维度。不传时按整行判断；传单列字符串按该列判断；传列表则只有这些列的组合同时重复才算重复。

## 有什么用

- 按业务主键去重
- 按多列组合判断重复

## 关键要点

- 单列可写 subset='姓名'
- 多列必须写列表 subset=['姓名','班级']
- 不传 subset 时按整行判断
- 多列组合重复才视为重复

## 边界与易混淆

单列写成列表 ['姓名'] 与字符串 '姓名' 效果等价，但多列不能写成字符串。

## 关联

- [[drop_duplicates]] — 组合使用
- [[duplicated]] — 组合使用

## 自测

subset=['姓名','班级'] 时，什么情况才算重复行？::只有姓名和班级两列的值组合完全相同时才算重复，单列相同不算。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
