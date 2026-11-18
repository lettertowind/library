---
term: np.zeros_like
aliases: [zeros_like, 按形状创建全 0 数组]
kind: method
domain: Numpy
tags: [概念/method, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
order: 4
stage: "S01E03 · 创建数组"
---

# np.zeros_like

> 别名：zeros_like、按形状创建全 0 数组

**根据已有数组的形状创建元素全为 0 的新数组。**

## 用法

**语法**：`np.zeros_like(a, dtype=None)`

**参数**：
- `a`：用于提供形状的参考数组，新数组的 shape 与它一致，原数组不会被修改
- `dtype`：可选，指定新数组的数据类型；默认沿用 `a` 的 dtype，`a` 是整型就得到整型，需要别的类型时显式传 `dtype=float` 等

**示例**：

```python
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])
z = np.zeros_like(a)

print(a.shape)        # (2, 3)
print(z)              # [[0 0 0]
                      #  [0 0 0]]
print(z.dtype)        # int64（沿用 a 的整型 dtype）

b = np.zeros_like(a, dtype=float)
print(b.dtype)        # float64
print(a[0, 0])        # 1（原数组未被改动）
```

## 解释

与 np.zeros 手动指定形状不同，zeros_like 复用传入数组的 shape，生成同形状全 0 数组，常用于初始化累加器或掩码。

## 有什么用

- 初始化与现有数据同形状的零矩阵
- 构造掩码/占位数组

## 关键要点

- 语法：np.zeros_like(a)
- 形状与 a 相同，元素全为 0
- 不改变原数组
- 默认 dtype 可能为 float64

## 边界与易混淆

与 np.zeros 的区别仅在形状来源：手动指定 vs 复用已有数组。

## 关联

- [[np.zeros]] — 对比项
- [[np.ones_like]] — 组合使用

## 自测

什么时候用 zeros_like 比 zeros 更方便？::当已有一个数组、想创建同形状全 0 数组时，无需再手写 shape

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
