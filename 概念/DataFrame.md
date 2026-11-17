---
term: DataFrame
aliases: [df, 二维数据表]
kind: concept
domain: 计算机/数据分析/Pandas
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 21
stage: "S02E06 · 数据结构之DataFrame"
order: 21
---

# DataFrame

> 别名：df、二维数据表

**Pandas 的二维数据结构，表示多行多列的数据表。**

## 解释

DataFrame 是 Pandas 中用于处理表格数据的核心结构，可以看作由多个 Series 组成。编程中常简写为 df。它支持按列排序、空值判断等操作。

## 有什么用

- 处理 Excel 等表格数据
- 多行多列数据的分析与操作

## 关键要点

- DataFrame 是二维数据表，表示多行多列
- 可以由多个 Series 组成
- 编程中常简写为 df
- 按某列排序用 df.sort_values(by='列名')

## 边界与易混淆

DataFrame 是二维的，更高维数据需用 Panel 或其他结构（已不推荐）。

## 关联

- [[Series]] — 上位概念
- [[sort_values]] — 组合使用

## 自测

DataFrame 和 Series 是什么关系？::DataFrame 是二维数据结构，可以由多个 Series 组成；Series 是一维的，可表示 DataFrame 的一行或一列。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
