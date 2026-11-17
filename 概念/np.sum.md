---
term: np.sum
aliases: [sum, 求和]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 13
stage: "S01E12 · 数学和统计方法"
---

# np.sum

> 别名：sum、求和

**对数组元素求和，可用 axis 指定沿哪个轴汇总。**

## 用法
**语法**：`np.sum(a, axis=None, dtype=None, keepdims=False)`
**参数**：
- `a`：待求和的数组或类数组对象。
- `axis`：指定沿哪个轴汇总；不指定时对所有元素求和，`axis=0` 跨行按列求和，`axis=1` 行内求和。
- `dtype`：指定累加时使用的数据类型，例如 `dtype=np.float64`。
- `keepdims`：是否保留被汇总轴的维度，设为 `True` 时该轴长度变为 1。

**示例**：
```python
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])

print(np.sum(A))                 # 21
print(np.sum(A, axis=0))         # [5 7 9]
print(np.sum(A, axis=1))         # [6 15]
print(np.sum(A, axis=1, keepdims=True))  # [[ 6]
                                          #  [15]]
```

## 解释

np.sum 是 NumPy 最基础的聚合函数，不指定 axis 时把所有元素加成一个标量；指定 axis=0 按列求和，axis=1 按行求和。它是理解其他统计函数轴向行为的入口。

## 有什么用

- 计算总和、按行/按列汇总
- 配合 axis 做分组聚合

## 关键要点

- 不指定 axis 时返回全局总和
- axis=0 行与行按位置相加，结果长度等于列数
- axis=1 每行内部相加，结果长度等于行数
- 二维数组默认按行优先展平后累加

## 边界与易混淆

axis 方向容易记反：0 轴是行方向（跨行汇总），1 轴是列方向（行内汇总）。

## 关联

- [[axis 参数]] — 组合使用
- [[np.prod]] — 对比项
- [[np.cumsum]] — 对比项

## 自测

对 3 行 4 列的数组执行 np.sum(A, axis=0)，结果是什么形状？::长度为 4 的一维数组，每个元素是对应列的和。
为什么 axis=0 的结果看起来像“每一列的和”？::因为 0 轴代表行方向，跨行按位置相加，每个位置对应一列。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
