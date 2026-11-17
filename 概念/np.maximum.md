---
term: np.maximum
aliases: [maximum, 逐元素最大值]
kind: method
domain: 计算机/数据分析/Numpy
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# np.maximum

> 别名：maximum、逐元素最大值

**对两个数组对应位置逐元素取较大值的二元通用函数。**

## 解释

np.maximum 接收两个数组，逐位置比较，谁大取谁，返回新数组。它体现二元通用函数「对位比较」的本质，而不是把数组汇总成一个最大值。

## 有什么用

- 按位取两列数据的较大值
- 实现下限截断（如不小于某值）

## 关键要点

- 逐元素比较，取较大值
- 返回同形状新数组
- 不汇总为单个最大值

## 边界与易混淆

与 np.max 不同：np.max 返回整体最大值标量。

## 关联

- [[二元通用函数]] — 上位概念
- [[np.minimum]] — 对比项
- [[np.max np.min]] — 对比项

## 自测

x=[1,9]、y=[5,3]，np.maximum(x,y) 结果？::[5, 9]，逐位置取较大值。
想实现「所有值不低于 0」，用哪个函数？::np.maximum(x, 0)，逐元素与 0 比较取较大值。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
