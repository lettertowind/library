---
term: pd.read_table
aliases: [read_table]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 17
stage: "S02E02 · 读取txt与csv文件"
---

# pd.read_table

> 别名：read_table

**Pandas 读取文本文件的函数，默认以制表符 \t 分隔。**

## 用法
**语法**：`pd.read_table(filepath_or_buffer, sep='\t', header='infer', names=None, index_col=None, usecols=None, dtype=None, nrows=None, encoding=None)`
**参数**：
- `filepath_or_buffer`：文件路径，也可以是 URL，或任何带 `read()` 方法的类文件对象
- `sep`：分隔符，默认是制表符 `'\t'`；读取逗号分隔文件时必须显式写成 `sep=','`，否则整行会被当成一列
- `header`：指定哪一行作为列名，默认用 `'infer'` 自动推断；传 `None` 表示文件中没有表头
- `names`：自定义列名列表，常与 `header=None` 配合使用
- `index_col`：指定用哪一列作为行索引，可以传列号或列名
- `usecols`：只读取指定的列，可以传列名列表或列号列表
- `dtype`：为指定列设置数据类型，例如 `{'id': str}`，可避免前导零丢失
- `nrows`：只读取前 n 行，常用于先预览大文件
- `encoding`：文件编码，中文文件常用 `'utf-8'` 或 `'gbk'`
**示例**：
```python
import pandas as pd
import io

tsv = io.StringIO("name\tage\nTom\t20\nJerry\t22\n")
df = pd.read_table(tsv)
print(df)
#     name  age
# 0    Tom   20
# 1  Jerry   22

csv = io.StringIO("name,age\nTom,20\nJerry,22\n")
print(pd.read_table(csv, sep=',').shape)  # (2, 2)  读逗号文件必须加 sep
```

## 解释

read_table 与 read_csv 功能一致，唯一区别是默认分隔符为制表符，适合 tsv 或 tab 分隔文件。读逗号分隔文件时需显式传 sep=','。

## 有什么用

- 读取 tsv 或 tab 分隔文本
- 与 read_csv 按习惯二选一

## 关键要点

- 默认 sep='\t'
- 读逗号文件必须手动 sep=','
- 与 read_csv 无文件类型限制差异

## 边界与易混淆

容易误以为 read_table 只能读 tsv，其实任何分隔文本都能读，只是默认分隔符不同。

## 关联

- [[pd.read_csv]] — 对比项
- [[sep 参数]] — 组合使用

## 自测

read_table 读逗号分隔文件为什么结果不对？如何修正？::默认按 \t 分隔找不到制表符，整行成一列；传 sep=',' 修正。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
