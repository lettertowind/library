---
term: applymap
aliases: [DataFrame.applymap]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# applymap

> 别名：DataFrame.applymap

**对 DataFrame 每个单元格逐个执行函数，返回同形状的新表。**

## 解释

applymap 是 DataFrame 专属的逐元素方法，把每个单元格的值单独传入函数。常用于统一格式化，如保留小数位、加单位等。

## 有什么用

- 把整表数字统一格式化为保留三位小数
- 对每个单元格套用同一清洗函数

## 关键要点

- 只作用于 DataFrame，不能用于 Series
- 逐单元格执行，不感知行或列的整体结构
- 常配合 lambda 与格式化字符串使用
- 格式化后返回字符串，数值类型会改变
- 使用频率低于 map 和 apply

## 边界与易混淆

与 apply 区别：apply 按行/列整体处理，applymap 只看单个单元格，无法跨列计算。

## 关联

- [[apply]] — 对比项
- [[DataFrame]] — 上位概念

## 自测

要按行用两列算出一个新值，能用 applymap 吗？::不能，applymap 每次只拿到一个单元格，跨列计算要用 apply(axis=1)。
applymap 格式化小数后，列的数据类型会怎样？::变成字符串（object），不再是数值类型。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
