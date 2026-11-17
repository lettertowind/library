---
term: DatetimeIndex
aliases: [日期时间索引, 日期索引]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# DatetimeIndex

> 别名：日期时间索引、日期索引

**以日期时间为标签的 Pandas 索引类型，支持按日期字符串筛选。**

## 解释

将日期列设为索引并用 pd.to_datetime 转换后得到，是 truncate 和部分字符串索引的前提。它让日期筛选可以像普通索引切片一样简洁。

## 有什么用

- 按年/月/日区间筛选数据
- 使用 truncate 截取日期范围

## 关键要点

- 由 pd.to_datetime 转换索引得到
- 使用 truncate 前必须排序
- 支持部分字符串索引如 数据['1989']
- 与普通索引区别：标签是时间戳

## 边界与易混淆

不是所有日期列都需要设为索引；使用 query 的 @ 日期条件时反而不能设为索引。

## 关联

- [[日期筛选三部曲]] — 组合使用
- [[truncate]] — 前置知识
- [[部分字符串索引]] — 上位概念

## 自测

DatetimeIndex 和普通 Index 的主要区别是什么？::DatetimeIndex 的标签是时间戳，支持按年/月/日字符串进行部分索引和日期范围截取。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p29 S02E14.筛选](https://www.bilibili.com/video/BV1ji4y157uB?p=29) · 2026-11-17
