---
term: ignore_index 参数
aliases: [ignore_index, 忽略索引, ignore_index=True]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 24
stage: "S02E09 · 连接查询之concat"
---

# ignore_index 参数

> 别名：ignore_index、忽略索引、ignore_index=True

**concat 或 append 中用于忽略原索引、生成连续新索引的参数。**

## 解释

设置 ignore_index=True 后，合并结果不再保留原对象的索引，而是按合并后的数据顺序从上到下生成新的连续整数索引。该参数只影响索引，不改变按列名对齐的规则。

## 有什么用

- 合并后不关心原索引，希望得到干净连续索引时
- 追加数据后需要重新编号时

## 关键要点

- 忽略原索引，生成新的连续整数索引
- 只影响索引，不改变列对齐规则
- 适用于 concat 和 append
- 字段不同时仍按列名对齐，缺失填 NaN

## 边界与易混淆

ignore_index 不改变数据内容和对齐逻辑，仅重置索引。

## 关联

- [[pd.concat]] — 组合使用
- [[append 方法]] — 组合使用
- [[reset_index]] — 对比项

## 自测

concat 时设置 ignore_index=True，字段不同的表合并后列如何对齐？::仍按列名对齐，缺失字段填 NaN，ignore_index 只影响索引。


### 补充 · 2026-11-17

直接连接两张索引不同的表会保留原索引，导致编号重复或不连续。设 ignore_index=True 后索引不参与对齐，只按列名对齐，行号重新编号。

- 只重置索引，不改变列对齐方式
- 与 sort 不是一回事：前者重编号，后者控制排序
- 字段不同的表合并时仍按列并集对齐并补 NaN
两张表索引都是 0~3，纵向合并后不设 ignore_index 会出现什么现象？::结果索引重复出现 0~3 两遍，无法唯一定位行。
ignore_index=True 会让原本对不齐的列自动对齐吗？::不会，它只重置索引；列对齐由列名并集机制完成。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p24 S02E09.连接查询之concat](https://www.bilibili.com/video/BV1ji4y157uB?p=24) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
