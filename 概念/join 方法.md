---
term: join 方法
aliases: [join, DataFrame.join, left.join(right)]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# join 方法

> 别名：join、DataFrame.join、left.join(right)

**DataFrame 按索引对齐横向拼接另一张表的简便方法。**

## 解释

join 语法简单，默认按索引把右表列横向拼到左表右侧，索引不一致处补空值。功能比 merge 有限，适合简单横向拼接，复杂场景建议用 merge。

## 有什么用

- 按索引快速横向拼接两表
- 一次连接多个 DataFrame

## 关键要点

- 默认按索引对齐，而非按同名列
- 索引不一致时对应位置产生空值
- on 参数是左表列匹配右表索引，与 merge 不同
- 支持列表一次连接多个表：left.join([right, right2])
- 功能有限，实际项目建议优先用 merge

## 边界与易混淆

join 的 on 语义与 merge 的 on 不同；默认按索引对齐，容易因索引不一致产生大量空值。

## 关联

- [[DataFrame 合并]] — 对比项
- [[索引对齐]] — 前置知识

## 自测

left.join(right) 默认按什么对齐？::按索引对齐，把右表列横向拼到左表右侧。
join 的 on='k' 与 merge 的 on='k' 有何不同？::join 是左表的 k 列去匹配右表的索引；merge 是左右表同名列 k 相互匹配。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
