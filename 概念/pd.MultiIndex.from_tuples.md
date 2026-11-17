---
term: pd.MultiIndex.from_tuples
aliases: [from_tuples, 元组创建 MultiIndex]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# pd.MultiIndex.from_tuples

> 别名：from_tuples、元组创建 MultiIndex

**用元组列表创建多层索引的方法。**

## 解释

from_tuples 接收一个元组列表，每个元组表示一个多层索引组合，元组内元素依次对应各层。它适合手工列举索引组合的场景。

## 有什么用

- 手工列举多层索引组合
- 从元组数据构造 MultiIndex

## 关键要点

- 每个元组代表一个索引组合
- 元组内元素顺序对应各层顺序
- 可用 names 给各层命名

## 边界与易混淆

组合较多时手写元组繁琐，此时更适合用 from_product。

## 关联

- [[分层索引]] — 组合使用
- [[pd.MultiIndex.from_product]] — 对比项

## 自测

from_tuples([('a',1),('b',2)]) 创建的是几层索引？::两层索引，每个元组内两个元素分别对应两层。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
