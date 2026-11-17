---
term: str.split
aliases: [split, 字符串拆分]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
---

# str.split

> 别名：split、字符串拆分

**按指定字符把字符串拆分成列表的方法。**

## 用法
**语法**：`Series.str.split(pat=None, n=-1, expand=False)`
**参数**：
- `pat`：分隔符，默认为空白字符；可以是字符串或正则表达式
- `n`：拆分次数，默认 `-1` 表示全部分隔符都参与拆分，`n=1` 表示只拆第一个分隔符
- `expand`：默认 `False` 时，返回的仍是包含列表的 Series；设为 `True` 时，返回拆成多列的 DataFrame
**示例**：
```python
import pandas as pd

s = pd.Series(["满血激活", "残血待机", "满血待机"])
print(s.str.split("血").tolist())
# [['满', '激活'], ['残', '待机'], ['满', '待机']]

print(s.str.split("血", expand=True))
#    0   1
# 0  满  激活
# 1  残  待机
# 2  满  待机

print(s.str.split("血", n=1, expand=True).shape)
# (3, 2)
```

## 解释

str.split 将每个字符串按分隔符切开，默认返回列表形式。可通过 n 控制拆分次数，通过 expand=True 把拆分结果展开成多列，效果类似 Excel 的分列。

## 有什么用

- 把“满血激活”拆成状态和动作
- 按分隔符把一列拆成多列
- 只拆分前 N 个分隔符

## 关键要点

- 默认 n=-1，全部分隔符都参与拆分
- n=1 表示只拆分第一个分隔符
- expand=True 将列表展开为多列
- 分隔符本身不出现在结果中

## 边界与易混淆

expand=True 时列数由最大拆分数量决定；空值仍保持为空。

## 关联

- [[Series.str 访问器]] — 上位概念
- [[str.rsplit]] — 对比项
- [[str.partition]] — 对比项

## 自测

str.split('血', expand=True) 和 str.split('血') 的结果差异是什么？::前者把拆分结果展开成多列，后者每行仍是一个列表。
n 参数默认值是多少，含义是什么？::默认 -1，表示所有分隔符都参与拆分。


### 补充 · 2026-11-17

Series.str.split 与 Python 内置 split 行为一致：分隔符本身被丢弃，空值仍为空值。通过 n 控制拆几次，通过 expand 控制结果是列表还是多列，是文本分列的主力方法。

- 不传分隔符时按空白拆分，结果仍是列表
- n 指定拆分次数，默认 n=-1 表示全部拆开
- expand=True 把列表展开成多列，默认 False 返回列表
想让 df['状态'] 按「血」拆成两列而不是两段列表，要加什么参数？::expand=True
字符串里有多个分隔符，但只想拆开前一个，用哪个参数控制？::n，传入较小的整数
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p38 S02E23.字符串操作（上）](https://www.bilibili.com/video/BV1ji4y157uB?p=38) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
