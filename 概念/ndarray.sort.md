---
term: ndarray.sort
aliases: [sort, 数组排序, 原地排序]
kind: method
domain: 计算机/数据分析/Numpy
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# ndarray.sort

> 别名：sort、数组排序、原地排序

**对数组按指定轴原地升序排序，直接修改原数组。**

## 解释

ndarray.sort(axis=-1, kind=None, order=None) 是原地排序方法，调用后原数组被改写，不需要重新赋值。axis 决定沿哪个方向排序。

## 有什么用

- 对一维数组升序排序
- 对二维数组按行或按列分别排序

## 关键要点

- 原地修改，无返回值可用
- axis=0 每列内部排序，axis=1 每行内部排序
- 默认 axis=-1 即最后一个轴
- kind 选排序算法，order 用于结构化数组

## 边界与易混淆

要保留原数组需先 copy；与 np.sort 不同，后者返回新数组。

## 关联

- [[axis 参数]] — 前置知识
- [[argsort]] — 对比项

## 自测

a.sort() 之后原数组 a 会变吗？::会，sort 是原地排序。
二维数组 axis=0 排序是按行还是按列？::按列，即每一列内部各自排序。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
