---
term: astype(str)
aliases: [astype, 类型转换, 转字符串]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 39
stage: "S02E24 · 字符串操作（下）"
order: 39
---

# astype(str)

> 别名：astype、类型转换、转字符串

**把 Series 数据类型转换为字符串的 Pandas 方法。**

## 解释

df['列'].astype(str) 把日期、数值等非字符串列转成字符串，之后才能安全调用 .str 访问器的方法。它是使用 Pandas 字符串操作的前置步骤。

## 有什么用

- 日期列转字符串后做正则提取
- 数值列转字符串后做文本处理

## 关键要点

- 真正做类型转换的是 astype，不是 .str
- 日期/数值列用 .str 前必须先转换
- 转换后原类型信息丢失

## 边界与易混淆

与 .str 访问器易混淆：.str 只调用方法，不改变类型。

## 关联

- [[Series.str 访问器]] — 前置知识

## 自测

对 datetime 列直接调用 .str.extract 会怎样？::会报错，需先 .astype(str) 转成字符串。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
