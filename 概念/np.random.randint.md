---
term: np.random.randint
aliases: [randint, 随机整数数组, random.randint]
kind: method
domain: Numpy
tags: [概念/method, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
---

# np.random.randint

> 别名：randint、随机整数数组、random.randint

**生成指定区间内的随机整数数组，区间左闭右开。**

## 用法
**语法**：`np.random.randint(low, high=None, size=None, dtype=int)`

**参数**：
- `low`：随机整数下界；若只给一个参数，则从 `0` 到 `low-1`
- `high`：上界（不含），给定时范围为 `[low, high)`
- `size`：输出形状，整数或元组
- `dtype`：数据类型，默认 `int`

**示例**：
```python
import numpy as np

np.random.seed(42)
print(np.random.randint(1, 10))        # 单个 1–9 的随机整数，如 7
print(np.random.randint(1, 10, 5))     # 5 个随机整数，如 [9 4 8 5 7]
print(np.random.randint(0, 2, (2, 3))) # 2 行 3 列的 0/1 矩阵
```

## 解释

调用形式为 np.random.randint(low, high, size)，在 [low, high) 内等概率取整数，size 决定生成个数或形状。常用于快速造测试数据来演示索引、排序、统计等操作。

## 有什么用

- 构造随机测试数组
- 模拟抽样数据
- 演示排序和统计函数

## 关键要点

- 参数顺序为低值、高值、size，高值取不到
- size 可为整数，也可为形状元组如 (3,4)
- 生成的是整数，与 np.random.rand 的 0~1 浮点不同
- 与 np.random.seed 配合可复现结果

## 边界与易混淆

上界不包含在内，写 randint(1,100) 得到的是 1~99；需要浮点随机数应换用 rand 或 uniform。

## 关联

- [[Numpy random 随机函数]] — 上位概念
- [[np.random.rand]] — 对比项

## 自测

np.random.randint(1, 100, 10) 生成的数据范围是什么？::10 个 1 到 99 之间的整数，不含 100

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p09 S01E08.神奇索引](https://www.bilibili.com/video/BV1ji4y157uB?p=9) · 2026-11-17
