---
term: agg
aliases: [aggregate, 聚合方法, DataFrameGroupBy.agg]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 41
stage: "S02E26 · 分组与聚合 groupby基础部分"
---

# agg

> 别名：aggregate、聚合方法、DataFrameGroupBy.agg

**对分组结果按列指定聚合方式的方法，支持一列一函数或一列多函数。**

## 用法
**语法**：`DataFrameGroupBy.agg(func)` / `DataFrameGroupBy.agg(字典)`

**参数**：
- `func`：聚合函数，可以是字符串（如 `'count'`、`'mean'`、`'sum'`）、Python 内置函数（如 `sum`、`max`，不加引号），或函数列表（一列多函数）
- 传入字典时，键为列名，值为该列要应用的聚合函数，可以为每列分别指定

**示例**：
```python
import pandas as pd

df = pd.DataFrame({
    '电号': ['A', 'A', 'B', 'B'],
    '1月': [100, 200, 300, 400],
    '2月': [10, 20, 30, 40]
})

# 不同列用不同聚合：1 月计数，2 月求和
print(df.groupby('电号').agg({'1月': 'count', '2月': sum}))
#     1月   2月
# 电号
# A     2   30
# B     2   70

# 一列多函数：2 月同时求和与平均
print(df.groupby('电号').agg({'2月': ['sum', 'mean']}))
#       2月
#      sum  mean
# 电号
# A     30  15.0
# B     70  35.0
```

## 解释

agg 基于列进行聚合，最大价值是「不同列用不同聚合函数」：传入字典 {列名: 函数} 即可分别指定 count、sum、max、mean 等。它与 groupby 分工不同——groupby 管按行分组，agg 管按列聚合。

## 有什么用

- 不同列需要不同统计口径时
- 一列同时要多个统计量时
- 替代多次 groupby 调用

## 关键要点

- 字典写法：df.groupby('电号').agg({'1月':'count','2月':sum})
- sum、max 是 Python 内置函数可不加引号
- count、mean 是 Pandas 聚合名，必须加引号
- 编辑器里内置函数会变色，可借此判断是否加引号

## 边界与易混淆

agg 负责列方向聚合，不要与 groupby 的行方向分组混淆；对非数值列用 sum/mean 会报错或得到意外结果。

## 关联

- [[groupby]] — 组合使用
- [[Pandas 数学统计函数]] — 上位概念

## 自测

要让 1 月计数、2 月求和，应该怎么写？::df.groupby('电号').agg({'1月':'count','2月':sum})。
为什么 'count' 要加引号而 sum 不用？::count 不是 Python 内置函数而是 Pandas 聚合名，sum 是 Python 内置函数。


### 补充 · 2026-11-17

agg 可接收字典，为不同列分别指定 count、sum、max、mean 等聚合方式，解决“不同列用不同函数”的需求。它也可接收单个函数名或函数列表。

- 字典键为列名，值为函数对象或函数名字符串
- Python 内置函数 sum、max 不加引号；Pandas 方法名 'count'、'mean' 要加引号
- agg 是基于列的聚合，和 groupby 按行拆分互补
为什么 agg 字典里写 'count': 'count' 要加引号，而 sum 不加？::count 是 Pandas 的聚合方法名，需用字符串；sum 是 Python 内置函数，可直接传函数对象。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p41 S02E26.分组与聚合 groupby基础部分](https://www.bilibili.com/video/BV1ji4y157uB?p=41) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
