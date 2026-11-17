---
term: SUMIF
aliases: [sumif, 条件求和]
kind: tool
domain: 计算机/办公软件/Excel
tags: [概念/tool, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# SUMIF

> 别名：sumif、条件求和

**Excel 中按条件对指定区域求和的函数。**

## 解释

SUMIF 先按条件筛选，再对符合条件的单元格求和，是 Excel 常用的条件汇总方式。它常被拿来类比 Pandas 的分组求和，但返回的是单个汇总值。

## 有什么用

- 按城市、类别等条件求和
- Excel 表格中的条件汇总

## 关键要点

- 语法：SUMIF(条件区域, 条件, [求和区域])
- 只按一个条件求和，多条件需用 SUMIFS
- 结果是一个汇总值，不保留分组明细
- 常与筛选、分类汇总等 Excel 操作配合

## 边界与易混淆

不等同于 groupby：SUMIF 是单元格公式，groupby 返回按组排列的结果表，可继续做多列多种聚合。

## 关联

- [[groupby]] — 对比项
- [[GROUP BY]] — 对比项

## 自测

SUMIF 和 groupby 都能按条件求和，核心区别是什么？::SUMIF 返回单个汇总值；groupby 返回按组排列的结果表，可继续做多列、多种聚合。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p41 S02E26.分组与聚合 groupby基础部分](https://www.bilibili.com/video/BV1ji4y157uB?p=41) · 2026-11-17
