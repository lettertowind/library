---
term: Power Query 追加查询
aliases: [追加查询, Append Queries, Power Query]
kind: tool
domain: 计算机/办公软件/Excel
tags: [概念/tool, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# Power Query 追加查询

> 别名：追加查询、Append Queries、Power Query

**Excel Power Query 中把多张结构相同表上下堆叠为一张表的操作。**

## 解释

属于 Power Query 的“追加”而非“合并”：追加是往底下加行，合并是按公共列横向扩展。它与 Pandas 纵向 concat/append 的思路一致，可作类比理解。

## 有什么用

- 把多个同结构的工作表/CSV 汇总成一张总表
- 为数据透视和建模准备宽表

## 关键要点

- 追加 = 加行（纵向），合并 = 按列扩（横向）
- 列名不一致时会产生大量 null 值
- 类比不是等价：实现细节与索引处理都不同

## 边界与易混淆

只是帮助理解的类比，不要当作与 pandas 完全一致的行为标准。

## 关联

- [[pd.concat]] — 对比项
- [[append 方法]] — 对比项
- [[VBA]] — 组合使用

## 自测

Power Query 的“追加查询”对应 pandas 的哪类操作？::纵向堆叠，即 axis=0 的 concat 或 append。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p24 S02E09.连接查询之concat](https://www.bilibili.com/video/BV1ji4y157uB?p=24) · 2026-11-17
