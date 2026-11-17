---
term: np.where
aliases: [where, 条件替换函数]
kind: method
domain: 计算机/数据分析/Numpy
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 14
stage: "S01E13 · 条件计算，排序，深潜拷贝【本季完】"
order: 14
---

# np.where

> 别名：where、条件替换函数

**按条件从两个候选值中逐元素选取，返回同形状新数组。**

## 解释

np.where(condition, x, y) 等价于向量化的 if-else：条件为真取 x，为假取 y。它不修改原数组，而是返回新数组，适合批量条件替换。

## 有什么用

- 按条件批量替换数组元素
- 把布尔条件转成两档取值

## 关键要点

- 语法为 np.where(条件, 真值, 假值)
- 返回新数组，原数组不变
- 条件通常是布尔数组，如 a > 3
- 与布尔赋值不同，它是取值而非就地修改

## 边界与易混淆

只支持两分支；多分支需嵌套 where 或改用 np.select。

## 关联

- [[布尔数组]] — 前置知识
- [[条件赋值]] — 对比项

## 自测

np.where(a>3, 520, 1314) 中 a 本身会被修改吗？::不会，返回的是新数组。
要按条件把元素分成三档，np.where 够用吗？::不够，需要嵌套 where 或使用 np.select。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
