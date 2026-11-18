---
term: str.rstrip
aliases: [rstrip, 右侧去除]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
---

# str.rstrip

> 别名：rstrip、右侧去除

**按字符集合从字符串右侧去除字符的方法。**

## 用法
**语法**：`Series.str.rstrip(to_strip=None)`
**参数**：
- `to_strip`：str 或 None，默认 None；指定右侧要清除的**字符集合**，集合中的符号按“任一字符属于集合就删除”的规则处理，不做子串匹配；为 None 时只清除右侧空白字符
**示例**：
```python
import pandas as pd
s = pd.Series(['  a  ', 'b--', '--c'])
print(s.str.rstrip().tolist())     # ['  a', 'b--', '--c'] 默认只去右侧空白
print(s.str.rstrip('-').tolist())  # ['  a  ', 'b', '--c'] 只去右侧的 '-'
print(s.str.rstrip(' -').tolist()) # ['  a', 'b', '--c'] 字符集合可含空格
print(s.str.lstrip('-').tolist())  # ['  a  ', 'b--', 'c'] 对照：lstrip 只动左侧
```
> 语义与内置 `str.rstrip` 完全一致；对非字符串列先 `.astype(str)`，缺失值默认保留为 NaN。

## 解释

str.rstrip(chars) 是 str.strip 的单侧版本，只从右边去除属于字符集合的字符。

## 有什么用

- 只清理右侧后缀
- 去除结尾的多余符号

## 关键要点

- 只从右侧去除
- 参数同样是字符集合
- 与 lstrip 方向相反

## 边界与易混淆

只处理右侧，左侧不动。

## 关联

- [[str.strip]] — 上位概念
- [[str.lstrip]] — 对比项

## 自测

只想去除字符串结尾的符号用哪个方法？::str.rstrip。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
