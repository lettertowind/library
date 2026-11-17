---
term: np.minimum
aliases: [minimum, 逐元素最小值]
kind: method
domain: 计算机/数据分析/Numpy
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 12
stage: "S01E11 · 通用函数：快速的逐元素数组函数"
order: 12
---

# np.minimum

> 别名：minimum、逐元素最小值

**对两个数组对应位置逐元素取较小值的二元通用函数。**

## 解释

np.minimum 接收两个数组，逐位置比较，谁小取谁，返回新数组。与 np.maximum 对称，用于按位取小或上限截断。

## 有什么用

- 按位取两列数据的较小值
- 实现上限截断（如不超过某值）

## 关键要点

- 逐元素比较，取较小值
- 返回同形状新数组
- 不汇总为单个最小值

## 边界与易混淆

与 np.min 不同：np.min 返回整体最小值标量。

## 关联

- [[二元通用函数]] — 上位概念
- [[np.maximum]] — 对比项
- [[np.max np.min]] — 对比项

## 自测

想实现「所有值不超过 100」，用哪个函数？::np.minimum(x, 100)，逐元素与 100 比较取较小值。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
