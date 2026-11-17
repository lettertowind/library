---
term: np.concatenate
aliases: [concatenate, NumPy 数组连接, np.concatenate]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# np.concatenate

> 别名：concatenate、NumPy 数组连接、np.concatenate

**NumPy 中沿指定轴把多个数组拼接成一个新数组的函数。**

## 用法

**语法**：`np.concatenate((a1, a2, ...), axis=0)`

**参数**：
- `a1, a2, ...`：待拼接的数组序列，必须打包成元组或列表传入（如 `[a, b]`）；单个标量要先包成 `[arr[0]]`
- `axis`：沿哪个轴拼接，默认 `0`；二维数组中 `axis=0` 表示行方向上下堆叠，`axis=1` 表示列方向左右并排
- 除拼接轴外，其余维度必须一致，否则报错

**示例**：

```python
import numpy as np

a = np.arange(9).reshape(3, 3)
print(np.concatenate([a, a], axis=0).shape)  # (6, 3)
print(np.concatenate([a, a], axis=1).shape)  # (3, 6)

x = np.array([1, 2, 3])
print(np.concatenate((x, [x[0]])))  # [1 2 3 1]
```

## 解释

接收一个数组列表和 axis 参数：axis=0 上下堆叠、axis=1 左右并排。它是 Pandas concat 的底层原型，先理解它才能理解 concat 的轴方向。

## 有什么用

- 把多个 ndarray 合成一个更大数组
- 矩阵拼装、特征横向扩列
- 为学习 Pandas concat 打基础

## 关键要点

- 第一个参数是列表 [a, b]，不是 a, b 两个位置参数
- axis=0 行方向堆叠：两个 3×3 变 6×3
- axis=1 列方向并排：两个 3×3 变 3×6
- 除拼接轴外，其余维度必须一致，否则报错

## 边界与易混淆

只按位置拼接 ndarray，没有索引和列名概念，因此不会做对齐、也不会补缺失值；需要按标签对齐时用 pd.concat。

## 关联

- [[pd.concat]] — 前置知识
- [[axis 参数]] — 组合使用
- [[Numpy 二维数组]] — 组合使用

## 自测

两个 3×3 数组执行 np.concatenate([a, a], axis=0) 后形状是多少？::6×3，行方向上下堆叠。
为什么 NumPy 拼接不会像 Pandas 横向拼接那样出现 NaN？::NumPy 按位置拼接，没有索引标签，不存在对不齐的情况。


### 补充 · 2026-11-17

np.concatenate 接收一个由多个序列组成的元组/列表，把它们首尾拼接。在极坐标绘图中用来把第一个值补到末尾，实现首尾闭合。

- 参数必须都是序列；单个元素要先写成 [x] 包成列表，否则报错
- 默认沿轴 0 拼接，一维数组结果是更长的一维数组
- 闭合时三条序列（数值、角度、类别）要分别拼接
np.concatenate((arr, arr[0])) 为什么容易报错？怎么改？::arr[0] 是单个元素而不是序列，需要写成 np.concatenate((arr, [arr[0]])) 把元素包成列表再拼。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p79 S03E30.玫瑰图](https://www.bilibili.com/video/BV1ji4y157uB?p=79) · 2026-11-17

concatenate 接收一个序列（元组或列表），里面放要拼在一起的所有数组，默认沿 axis=0 拼接。雷达图里用它把首项追加到末尾完成闭合。

- 待拼接对象必须打包成元组或列表传入，少写一层括号会报错
- 标量要先包成 [arr[0]] 这种单元素序列才能拼
- 默认 axis=0，一维数组就是首尾相接
np.concatenate(a01, [a01[0]]) 为什么报错？::第一个参数必须是一个序列（元组/列表），正确写法是 np.concatenate((a01, [a01[0]]))。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p71 S03E22.雷达图](https://www.bilibili.com/video/BV1ji4y157uB?p=71) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p24 S02E09.连接查询之concat](https://www.bilibili.com/video/BV1ji4y157uB?p=24) · 2026-11-17
