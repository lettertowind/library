---
term: dt 访问器
aliases: [dt.month, dt.year, .dt]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 26
stage: "S02E11 · 列与列之间的计算"
---

# dt 访问器

> 别名：dt.month、dt.year、.dt

**从 datetime 列中提取年、月、日等时间成分的访问器。**

## 用法
**语法**：`Series.dt.<属性>`（要求该列 dtype 为 datetime64）

**参数**：
- `dt.year` / `dt.month` / `dt.day`：提取年、月、日，返回整数列
- `dt.hour` / `dt.minute`：提取时、分
- `dt.date`：返回 `datetime.date` 对象，适合按天分组
- `dt.dayofweek`：星期几，0=周一

**示例**：
```python
import pandas as pd
df = pd.DataFrame({'时间': ['2026-11-17 09:30', '2026-11-17 14:05', '2026-11-18 09:10'],
                   '金额': [100, 200, 150]})
# 字符串列直接 .dt 会报错，先转 datetime
df['时间'] = pd.to_datetime(df['时间'])
df['月'] = df['时间'].dt.month
df['时'] = df['时间'].dt.hour
print(df.groupby([df['时间'].dt.date, df['时间'].dt.hour])['金额'].sum())
# 时间          金额
# 2026-11-17 9   100
#            14  200
# 2026-11-18 9   150
```

## 解释

对日期列用 .dt.month 取月份、.dt.year 取年份，是环比按月聚合、同比按年透视的前置步骤。前提是该列必须是 datetime 类型。

## 有什么用

- 从日期提取月份做月度聚合
- 从日期提取年份做同比透视

## 关键要点

- 列必须是 datetime 类型才能用 .dt
- dt.month 取月、dt.year 取年
- 常与 groupby、pivot_table 配合
- 字符串日期需先 pd.to_datetime 转换

## 边界与易混淆

对非日期列使用 .dt 会报错，需先转换类型。

## 关联

- [[pivot_table]] — 前置知识
- [[groupby]] — 组合使用

## 自测

对字符串格式的日期列直接用 .dt.month 会怎样？::会报错，需先用 pd.to_datetime 转成 datetime 类型。


### 补充 · 2026-11-17

时间列转成 datetime 后，用 .dt 可提取 year、month、hour 等分量，直接作为分组键或筛选条件。它把 Excel 中「分列再统计」的流程压缩成一行。

- df['时间'].dt.year / .month / .hour 提取时间分量
- 多个分量放进列表即可多键分组
- 使用前时间列必须是 datetime 类型，否则先 pd.to_datetime
统计每天各小时的订单量，分组键怎么写？::df.groupby([df['时间'].dt.date, df['时间'].dt.hour])。
对字符串时间列直接用 .dt 会怎样？::报错，需先用 pd.to_datetime 转成 datetime 类型。

对 datetime 类型的 Series 使用 .dt 后，可像对象属性一样取出 year、month、hour 等分量，返回普通数值 Series。这些分量既能用于筛选，也能直接作为 groupby 的分组键，从而把“某年某时段的统计”压缩成一行代码。

- 前提是列已经是 datetime 类型，否则 .dt 会报错，需先 to_datetime。
- 常用属性：dt.year、dt.month、dt.hour，还有 dt.day、dt.minute。
- 多个时间维度用列表组合成多键分组。
想按“年 + 小时”统计销售，分组键怎么写？::groupby([df['时间'].dt.year, df['时间'].dt.hour])。
时间列是字符串时能直接用 .dt 吗？::不能，需要先 pd.to_datetime 转换类型。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p42 S02E27.分组对象和创建](https://www.bilibili.com/video/BV1ji4y157uB?p=42) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
