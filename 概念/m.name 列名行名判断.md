---
term: m.name 列名行名判断
aliases: [m.name, Series.name, 按名称选择性应用]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 26
stage: "S02E11 · 列与列之间的计算"
---

# m.name 列名行名判断

> 别名：m.name、Series.name、按名称选择性应用

**在 apply 回调中用 Series 的 name 属性判断当前列名或行索引名，实现只对指定列/行运算。**

## 用法
**语法**：`DataFrame.apply(func, axis=0, raw=False, result_type=None)`，回调里用 `m.name` 取列名或行索引名
**参数**：
- `func`：作用于每列或每行的函数，接收到的参数是 Series，含 `name` 属性
- `axis`：`0` 或 `'index'` 按列传入，`m.name` 是列名；`1` 或 `'columns'` 按行传入，`m.name` 是行索引名
- `raw`：为 True 时传入 ndarray 而非 Series，此时没有 `m.name`
- `result_type`：`'expand'`/`'reduce'`/`'broadcast'`，控制返回结果的展开方式，一般默认即可
**示例**：
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'x': [1, 4, 9], 'y': [16, 25, 36], 'z': [2, 3, 4]},
                  index=['a', 'b', 'c'])
# 只对 x、y 两列开方，z 列原样返回
r = df.apply(lambda m: np.sqrt(m) if m.name in ['x', 'y'] else m)
print(r)
#      x     y  z
# a  1.0   4.0  2
# b  2.0   5.0  3
# c  3.0   6.0  4

# 按行：m.name 是行索引名，只处理 a 行
print(df.apply(lambda m: m * 10 if m.name == 'a' else m, axis=1))
#     x   y   z
# a  10  40  20
# b   4  25   3
# c   9  36   4
```

## 解释

DataFrame.apply 的回调参数 m 是一个 Series，m.name 在按列时是列名、按行时是行索引名。用 lambda m: np.sqrt(m) if m.name == 'x' else m 即可只对 x 列开方，其余原样返回；用 m.name in ['x','y'] 可对多列生效。

## 有什么用

- 只对指定列做变换
- 只对指定行做变换（配 axis=1）
- 多列/多行批量选择处理

## 关键要点

- 按列时 m.name 是列名，按行时是行索引名
- 条件不满足时返回 m 本身即保持原样
- 用 in 列表可一次选多列或多行
- 需与 axis 配合决定按行还是按列

## 边界与易混淆

依赖回调参数是 Series；若用其他方式遍历则无 m.name。

## 关联

- [[apply]] — 组合使用
- [[axis 参数]] — 前置知识
- [[lambda 表达式]] — 组合使用

## 自测

如何只对 x、y 两列开方而 z 列不变？::数据.apply(lambda m: np.sqrt(m) if m.name in ['x','y'] else m)。
按行 apply 时 m.name 代表什么？::代表当前行的行索引名称。


### 补充 · 2026-11-17

DataFrame.apply 会逐列（axis=0）或逐行（axis=1）把 Series 传给回调，这个 Series 的 name 就是列名或行索引名。配合三元表达式即可只对某列或某行计算，其余原样返回。多个目标用 m.name in ['x','y'] 判断。

- 按列操作时 m.name 是列名，按行操作时是行索引名
- 单目标：m.name == 'x'；多目标：m.name in ['x','y']
- 必须配合 else 原样返回 m，否则其余行/列会丢失
想让 x、y 两列平方而 z 列不变，回调条件怎么写？::lambda m: np.square(m) if m.name in ['x','y'] else m。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p26 S02E11.列与列之间的计算](https://www.bilibili.com/video/BV1ji4y157uB?p=26) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
