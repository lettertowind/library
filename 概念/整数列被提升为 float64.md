---
term: 整数列被提升为 float64
aliases: [int 变 float, 缺失值导致类型提升, 1 显示成 1.0]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
---

# 整数列被提升为 float64

> 别名：int 变 float、缺失值导致类型提升、1 显示成 1.0

**整数列只要含空值，读入后就会整体变成 float64，整数显示为 1.0。**

## 解释

NumPy 的 int 类型不能表示缺失，Pandas 只能把这类列提升为 float64 来容纳 NaN。这是读 Excel、CSV、数据库时最常遇到的坑：源表看起来是整数，进 DataFrame 后带上小数点。

## 有什么用

- 排查读入数据后编号列莫名带小数
- 清洗后把列类型还原为整数

## 关键要点

- 触发条件：整数列中存在空值
- 表现为 1 变成 1.0，dtypes 显示 float64
- 解决思路：处理缺失值后用 astype 转回整数
- 非时间空值是 NaN，时间空值是 NaT
- 了解 NumPy 的 int32/int64/float32/float64 才能理解成因

## 边界与易混淆

不是读取出错，而是类型系统的必然结果；用可空整数类型 Int64 也可规避。

## 关联

- [[NaN]] — 前置知识
- [[Numpy 数据类型位宽]] — 前置知识
- [[object 数据类型]] — 对比项
- [[astype(str)]] — 组合使用

## 自测

从 Excel 读入的序号列显示成 1.0、2.0，最可能的原因是什么？::该列存在空值，Pandas 把整数列提升成了 float64

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p38 S02E23.字符串操作（上）](https://www.bilibili.com/video/BV1ji4y157uB?p=38) · 2026-11-17
