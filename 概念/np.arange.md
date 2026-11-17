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

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
