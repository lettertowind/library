---
term: Numpy reshape
aliases: [reshape, np.arange().reshape, 改变数组形状]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 5
stage: "S01E04 · 多维数组"
---

# Numpy reshape

> 别名：reshape、np.arange().reshape、改变数组形状

**在不改变数据的前提下把数组重排为指定形状。**

## 用法
**语法**：`ndarray.reshape(shape)` 或 `np.reshape(a, newshape)`

**参数**：
- `shape`：目标形状。可以写成多个整数（如 `9, 4`），也可以写成元组 `(9, 4)`。其中某一维可以填 `-1`，让 NumPy 根据元素总数自动推断该维大小
- `order`：填充顺序，默认为 `'C'`（按行优先填充）；可填 `'F'`（按列优先填充）

**示例**：
```python
import numpy as np

a = np.arange(36)
b = a.reshape(9, 4)          # 或 a.reshape((9, 4))
print(b.shape)               # (9, 4)
print(b[4])                  # [16 17 18 19]
print(b[0])                  # [0 1 2 3]

c = a.reshape(4, -1)         # -1 自动推断为 9
print(c.shape)               # (4, 9)
print(c[1])                  # [ 9 10 11 12 13 14 15 16 17]

d = np.arange(6).reshape(2, 3, order='F')
print(d)                     # [[0 2 4]
                             #  [1 3 5]]
```

## 解释

reshape 按行优先把一维数据填充成指定的行列结构，常用于把 arange 生成的一串数变成二维数组来做索引练习。元素总数必须与目标形状匹配。

## 有什么用

- 把一维序列转成二维矩阵
- 构造练习或演示用的多维数组

## 关键要点

- 元素总数必须等于目标形状各维乘积
- 默认按行优先（C 顺序）填充
- np.arange(36).reshape(9,4) 得到 9 行 4 列

## 边界与易混淆

形状不匹配会报错；reshape 返回视图或副本取决于内存布局，不要假设一定是原数组。

## 关联

- [[Numpy 二维数组]] — 组合使用
- [[Numpy 索引]] — 前置知识

## 自测

np.arange(36).reshape(9,4) 得到几行几列？第 4 行是什么？::9 行 4 列；第 4 行是 [16,17,18,19]。


### 补充 · 2026-11-17

它把原数组按新形状重新组织，元素顺序通常不变；新形状各维长度乘积必须等于原数组 size。

- reshape(2,5) 表示目标为 2 行 5 列
- 前后元素总数必须严格一致
- 总元素数 = 各维长度乘积 = size
np.arange(10).reshape(2,4) 为什么报错？::2×4=8，与原数组 10 个元素不一致。
reshape 会改变数组中的元素值吗？::不会，只改变组织形状。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p06 S01E05.数组计算](https://www.bilibili.com/video/BV1ji4y157uB?p=6) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
