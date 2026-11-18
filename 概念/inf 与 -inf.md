---
term: inf 与 -inf
aliases: [无穷大, 正无穷, 负无穷, Infinity]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 34
stage: "S02E19 · 算数运算与数据对齐"
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


### 补充 · 2026-11-17

在数组运算中，1/0 得到 inf，-1/0 得到 -inf，0/0 得到 NaN。它们与 NaN 语义不同（一个是溢出、一个是缺失），因此 fillna 默认无法处理，必须先转成空值再填充。

- 1/0 → inf，-1/0 → -inf，0/0 → NaN
- inf 不是缺失值，fillna 默认替换不了
- 标准处理链：use_inf_as_na 转 NaN，再 fillna(0)
为什么 df.fillna(0) 处理不掉结果里的 inf？::因为 inf 是数值溢出得到的无穷大，不被判定为缺失值，fillna 只匹配 NaN，所以原样保留。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p34 S02E19.算数运算与数据对齐](https://www.bilibili.com/video/BV1ji4y157uB?p=34) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
