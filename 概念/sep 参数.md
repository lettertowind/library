---
term: sep 参数
aliases: [sep, 分隔符参数, delimiter]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 17
stage: "S02E02 · 读取txt与csv文件"
---

# sep 参数

> 别名：sep、分隔符参数、delimiter

**read_csv/read_table 中指定字段分隔符的参数。**

## 解释

sep 决定 Pandas 如何切分每行文本。可传单个字符如 ','、'\t'，也可传正则表达式如 r'\s+' 处理混合空白分隔。分隔符选错会导致整行被当成一列。

## 有什么用

- 匹配文件实际分隔方式
- 处理空格与制表符混合的复杂文本

## 关键要点

- read_csv 默认 ','，read_table 默认 '\t'
- sep=r'\s+' 匹配一个或多个空白字符
- 正则分隔符可处理混合分隔场景

## 边界与易混淆

正则分隔符需注意转义与性能；简单固定分隔符优先用普通字符。

## 关联

- [[正则表达式]] — 组合使用
- [[pd.read_csv]] — 组合使用

## 自测

文件里既有空格又有制表符，sep 该怎么写？::sep=r'\s+'，匹配一个或多个空白字符。


### 补充 · 2026-11-17

read_csv 默认按逗号切分，遇到 Tab 分隔的文件必须写成 sep='\t'，否则整行会被当成一列。这一参数决定了读进来是一张表还是一堆错位的字符串。

- 默认值是逗号，Tab 分隔写 sep='\t'
- 分隔符写错时表现为整行挤成一列
- 写 CSV 时也可用 sep 指定输出分隔符
读一份 Tab 分隔的 txt，读出来只有一列，最可能的原因是什么？::没写 sep='\t'，Pandas 按默认逗号切分，整行成了一列
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p25 S02E10.各种数据自动填充](https://www.bilibili.com/video/BV1ji4y157uB?p=25) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
