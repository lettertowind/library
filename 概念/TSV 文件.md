---
term: TSV 文件
aliases: [制表符分隔文件, tab-separated values]
kind: concept
domain: 数据分析/数据格式
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# TSV 文件

> 别名：制表符分隔文件、tab-separated values

**用制表符（Tab）作为字段分隔符的文本表格文件。**

## 解释

TSV 与 CSV 都是纯文本表格，区别只在分隔符：CSV 用逗号，TSV 用制表符。因为字段里很少含制表符，TSV 在天生物学、基因数据等场景更常见。

## 有什么用

- 保存表格数据，比 Excel 更轻量、跨语言通用
- 字段中天然包含逗号时，用 TSV 可免去引号转义

## 关键要点

- 分隔符是 `\t`，读取时 `sep='\t'`
- 文件扩展名常为 `.tsv` 或 `.txt`
- `pd.read_table()` 默认按制表符分隔，等价于 `pd.read_csv(sep='\t')`

## 边界与易混淆

TSV 不等于 CSV：分隔符不同，直接用 `read_csv` 读 TSV 会得到一整列。看到 `.txt` 后缀要先确认实际分隔符。

## 关联

- [[CSV 文件]] — 对比项
- [[pd.read_table]] — 读取方法
- [[sep 参数]] — 指定分隔符

## 自测

一个 `.txt` 文件读进来发现只有一列，最可能的原因是什么？::分隔符没指定对，文件可能是 Tab 分隔的 TSV，应改用 `pd.read_table()` 或 `pd.read_csv(sep='\t')`。

## 出处

- 孙兴华《Python 数据分析三部曲》p17（B站）· https://www.bilibili.com/video/BV1ji4y157uB?p=17 · 2026-11-17
