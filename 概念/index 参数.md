---
term: index 参数
aliases: [index=, 索引参数]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 20
stage: "S02E05 · 数据结构之Series"
order: 20
---

# index 参数

> 别名：index=、索引参数

**pd.Series() 中用于指定自定义索引的参数。**

## 解释

创建 Series 时，通过 index 参数传入一个列表，可以将默认的整数索引替换为自定义索引。常用于索引和数据分别存放在两个列表中的场景。

## 有什么用

- 创建 Series 时指定自定义索引
- 将两个列表组合成带索引的 Series

## 关键要点

- index 参数接收一个列表
- pd.Series() 中先放值，再通过 index= 指定索引
- 可将默认的 0,1,2,3 替换为自定义索引如 a,b,c,d

## 边界与易混淆

index 列表长度必须与数据值长度一致，否则报错。

## 关联

- [[Series]] — 组合使用

## 自测

用两个列表创建 Series 时，值和索引分别放在哪里？::值放在 pd.Series() 的第一个位置，索引列表通过 index= 参数传入。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
