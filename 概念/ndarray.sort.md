---
term: ndarray.sort
aliases: [sort, 数组排序, 原地排序]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 14
stage: "S01E13 · 条件计算，排序，深潜拷贝【本季完】"
---

# ndarray.sort

> 别名：sort、数组排序、原地排序

**对数组按指定轴原地升序排序，直接修改原数组。**

## 用法

**语法**：`ndarray.sort(axis=-1, kind=None, order=None)`

**参数**：
- `axis`：指定排序沿哪个轴进行，默认 `-1`，即最后一个轴；对二维数组，`axis=0` 表示每一列内部各自排序，`axis=1` 表示每一行内部各自排序
- `kind`：指定排序算法，可选 `'quicksort'`、`'mergesort'`、`'heapsort'`、`'stable'`，默认 `None`，即使用 quicksort
- `order`：仅在结构化数组中使用，用于指定按哪个字段排序

**示例**：

```python
import numpy as np

a = np.array([3, 1, 2])
a.sort()            # 原地排序，返回 None
print(a)            # [1 2 3]

b = np.array([[3, 1], [2, 4]])
b.sort(axis=0)      # 每列内部各自升序
print(b)
# [[2 1]
#  [3 4]]

c = b.copy()        # 要保留原数组需先 copy
c.sort()            # 默认 axis=-1，每行内部各自升序
print(c)
# [[1 2]
#  [3 4]]
```

注意：`sort` 会直接改写原数组，且没有可用的返回值。如果希望保留原数组并得到排序结果，应改用 `np.sort`。

## 解释

ndarray.sort(axis=-1, kind=None, order=None) 是原地排序方法，调用后原数组被改写，不需要重新赋值。axis 决定沿哪个方向排序。

## 有什么用

- 对一维数组升序排序
- 对二维数组按行或按列分别排序

## 关键要点

- 原地修改，无返回值可用
- axis=0 每列内部排序，axis=1 每行内部排序
- 默认 axis=-1 即最后一个轴
- kind 选排序算法，order 用于结构化数组

## 边界与易混淆

要保留原数组需先 copy；与 np.sort 不同，后者返回新数组。

## 关联

- [[axis 参数]] — 前置知识
- [[argsort]] — 对比项

## 自测

a.sort() 之后原数组 a 会变吗？::会，sort 是原地排序。
二维数组 axis=0 排序是按行还是按列？::按列，即每一列内部各自排序。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
