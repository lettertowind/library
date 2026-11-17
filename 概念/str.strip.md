---
term: str.strip
aliases: [strip, 去除两端字符]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
order: 38
---

# str.strip

> 别名：strip、去除两端字符

**按字符集合从字符串两端去除字符的方法。**

## 解释

str.strip(chars) 从两端不断去除属于 chars 集合的字符，直到遇到不在集合中的字符。参数是字符集合而非完整子串，这是最容易误解的地方。

## 有什么用

- 清理“中远近离”这类前后缀
- 去除多余符号

## 关键要点

- 参数是字符集合，不是完整子串
- 会反复去除直到遇到集合外字符
- lstrip 只去左侧，rstrip 只去右侧

## 边界与易混淆

不能按完整子串去除；需要按子串去除时用 str.replace。

## 关联

- [[str.replace 正则替换]] — 对比项
- [[Series.str 访问器]] — 上位概念

## 自测

str.strip('中远近离') 对“中远距离”的结果是什么？::“距离”，两端属于该字符集合的字符都被去除。
strip 的参数是完整子串还是字符集合？::字符集合，会逐个字符判断是否去除。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
