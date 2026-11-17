---
term: Pandas
aliases: [pandas, Pandas 库]
kind: tool
domain: 数据分析/Python
tags: [概念/tool, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# Pandas

> 别名：pandas、Pandas 库

**Python 中处理表格数据的核心库，提供 Series 与 DataFrame 两种数据结构。**

## 解释

Pandas 建立在 NumPy 之上，专为带行列标签的表格数据设计。它把「读文件—清洗—连接—分组—输出」这一整套数据分析流程封装成简洁的 API，是课程第二季的主角。

## 有什么用

- 读写 CSV、Excel、数据库等多种数据源
- 缺失值处理、筛选、排序、去重、分组聚合
- 把分析结果输出成业务可看的表格

## 关键要点

- 两个核心结构：一维 Series、二维 DataFrame
- 数据与索引分离，索引对齐是很多操作的隐含规则
- 大部分方法默认返回新对象，不改原表；要原地修改需 `inplace=True`
- 与 NumPy 的关系：底层数组通用 NumPy 能力，外层加标签与表格语义

## 边界与易混淆

Pandas 擅长处理内存中的中小规模表格数据，不是数据库替代方案。数据量大到内存装不下时，要改用数据库或分块处理。

## 关联

- [[DataFrame]] — 核心结构
- [[Series]] — 核心结构
- [[NumPy 函数在 pandas 中的应用]] — 组合使用
- [[pd.read_csv]] — 常用入口

## 自测

为什么说 Pandas 建立在 NumPy 之上？::DataFrame 的底层仍是 NumPy 数组，向量化运算、dtype、广播等能力都来自 NumPy，Pandas 在其上加了行列标签与表格操作。

## 出处

- 孙兴华《Python 数据分析三部曲》p15–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
