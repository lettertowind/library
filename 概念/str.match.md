---
term: str.match
aliases: [match, 正则匹配判断]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 39
stage: "S02E24 · 字符串操作（下）"
---

# str.match

> 别名：match、正则匹配判断

**判断字符串是否匹配指定正则表达式并返回布尔值的方法。**

## 用法
**语法**：`Series.str.match(pattern, case=True, flags=0, na=None)`

**参数**：
- `pattern`：正则表达式字符串，建议用原始字符串 `r'...'` 书写，避免反斜杠被转义
- `case`：是否区分大小写，默认 `True`
- `flags`：传给 `re` 模块的编译标志，如 `re.IGNORECASE`
- `na`：遇到缺失值（NaN）时返回的填充值，默认 `None`，结果为 `NaN` 而非 `False`

**示例**：
```python
import pandas as pd

s = pd.Series(['12激活', '满血激活', '3激活', None])
print(s.str.match(r'\d{2}激'))
# 0     True
# 1    False
# 2    False
# 3      NaN
# dtype: object
```

注意：`match` 只从字符串开头匹配，`'满血激活'` 返回 `False`；要提取内容请改用 `str.extract`。

## 解释

Series.str.match(pattern) 对每个元素做正则匹配，返回 True/False。常用于按模式筛选或标记数据，如判断状态列是否符合'两位数字+激'的格式。

## 有什么用

- 按正则模式筛选行
- 标记符合格式的数据

## 关键要点

- 返回布尔 Series
- pattern 用原始字符串 r'...' 书写
- \d 表示数字，{2} 表示出现两次
- 注意中英文符号切换导致匹配失败

## 边界与易混淆

match 从字符串开头匹配；需要提取内容用 extract，需要替换用 replace。

## 关联

- [[str.extract]] — 对比项
- [[str.replace]] — 对比项

## 自测

str.match(r'\d{2}激') 对 '满血激活' 返回什么？::False，因为开头不是两位数字。


### 补充 · 2026-11-17

str.match 只做「是否匹配」的判断，不做提取，也不做全文搜索——它默认从字符串起始位置开始比对。常配合 na 参数把缺失值统一成 False，再用布尔索引筛出目标行。

- na 参数控制缺失值结果，na=False 把 NA 直接变成 False
- \d 表示数字，{2} 是量词，r'\d{2}激' 即前两位数字后接「激」
- 从左往右但要整段匹配起点，不同于 search 的任意位置查找
为什么筛选时最好写 str.match(pattern, na=False)？::缺失值默认返回 NA，不是布尔值，直接用于筛选会出错或漏掉；na=False 把它统一成不匹配。
想从「20激」里取出「20」应该用 str.match 还是 str.extract？::用 str.extract 加捕获组 r'(\d{2})激'；str.match 只返回 True/False。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p39 S02E24.字符串操作（下）](https://www.bilibili.com/video/BV1ji4y157uB?p=39) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
