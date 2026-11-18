---
term: NumPy 函数在 pandas 中的应用
aliases: [np.sqrt, NumPy 函数, 整表计算]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 26
stage: "S01E11 · 通用函数：快速的逐元素数组函数"
---

# NumPy 函数在 pandas 中的应用

> 别名：np.sqrt、NumPy 函数、整表计算

**把 NumPy 的逐元素函数直接用于 Series 或 DataFrame 做整表计算。**


## 用法
**语法**：`np.sqrt(df)` / `df.apply(np.sqrt)`
**参数**：
- NumPy 函数（如 `np.sqrt`、`np.log`、`np.exp`）：只有一个位置参数，即待计算的 Series、DataFrame 或标量，返回同形状对象
- `df.apply(func)`：`func` 为逐列（默认 `axis=0`）调用的函数，可直接传 `np.sqrt`；按行算用 `axis=1`
**示例**：
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 4, 9], 'B': [16, 25, 36]})

print(np.sqrt(df))          # 整表开方，逐元素
print(df.apply(np.sqrt))    # 作为 apply 回调，默认逐列
print(df['A'].apply(np.sqrt))  # 单列
```
输出均为 A 列 `0 1.0 / 1 2.0 / 2 3.0`、B 列 `0 4.0 / 1 5.0 / 2 6.0` 的 DataFrame（单列为 Series）；三者结果一致，验证 NumPy 函数既可直接整表算，也能当 apply 回调。

## 解释

NumPy 函数如 np.sqrt 是逐元素通用函数，可直接作用于 pandas 对象，也可作为 apply 的回调。整张表做数学计算时优先用 NumPy，单列自定义逻辑时用 Series + apply。

## 有什么用

- 整表开方、取对数等数学变换
- apply 中传入 np.sqrt 等

## 关键要点

- NumPy 函数需写 np. 前缀，内置函数直接写名
- 整表计算优先 NumPy，单列常用 Series+apply
- np.sqrt 可作 apply 回调，逐列或逐行计算
- 先学 NumPy 再学 pandas 的原因之一

## 边界与易混淆

NumPy 函数是逐元素数学运算，不含业务逻辑；条件分支需 lambda 包裹。

## 关联

- [[np.sqrt]] — 组合使用
- [[apply]] — 组合使用
- [[通用函数]] — 上位概念

## 自测

为什么 apply 里写 np.sqrt 要带 np. 前缀，而 len 不用？::np.sqrt 属于 NumPy 库需模块前缀，len 是 Python 内置函数直接写名。
整张表做数学计算时优先用什么？::优先用 NumPy 函数，而不是逐列 Series 操作。


### 补充 · 2026-11-17

NumPy 函数天生逐元素运算，DataFrame.apply(np.square) 或整列 * 运算都会作用到每个元素上。因为来自 NumPy 库，写的时候必须带 np. 前缀；而 len 这类 Python 内置函数则直接写名字。

- np.square 是平方，np.sqrt 才是平方根，别被口述带偏，以代码和结果为证
- 库函数要写库前缀 np.，内置函数（len）直接写
- 整表计算优先 NumPy 方案，效率与写法都优于逐行循环
np.sqrt 与 np.square 分别做什么？::sqrt 求平方根，square 求平方。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p26 S02E11.列与列之间的计算](https://www.bilibili.com/video/BV1ji4y157uB?p=26) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
