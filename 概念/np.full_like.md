---
term: np.full_like
aliases: [full_like, 按形状填充指定值]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 5
stage: "S01E04 · 多维数组"
---

# np.full_like

> 别名：full_like、按形状填充指定值

**根据已有数组的形状创建新数组，并全部填充为指定值。**

## 用法

**语法**：`np.full_like(a, fill_value, dtype=None)`

**参数**：
- `a`：参照数组，新数组的形状与它完全一致，`a` 本身不会被修改
- `fill_value`：必填，要填充的数值；漏写会直接报错，这与 `np.full` 相同
- `dtype`：可选，新数组的数据类型；默认沿用 `a` 的数据类型，因此整数数组里填 `1.5` 会被截断，需要小数时显式写 `dtype=float`

**示例**：
```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.full_like(a, 520)          # 复用形状，全部填 520
print(b)
# [[520 520 520]
#  [520 520 520]]
print(b.shape, a.shape)           # 形状一致，原数组不变
# (2, 3) (2, 3)

c = np.full_like(a, 1.5, dtype=float)   # 不指定 dtype 会得到全 1
print(c)
# [[1.5 1.5 1.5]
#  [1.5 1.5 1.5]]
print(a)                          # a 仍是原值
# [[1 2 3]
#  [4 5 6]]
```

## 解释

full_like 结合了「复用形状」和「自定义填充值」：第一个参数是参照数组，第二个参数是要填充的数值。

## 有什么用

- 需要与现有数组同形状、同填充值的数组时
- 批量生成常量矩阵

## 关键要点

- 语法：np.full_like(a, 520)，第二个参数必填
- 形状与 a 相同，元素全为填充值
- 不修改原数组
- 易错：漏写第二个参数或漏写 np 前缀

## 边界与易混淆

与 np.full 的区别：full 手动传形状元组，full_like 复用已有数组形状。

## 关联

- [[np.full]] — 对比项
- [[np.ones_like]] — 组合使用

## 自测

np.full_like(a, 520) 中两个参数分别是什么含义？::第一个是参照形状的数组 a，第二个是要填充的数值 520

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
