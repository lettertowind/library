---
term: NaN
aliases: [Not a Number, 缺失值]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 31
stage: "S02E16 · 处理缺失值"
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


### 补充 · 2026-11-17

NaN 具有传播性：只要参与运算的一方是 NaN，结果就还是 NaN，不会自动当 0 处理。因此含空值的数据直接相加、相除会得到大量空值，必须先 fillna 或用 fill_value 指定替代值。

- NaN + 1 = NaN，1 + NaN = NaN，加减乘除都一样
- 0/0 也会得到 NaN，与缺失值使用同一表示
- 处理方式：fillna(0) 预先填充，或灵活算术方法 fill_value
一列含 NaN 的销量与另一列数字直接相加，这一行结果是什么？想按 0 参与该怎么办？::结果仍是 NaN；需先 fillna(0) 填充，或用灵活算术方法 add(..., fill_value=0)。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p34 S02E19.算数运算与数据对齐](https://www.bilibili.com/video/BV1ji4y157uB?p=34) · 2026-11-17

缺失值最直观的表现是空单元格或 NaN，但讲师特意强调「缺失值不仅仅只是空值」，占位符、错误编码等也属于缺失范畴。Pandas 处理缺失值围绕三步展开：查看（isnull/notnull）、删除（dropna）、填充（fillna），本节只覆盖空值型缺失。

- 初步理解：缺失值约等于空值，但二者并不等价
- 查看用 isnull/notnull，删除用 dropna，填充用 fillna
- 见到一个空值就删行删列，容易造成大量数据损失
为什么不能一检测到空值就把整行删掉？::含空值的行往往还有其他有效字段，直接删除会丢失大量可用信息；通常只在整行全空或关键列缺失时才删除。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p31 S02E16.处理缺失值](https://www.bilibili.com/video/BV1ji4y157uB?p=31) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
