---
term: axis=1 按列分组
aliases: [axis=1, 列方向分组, 按列聚合]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 41
stage: "S02E26 · 分组与聚合 groupby基础部分"
---

# axis=1 按列分组

> 别名：axis=1、列方向分组、按列聚合

**groupby 中 axis=1 表示沿列方向分组，把多个月份列合并成季度等汇总列。**

## 用法
**语法**：旧版 `df.groupby(by, axis=1).sum()`；pandas 2.x 推荐写成 `df.T.groupby(by).sum().T`
**参数**：
- `by`：分组依据，常用「列名 → 组名」的映射字典，也可传与列等长的列表
- `axis`：旧版取 `1` 表示按列名分组（横向归并）；该参数在 pandas 2.0 已移除，在新版本中传 `axis=1` 会触发 `TypeError`/`FutureWarning`，因此需要先转置再分组
**示例**：
```python
import pandas as pd

df = pd.DataFrame({'1月': [1, 2], '2月': [3, 4], '3月': [5, 6]}, index=['A', 'B'])
q = {'1月': '一季度', '2月': '一季度', '3月': '二季度'}

# 旧版写法：df.groupby(q, axis=1).sum()  ← pandas 2.x 已移除
print(df.T.groupby(q).sum().T)
#        一季度  二季度
# A         4      5
# B         6      6
```

## 解释

默认 groupby 按行分组，axis=1 则把每一列当作分组对象，配合字典映射可把 1、2、3 月横向合并成一季度。这是 Pandas 做季度/类别横向汇总的简洁手段，比 Power BI 建时间表和度量值轻量得多。

## 有什么用

- 月份列汇总成季度列
- 多列按类别横向合并
- 宽表结构的列方向归并

## 关键要点

- 写法：df.groupby(季度映射, axis=1).sum()
- 字典把多个列名映射到同一个目标组名
- 聚合后原月份列被合并为季度列
- 可提前准备月份→季度、地区标准化等常用映射字典

## 边界与易混淆

axis=1 只对列名做分组，不改变行；若列名与映射字典键不匹配，未映射列会被丢弃或报错。

## 关联

- [[groupby]] — 组合使用
- [[axis 参数]] — 前置知识
- [[分层索引]] — 对比项

## 自测

df.groupby({'1月':'一季度','2月':'一季度'}, axis=1).sum() 的结果列是什么？::只剩「一季度」一列，值为 1 月与 2 月之和。
axis=1 分组和按行 groupby 的本质区别是什么？::前者把列当作分组单位横向合并，后者把行按值分组纵向聚合。


### 补充 · 2026-11-17

默认 groupby 沿行方向按列值分组；axis=1 则把每一列当作一条待分组记录，常用于“列名到分组的映射”场景，如把各月份列归入对应季度。

- 写法：数据.groupby(对应关系, axis=1).sum()，对应关系是列到分组的映射
- 行方向分组是默认值 axis=0，不要混淆
- 配合 level 使用：数据.groupby(level="季度", axis=1).sum()
要把“1月、2月、3月”三列合并成“一季度”，该用 axis=0 还是 axis=1？::axis=1，因为被合并的对象是列，需要传入列到分组的映射。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p41 S02E26.分组与聚合 groupby基础部分](https://www.bilibili.com/video/BV1ji4y157uB?p=41) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
