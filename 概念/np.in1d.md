---
term: np.in1d
aliases: [in1d, 元素存在判断, 成员判断]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 14
stage: "S01E13 · 条件计算，排序，深潜拷贝【本季完】"
---

# np.in1d

> 别名：in1d、元素存在判断、成员判断

**逐元素判断第一个数组的元素是否出现在第二个数组中，返回布尔数组。**

## 用法

**语法**：`np.in1d(ar1, ar2, assume_unique=False, invert=False)`
**参数**：
- `ar1`：待检查的数组，返回的布尔数组与它形状相同
- `ar2`：作为“集合”的数组，用来判断 `ar1` 中的元素是否属于它
- `assume_unique`：布尔值，默认 `False`；设为 `True` 时假定两个数组均已去重，可加快判断速度（前提是确实唯一，否则结果可能不准）
- `invert`：布尔值，默认 `False`；设为 `True` 时对结果取反，即返回“不属于”的布尔数组

**示例**：

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 4, 6])

print(np.isin(a, b))                 # [False  True False  True False]
print(a[np.isin(a, b)])              # [2 4]
print(~np.isin(a, b))    # [ True False  True False  True]
```

注意：函数原名 `np.in1d`（中间是数字 1），numpy 2.0 起已移除，改用 `np.isin`，语义完全一致。

## 解释

np.in1d(ar1, ar2) 对 ar1 的每个元素检查是否属于 ar2，返回与 ar1 同形状的布尔数组。本质是向量化的成员判断。

## 有什么用

- 筛选出属于某集合的元素
- 做集合成员检查

## 关键要点

- 返回与 ar1 同形状的布尔数组
- 函数名中是数字 1 不是字母 l
- 可配合布尔索引筛选元素
- 与集合的交并思想相关

## 边界与易混淆

只判断成员关系，不返回交集本身；求交集需其他方法。

## 关联

- [[np.unique]] — 组合使用
- [[布尔索引筛选]] — 组合使用

## 自测

np.isin(a, b) 返回的是什么？::与 a 同形状的布尔数组，表示每个元素是否在 b 中。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
