---
term: DataFrame
aliases: [df, 二维数据表]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 21
stage: "S02E06 · 数据结构之DataFrame"
---

# DataFrame

> 别名：df、二维数据表

**Pandas 的二维数据结构，表示多行多列的数据表。**

## 解释

DataFrame 是 Pandas 中用于处理表格数据的核心结构，可以看作由多个 Series 组成。编程中常简写为 df。它支持按列排序、空值判断等操作。

## 有什么用

- 处理 Excel 等表格数据
- 多行多列数据的分析与操作

## 关键要点

- DataFrame 是二维数据表，表示多行多列
- 可以由多个 Series 组成
- 编程中常简写为 df
- 按某列排序用 df.sort_values(by='列名')

## 边界与易混淆

DataFrame 是二维的，更高维数据需用 Panel 或其他结构（已不推荐）。

## 关联

- [[Series]] — 上位概念
- [[sort_values]] — 组合使用

## 自测

DataFrame 和 Series 是什么关系？::DataFrame 是二维数据结构，可以由多个 Series 组成；Series 是一维的，可表示 DataFrame 的一行或一列。


### 补充 · 2026-11-17

DataFrame 就是一张二维表格，对应 Excel 里的一个工作表。它的每一行、每一列单独看都是一个 Series。编程时习惯简写为 df，讲师在教学时也用中文变量名以便初学者一眼看懂含义。

- 二维结构：同时有行、列两个方向
- 由多个 Series 组合而成，一列就是一个 Series
- 惯例简写为 df，教学场景可用中文变量名替代
DataFrame 和 Series 的结构差异是什么？::DataFrame 是二维（行 + 列），Series 是一维；DataFrame 的每一列/行本质上都是一个 Series。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p20 S02E05.数据结构之Series](https://www.bilibili.com/video/BV1ji4y157uB?p=20) · 2026-11-17

DataFrame 是 Pandas 的核心容器，每列可以是不同数据类型（数值、字符、布尔）。它同时拥有行标签和列标签两套索引，既能按标签也能按位置取数。结构上可理解为“由多个 Series 按列名拼成的字典”。

- 行索引定位行，列索引（字段名）定位列，二者都不是数据本身
- 每列可有独立数据类型，用 dtypes 查看
- 取单列 df['a'] 返回 Series，取多列必须写 df[['a','b']]
df['姓名'] 用 type 查看得到什么？能据此判断元素是字符串吗？::得到 pandas.core.series.Series；不能，元素类型要看 df.dtypes（object/int64 等）
为什么说 DataFrame 是“多个 Series 组成的字典”？::每个 Series 的 name 成为列名，Series 的 index 成为对齐依据，整体就是键为列名的字典结构
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p21 S02E06.数据结构之DataFrame](https://www.bilibili.com/video/BV1ji4y157uB?p=21) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
