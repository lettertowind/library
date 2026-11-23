---
term: ffill 与 bfill
aliases: [df.ffill, df.bfill, Series.ffill, Series.bfill, 前向填充, 后向填充, 向下填充, 向上填充]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-23
order: 31
stage: "S02E16 · 处理缺失值"
---

# ffill 与 bfill

> 别名：df.ffill、df.bfill、Series.ffill、Series.bfill、前向填充、后向填充、向下填充、向上填充

**用相邻的有效值传播填充缺失值：`ffill` 往前找，`bfill` 往后找。**

## 用法

**语法**：

```python
DataFrame.ffill(*, axis=None, inplace=False, limit=None, limit_area=None)
DataFrame.bfill(*, axis=None, inplace=False, limit=None, limit_area=None)
```

Series 上用法完全相同：`s.ffill()`、`s.bfill()`。

**参数**：
- `axis`：填充方向，`0`/`'index'`（默认，沿行向下或向上）或 `1`/`'columns'`（沿列左右）
- `limit`：最多连续填充几个空值，其余保持为空
- `limit_area`：`'inside'` 只填被有效值夹在中间的空值，`'outside'` 只填两端露在外面的空值
- `inplace`：默认 `False` 返回新对象，`True` 原地修改

**示例**：

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({"A": [1, np.nan, np.nan, 4], "B": [np.nan, 20, np.nan, 40]})
print(df)
#      A     B
# 0  1.0   NaN
# 1  NaN  20.0
# 2  NaN   NaN
# 3  4.0  40.0

print(df.ffill())          # 用上方最近的有效值向下填
#      A     B
# 0  1.0   NaN   ← 顶部没有前值，仍是 NaN
# 1  1.0  20.0
# 2  1.0  20.0
# 3  4.0  40.0

print(df.bfill())          # 用下方最近的有效值向上填
#      A     B
# 0  1.0  20.0
# 1  4.0  20.0
# 2  4.0  40.0
# 3  4.0  40.0

print(df.ffill(limit=1))   # 每段连续空值最多填 1 个
#      A     B
# 0  1.0   NaN
# 1  1.0  20.0
# 2   NaN  20.0   ← 超出 limit，保持为空
# 3  4.0  40.0

print(df.ffill(axis=1))    # 横向填充：从左往右找有效值
#      A     B
# 0  1.0   1.0
# 1  NaN  20.0
# 2  NaN   NaN
# 3  4.0  40.0

s = pd.Series([1, np.nan, np.nan, np.nan])
print(s.ffill().tolist())              # [1.0, 1.0, 1.0, 1.0]
print(pd.Series([np.nan, np.nan, 3, 4]).bfill().tolist())   # [3.0, 3.0, 3.0, 4.0]
```

## 解释

`ffill`（forward fill）沿指定方向找**前面**最近的非空值填进当前空位，`bfill`（backward fill）则找**后面**的非空值。两者都只处理 NaN，有效值本身不动。填充会一直延续，直到遇到下一个有效值或被 `limit` 截断。

## 有什么用

- 时间序列、传感器采样等「值应保持不变直到下次更新」的场景
- 有序数据的空缺补全，保持趋势连续
- 比填均值更适合有前后依赖关系的数据

## 关键要点

- `ffill` = 前向/向下填充，`bfill` = 后向/向上填充
- 两个方向都找不到有效值时（如开头全空用 ffill），该位置仍是 NaN
- `axis=1` 可把上下方向变成左右方向
- 默认返回新对象，要原地改需 `inplace=True`
- 旧写法 `pad` / `backfill` 是它们的别名，仅为兼容保留

## 边界与易混淆

**这是最容易踩的坑**：老教程写的 `df.fillna(method='ffill')` 在 pandas 2.1 起被弃用，pandas 3.0 已彻底移除，现在会直接报 `TypeError: fillna() got an unexpected keyword argument 'method'`。看到旧代码必须改成 `df.ffill()` / `df.bfill()`。

另外，`ffill`/`bfill` 只是搬运已有的值，不做推断；要按趋势算出新值应该用 `interpolate()`（线性插值）。

## 关联

- [[fillna]] — 上位概念，按常量或字典填充
- [[limit 参数（fillna）]] — 限制填充个数
- [[axis 参数]] — 控制填充方向
- [[inplace 参数]] — 是否原地修改
- [[isnull]] — 填充前先看缺失分布
- [[NaN]] — 处理对象
- [[shift]] — 对比项：平移而非填充

## 自测

`ffill()` 和 `bfill()` 的填充方向分别是什么？::ffill 用前面（上方）最近的有效值向下填，bfill 用后面（下方）最近的有效值向上填。

一列开头连续 3 个空值，直接 `ffill()` 后开头还是空，为什么？::ffill 只往前找有效值，开头之前没有值可借，所以保持 NaN；这种位置只能用 bfill 或填常量。

旧代码 `df.fillna(method='ffill')` 在新版 pandas 报什么错？::TypeError，`method` 关键字已被移除，应改写成 `df.ffill()`。

## 出处

- 孙兴华《Python 数据分析三部曲》p31 · S02E16 处理缺失值（B站）· https://www.bilibili.com/video/BV1ji4y157uB?p=31 · 2026-11-17
