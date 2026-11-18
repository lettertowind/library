---
term: ndim 属性
aliases: [ndim, 维度数]
kind: concept
domain: Numpy
tags: [概念/concept, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
order: 4
stage: "S01E03 · 创建数组"
---

# ndim 属性

> 别名：ndim、维度数

**返回数组的维度数，一维为 1、二维为 2、三维为 3。**

## 解释

a.ndim 直接给出数组是几维。它等于 shape 返回元组的长度，因此实际使用较少，多数场景用 shape 就能判断维度。

## 有什么用

- 快速判断数组是几维

## 关键要点

- 一维返回 1，二维返回 2
- 等于 len(a.shape)
- 使用频率低于 shape

## 边界与易混淆

ndim 是维度数，不是元素个数（那是 size）。

## 关联

- [[shape 属性]] — 对比项
- [[size 属性]] — 对比项

## 自测

shape 为 (2,2,3) 的数组 ndim 是多少？::3，因为 shape 元组有三个数字。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
