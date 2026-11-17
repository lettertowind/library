---
term: get_dummies
aliases: [str.get_dummies, 哑变量编码, one-hot 编码]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 37
stage: "S02E22 · 离散化和分箱"
order: 37
---

# get_dummies

> 别名：str.get_dummies、哑变量编码、one-hot 编码

**把字符串按分隔符拆成多个 token 并生成 0/1 哑变量列的 Pandas 方法。**

## 解释

Series.str.get_dummies(sep=...) 按指定分隔符切分字符串，每个出现的 token 成为一列，行内标记是否包含该 token。适合一个字段里塞了多个标签的多值字段。

## 有什么用

- 多标签字段转 one-hot
- 把'中远距离'这类复合值拆成独立特征

## 关键要点

- sep 参数指定拆分字符
- 每个 token 生成一列 0/1 标记
- 适合多值字段的特征工程
- 平时用得少，但遇到多标签场景无可替代

## 边界与易混淆

只适合分隔符清晰的多值字段；token 过多会导致列爆炸。

## 关联

- [[Series.str 访问器]] — 上位概念
- [[pivot_table]] — 对比项

## 自测

对'近距离'用 sep='距' 调用 get_dummies，会得到哪些列？::会得到'近'和'离'两列（以及数据中其他行出现的 token 列）。
get_dummies 和 pivot_table 都能做特征展开，区别在哪？::get_dummies 按分隔符拆字符串生成 0/1 列，pivot_table 按行列分组聚合数值。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
