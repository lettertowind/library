---
term: np.ones_like
aliases: [ones_like, 按形状创建全 1 数组]
kind: method
domain: Numpy
tags: [概念/method, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
order: 4
stage: "S01E03 · 创建数组"
---

# np.ones_like

> 别名：ones_like、按形状创建全 1 数组

**根据已有数组的形状创建元素全为 1 的新数组。**

## 用法
**语法**：`np.ones_like(a, dtype=None)`
**参数**：
- `a`：参照数组，新数组的形状与 `a` 的 shape 完全一致，原数组不会被修改
- `dtype`：可选，指定新数组的数据类型，如 `dtype=int`；不传时通常为 float64，与 `a` 的 dtype 无关
**示例**：
```python
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.ones_like(a)

print(a.shape)        # (2, 3)
print(b.shape)        # (2, 3)
print(b)              # [[1. 1. 1.]
                      #  [1. 1. 1.]]
print(b.dtype)        # float64

c = np.ones_like(a, dtype=int)
print(c)              # [[1 1 1]
                      #  [1 1 1]]
print(c.dtype)        # int64
print(a)              # [[1 2 3]
                      #  [4 5 6]]  原数组未被修改
```

## 解释

与 np.ones 需要手动传形状不同，ones_like 直接读取传入数组的 shape，生成同形状的全 1 数组，原数组不受影响。

## 有什么用

- 需要与现有数组同形状的占位/掩码数组时
- 避免手写 shape 元组出错

## 关键要点

- 语法：np.ones_like(a)，不要漏写 np 前缀
- 新数组形状与 a 完全一致，元素全为 1
- 不修改原数组 a
- 默认 dtype 可能为 float64，可用 dtype 参数指定

## 边界与易混淆

与 np.ones 的区别：ones 手动指定形状，ones_like 复用已有数组形状。

## 关联

- [[np.ones]] — 对比项
- [[np.zeros_like]] — 组合使用
- [[np.full_like]] — 组合使用

## 自测

a 是 2 行 3 列数组，np.ones_like(a) 的结果形状和内容是什么？::形状仍为 (2, 3)，所有元素为 1

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
