---
term: sort_values
aliases: [sort_values(), 按值排序]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# sort_values

> 别名：sort_values()、按值排序

**按数据值对 Series 或 DataFrame 进行排序的方法。**

## 解释

sort_values() 用于将数据按照值的大小或顺序排列。在 DataFrame 中通常配合 by 参数指定按哪一列排序，例如 df.sort_values(by='入职日期')。功能类似 Excel 的排序。

## 有什么用

- 按某列的值排序
- 对日期、数值等排序

## 关键要点

- 按数据值排序
- DataFrame 中用 by= 指定排序列
- 与 Excel 的排序功能类似

## 边界与易混淆

按索引排序需用 sort_index()；多列排序可传列表给 by。

## 关联

- [[Series]] — 组合使用
- [[DataFrame]] — 组合使用
- [[sort_index]] — 对比项

## 自测

在 DataFrame 中按“入职日期”列排序应该怎么写？::df.sort_values(by='入职日期')


### 补充 · 2026-11-17

sort_values 是 Pandas 最常用的排序方法，默认按列值对行排序。通过 by 指定排序键，ascending 控制方向，inplace 控制是否改原表。

- by 单字段写字符串，多字段写列表，列表顺序即优先级
- ascending 默认 True 升序，False 为降序
- 多字段时 ascending 也写列表，与 by 一一对应
按语文降序、数学升序排序，by 和 ascending 怎么写？::by=['语文','数学'], ascending=[False, True]
多字段排序后数学列看起来不是全局升序，为什么？::数学只在前一字段语文相同的分组内排序，不保证整列独立有序

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
