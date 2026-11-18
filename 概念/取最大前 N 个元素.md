---
term: 取最大前 N 个元素
aliases: [top-n 取值, 最大 n 个数, argsort 取最大值]
kind: method
domain: Numpy
tags: [概念/method, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
---

# 取最大前 N 个元素

> 别名：top-n 取值、最大 n 个数、argsort 取最大值

**先用 argsort 取得排序下标，再用神奇索引取回前 N 大元素的值。**

## 用法

**语法**：`arr[arr.argsort()[-N:]]`

**参数**：
- `arr`：一维 numpy 数组，即需要从中取值的数组。
- `N`：要取出的元素个数，为正整数；取最大 N 个时用 `[-N:]`，取最小 N 个时用 `[:N]`。

**示例**：
```python
import numpy as np

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
top3 = arr[arr.argsort()[-3:]]
print(top3)  # [5 6 9]

# 注意：结果按升序排列，不是降序
```

## 解释

因为 argsort 返回的是顺序而非数值，把末尾 N 个下标切出来交给原数组，就能拿到最大的 N 个元素。这是“先求位置、再按位置取值”这一模式的典型用法，同样适用于最小值。

## 有什么用

- 从一维数组中取最大或最小的若干元素
- 排行榜式取值

## 关键要点

- 写法为 arr[arr.argsort()[-3:]]，取最大的三个
- 结果按升序给出，不是降序
- 取最小值把切片换成 [:3]
- 比较绕时可分两步写：先 idx = arr.argsort()，再 arr[idx]

## 边界与易混淆

只适用于一维数组；二维数组需先展平或用扁平化下标，否则 argsort 返回的是沿轴的顺序。

## 关联

- [[argsort]] — 前置知识
- [[神奇索引]] — 组合使用

## 自测

如何用一行代码取出 arr 中最大的 5 个元素？::arr[arr.argsort()[-5:]]，先得到末尾 5 个排序下标再用神奇索引取值

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p09 S01E08.神奇索引](https://www.bilibili.com/video/BV1ji4y157uB?p=9) · 2026-11-17
