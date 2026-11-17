---
term: np.ones
aliases: [ones, 全 1 数组]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 4
stage: "S01E03 · 创建数组"
order: 4
---

# np.ones

> 别名：ones、全 1 数组

**创建元素全为 1 的数组，形状由参数指定。**

## 解释

np.ones(shape) 生成全 1 数组，默认浮点型。一维传一个整数，二维及以上传元组如 (2,3)。可选 dtype 指定类型，order 默认 C 无需改动。

## 有什么用

- 生成全 1 的占位数组
- 构造掩码或初始化矩阵

## 关键要点

- 一维：np.ones(3) 得 [1. 1. 1.]
- 二维：np.ones((2,3)) 需传元组
- 默认 dtype 为浮点型
- order 参数默认 C，基础阶段忽略

## 边界与易混淆

二维及以上形状必须用元组，写成 np.ones(2,3) 会报错。

## 关联

- [[np.zeros]] — 对比项
- [[np.full]] — 对比项
- [[shape 属性]] — 组合使用

## 自测

np.ones((2,3)) 和 np.ones(3) 有什么区别？::前者是 2 行 3 列全 1 二维数组，后者是 3 个元素的全 1 一维数组。


### 补充 · 2026-11-17

np.ones 接收形状元组，可创建一维、二维、三维乃至更高维的全 1 数组；默认 dtype 常为 float64，可用 dtype 参数改为整型。

- 语法：np.ones((3, 3))，形状必须传元组
- np.ones((2, 3, 3)) 创建三维全 1 数组
- 默认 dtype 可能为 float64，即使显示为 1
np.ones((2, 3, 3)) 创建的是什么形状的数组？::三维数组，2 块 3 行 3 列，形状 (2, 3, 3)

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
