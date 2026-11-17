---
term: dropna 参数（透视表）
aliases: [dropna, 删除全空列]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 43
stage: "S02E28 · 数据透视表"
order: 43
---

# dropna 参数（透视表）

> 别名：dropna、删除全空列

**pivot_table 中控制是否移除全部为空的列的参数。**

## 解释

dropna 默认 False；设为 True 时，结果中所有条目均为空的列会被移除，不再显示。它不影响有值数据的计算，只是清理结果中无意义的空列。

## 有什么用

- 透视结果出现整列空值时清理显示
- 导出前精简结果表

## 关键要点

- 默认 False
- True 时删除全空列
- 不影响正常有值数据的计算

## 边界与易混淆

与 DataFrame.dropna 同名但作用范围不同，这里只针对透视结果的全空列。

## 关联

- [[pivot_table]] — 组合使用
- [[fill_value 参数]] — 对比项

## 自测

dropna=True 会删除含部分空值的列吗？::不会，只删除所有条目均为空的列。


### 补充 · 2026-11-17

dropna() 默认 axis=0、how='any'，即只要某行有一个空值就删除该行。通过 axis、how、thresh、subset 可以精细控制删除条件，inplace 控制是否原地修改。

- 默认 axis=0、how='any'：行内有一个空值就删
- how='all'：整行/整列全空才删
- thresh=n：非缺失值少于 n 才删除
dropna(thresh=2) 的含义是什么？::保留至少有两个非缺失值的行/列，非缺失值少于 2 的才删除。
想只根据语文、数学两列判断是否删除行，怎么写？::df.dropna(subset=['语文','数学'])。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
