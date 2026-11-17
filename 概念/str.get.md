---
term: str.get
aliases: [get, 取指定位置字符]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# str.get

> 别名：get、取指定位置字符

**获取字符串中指定索引位置的单个字符的方法。**

## 解释

str.get(i) 按索引取出每个字符串的第 i 个字符，索引从 0 开始。参数只能是整型；越界或原值为空时返回 NaN，并可能导致整列变成 float64。

## 有什么用

- 提取固定位置的字符，如首字母
- 从编码字符串中取某一位

## 关键要点

- 索引从 0 开始
- 参数只能传 int，不能传浮点
- 越界返回 NaN，整列可能变 float64
- 原列有空值时也可能导致 float64

## 边界与易混淆

只能取单个字符，不能取范围；取范围要用 str.slice。

## 关联

- [[str.slice]] — 对比项
- [[负索引]] — 前置知识
- [[Series.str 访问器]] — 上位概念

## 自测

str.get(2) 取的是第几个字符？::第 3 个字符，因为索引从 0 开始。
为什么 str.get 之后整列可能变成 float64？::因为越界或空值位置返回 NaN，整列被提升为浮点型。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
