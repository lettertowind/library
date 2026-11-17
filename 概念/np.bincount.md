---
term: np.bincount
aliases: [bincount, 频次统计]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 13
stage: "S01E12 · 数学和统计方法"
order: 13
---

# np.bincount

> 别名：bincount、频次统计

**统计非负整数数组中每个值出现的次数。**

## 解释

np.bincount 返回长度为 max+1 的频次数组，下标即原值。配合 np.argmax 可求众数，但只能处理非负整数，不能直接用于浮点数或二维数组。

## 有什么用

- 统计整数频次
- 配合 argmax 求一维众数

## 关键要点

- 只接受非负整数
- 返回数组下标对应原值，值为出现次数
- 配合 np.argmax 可找众数

## 边界与易混淆

浮点数和二维数组不能直接使用，众数建议改用 Pandas。

## 关联

- [[众数]] — 组合使用
- [[np.argmax np.argmin]] — 组合使用

## 自测

为什么 np.bincount 不能直接统计浮点数组？::它用值作为下标索引频次数组，浮点数无法作为下标。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
