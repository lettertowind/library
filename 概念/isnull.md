---
term: isnull
aliases: [isnull(), 判断空值]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 20
stage: "S02E05 · 数据结构之Series"
---

# isnull

> 别名：isnull()、判断空值

**判断数据是否为空值，返回布尔值（空为 True）。**

## 用法
**语法**：`df.isnull()` / `series.isnull()`（别名 `df.isna()`）

**参数**：无。`isnull()` 不接受参数，直接对 DataFrame 或 Series 逐元素返回布尔值。

**示例**：
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "成绩": [90, np.nan, 75],
})
print(df.isnull())
#    姓名     成绩
# 0  False  False
# 1  False   True
# 2  False  False

print(df["成绩"].isnull().sum())  # 1  —— 判断不统计，配合 sum() 才计数
print(df.notnull().all().all())   # False —— 与 notnull() 结果相反
```

## 解释

isnull() 对每个元素判断是否为空，空值返回 True，非空返回 False。常用于发现缺失值，Pandas 中空值常用 NaN 表示。

## 有什么用

- 检测缺失值
- 数据清洗前排查空值

## 关键要点

- 空值返回 True，非空返回 False
- 常与 NaN 缺失值配合使用
- 与 notnull() 结果相反

## 边界与易混淆

只判断是否为空，不统计数量；统计可用 sum() 配合。

## 关联

- [[notnull]] — 对比项
- [[Series]] — 组合使用

## 自测

isnull() 对空值和非空值分别返回什么？::空值返回 True，非空值返回 False。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
