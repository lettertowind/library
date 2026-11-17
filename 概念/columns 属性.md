---
term: columns 属性
aliases: [df.columns, 列索引, 查看列名]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# columns 属性

> 别名：df.columns、列索引、查看列名

**返回 DataFrame 全部列标签（字段名）的 Index 对象。**

## 解释

df.columns 用来查表有哪些字段，与 df.index 查行标签相对应。它返回的是 pandas 的 Index 对象，可遍历、可转成列表。给 df.columns 整体赋值即可批量重命名列。

## 有什么用

- 读表后先确认字段名拼写
- 批量改列名前取出旧列名
- 排查列名重复导致的取数异常

## 关键要点

- 返回 Index 对象，list(df.columns) 可转普通列表
- df.columns = [...] 整体重命名，个数必须与列数一致
- 与 df.index 一起构成 DataFrame 的行列双索引
- 列名重复时 df['a'] 返回 DataFrame 而不是 Series

## 边界与易混淆

列标签是“名字”，不是位置；改名后 loc 要用新名，iloc 不受影响。

## 关联

- [[DataFrame]] — 上位概念
- [[标签索引与位置索引]] — 组合使用
- [[dtypes 属性]] — 对比项
- [[loc]] — 组合使用

## 自测

如何一次性拿到表里所有字段名并存成列表？::list(df.columns)
df.columns 和 df.index 返回的东西本质区别是什么？::分别是列标签和行标签，都是 Index 对象，但作用维度不同

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p21 S02E06.数据结构之DataFrame](https://www.bilibili.com/video/BV1ji4y157uB?p=21) · 2026-11-17
