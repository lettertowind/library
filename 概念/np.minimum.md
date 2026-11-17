---
term: np.minimum
aliases: [minimum, 逐元素最小值]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 12
stage: "S01E11 · 通用函数：快速的逐元素数组函数"
---

# np.minimum

> 别名：minimum、逐元素最小值

**对两个数组对应位置逐元素取较小值的二元通用函数。**

## 用法
**语法**：`np.minimum(x1, x2, /, out=None, *, where=True)`
**参数**：
- `x1, x2`：参与比较的两个数组（或标量），需可广播到同一形状，逐位置比较取较小值
- `out`：可选，存放结果的数组；提供时结果写入其中并返回
- `where`：可选，布尔数组或条件，为 True 的位置才计算取小，否则保留 `out` 原值
**示例**：
```python
import numpy as np

x = np.array([3, 1, 4, 1, 5])
y = np.array([2, 7, 1, 8, 5])

print(np.minimum(x, y))        # [2 1 1 1 5]
print(np.minimum(x, 3))        # [3 1 3 1 3]  —— 上限截断为 3
print(np.min(x))               # 1  —— 对比：np.min 汇总为标量
```

## 解释

np.minimum 接收两个数组，逐位置比较，谁小取谁，返回新数组。与 np.maximum 对称，用于按位取小或上限截断。

## 有什么用

- 按位取两列数据的较小值
- 实现上限截断（如不超过某值）

## 关键要点

- 逐元素比较，取较小值
- 返回同形状新数组
- 不汇总为单个最小值

## 边界与易混淆

与 np.min 不同：np.min 返回整体最小值标量。

## 关联

- [[二元通用函数]] — 上位概念
- [[np.maximum]] — 对比项
- [[np.max np.min]] — 对比项

## 自测

想实现「所有值不超过 100」，用哪个函数？::np.minimum(x, 100)，逐元素与 100 比较取较小值。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
