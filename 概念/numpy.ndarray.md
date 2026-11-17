---
term: numpy.ndarray
aliases: [ndarray, NumPy 数组类型]
kind: concept
domain: 计算机/数据分析/Numpy
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 4
stage: "S01E03 · 创建数组"
order: 4
---

# numpy.ndarray

> 别名：ndarray、NumPy 数组类型

**NumPy 的核心多维数组对象类型，所有创建函数最终都返回它。**

## 解释

ndarray 是 NumPy 独有的数组数据结构，支持向量化运算和高效内存存储。用 type() 查看数组对象会得到 <class 'numpy.ndarray'>，可用来确认结果不是 Python 列表。

## 有什么用

- 确认创建结果是否为 NumPy 数组
- 理解 NumPy 所有运算的数据载体

## 关键要点

- type(a) 输出 <class 'numpy.ndarray'>
- 与 Python list 是不同对象类型
- np.array、np.arange、np.ones 等均返回 ndarray
- 支持 shape/ndim/size/dtype 等属性

## 边界与易混淆

ndarray 不是 list，很多 list 方法（如 append）在数组上行为不同或不存在。

## 关联

- [[np.array]] — 上位概念
- [[shape 属性]] — 组合使用

## 自测

如何确认一个变量是 NumPy 数组而不是列表？::用 type(变量) 查看，输出 <class 'numpy.ndarray'> 即为 NumPy 数组。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
