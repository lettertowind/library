---
term: str.endswith
aliases: [endswith, 结尾判断]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
---

# str.endswith

> 别名：endswith、结尾判断

**判断字符串是否以指定内容结尾的方法。**

## 用法
**语法**：`Series.str.endswith(pat, na=None)`

**参数**：
- `pat`：要判断的后缀，str 或 tuple（可一次传入多个后缀）
- `na`：遇到缺失值（NaN）时返回的值，默认 None，此时缺失位置返回 NaN 而非 False

**示例**：
```python
import pandas as pd

s = pd.Series(['data.csv', 'report.xlsx', 'notes.txt', None])
print(s.str.endswith('.csv').tolist())
# [True, False, False, False]

print(s.str.endswith(('.csv', '.txt'), na=False).tolist())
# [True, False, True, False]

df = pd.DataFrame({'file': ['a.csv', 'b.xlsx', 'c.csv']})
print(df[df['file'].str.endswith('.csv')])
#    file
# 0  a.csv
# 2  c.csv
```

## 解释

str.endswith 对每个元素判断是否以指定内容结尾，返回布尔值。用法与 str.startswith 对称，同样支持 na 参数。

## 有什么用

- 筛选以某后缀结尾的记录
- 按文件扩展名分类

## 关键要点

- 返回布尔值
- 支持 na 参数
- 与 startswith 方向相反

## 边界与易混淆

只判断结尾，不判断包含。

## 关联

- [[str.startswith]] — 对比项
- [[Series.str 访问器]] — 上位概念

## 自测

判断字符串是否以“.csv”结尾用哪个方法？::str.endswith('.csv')。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
