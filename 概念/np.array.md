---
term: np.array
aliases: [array, 创建数组]
kind: method
domain: Numpy
tags: [概念/method, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
order: 4
stage: "S01E03 · 创建数组"
---

# np.array

> 别名：array、创建数组

**NumPy 中把列表、元组、range 等序列转换为 ndarray 的通用创建函数。**

## 用法

**语法**：`np.array(object, dtype=None)`

**参数**：
- `object`：任意可迭代序列，如列表、元组、range，也可以是嵌套列表（构造二维数组）
- `dtype`：可选，指定元素类型如 `np.float64`、`np.int32`；不写时 NumPy 自动探测

**示例**：
```python
import numpy as np

# range 转数组，等价于 np.arange(1, 6)
a = np.array(range(1, 6))
print(a)            # [1 2 3 4 5]

# 元组转数组
b = np.array((1.5, 2.5, 3.5))
print(b)            # [1.5 2.5 3.5]

# 嵌套列表构造四行五列的二维数组
A = np.array([[0, 1, 2, 3, 4],
              [5, 6, 7, 8, 9],
              [10, 11, 12, 13, 14],
              [15, 16, 17, 18, 19]])
print(A.shape)      # (4, 5)
print(A[-1, 2])     # 12

# 手动指定 dtype
c = np.array([1, 2, 3], dtype=np.float64)
print(c)            # [1. 2. 3.]
```

## 解释

np.array 是 NumPy 最基础的数组创建入口，接收任意可迭代序列并返回 ndarray。它既能包装 range 生成序列，也能直接接收手写列表或元组。相比 np.arange，写法更通用但更啰嗦。

## 有什么用

- 把 Python 列表/元组/range 转成 NumPy 数组
- 需要从已有序列构造数组时

## 关键要点

- 可接收列表、元组、range 或其他序列
- 不指定 dtype 时 NumPy 自动探测元素类型
- np.array(range(1,6)) 与 np.arange(1,6) 效果相同
- 手动写列表较麻烦，一般优先用 np.arange

## 边界与易混淆

np.array 是通用转换函数，不是专门生成等差序列的工具；生成等差序列更推荐 np.arange。

## 关联

- [[np.arange]] — 对比项
- [[Numpy 二维数组]] — 组合使用
- [[dtype 参数]] — 组合使用

## 自测

np.array(range(1,6)) 和 np.arange(1,6) 输出是否相同？为什么？::相同，都是 [1 2 3 4 5]；前者把 range 序列转成数组，后者直接生成等差数组。


### 补充 · 2026-11-17

np.array() 接收列表、元组、已有数组或其他序列，返回内容相同但类型为 ndarray 的新数组；不指定类型时按输入内容自动推断元素类型。它是把已有 Python 数据结构纳入 NumPy 计算的入口。

- 写法 np.array([1,2,3,4,5])，外层括号是方法的括号，内部是列表
- 也可传元组 np.array((1,2,3,4,5)) 或已有数组
- 元素之间必须用英文逗号分隔
np.array((1,2,3)) 和 np.array([1,2,3]) 结果有区别吗？::没有，列表和元组都能被转换成同样的 ndarray。
为什么 np.array 内部还需要再写一对方括号？::外层括号属于 np.array 这个方法，内层方括号才是被转换的列表数据。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p04 S01E03.创建数组](https://www.bilibili.com/video/BV1ji4y157uB?p=4) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
