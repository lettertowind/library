---
term: np.arange
aliases: [arange, 数组版 range]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 4
stage: "S01E03 · 创建数组"
---

# np.arange

> 别名：arange、数组版 range

**NumPy 中按 start/stop/step 生成等差一维数组的函数，相当于 range 的数组版。**

## 用法

**语法**：`np.arange([start, ]stop, [step], dtype=None)`

**参数**：
- `start`：起始值，包含在生成的序列里；只传一个参数时默认为 0
- `stop`：结束值，不包含在生成的序列里，要取到 n 就要写 n+1
- `step`：步长，默认为 1，取值可为负，也允许为浮点数
- `dtype`：可选，指定输出数组的元素类型，不写就按传入的数值自动推断

**示例**：
```python
import numpy as np

print(np.arange(5))           # [0 1 2 3 4]
print(np.arange(1, 6))        # [1 2 3 4 5]
print(np.arange(1, 10, 2))    # [1 3 5 7 9]
print(np.arange(0, 1, 0.25))  # [0.   0.25 0.5  0.75]
```

## 解释

np.arange(start, stop, step) 返回 ndarray，规则与 Python range 一致：含 start 不含 stop。只传一个参数时从 0 开始，step 可省略。它是创建数值序列最简洁的方式。

## 有什么用

- 快速生成等差数值序列
- 替代 np.array(range(...)) 的啰嗦写法

## 关键要点

- 语法 np.arange(start, stop, step)，含头不含尾
- 只传一个数时默认从 0 开始、步长 1
- 返回类型是 ndarray，不是 range 对象
- 比 np.array(range(...)) 更推荐

## 边界与易混淆

step 为浮点数时可能因浮点精度出现意外元素个数，需留意。

## 关联

- [[np.array]] — 对比项
- [[Numpy 切片]] — 前置知识

## 自测

np.arange(1,10,2) 输出什么？::[1 3 5 7 9]，从 1 开始到 10 之前、步长 2。


### 补充 · 2026-11-17

np.arange(1, n+1) 生成从 1 到 n 的数组。与 range 一样结束位置不包含自身；从 0 开始可省略起始位置，非 0 起始必须指定。

- 结束位置不包含自身，取到 n 要写 n+1
- 从 0 开始可省略起始参数
- 非 0 起始必须显式指定起始值
要生成 1 到 5 的数组，np.arange 应怎么写？::np.arange(1, 6)，结束位置不包含自身。
np.arange(5) 生成什么？::从 0 开始到 4 的数组 [0,1,2,3,4]。

np.arange 的参数规则与 Python 内置 range 基本一致：默认从 0 开始、结束值不包含自身。区别在于它返回的是 NumPy 数组，可以直接参与逐元素运算，而 range 只返回惰性序列。它是构造测试数组和批量数据最常用的入口。

- 结束值不包含自身，取 1 到 n 要写 np.arange(1, n+1)
- 省略起始值时默认从 0 开始
- 返回 ndarray，可直接做 **、+ 等逐元素运算
要生成 [1,2,3] 应该写 np.arange(1, ?)？::np.arange(1, 4)，因为结束值不包含自身。
np.arange 与 range 最本质的区别是什么？::np.arange 返回可直接运算的 ndarray，range 返回惰性序列，需转成列表才能逐项处理。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p03 S0102.体验Numpy与for循环的区别](https://www.bilibili.com/video/BV1ji4y157uB?p=3) · 2026-11-17

np.arange(start, stop, step) 相当于把 range() 和 np.array() 合并，直接返回 ndarray，省去外层 array 调用。它是创建连续范围数组最简洁的做法。

- np.arange(1,6) 得到 [1 2 3 4 5]，结束值不包含
- 第三参数是步长：np.arange(1,10,2) 得到 [1 3 5 7 9]
- 只传一个数时从 0 开始，np.arange(5) 得到 [0 1 2 3 4]
np.arange(1,6) 和 np.array(range(1,6)) 结果一样吗？::完全一样，只是 np.arange 少写一层 array，更简洁。
np.arange(10, 0, -2) 会得到什么？::从 10 开始每次减 2，到 0 前结束：[10 8 6 4 2]。步长为负即倒序。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p04 S01E03.创建数组](https://www.bilibili.com/video/BV1ji4y157uB?p=4) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
