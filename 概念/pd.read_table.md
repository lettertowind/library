---
term: pd.read_table
aliases: [read_table]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 17
stage: "S02E02 · 读取txt与csv文件"
order: 17
---

# pd.read_table

> 别名：read_table

**Pandas 读取文本文件的函数，默认以制表符 \t 分隔。**

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
