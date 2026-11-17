---
term: how 参数（dropna）
aliases: [how, how='any', how='all', 删除条件参数]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# how 参数（dropna）

> 别名：how、how='any'、how='all'、删除条件参数

**dropna 中决定「有缺失就删」还是「全空才删」的条件参数。**

## 解释

how 的默认值是 'any'，只要行或列里出现一个缺失值就删除，杀伤力很大。设成 'all' 后语义变为「整行或整列全部为空才删」，才是业务中更常用的口径，通常与 axis=1 组合删除全空列。

## 有什么用

- 只想清理彻底空白的行或列时
- 与 axis 组合做精准的删除控制

## 关键要点

- how='any' 是默认值：有一个缺失就删该行/列
- how='all' 只有整行或整列全空才删除
- how 必须结合 axis 理解：先定方向，再定条件
- dropna(axis=1, how='all') 是删除全空列的常用写法

## 边界与易混淆

how 只描述「空到什么程度才删」，不能按缺失比例删除，比例类需求要用 thresh。

## 关联

- [[dropna]] — 上位概念
- [[thresh 参数]] — 对比项
- [[axis 参数]] — 组合使用

## 自测

how='any' 与 how='all' 的本质区别是什么？::any 是「有缺失就删」，all 是「全部缺失才删」，后者保留数据的力度更大。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p31 S02E16.处理缺失值](https://www.bilibili.com/video/BV1ji4y157uB?p=31) · 2026-11-17
