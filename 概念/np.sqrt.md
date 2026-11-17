---
term: np.sqrt
aliases: [sqrt, 平方根函数]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 12
stage: "S01E11 · 通用函数：快速的逐元素数组函数"
---

# np.sqrt

> 别名：sqrt、平方根函数

**对数组每个元素计算非负平方根的一元通用函数。**

## 用法

**语法**：`np.sqrt(x, /, out=None, *, where=True, dtype=None)`

**参数**：
- `x`：输入数组或标量，逐元素计算非负平方根，输入输出形状一致
- `out`：可选，用于存放结果的数组，形状需与返回值匹配
- `where`：可选，布尔数组，为 True 的位置才计算，否则保留 `out` 原值
- `dtype`：可选，指定输出数据类型

**示例**：

```python
import numpy as np

a = np.array([1, 4, 9, 16])
print(np.sqrt(a))          # [1. 2. 3. 4.]

b = np.array([4, -1])
print(np.sqrt(b))          # [ 2. nan]，负数处触发 RuntimeWarning

# 配合 pandas 对整个表逐元素开方
# 数据.apply(np.sqrt)
```

## 解释

np.sqrt 接收一个数组，返回同形状数组，每个元素为原元素的平方根。它是典型的一元通用函数，常用于数值变换和统计计算。

## 有什么用

- 对数据做开方变换
- 标准差等统计公式中的开方步骤

## 关键要点

- 逐元素计算平方根
- 返回非负平方根
- 输入输出形状一致

## 边界与易混淆

负数输入会得到 nan 并告警，需先处理负值。

## 关联

- [[一元通用函数]] — 上位概念

## 自测

np.sqrt 对含负数的数组会怎样？::负数元素返回 nan 并触发运行时警告，因为实数范围内无平方根。


### 补充 · 2026-11-17

np.sqrt 是最典型的一元通用函数，等价于对每个元素调用 math.sqrt，但无需写循环。它常被用作讲解「逐元素操作」的第一例。

- 输入一个数组，输出同形状数组
- 返回正平方根，负数会得到 nan 并告警
- 演示常用 np.arange(8) 生成 0~7 作为输入
np.sqrt(np.arange(8)) 会返回几个值？如果输入里含 -1 会怎样？::返回 8 个值，形状和长度不变；-1 处得到 nan 并触发运行时告警，而不是抛异常。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p12 S01E11.通用函数：快速的逐元素数组函数](https://www.bilibili.com/video/BV1ji4y157uB?p=12) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
