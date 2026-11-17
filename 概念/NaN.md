---
term: NaN
aliases: [Not a Number, 缺失值]
kind: concept
domain: 计算机/数据分析/Pandas
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# NaN

> 别名：Not a Number、缺失值

**Pandas 中表示缺失值或非数字值的特殊标记。**

## 解释

NaN 是 Not a Number 的缩写，在数据分析中常作为缺失值处理。Pandas 读取数据时，空单元格常被识别为 NaN，可用 isnull() 检测。

## 有什么用

- 表示缺失数据
- 配合 isnull()/notnull() 检测空值

## 关键要点

- NaN 表示 Not a Number，即非数字
- 在数据分析中常作为缺失值
- 可用 isnull() 判断是否为 NaN

## 边界与易混淆

NaN 是浮点类型，与 None 不同；比较时不能用 == 判断。

## 关联

- [[isnull]] — 组合使用
- [[notnull]] — 组合使用

## 自测

NaN 在数据分析中通常代表什么？如何检测？::代表缺失值；可用 isnull() 检测，返回 True 表示是空值。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
