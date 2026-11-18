---
term: np.random.rand
aliases: [random.rand, rand, 随机数数组生成]
kind: method
domain: Numpy
tags: [概念/method, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
order: 11
stage: "S01E10 · random 随机函数"
---

# np.random.rand

> 别名：random.rand、rand、随机数数组生成

**按参数个数生成对应维度的 [0,1) 均匀分布随机浮点数组。**

## 用法
**语法**：`np.random.rand(d0, d1, ..., dn)`

**参数**：
- `d0, d1, ..., dn`：各个维度的长度，必须是正整数；参数个数决定输出数组的维度
- 不传任何参数时返回一个随机浮点数

**示例**：
```python
import numpy as np

# 不传参数：返回单个随机浮点数
print(np.random.rand())        # 例如 0.417022004702574

# 传两个参数：生成 2 行 3 列二维数组
arr = np.random.rand(2, 3)
print(arr.shape)               # (2, 3)
print((arr >= 0).all() and (arr < 1).all())  # True

# 传三个参数：生成 (2, 3, 3) 三维数组
print(np.random.rand(2, 3, 3).ndim)  # 3
```

## 解释

np.random.rand 的参数个数决定输出维度：不传参数返回单个随机数，传 1 个返回一维数组，传 2 个返回二维数组，传 3 个返回三维数组。

## 有什么用

- 快速生成随机测试数据
- 初始化权重或模拟数据

## 关键要点

- 参数个数 = 输出维度，参数值 = 各维度长度
- 不传参数返回单个随机浮点数
- np.random.rand(2, 3) 生成 2 行 3 列二维数组
- 结果默认是浮点型，范围 [0, 1)

## 边界与易混淆

与标准库 random 不同，使用 np.random 无需 import random；rand 只生成均匀分布，其他分布需用别的函数。

## 关联

- [[Numpy random 随机函数]] — 上位概念
- [[Numpy 多维数组]] — 组合使用

## 自测

np.random.rand(2, 3, 3) 生成的是什么维度和形状的数组？::三维数组，形状为 (2, 3, 3)，即 2 块 3 行 3 列


### 补充 · 2026-11-17

np.random.rand 的参数不是数值范围而是形状：不传参数得到一个随机小数，传 1 个数得到一维数组，传 2 个数得到二维数组，传 3 个数得到三维数组。这种“参数个数即维度”的写法与 ones/zeros 需要传元组不同，容易混淆。

- 不传参 → 单个随机小数
- 传 1 个数 → 一维数组；传 2 个数 → 二维；传 3 个数 → 三维
- np.random.rand(2,3,3) 得到两块 3×3 的随机数组
np.random.rand(2,3,3) 会得到什么？::一个三维随机数组，共 2 块、每块 3 行 3 列，元素是 [0,1) 的浮点数。
想得到一个单独的随机小数，参数该怎么写？::直接调用 np.random.rand()，不传任何参数。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p05 S01E04.多维数组](https://www.bilibili.com/video/BV1ji4y157uB?p=5) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
