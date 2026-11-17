---
term: pivot_table
aliases: [pd.pivot_table, 数据透视表]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 43
stage: "S02E28 · 数据透视表"
---

# pivot_table

> 别名：pd.pivot_table、数据透视表

**按行、列维度分组聚合并生成交叉表的 Pandas 函数。**

## 用法
**语法**：`pd.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True)`

**参数**：
- `data`：待透视的 DataFrame
- `values`：要聚合的数值列，建议显式指定，避免输出过多列
- `index`：行分组列名，可传列表形成多层行索引
- `columns`：列分组列名，展开为结果表的列；传变量时不要加引号
- `aggfunc`：聚合函数，默认是 `'mean'`，求和务必写 `'sum'`
- `fill_value`：替换结果中的缺失值，常写 `0`
- `margins`：是否追加行列小计/总计，小计方式跟随 `aggfunc`
- `dropna`：默认 `True`，为 `True` 时丢弃全空列

**示例**：
```python
import pandas as pd

df = pd.DataFrame({
    "店号": ["A", "A", "B", "B"],
    "年份": [2019, 2020, 2019, 2020],
    "销量": [10, 15, 20, 30],
})

pt = pd.pivot_table(df, values="销量", index="店号",
                    columns="年份", aggfunc="sum", fill_value=0)
print(pt)
# 年份   2019  2020
# 店号
# A        10    15
# B        20    30

pt["同比"] = pt[2020] / pt[2019] - 1
print(pt["同比"])
# 店号
# A    0.5
# B    0.5
# Name: 同比, dtype: float64
```

## 解释

pivot_table 用 index 指定行、columns 指定列、values 指定值、aggfunc 指定聚合方式，等价于 Excel 数据透视表。计算同比时用它把年份展开成列，再在列间做加减除。

## 有什么用

- 按店号和年份构造交叉表
- 多维度汇总与透视分析

## 关键要点

- index 行、columns 列、values 值、aggfunc 聚合
- 默认聚合可能是平均值，须显式 aggfunc="sum"
- columns 传变量时不要加引号，加引号会当字符串
- 结果可直接做列间运算算同比

## 边界与易混淆

columns 传变量名与传字符串含义不同，是最常见的报错来源。

## 关联

- [[同比]] — 组合使用
- [[groupby]] — 对比项

## 自测

pivot_table 不写 aggfunc 可能出什么问题？::默认可能按平均值聚合，得到的不是求和结果，同比就算错了。


### 补充 · 2026-11-17

pivot_table 是 Pandas 实现数据透视表的核心方法，思路与 Excel 数据透视表一致。它通过 index 指定行分组、columns 指定列分组、values 指定聚合列、aggfunc 指定聚合方式，把明细数据压缩成多维汇总表。多条件分组统计时应优先使用它。

- 四个核心参数：index、values、columns、aggfunc
- index 可传列名列表，形成多层行索引
- values 应显式指定，避免几十列全部显示
想让透视表行方向先按部门再按销售人员分组，index 应该怎么写？::index=['部门', '销售人员']，传列名列表形成多层行索引。
pivot_table 的 margins=True 得到的小计一定是求和吗？::不一定，小计方式跟随 aggfunc，用 mean 时小计就是平均。

它把分组、聚合和行列重排合成一步，适合多条件汇总。核心是 index 决定行分组，columns 决定列分组，values 选数值列，aggfunc 定聚合方式。相比 groupby，结果更接近 Excel 数据透视表。

- 四个核心参数：index、values、columns、aggfunc。
- 补充参数：fill_value 填缺失、dropna 删全空列、margins 加小计。
- values 选显示数值列；columns 在列方向加分组，二者易混。
pivot_table 中 values 和 columns 分别控制什么？::values 选结果中显示的数值列；columns 在列方向增加分组字段。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p43 S02E28.数据透视表](https://www.bilibili.com/video/BV1ji4y157uB?p=43) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
