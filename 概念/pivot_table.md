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
order: 43
---

# pivot_table

> 别名：pd.pivot_table、数据透视表

**按行、列维度分组聚合并生成交叉表的 Pandas 函数。**

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

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
