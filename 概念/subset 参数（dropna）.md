---
term: subset 参数（dropna）
aliases: [subset, 按列判断缺失, dropna subset]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 31
stage: "S02E16 · 处理缺失值"
---

# subset 参数（dropna）

> 别名：subset、按列判断缺失、dropna subset

**dropna 中指定只在哪些列范围内检查缺失值。**

## 解释

默认 dropna 检查整张表，subset 可以把判断范围缩小到指定列，只有这些列出现缺失时才触发删除，其他列不参与判断。

## 有什么用

- 只关心关键字段是否缺失时
- 避免无关列的空值误删样本

## 关键要点

- subset 接收列名列表
- 只在指定列中检查缺失
- 其他列的缺失不影响删除判断
- 是 dropna 的重点参数

## 边界与易混淆

subset 只缩小检查范围，不改变 how/thresh 的判断逻辑。

## 关联

- [[dropna 参数（透视表）]] — 上位概念
- [[how 参数]] — 组合使用

## 自测

df.dropna(subset=['语文','数学']) 的删除依据是什么？::只看语文、数学两列是否有缺失，有则删除对应行。
subset 和直接选列再 dropna 有什么区别？::subset 保留整表其他列，只缩小判断范围；选列会丢掉其他列。


### 补充 · 2026-11-17

整表逐列检查往往过于苛刻，subset 把判断范围收窄到关键列：data.dropna(subset=['语文','数学']) 只在这两列里找空值，命中就删整行，其他列是否为空不影响判断。这是讲师反复强调的重点参数。

- 传入列名列表，只在这些列中检查空值
- 命中空值后删除的是整行，而不只是这个单元格
- 未被列入 subset 的列不参与判断
data.dropna(subset=['语文']) 时，某行语文有值但英语为空，这行会被删吗？::不会。判断范围只在语文列，英语为空不参与判断。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p31 S02E16.处理缺失值](https://www.bilibili.com/video/BV1ji4y157uB?p=31) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
