---
term: fillna
aliases: [df.fillna, 空值填充]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 31
stage: "S02E16 · 处理缺失值"
---

# fillna

> 别名：df.fillna、空值填充

**将 DataFrame 中的缺失值替换为指定值的方法。**


## 用法
**语法**：`df.fillna(value=None, method=None, inplace=False, limit=None)`

**参数**：
- `value`：填充值，标量统一填充，字典按列名指定不同值
- `method`：旧版写法，`'ffill'` 用前值、`'bfill'` 用后值；pandas 2.x 已废弃，改用 `df.ffill()` / `df.bfill()`
- `inplace`：默认 `False` 返回新对象，`True` 则原地修改
- `limit`：最多连续填充多少个空值

**示例**：
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({"A": [1, np.nan, 3], "B": [np.nan, 20, 30]})
print(df.fillna(0))                     # 统一填 0
print(df.fillna({"A": 9, "B": 99}))     # 按列填不同值
print(df.ffill())                       # 用前一个非空值填充（新版写法）
```

## 解释

fillna(value) 扫描所有 NaN 位置并填入给定值，非空值保持不变。它是数据清洗中最常用的缺失值处理手段之一，可填 0、均值或指定常量。

## 有什么用

- 清洗含缺失值的数据
- 为后续计算补齐空值

## 关键要点

- 只填充 NaN，不改动非空值
- 可填任意常量，如 0、1、均值
- 默认返回新对象，不修改原表
- 常与 isnull 配合先检查再填充

## 边界与易混淆

填充值选择不当会引入偏差；需要原地修改时要加 inplace=True。

## 关联

- [[NaN]] — 前置知识
- [[isnull]] — 组合使用
- [[DataFrame]] — 上位概念

## 自测

df.fillna(0) 会把非空值也改成 0 吗？::不会，只填充 NaN 位置，非空值保持不变。
填充缺失值前为什么要先用 isnull 检查？::先确认缺失分布和比例，才能决定填什么值、是否值得填。


### 补充 · 2026-11-17

fillna() 支持三种主要填充方式：传常量统一填充、传字典按列填充不同值、用 method 参数以前值或后值填充。配合 axis 可改变填充方向，limit 限制填充数量。

- 传常量：所有空值填同一个值
- 传字典：按列指定不同填充值
- method='ffill'/'pad' 用前值，'bfill'/'backfill' 用后值
不同列要填不同值，fillna 怎么传参？::传字典，如 df.fillna({'语文':0.1,'数学':0.2})。
fillna(method='bfill') 和 ffill 有什么区别？::bfill 用后面的有效值向上填充，ffill 用前面的有效值向下填充。

fillna 是缺失值处理中使用频率最高的一步。它支持三种填充方式：常量统一填充、字典按列指定不同值、method 按前后有效值传播填充；再配合 axis 控制方向、limit 控制数量，就能覆盖大部分补数场景。

- data.fillna(520) 把所有空值统一填充为 520
- 字典填充：键是列名、值是填充值，如 {'语文':0.1,'数学':0.2}
- method='ffill' 用前面的值向下填，'bfill' 用后面的值向上填
要给语文列填 0.1、数学列填 0.2、英语列填 0.3，fillna 的参数该怎么写？::传入字典：data.fillna({'语文':0.1,'数学':0.2,'英语':0.3})，键为列名、值为该列填充值。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p31 S02E16.处理缺失值](https://www.bilibili.com/video/BV1ji4y157uB?p=31) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
