---
term: np.max np.min
aliases: [max, min, 最大值, 最小值]
kind: method
domain: 计算机/数据分析/Numpy
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# np.max np.min

> 别名：max、min、最大值、最小值

**返回数组中的最大值或最小值，可指定 axis。**

## 解释

np.max 和 np.min 是全局极值函数，不指定 axis 时返回整个数组的极值；指定 axis 时返回沿该轴的一维结果。与 argmax/argmin 配合可同时拿到值和位置。

## 有什么用

- 找极值
- 按行或按列取最大最小

## 关键要点

- 不指定 axis 返回全局极值
- axis=0 返回每列极值，axis=1 返回每行极值
- 与 argmax/argmin 配合定位极值

## 边界与易混淆

含 NaN 时结果可能为 NaN，需要 nanmax 等变体处理。

## 关联

- [[np.argmax np.argmin]] — 组合使用
- [[np.sum]] — 对比项

## 自测

对 3x4 数组执行 np.max(A, axis=1)，返回几个值？::3 个，每行一个最大值。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
