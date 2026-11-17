---
term: Numpy 二维数组
aliases: [ndarray 二维, 矩阵]
kind: concept
domain: 数据分析/Numpy
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
stage: "S01E06 · 基础索引与切片"
order: 7
---

# Numpy 二维数组

> 别名：ndarray 二维、矩阵

**用 np.array 创建、按行和列组织数据的二维数据结构。**

## 解释

二维数组是 Numpy 处理表格型数据的核心结构，用行索引和列索引定位元素。可类比 Excel 的 offset 函数，按行偏移、列偏移定位区域。

## 有什么用

- 表示表格型/矩阵型数据
- 作为索引与切片的操作对象

## 关键要点

- 用 np.array 嵌套列表创建
- 定位思想是“先行后列”
- 可类比 Excel offset 的行列偏移
- 取单列后结果退化为一维数组

## 边界与易混淆

二维索引规则建立在一维索引与切片之上，一维不熟应先补 Python 基础。

## 关联

- [[Numpy 索引]] — 下位概念
- [[Numpy 切片]] — 下位概念

## 自测

为什么说二维数组索引可以类比 Excel 的 offset？::两者都通过行偏移和列偏移来定位元素或区域，核心都是先行后列的定位思想。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
