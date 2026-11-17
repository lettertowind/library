---
term: isna
aliases: [isnull, df.isna, 判断缺失值]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 31
stage: "S02E16 · 处理缺失值"
---

# isna

> 别名：isnull、df.isna、判断缺失值

**逐元素判断是否为缺失值，返回同形状的布尔表。**

## 用法
**语法**：`DataFrame.isna()` / `Series.isna()`（别名 `isnull()`，行为完全一致）
**参数**：无
**示例**：
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({"A": [1, np.nan, 3], "B": ["x", None, "z"]})
print(df.isna())
#        A      B
# 0  False  False
# 1   True   True
# 2  False  False

print(df.isna().sum())   # 每列缺失数量
# A    1
# B    1
# dtype: int64

print(df.isna().sum().sum())  # 全表缺失总数：2
print((~df.isna()).equals(df.notna()))  # 与 notna 互为取反：True
```

## 解释

isna() 与 isnull() 完全等价，返回 True 表示该位置缺失、False 表示非空。它是查看缺失值分布的基础工具，结果可直接用于筛选或计数。

## 有什么用

- 快速定位空值位置
- 配合 sum 统计每列缺失数量

## 关键要点

- isna 与 isnull 是同一函数的两个名字
- 返回布尔 DataFrame/Series，True 代表缺失
- 常与 sum() 组合统计各列缺失数
- 与 notna/notnull 互为取反

## 边界与易混淆

只判断空值形态的缺失，不识别占位符等隐性缺失。

## 关联

- [[notnull]] — 对比项
- [[缺失值处理]] — 上位概念
- [[布尔索引筛选]] — 组合使用

## 自测

df.isna().sum() 得到的是什么？::每一列缺失值的数量。
isna 和 notna 的结果是什么关系？::逻辑取反关系，同一位置结果相反。


### 补充 · 2026-11-17

isnull() 把一个表格或序列转换成同形状的布尔结果，空值位置标记为 True。常用于统计缺失数量（配合 sum）和筛出含缺失的行。

- 函数名后必须带括号
- 空值位置为 True，非空为 False
- 判断对象是整表时返回同形状的布尔 DataFrame
对整表调用 isnull() 得到的结果里 True 表示什么？::该位置是缺失值（如空单元格被读成 NaN）。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p20 S02E05.数据结构之Series](https://www.bilibili.com/video/BV1ji4y157uB?p=20) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
