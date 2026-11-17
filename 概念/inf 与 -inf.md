---
term: inf 与 -inf
aliases: [无穷大, 正无穷, 负无穷, Infinity]
kind: concept
domain: 计算机/数据分析/Pandas
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 34
stage: "S02E19 · 算数运算与数据对齐"
order: 34
---

# inf 与 -inf

> 别名：无穷大、正无穷、负无穷、Infinity

**非零数除以 0 产生的正负无穷大值。**

## 解释

在浮点运算中，1/0 得 inf，-1/0 得 -inf，0/0 得 NaN。它们不是缺失值，不能被 fillna 直接替换，需要先转为 NaN 或单独处理。

## 有什么用

- 除法运算结果检查
- 数据清洗时识别异常值

## 关键要点

- 1/0 = inf，-1/0 = -inf，0/0 = NaN
- inf 不是空值，fillna 无效
- 处理方式：use_inf_as_na 或 replace 转 NaN
- 展示结果时 inf 通常需要清洗掉

## 边界与易混淆

易与 NaN 混淆：NaN 是缺失值，inf 是数值溢出结果。

## 关联

- [[use_inf_as_na]] — 下位概念
- [[NaN]] — 对比项

## 自测

0/0 和 1/0 分别得到什么？::0/0 得 NaN，1/0 得 inf。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
