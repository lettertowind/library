---
term: str.cat
aliases: [cat, 字符串拼接, concatenate]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
---

# str.cat

> 别名：cat、字符串拼接、concatenate

**将 Series 中字符串与指定字符或等长序列拼接的方法。**

## 用法
**语法**：`Series.str.cat(others=None, sep=None, na_rep=None, join='left')`
**参数**：
- `others`：要拼接的另一列、列表或固定字符，必须与目标列等长；不传时把整列首尾相连成一个长字符串
- `sep`：连接符，不传时字符串直接紧贴拼接
- `na_rep`：空值的替代文本，不指定时空值会让整条结果变成 NaN
- `join`：`others` 为 Series 时的索引对齐方式，默认 `'left'`
**示例**：
```python
import pandas as pd

s = pd.Series(['张', '李', '王'])
print(s.str.cat())            # 张李王
print(s.str.cat(sep='-'))     # 张-李-王

df = pd.DataFrame({'姓': ['张', '李'], '名': ['三', '四']})
print(df['姓'].str.cat(df['名'], sep='').tolist())        # ['张三', '李四']
print(df['姓'].str.cat(['变身'] * len(df), sep='').tolist())  # ['张变身', '李变身']

s2 = pd.Series(['A', None])
print(s2.str.cat(na_rep='?'))  # A?
```

## 解释

str.cat 用于把一列字符串与另一列、列表或固定字符连接起来，类似“穿糖葫芦”。不传参时把整列所有值首尾相连成一个长字符串；传参时可逐行拼接，但额外数据必须与目标列等长。

## 有什么用

- 把多个姓名合并成一个长文本
- 给每行数据追加固定后缀
- 按分隔符拼接多列内容

## 关键要点

- 不传参时整列平行连接成一个字符串
- sep 参数指定连接符
- 额外拼接数据必须与目标列等长
- na_rep 参数替换空值，避免结果出现 NaN

## 边界与易混淆

逐行拼接时额外数据长度必须等于行数，否则报错；空值需用 na_rep 显式处理。

## 关联

- [[Series.str 访问器]] — 上位概念
- [[str.join]] — 对比项
- [[NaN]] — 前置知识

## 自测

df['姓名'].str.cat(['变身']*len(df), sep='') 中为什么必须乘 len(df)？::因为逐行拼接要求额外数据与姓名列等长，长度不等会报错。
str.cat 不传任何参数时结果是什么？::把整列所有字符串首尾相连成一个长字符串。


### 补充 · 2026-11-17

Series.str.cat 默认把一列所有元素首尾相连（像穿糖葫芦），用 sep 加分隔符，用 na_rep 给空值一个替代文本。若要与另一组内容逐行拼接，传入的序列必须与原列等长。

- 无参数调用时整列元素直接连成一串，难以辨认
- sep 指定元素之间的分隔符，如 sep='、'
- 逐行追加内容时必须等长，用 ['内容'] * len(df) 构造
给每个姓名后加「变身」，为什么不能只写 str.cat('变身')？::因为要提供与原列等长的序列，如 ['变身'] * len(df)，否则长度不匹配
姓名列有空值时拼出来是 NaN，怎么让空位显示「无名」？::加参数 na_rep='无名'
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p38 S02E23.字符串操作（上）](https://www.bilibili.com/video/BV1ji4y157uB?p=38) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
