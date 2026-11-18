---
term: groupby
aliases: [分组, DataFrame.groupby, 分组聚合]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 41
stage: "S02E26 · 分组与聚合 groupby基础部分"
---

# groupby

> 别名：分组、DataFrame.groupby、分组聚合

**按指定键把数据拆成若干组，再对每组分别计算并合并结果。**


## 用法
**语法**：`df.groupby(by=None, level=None, as_index=True, sort=True, dropna=True)`
**参数**：
- `by`：分组键，可以是列名字符串、列名列表（多键）、Series、字典或函数
- `level`：按索引层级名称或位置分组，与 `by` 二选一
- `as_index`：默认 True，分组键作为结果的行索引；设 False 则还原成普通列
- `sort`：默认 True，对分组键排序；设 False 可保留原出现顺序、略快
- `dropna`：默认 True，分组键为 NaN 的行整组丢弃
**示例**：
```python
import pandas as pd

df = pd.DataFrame({"城市": ["北京", "上海", "北京", "上海"], "人数": [10, 20, 30, 40]})
print(df.groupby("城市")[["人数"]].sum())
#       人数
# 城市
# 北京    40
# 上海    60

print(df.groupby("城市", as_index=False)["人数"].sum())
#    城市  人数
# 0  北京   40
# 1  上海   60
# 旧版 df.groupby(level="季度", axis=1).sum() 在 pandas 2.x 已废弃，改用 df.T.groupby(level="季度").sum().T
```

## 解释

groupby 是 Pandas 的核心分组机制，思想是「拆分—应用—合并」：先按一列或多列（或索引层级、函数、字典）把行分组，再对每组应用聚合函数，最后把各组结果拼回一张表。它对应 SQL 的 GROUP BY 和 Excel 的 SUMIF，但聚合方式远不止求和。

## 有什么用

- 按维度汇总数据，如按城市/区域统计人数与金额
- 为后续 agg、transform、apply 提供分组对象
- 替代手工 for 循环逐组计算

## 关键要点

- 语法：df.groupby(按谁分组)[对谁聚合].聚合函数()
- 单个分组键写字符串，多个分组键写列表
- 建议统一写成列表套列表 [["人数"]]，避免格式出错
- 只做一种聚合可直接接 .sum()；多种聚合先保存分组对象复用
- Pandas 中应尽量避免 for 循环遍历分组

## 边界与易混淆

groupby 本身只完成分组，不计算；必须接聚合函数或 agg 才有结果。按索引层级分组需先用 set_index 提升层级。

## 关联

- [[agg]] — 组合使用
- [[set_index]] — 前置知识
- [[分层索引]] — 组合使用
- [[pivot_table]] — 对比项

## 自测

groupby 之后不加聚合函数，得到的是什么？::一个 DataFrameGroupBy 分组对象，尚未产生计算结果。
为什么建议把聚合列写成 [["人数"]] 而不是 ["人数"]？::列表套列表保证结果仍是 DataFrame，分组键增多时也不易写错格式。


### 补充 · 2026-11-17

groupby 是“拆分—应用—合并”的入口：先按分组键切分，再对选定的列执行 sum/mean/count 等聚合。分组键可以是列名、Series、布尔条件或其列表，这让它几乎能表达任何分组口径。

- 固定结构：data.groupby(分组键)聚合列.聚合函数()。
- 选择聚合列必须用双层列表 [[列1, 列2]]。
- 口诀：一定要明确“按谁分组、按谁聚合”。
data.groupby('班级')[['语文','数学']].sum() 里两层方括号各起什么作用？::内层列表选聚合列，外层是索引语法，取出这些列做聚合。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p42 S02E27.分组对象和创建](https://www.bilibili.com/video/BV1ji4y157uB?p=42) · 2026-11-17

groupby 按一个或多个键把行归组，再对每组应用 sum、mean、median 等聚合函数。它是拆分-应用-合并模式在 Pandas 中的实现。

- 基本语法：df.groupby(键)[聚合列].聚合函数()
- 分组键可为列名、列表、函数、字典或 level
- 分组对象可保存复用：grouped = df.groupby('电号')，再 grouped.sum()
如果同一分组要反复求 sum、mean、median，怎样写更合理？::先保存 grouped = df.groupby(...)，再分别调用 grouped.sum()、grouped.mean() 等，避免重复分组。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p41 S02E26.分组与聚合 groupby基础部分](https://www.bilibili.com/video/BV1ji4y157uB?p=41) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
