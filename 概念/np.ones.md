---
term: np.ones
aliases: [ones, 全 1 数组]
kind: method
domain: Numpy
tags: [概念/method, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
order: 4
stage: "S01E03 · 创建数组"
---

# np.ones

> 别名：ones、全 1 数组

**创建元素全为 1 的数组，形状由参数指定。**

## 用法

**语法**：`np.ones(shape, dtype=None, order='C')`

**参数**：
- `shape`：形状。一维可传一个整数如 `3`，也可传元组 `(3,)`；二维及以上必须传元组，如 `(2, 3)`
- `dtype`：可选，指定元素数据类型；不指定时为浮点型（通常 `float64`）
- `order`：可选，默认 `'C'`，表示按 C 语言内存顺序存储，基础阶段无需改动

**示例**：
```python
import numpy as np

a = np.ones(3)              # 一维，传一个整数
print(a)                    # [1. 1. 1.]
print(a.dtype)              # float64

b = np.ones((2, 3))         # 二维，必须传元组
print(b)
# [[1. 1. 1.]
#  [1. 1. 1.]]
print(b.shape)              # (2, 3)

c = np.ones((2, 2), dtype=int)   # 指定整型
print(c)                    # [[1 1]
                            #  [1 1]]
print(c.dtype)              # int64

print(np.ones((2, 3, 3)).shape)  # (2, 3, 3)，2 块 3 行 3 列
```

## 解释

np.ones(shape) 生成全 1 数组，默认浮点型。一维传一个整数，二维及以上传元组如 (2,3)。可选 dtype 指定类型，order 默认 C 无需改动。

## 有什么用

- 生成全 1 的占位数组
- 构造掩码或初始化矩阵

## 关键要点

- 一维：np.ones(3) 得 [1. 1. 1.]
- 二维：np.ones((2,3)) 需传元组
- 默认 dtype 为浮点型
- order 参数默认 C，基础阶段忽略

## 边界与易混淆

二维及以上形状必须用元组，写成 np.ones(2,3) 会报错。

## 关联

- [[np.zeros]] — 对比项
- [[np.full]] — 对比项
- [[shape 属性]] — 组合使用

## 自测

np.ones((2,3)) 和 np.ones(3) 有什么区别？::前者是 2 行 3 列全 1 二维数组，后者是 3 个元素的全 1 一维数组。


### 补充 · 2026-11-17

np.ones 接收形状元组，可创建一维、二维、三维乃至更高维的全 1 数组；默认 dtype 常为 float64，可用 dtype 参数改为整型。

- 语法：np.ones((3, 3))，形状必须传元组
- np.ones((2, 3, 3)) 创建三维全 1 数组
- 默认 dtype 可能为 float64，即使显示为 1
np.ones((2, 3, 3)) 创建的是什么形状的数组？::三维数组，2 块 3 行 3 列，形状 (2, 3, 3)

np.ones(shape) 按给定形状生成全 1 数组，常用于占位、掩码或初始化；形状既可以是一个整数，也可以是多维元组。

- np.ones(3) 得到三个 1，np.ones((2,3)) 得到两行三列全 1
- 一维只写一个数字即可，二维及以上必须写元组
- 第二个参数 dtype 控制元素类型，不写时默认浮点型
np.ones(2, 3) 能正常创建两行三列数组吗？::不能，多维形状必须传元组 np.ones((2, 3))。
np.ones(3) 的元素是整数 1 还是浮点 1.0？::默认是浮点 1.0，需要整数要显式指定 dtype=int。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p04 S01E03.创建数组](https://www.bilibili.com/video/BV1ji4y157uB?p=4) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
