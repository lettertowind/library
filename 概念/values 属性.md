---
term: values 属性
aliases: [df.values, 查询值, 纯数据数组]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
---

# values 属性

> 别名：df.values、查询值、纯数据数组

**返回 DataFrame 剥离行列标签后的纯数据 ndarray。**

## 解释

df.values 把表变成 NumPy 二维数组，只留数据、丢掉行索引和列名。适合交给只认数组的下游函数（如 sklearn、matplotlib）。代价是丢失标签信息，且混合类型会被统一成 object 或 float。

## 有什么用

- 把表格数据喂给 NumPy/sklearn 接口
- 查看底层数组形态
- 做纯数值计算前的转换

## 关键要点

- 返回 numpy.ndarray，不再带行名和列名
- 混合数据类型时整体 dtype 可能退化为 object
- 需要保留标签就别用 values，直接操作 DataFrame
- 新版更推荐 to_numpy()，行为更明确

## 边界与易混淆

转换后列顺序仍按原列序，但一旦下游改动数组，原 DataFrame 的标签就对不上了。

## 关联

- [[DataFrame]] — 上位概念
- [[columns 属性]] — 对比项
- [[Numpy 二维数组]] — 上位概念

## 自测

df.values 之后还能知道第 2 列叫什么名字吗？::不能，标签信息已丢失，只能靠原列顺序推断

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p21 S02E06.数据结构之DataFrame](https://www.bilibili.com/video/BV1ji4y157uB?p=21) · 2026-11-17
