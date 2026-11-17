---
term: Series.str 访问器
aliases: [.str, str 访问器, 字符串方法访问器]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 39
stage: "S02E24 · 字符串操作（下）"
order: 39
---

# Series.str 访问器

> 别名：.str、str 访问器、字符串方法访问器

**Pandas 中用于对 Series 逐元素调用字符串方法的访问器。**

## 解释

通过 Series.str.xxx() 可以把 Python 字符串方法（如 lower、find、replace）向量化应用到整列。它只做方法调用，不做类型转换；非字符串列必须先 .astype(str) 才能使用。

## 有什么用

- 批量清洗文本列
- 对整列做查找、替换、正则提取

## 关键要点

- .str 是访问器，不是类型转换函数
- 日期/数值列需先 .astype(str) 再调用 .str
- 支持大部分 Python 字符串方法和部分正则方法
- 返回结果仍是 Series，可继续链式操作

## 边界与易混淆

易与 .astype(str) 混淆：后者才是类型转换；对非字符串列直接 .str 会报错或行为异常。

## 关联

- [[Series]] — 上位概念
- [[astype(str)]] — 前置知识

## 自测

为什么日期列不能直接 .str.find('-')？::因为日期列是 datetime 类型，.str 只对字符串生效，需先 .astype(str) 转换。
.str 和 .astype(str) 的本质区别是什么？::.str 是字符串方法访问器，.astype(str) 是类型转换。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
