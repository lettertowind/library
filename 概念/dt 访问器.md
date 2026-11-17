---
term: dt 访问器
aliases: [dt.month, dt.year, .dt]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 26
stage: "S02E11 · 列与列之间的计算"
order: 26
---

# dt 访问器

> 别名：dt.month、dt.year、.dt

**从 datetime 列中提取年、月、日等时间成分的访问器。**

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

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
