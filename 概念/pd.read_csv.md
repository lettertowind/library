---
term: pd.read_csv
aliases: [read_csv, 读取 CSV]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 17
stage: "S02E02 · 读取txt与csv文件"
---

# pd.read_csv

> 别名：read_csv、读取 CSV

**Pandas 读取分隔文本文件的核心函数，默认逗号分隔。**

## 用法
**语法**：`pd.read_csv(filepath_or_buffer, sep=',', header='infer', names=None, usecols=None, nrows=None, encoding=None)`
**参数**：
- `filepath_or_buffer`：文件路径或类文件对象（如 `StringIO`），不限于 `.csv` 后缀的分隔文本
- `sep`：分隔符，默认 `','`；读取制表符文件时用 `sep='\t'`
- `header`：表头所在行号，默认为 `'infer'`；文件无表头时写 `None`，再配合 `names` 自定义列名
- `names`：自定义列名列表，常与 `header=None` 搭配
- `usecols`：只读入指定列，减少内存占用
- `nrows`：只读取前 n 行，真正减少内存中的数据量；`head()` 只影响显示
- `encoding`：文件编码，中文乱码时用 `'utf-8'` 或 `'gbk'`
**示例**：
```python
import io
import pandas as pd

txt = "1\t杨过\t95\n2\t小龙女\t88\n3\t郭靖\t90\n"
df = pd.read_csv(io.StringIO(txt), sep='\t', header=None,
                 names=['序号', '姓名', '分数'], nrows=2)
print(df.values.tolist())
# [[1, '杨过', 95], [2, '小龙女', 88]]   ← nrows 只读入 2 行
print(df.columns.tolist())
# ['序号', '姓名', '分数']
```

## 解释

read_csv 是 Pandas 读取文本数据的入口函数，可读 txt、csv、tsv 等分隔文本。默认 sep=','，通过参数可适配制表符、正则分隔符、无表头、指定索引、跳过行、限制行数等场景。

## 有什么用

- 读取 csv/txt/tsv 数据文件
- 大数据文件先预览或限制行数读取

## 关键要点

- 默认 sep=','，读制表符文件需 sep='\t'
- 与 read_table 本质相同，仅默认分隔符不同
- header=None 表示文件无表头，配合 names 自定义列名
- nrows 真正限制读取行数，head() 只影响显示
- encoding='utf-8' 解决中文乱码

## 边界与易混淆

read_csv 不是只能读 .csv 后缀文件，任何分隔文本都能读；与 head() 的区别在于是否真正减少内存中的数据量。

## 关联

- [[pd.read_table]] — 对比项
- [[header 参数]] — 组合使用
- [[nrows 参数]] — 组合使用
- [[pd.read_excel]] — 对比项

## 自测

一个用制表符分隔的 txt 文件，用 read_csv 直接读会怎样？怎么修正？::会整行当成一列；需指定 sep='\t'。
nrows=3 和 print(data.head(3)) 对内存的影响有何不同？::nrows 只读 3 行进内存；head(3) 已读全部数据，只是显示 3 行。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
