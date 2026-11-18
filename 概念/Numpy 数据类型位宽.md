---
term: Numpy 数据类型位宽
aliases: [int32, int64, float32, float64, 数据类型位数]
kind: concept
domain: Numpy
tags: [概念/concept, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
---

# Numpy 数据类型位宽

> 别名：int32、int64、float32、float64、数据类型位数

**NumPy 类型名后面的数字，表示该类型占用的二进制位数。**

## 解释

NumPy 的整数和浮点数都按位宽细分：int32、int64 是整数型，float32、float64 是浮点型。位数越多，可表示的数值范围和精度越大，同时占用内存也越多，所以同一份数据可以选择更省内存的类型。

## 有什么用

- 为大数组选择更省内存的类型
- 控制精度，如 float32 加快计算

## 关键要点

- int 表示整数型，float 表示浮点型，后缀数字是位宽
- 位数越大范围与精度越高，内存占用也越大
- 默认整型随平台可能是 int32 或 int64
- 基础阶段只需认识这四种常见类型即可

## 边界与易混淆

位宽不足会导致溢出或精度丢失；float32 与 float64 参与运算时结果通常会向位数高的一方提升。

## 关联

- [[dtype 参数]] — 组合使用
- [[NumPy 默认数据类型 float64]] — 上位概念

## 自测

同样存一百万个整数，用 int32 和 int64 有什么区别？::int32 每个元素占 32 位、内存约为 int64 的一半，但可表示的范围也更小。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p04 S01E03.创建数组](https://www.bilibili.com/video/BV1ji4y157uB?p=4) · 2026-11-17
