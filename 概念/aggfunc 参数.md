---
term: aggfunc 参数
aliases: [aggfunc, 聚合函数参数]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 43
stage: "S02E28 · 数据透视表"
---

# aggfunc 参数

> 别名：aggfunc、聚合函数参数

**pivot_table 中指定聚合方式的参数，决定汇总值怎么算。**

## 解释

aggfunc 告诉 Pandas 对 values 列做求和、平均、计数还是其他运算。可传单个函数、函数列表（生成多种聚合结果），或字典（对不同值列分别指定聚合方式）。使用 NumPy 函数前必须先 import numpy。

## 有什么用

- 指定透视表的汇总口径
- 对不同指标列用不同聚合方式

## 关键要点

- 常用值：sum、mean、count、len
- 可传列表，一次生成多种聚合结果
- 可传字典，如 {'数量':'sum','金额':'mean'}
- len 只能用 Python 内置 len，np.len 会报错
- 其他 NumPy 聚合函数写 np.函数名，需先导入

## 边界与易混淆

len 是特例，不能写成 np.len；不确定时统一用 np.函数名但须先 import numpy。

## 关联

- [[pivot_table]] — 组合使用
- [[np.mean]] — 组合使用

## 自测

想让数量列求和、金额列求平均，aggfunc 怎么写？::aggfunc={'数量': 'sum', '金额': 'mean'}。
为什么 np.len 会报错？::NumPy 没有 len 函数，应使用 Python 内置的 len。


### 补充 · 2026-11-17

aggfunc 决定对 values 中的数值列做求和、平均还是计数。它可以接收函数列表，从而一次输出多种聚合结果。不要依赖默认聚合方式，业务分析中应显式设置。

- 可传列表，如 ['sum', np.mean]。
- Python 自带 sum 可直接写，也可写 np.sum。
- NumPy 的 mean 需先 import numpy as np 再写 np.mean。
在 aggfunc 中写 np.len 为什么不对？::len 是 Python 内置函数，不能加 np.，应直接写 len。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p43 S02E28.数据透视表](https://www.bilibili.com/video/BV1ji4y157uB?p=43) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
