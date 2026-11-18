---
term: labels 参数
aliases: [labels, labels=[...], 标签列表参数]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 30
stage: "S02E15 · 数据删除 drop函数"
---

# labels 参数

> 别名：labels、labels=[...]、标签列表参数

**drop 中用于一次传入多个待删除行/列标签的列表参数。**

## 解释

labels 参数让 drop 支持批量删除：把多个行标签或列标签放进列表传给 labels。删除单标签可直接传，删除多标签必须用 labels 列表，否则会被误解析。

## 有什么用

- 批量删除多行
- 批量删除多列
- 按标签集合清理数据

## 关键要点

- 多标签删除必须用 labels=[...] 列表形式
- 列表内标签用逗号分隔
- 配合 axis=1 可批量删列
- 单标签可省略 labels 直接传

## 边界与易混淆

labels 传的是标签不是位置；若索引是默认 RangeIndex，标签恰好等于行号，容易误以为是按位置删除。

## 关联

- [[drop]] — 组合使用
- [[axis 参数]] — 组合使用

## 自测

要删除行标签 1 和 3，正确写法是什么？::df.drop(labels=[1, 3])，默认 axis=0 按行删除。
labels 里写的是行号还是行标签？::行标签。默认索引下二者恰好一致，但本质是标签。


### 补充 · 2026-11-17

labels 是 drop 的标签入口：传单个标签时可省略参数名直接写，传多个标签时必须以列表形式交给 labels。行标签和列标签都走这个参数，具体删行还是删列由 axis 决定。

- 多标签必须用列表：labels=[1, 3]
- 单个标签可省略参数名：data.drop(1)
- 删行删列共用 labels，靠 axis 区分方向
删除行标签 1 和 3，两种写法分别是什么？::data.drop(labels=[1, 3])，或显式写成 data.drop(labels=[1,3], axis=0)；只写 data.drop(1, 3) 是错的。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p30 S02E15.数据删除 drop函数](https://www.bilibili.com/video/BV1ji4y157uB?p=30) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
