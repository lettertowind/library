---
term: notna
aliases: [notnull, df.notna, 判断非缺失值]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 31
stage: "S02E16 · 处理缺失值"
---

# notna

> 别名：notnull、df.notna、判断非缺失值

**逐元素判断是否为非缺失值，返回布尔表，True 表示非空。**

## 用法
**语法**：`DataFrame.notna()` / `Series.notna()`（别名 `notnull()`）

**参数**：无

**示例**：
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, np.nan, 3], 'B': ['x', None, 'z']})
print(df.notna())
#        A      B
# 0   True   True
# 1  False  False
# 2   True   True

print(df.notna().sum())      # 每列有效值数量
# A    2
# B    2
# dtype: int64

print(df[df['A'].notna()])   # 布尔索引保留 A 列非空的行
#      A     B
# 0  1.0     x
# 2  3.0     z
```

## 解释

notna() 与 notnull() 等价，是 isna 的取反。用于保留有效数据、统计非空数量，或在填充前确认哪些位置需要处理。

## 有什么用

- 筛选出非空行
- 统计每列有效值数量

## 关键要点

- notna 与 notnull 是同一函数
- True 表示非缺失，与 isna 相反
- 常与 sum() 组合统计有效值数量
- 可用于布尔索引保留有效行

## 边界与易混淆

同样只识别空值形态的缺失。

## 关联

- [[isnull]] — 对比项
- [[缺失值处理]] — 上位概念

## 自测

想统计每列有效值个数，用哪个函数？::df.notna().sum()。
notna 与 notnull 有区别吗？::没有，是同一函数的别名。


### 补充 · 2026-11-17

notnull() 是 isnull() 的取反版本，常用于只保留有效数据的过滤条件，语义上比「取反 isnull」更直观。

- 与 isnull() 结果互补，True/False 完全颠倒
- 函数名后必须带括号
- notna 是同义写法
同一张表上 isnull() 与 notnull() 的结果有什么关系？::逐元素取反，True/False 完全相反。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p20 S02E05.数据结构之Series](https://www.bilibili.com/video/BV1ji4y157uB?p=20) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
