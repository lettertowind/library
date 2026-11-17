---
term: np.maximum
aliases: [maximum, 逐元素最大值]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 12
stage: "S01E11 · 通用函数：快速的逐元素数组函数"
---

# np.maximum

> 别名：maximum、逐元素最大值

**对两个数组对应位置逐元素取较大值的二元通用函数。**

## 用法
**语法**：`np.maximum(x1, x2)`
**参数**：
- `x1`：参与比较的第一个数组或标量，逐元素比较的一方
- `x2`：参与比较的第二个数组或标量，需能与 `x1` 广播对齐
- 返回：与广播后形状相同的新数组，每个元素为对应位置上的较大值

**示例**：
```python
import numpy as np

x = np.array([1, 9])
y = np.array([5, 3])
print(np.maximum(x, y))        # [5 9]，逐位置取较大值

z = np.array([-2, 0, 3, 7])
print(np.maximum(z, 0))        # [0 0 3 7]，下限截断，所有值不低于 0
```

## 解释

np.maximum 接收两个数组，逐位置比较，谁大取谁，返回新数组。它体现二元通用函数「对位比较」的本质，而不是把数组汇总成一个最大值。

## 有什么用

- 按位取两列数据的较大值
- 实现下限截断（如不小于某值）

## 关键要点

- 逐元素比较，取较大值
- 返回同形状新数组
- 不汇总为单个最大值

## 边界与易混淆

与 np.max 不同：np.max 返回整体最大值标量。

## 关联

- [[二元通用函数]] — 上位概念
- [[np.minimum]] — 对比项
- [[np.max np.min]] — 对比项

## 自测

x=[1,9]、y=[5,3]，np.maximum(x,y) 结果？::[5, 9]，逐位置取较大值。
想实现「所有值不低于 0」，用哪个函数？::np.maximum(x, 0)，逐元素与 0 比较取较大值。


### 补充 · 2026-11-17

np.maximum 属于二元通用函数，数学上是 z_i = max(x_i, y_i)。它回答的是「同一位上谁大取谁」，常用于两组数据逐点取上限，比如用阈值数组给数据封顶。

- 对位比大小，谁大取谁，返回新数组
- 数学表达 z_i = max(x_i, y_i)
- 常配合 np.random.randint 生成的随机数组做演示
x=[3,1]、y=[2,4]，np.maximum(x,y) 结果是？若换成 np.max(x) 又从含义上有何不同？::maximum 得 [3,4]，逐位取大；np.max(x) 得 3，是把整个 x 归约成一个最大值。
想给一组数据设下限 0（负数都变成 0），用 maximum 怎么写？::np.maximum(data, 0)，标量 0 会广播到每个元素参与比较。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p12 S01E11.通用函数：快速的逐元素数组函数](https://www.bilibili.com/video/BV1ji4y157uB?p=12) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
