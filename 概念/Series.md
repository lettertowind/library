---
term: Series
aliases: [pd.Series, 一维数据结构]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 20
stage: "S02E05 · 数据结构之Series"
---

# Series

> 别名：pd.Series、一维数据结构

**Pandas 的一维数据结构，由索引和数据值两部分组成。**

## 解释

Series 是 Pandas 最基础的数据结构，可以表示一行或一列数据。它由 index（索引）和 values（数据值）构成，默认索引是从 0 开始的整数。多个 Series 可以组成 DataFrame。

## 有什么用

- 表示单行或单列数据
- 作为 DataFrame 的组成单元
- 快速创建和查询一维数据

## 关键要点

- Series 是一维数据，由索引 index 和数据 values 组成
- 默认索引从 0 开始，步长为 1，结束值不包含
- 类名 Series 首字母必须大写
- 单独看 Series 无法确定是行还是列，加入 DataFrame 后才确定
- 多键查询返回的仍是 Series 类型

## 边界与易混淆

Series 是一维的，不能直接表示多行多列；二维数据需用 DataFrame。

## 关联

- [[DataFrame]] — 组合使用
- [[index 参数]] — 组合使用
- [[sort_index]] — 组合使用
- [[sort_values]] — 组合使用
- [[isnull]] — 组合使用
- [[notnull]] — 组合使用

## 自测

Series 由哪两部分组成？默认索引是什么样的？::由索引 index 和数据 values 组成；默认索引是从 0 开始的整数，步长 1，结束值不包含。
为什么说单独一个 Series 无法确定是行还是列？::因为 Series 本身只是一维序列，只有加入 DataFrame 后，根据加入方式才确定它成为一行或一列。


### 补充 · 2026-11-17

DataFrame 的每一列就是一个 Series。df['姓名'] 与 df.姓名 完全等价，取出的都是 Series；绘图时通常无需转成列表。

- df['列名'] 与 df.列名 等价，返回同一个 Series
- Series 由索引 index 和值 values 两部分组成
- 取值数组用 .values，转 Python 列表用 .values.tolist()
要把某一列变成普通 Python 列表，怎么写？::df['列名'].values.tolist()，先取 values 再 tolist。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p50 S03E03.分组柱状图](https://www.bilibili.com/video/BV1ji4y157uB?p=50) · 2026-11-17

Series 是 pandas 最基础的数据结构，相当于带标签的一维数组，可以表示表格中的一行，也可以表示一列。多个 Series 按列拼在一起就构成 DataFrame。所有取值、排序、空值判断操作都建立在「索引 + 值」这两部分之上。

- 由 index（索引）和 values（值）组成，打印时左侧索引、右侧数据值
- 构造用 pd.Series()，S 必须大写，小写 series 不是正确用法
- 第一个位置参数放的是值，索引由 index= 参数指定
一个 Series 打印出来左右两部分分别是什么？::左边是索引列 index（默认 0、1、2…），右边是用户的数据值 values。
为什么说「Series 可以是一行也可以是一列」？::因为它只是带索引的一维序列，加入 DataFrame 时按不同方向拼接才决定成为行或列。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p20 S02E05.数据结构之Series](https://www.bilibili.com/video/BV1ji4y157uB?p=20) · 2026-11-17

Series 由一组值和一列索引组成，可以理解为“带标签的一维数据”。它是 DataFrame 的组成单元：把 DataFrame 的某一列（或某一行）取出来，得到的就是一个 Series。

- Series 是一维数据，不是“一维数组”
- 一维数组只能表示一行，而一维数据可以是一行也可以是一列
- 可用 pd.Series(...) 直接创建，也可从 DataFrame 取列得到
为什么说“Series 就是一维数组”这个说法不准确？::一维数组只能表示一行；Series 既可以是一行也可以是一列，是带索引的一维数据。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p16 S02E01.数据类型与新建文件](https://www.bilibili.com/video/BV1ji4y157uB?p=16) · 2026-11-17

Series 由一组值和一套索引组成，可选一个 name 作为列名。从 DataFrame 取一列得到的就是 Series；多个 Series 按 name 作列名、按 index 对齐就能拼回 DataFrame。

- 组成是 values + index，name 可指定列名
- df['列名'] 返回 Series，type 显示 pandas.core.series.Series
- 多列查询返回的则是 DataFrame
为什么 df['姓名'] 的 type 结果里看不到 str？::取列返回的是 Series 容器，元素类型由该 Series 的 dtype（object）体现
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p21 S02E06.数据结构之DataFrame](https://www.bilibili.com/video/BV1ji4y157uB?p=21) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
