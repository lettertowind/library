---
term: na 参数
aliases: [na, na=False, 空值处理参数, na_rep 之外的 na]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
---

# na 参数

> 别名：na、na=False、空值处理参数、na_rep 之外的 na

**字符串判断类方法中统一用来指定空值返回结果的参数。**

## 解释

contains、startswith、endswith、repeat 等方法都提供 na 参数：不写时空值原样返回 NaN，写成 na=False/True 则统一变成布尔值，写成某个字符串则空位显示该文本。它让布尔筛选结果可以直接用于条件过滤。

## 有什么用

- 布尔判断结果中排除空值干扰
- 让过滤条件不因 NaN 而失效

## 关键要点

- 不设 na 时，空值在布尔结果中仍显示为 NaN
- na=False 把空值当「不匹配」，最常用于筛选
- na=True 把空值当「匹配」
- na 也可传字符串，如 na='没有'，结果列变成 object
- 这是跨方法的通用约定，不是某个方法独有

## 边界与易混淆

与 cat 的 na_rep 不是同一个参数：na 改的是返回值，na_rep 改的是拼接前的替代文本。

## 关联

- [[str.contains]] — 组合使用
- [[str.startswith]] — 组合使用
- [[str.cat]] — 对比项
- [[NaN]] — 前置知识

## 自测

用 str.contains 做布尔筛选时为什么建议加 na=False？::否则空值位置返回 NaN，布尔索引会报错或结果不可控

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p38 S02E23.字符串操作（上）](https://www.bilibili.com/video/BV1ji4y157uB?p=38) · 2026-11-17
