---
term: np.zeros
aliases: [zeros, 全 0 数组]
kind: method
domain: Numpy
tags: [概念/method, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
order: 4
stage: "S01E03 · 创建数组"
---

# np.zeros

> 别名：zeros、全 0 数组

**创建元素全为 0 的数组，形状由参数指定。**

## 用法
**语法**：`np.zeros(shape, dtype=float)`

**参数**：
- `shape`：形状。一维传一个整数（如 `3`），二维及以上传元组（如 `(3, 3)`、`(2, 3, 3)`）
- `dtype`：可选，指定元素数据类型；不指定时默认为浮点型 `float64`
- `order`：可选，默认 `C`，表示按 C 语言的内存顺序存储；基础阶段可以忽略

**示例**：
```python
import numpy as np

print(np.zeros(3))            # [0. 0. 0.]
print(np.zeros((3, 3)))       # 3 行 3 列全 0 的二维数组
print(np.zeros((2, 3, 3)))    # 2 块 3 行 3 列的三维数组
print(np.zeros((2, 3), dtype=int))  # 指定整型，元素为 0 而非 0.
```

## 解释

np.zeros(shape) 生成全 0 数组，参数规则与 np.ones 完全一致：一维传整数，二维及以上传元组，可选 dtype。常用于初始化占位矩阵。

## 有什么用

- 初始化全 0 矩阵
- 作为累加或填充的容器

## 关键要点

- 一维：np.zeros(3) 得 [0. 0. 0.]
- 二维：np.zeros((3,3)) 需传元组
- 参数规则与 np.ones 相同
- 默认 dtype 为浮点型

## 边界与易混淆

与 np.ones 仅填充值不同，形状参数规则完全一致。

## 关联

- [[np.ones]] — 对比项
- [[np.full]] — 对比项

## 自测

np.zeros((3,3)) 生成什么？::3 行 3 列、元素全为 0 的二维数组。


### 补充 · 2026-11-17

np.zeros 接收形状元组，可创建任意维度的全 0 数组，常用于初始化累加器或占位矩阵；默认 dtype 常为 float64。

- 语法：np.zeros((3, 3))，形状传元组
- 支持三维及以上，如 np.zeros((2, 3, 3))
- 默认 dtype 可能为 float64
np.zeros((3, 3)) 的元素默认是什么数据类型？::通常是 float64，即使元素显示为 0

把 np.ones 换成 np.zeros 即可得到全 0 数组，形状与类型参数规则完全一致，是最常见的数组初始化方式。

- np.zeros(3) 得到三个 0，np.zeros((3,3)) 得到三行三列全 0
- 形状规则与 np.ones 相同：一维写数字，多维写元组
- dtype 默认浮点型，可显式指定为 int
为什么初始化数组常用 zeros 而不是直接写数值列表？::zeros 只给形状就能生成任意大小数组，避免手写长列表，之后可整体赋值。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p04 S01E03.创建数组](https://www.bilibili.com/video/BV1ji4y157uB?p=4) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
