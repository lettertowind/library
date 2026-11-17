---
term: usecols 参数
aliases: [usecols, 选择列区域, usecols='F:I']
kind: concept
domain: 计算机/数据分析/Pandas
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# usecols 参数

> 别名：usecols、选择列区域、usecols='F:I'

**read_excel/read_csv 中指定只读取哪些列的参数，支持列名列表或 Excel 式区间。**

## 解释

usecols 用于在读取阶段就裁掉无关列，减少内存占用并避开左侧空列。它可以直接写 Excel 风格的区间字符串如 'F:I'，也可以传列名列表。

## 有什么用

- Excel 左侧有空列需要跳过
- 只关心部分列、想加快读取
- 配合 skiprows 修复表头错位

## 关键要点

- 支持 'F:I' 这种 Excel 列区间写法
- 也可传列名列表 ['姓名','性别']
- 与 skiprows 配合可解决空行空列导致的表头错位
- CSV 一般不需要，因为通常无空列

## 边界与易混淆

区间写法依赖 Excel 列字母，列顺序变动时容易失效；列名列表更稳健。

## 关联

- [[skiprows 参数]] — 组合使用
- [[pd.read_excel]] — 组合使用

## 自测

usecols='F:I' 和 usecols=['姓名','性别'] 有什么区别？::前者按 Excel 列字母区间取列，后者按列名取列；列顺序变化时前者可能取错。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
