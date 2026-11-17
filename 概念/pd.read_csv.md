---
term: pd.read_csv
aliases: [read_csv, 读取 CSV]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# pd.read_csv

> 别名：read_csv、读取 CSV

**Pandas 读取分隔文本文件的核心函数，默认逗号分隔。**

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
