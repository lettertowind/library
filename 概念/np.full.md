---
term: np.full
aliases: [full, 指定值数组]
kind: method
domain: Numpy
tags: [概念/method, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
order: 4
stage: "S01E03 · 创建数组"
---

# np.full

> 别名：full、指定值数组

**创建用指定数值填充的数组，形状和填充值都由参数给出。**

## 用法
**语法**：`np.full(shape, fill_value, dtype=None)`

**参数**：
- `shape`：形状，一维传一个整数（如 `3`），二维及以上传元组（如 `(3, 3)`）
- `fill_value`：填充值，数组中每个元素都取这个数值
- `dtype`：可选，指定元素数据类型，不写则由 `fill_value` 推断

**示例**：
```python
import numpy as np

print(np.full(3, 520))
# [520 520 520]

print(np.full((3, 3), 520))
# [[520 520 520]
#  [520 520 520]
#  [520 520 520]]

print(np.full((2, 3), 1.5).dtype)
# float64
```

## 解释

np.full(shape, fill_value) 是 np.ones/np.zeros 的泛化版：第一个参数是形状，第二个参数是填充值。例如 np.full(3,520) 得到三个 520。

## 有什么用

- 生成任意常量填充的数组
- 需要非 0/1 默认值的初始化

## 关键要点

- 语法 np.full(shape, fill_value)
- 一维：np.full(3,520)
- 二维：np.full((3,3),520)
- 可指定 dtype，order 默认 C

## 边界与易混淆

fill_value 是第二个位置参数，不要与形状参数顺序写反。

## 关联

- [[np.ones]] — 上位概念
- [[np.zeros]] — 对比项

## 自测

np.full((3,3),520) 生成什么？::3 行 3 列、每个元素都是 520 的二维数组。


### 补充 · 2026-11-17

np.full 需要两个参数：形状元组和填充值，例如 np.full((3, 3), 520) 创建 3 行 3 列、元素全为 520 的数组。

- 语法：np.full((3, 3), 520)
- 第一个参数是形状元组，第二个是填充值
- 支持多维形状
np.full((3, 3), 520) 生成什么数组？::3 行 3 列、所有元素都是 520 的二维数组

np.full(shape, fill_value) 的第一个参数是形状，第二个参数是要填满数组的数值，弥补了 ones 只能填 1、zeros 只能填 0 的限制。

- np.full(3, 520) 得到三个 520
- np.full((3,3), 520) 得到三行三列全为 520
- 第一参数是形状，写法与 ones、zeros 完全一致
np.full((2,3), 7) 和 np.ones((2,3)) * 7 有什么区别？::结果数值相同，但 full 一步创建，不需要额外的乘法运算，更直观。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p04 S01E03.创建数组](https://www.bilibili.com/video/BV1ji4y157uB?p=4) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
