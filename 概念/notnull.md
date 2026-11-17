---
term: notnull
aliases: [notnull(), 判断非空]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 20
stage: "S02E05 · 数据结构之Series"
---

# notnull

> 别名：notnull()、判断非空

**判断数据是否不为空，返回布尔值（非空为 True）。**

## 用法
**语法**：`DataFrame.notnull()` / `Series.notnull()`
**参数**：无
**示例**：
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'姓名': ['张三', '李四', '王五'], '分数': [90, np.nan, 75]})
print(df.notnull())
#    姓名   分数
# 0  True  True
# 1  True  False
# 2  True  True

print(df[df['分数'].notnull()])
#    姓名    分数
# 0  张三  90.0
# 2  王五  75.0

print(df['分数'].notnull().sum())  # 2
```

## 解释

notnull() 与 isnull() 相反，非空值返回 True，空值返回 False。用于筛选非空数据或确认数据完整性。

## 有什么用

- 筛选非空数据
- 确认数据完整性

## 关键要点

- 非空返回 True，空返回 False
- 与 isnull() 结果相反

## 边界与易混淆

只判断是否非空，不处理空值；填充空值需用 fillna() 等。

## 关联

- [[isnull]] — 对比项
- [[Series]] — 组合使用

## 自测

notnull() 和 isnull() 的结果是什么关系？::两者结果相反：notnull() 非空为 True，isnull() 空为 True。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
