---
term: np.cumprod
aliases: [cumprod, 累计积]
kind: method
domain: 计算机/数据分析/Numpy
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# np.cumprod

> 别名：cumprod、累计积

**从首元素开始逐步累乘，返回展平后等长的一维数组。**

## 解释

np.cumprod 与 cumsum 对称，返回每一步的累计乘积。首项若为 0，后续所有累计积都为 0，因此演示时首项不能设为 0。

## 有什么用

- 计算复利式累计增长
- 观察连乘过程

## 关键要点

- 返回长度等于元素总数的一维数组
- 首项为 0 会导致后续全部为 0
- 二维数组按展平顺序累乘

## 边界与易混淆

数值增长极快，容易溢出，业务中使用场景有限。

## 关联

- [[np.cumsum]] — 对比项
- [[np.prod]] — 对比项

## 自测

为什么演示 cumprod 时数组首项不能设为 0？::因为 0 乘任何数都是 0，后续累计积会全部变成 0。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
