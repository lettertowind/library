---
term: Numpy 数组形状
aliases: [shape, 形状元组, 数组 shape]
kind: concept
domain: Numpy
tags: [概念/concept, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
---

# Numpy 数组形状

> 别名：shape、形状元组、数组 shape

**描述数组每个维度长度的元组。**

## 解释

如 (2,5) 表示两行五列，(5,) 表示一维五元素，(3,4,2) 表示三块四行两列。广播判断和 reshape 都以形状元组为依据。

## 有什么用

- 查看数组是几维、每维多长
- 判断两个数组能否广播
- 确定 reshape 的目标形状

## 关键要点

- 一维数组形状形如 (n,)，不是 (1,n)
- 二维数组形状为 (行数,列数)
- 三维数组形状为 (块数,行数,列数)
- reshape 参数就是目标形状

## 边界与易混淆

(5,) 是一维数组，(1,5) 是二维数组；两者形状不同。

## 关联

- [[Numpy reshape]] — 组合使用
- [[广播机制]] — 前置知识
- [[ndim 属性]] — 组合使用

## 自测

np.array([1,2,3]) 的 shape 是什么？::(3,)，是一维数组。
(3,4,2) 表示什么？::三维数组：3 块，每块 4 行 2 列。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p06 S01E05.数组计算](https://www.bilibili.com/video/BV1ji4y157uB?p=6) · 2026-11-17
