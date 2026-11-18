---
term: size 属性
aliases: [size, 元素总数]
kind: concept
domain: Numpy
tags: [概念/concept, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
order: 4
stage: "S01E03 · 创建数组"
---

# size 属性

> 别名：size、元素总数

**返回数组中所有元素的总个数。**

## 解释

a.size 统计数组内全部数据元素数目，与维度无关。例如 7 个元素的一维数组 size 为 7，2 行 3 列的二维数组 size 为 6。

## 有什么用

- 统计数组元素总数
- 与 shape 配合理解数组规模

## 关键要点

- 返回整数，表示元素总个数
- 等于 shape 各维度数字的乘积
- 与 ndim（维度数）不同

## 边界与易混淆

size 是元素总数，不是内存字节数。

## 关联

- [[shape 属性]] — 对比项
- [[ndim 属性]] — 对比项

## 自测

shape 为 (2,3) 的数组 size 是多少？::6，2×3=6 个元素。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
