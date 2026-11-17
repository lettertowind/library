---
term: Series
aliases: [pd.Series, 一维数据结构]
kind: concept
domain: 计算机/数据分析/Pandas
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# Series

> 别名：pd.Series、一维数据结构

**Pandas 的一维数据结构，由索引和数据值两部分组成。**

## 解释

Series 是 Pandas 最基础的数据结构，可以表示一行或一列数据。它由 index（索引）和 values（数据值）构成，默认索引是从 0 开始的整数。多个 Series 可以组成 DataFrame。

## 有什么用

- 表示单行或单列数据
- 作为 DataFrame 的组成单元
- 快速创建和查询一维数据

## 关键要点

- Series 是一维数据，由索引 index 和数据 values 组成
- 默认索引从 0 开始，步长为 1，结束值不包含
- 类名 Series 首字母必须大写
- 单独看 Series 无法确定是行还是列，加入 DataFrame 后才确定
- 多键查询返回的仍是 Series 类型

## 边界与易混淆

Series 是一维的，不能直接表示多行多列；二维数据需用 DataFrame。

## 关联

- [[DataFrame]] — 组合使用
- [[index 参数]] — 组合使用
- [[sort_index]] — 组合使用
- [[sort_values]] — 组合使用
- [[isnull]] — 组合使用
- [[notnull]] — 组合使用

## 自测

Series 由哪两部分组成？默认索引是什么样的？::由索引 index 和数据 values 组成；默认索引是从 0 开始的整数，步长 1，结束值不包含。
为什么说单独一个 Series 无法确定是行还是列？::因为 Series 本身只是一维序列，只有加入 DataFrame 后，根据加入方式才确定它成为一行或一列。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
