---
term: append 方法
aliases: [append, 追加, DataFrame.append, Series.append]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# append 方法

> 别名：append、追加、DataFrame.append、Series.append

**Series 和 DataFrame 的方法，将新数据追加到原对象下方并按列对齐。**

## 解释

append 用于在 DataFrame 或 Series 末尾追加行，按列名对齐，缺失字段填 NaN。效果类似 concat 的纵向连接，但语法更简洁。注意 append 在新版 Pandas 中已被弃用，推荐使用 pd.concat。

## 有什么用

- 向现有表追加一行或多行数据
- 快速合并两个结构相似的表

## 关键要点

- 按列名对齐，缺失字段自动填 NaN
- 可追加 Series、字典或 DataFrame
- ignore_index=True 可忽略原索引生成新索引
- 新版 Pandas 已弃用，建议改用 pd.concat

## 边界与易混淆

append 不是 concat 的方法，而是 DataFrame/Series 的方法；新版 Pandas 中已弃用。

## 关联

- [[pd.concat]] — 对比项
- [[ignore_index 参数]] — 组合使用

## 自测

df1.append(s2, ignore_index=True) 中 ignore_index=True 的作用是什么？::忽略原索引，按追加后的顺序生成新的连续索引。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
