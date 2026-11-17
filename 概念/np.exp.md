---
term: np.exp
aliases: [exp, 指数函数]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 12
stage: "S01E11 · 通用函数：快速的逐元素数组函数"
---

# np.exp

> 别名：exp、指数函数

**对数组每个元素计算 e 的 x 次方的一元通用函数。**

## 用法
**语法**：`np.exp(x, /, out=None, *, where=True, dtype=None)`

**参数**：
- `x`：输入数组或标量，逐元素计算 e 的 x 次方
- `out`：可选，用于存放结果的数组，形状需与返回值一致
- `where`：可选，布尔数组或条件，为 True 的位置才参与计算
- `dtype`：可选，指定输出数据类型

**示例**：
```python
import numpy as np

a = np.array([0, 1, 2])
print(np.exp(a))          # [1.         2.71828183 7.3890561 ]
print(np.exp(0))          # 1.0
print(np.exp(a).shape)    # (3,)，输入输出形状一致
print(np.exp(np.array([1000.0])))  # [inf]，大数值溢出
```

## 解释

np.exp 接收一个数组，返回每个元素的自然指数 e^x。常见于概率论、统计模型和科学计算中的指数变换。

## 有什么用

- 概率与统计计算中的指数运算
- 对数据做指数变换

## 关键要点

- 逐元素计算 e 的 x 次方
- e 为自然对数底数
- 输入输出形状一致

## 边界与易混淆

大数值输入易溢出为 inf，需注意数值范围。

## 关联

- [[一元通用函数]] — 上位概念

## 自测

np.exp([0,1]) 的结果是什么？::[1., e]，即 [1., 2.718...]。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
