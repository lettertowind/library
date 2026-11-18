---
term: Timedelta
aliases: [时间差类型, 时间间隔类型, days]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 26
stage: "S02E11 · 列与列之间的计算"
---

# Timedelta

> 别名：时间差类型、时间间隔类型、days

**pandas 中表示两个时间点之差的类型，可直接取 .days 得整数天数。**

## 解释

两个日期列相减得到 Timedelta 对象，显示形如 7 days、190 days。它不是普通字符串，而是专门的时间差类型，可通过 .days 属性提取整数天数，便于后续计算。

## 有什么用

- 计算保质期、账龄、间隔天数
- 日期列相减后转整数

## 关键要点

- 日期列相减自动得到 Timedelta
- 用 .days 取整数天数
- 是否含当天需业务决定，含当天则 +1
- 可直接用 apply(lambda x: x.days) 转换

## 边界与易混淆

Timedelta 与 datetime 不同：前者是差值，后者是时间点；.days 只取整天数，忽略时分秒。

## 关联

- [[pd.to_datetime]] — 前置知识
- [[apply]] — 组合使用

## 自测

结束日期减起始日期得到什么类型？怎么变成整数天数？::得到 Timedelta，用 .days 属性取整数天数。
保质期计算中“当天算不算”由谁决定？::由业务逻辑决定，含当天就在结果上加 1，不是 pandas 固定规则。


### 补充 · 2026-11-17

timedelta 用来做日期加减，例如起始日期 + timedelta(days=i) 得到第 i 天。它把“间隔”封装成可运算对象，避免手工拆分年月日。

- 支持 days、seconds、microseconds、milliseconds、minutes、hours、weeks
- 不支持 months 和 years 参数
- 日期 + timedelta 得到新日期
timedelta(days=30) 和“加一个月”在 2 月场景下结果一样吗？::不一样，30 天是固定长度，加一个月要按日历月份算，2 月只有 28/29 天。

timedelta(days=i) 生成 i 天的时间差，加到 date 上就得到“起始日期 + i 天”，是按天填充日期最直接的工具。支持 days、seconds、microseconds、milliseconds、minutes、hours、weeks 等单位。

- 常用参数：days、seconds、microseconds、milliseconds、minutes、hours、weeks
- 没有 months、years 参数，月/年必须自己写算法
- date + timedelta 返回新日期，原对象不被修改
想加 3 个月能用 timedelta(months=3) 吗？::不能，timedelta 没有 months 参数，要自己写累加月算法
起始日期 2020-05-26 加 timedelta(days=2) 得到什么？::2020-05-28
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p25 S02E10.各种数据自动填充](https://www.bilibili.com/video/BV1ji4y157uB?p=25) · 2026-11-17

Timedelta 是日期运算的产物，类似 Python 的 datetime.timedelta。它的显示形式如 7 days，其中的 days 是类型标识，不能直接当作整数参与算术或统计，需取 .days 属性。

- 两个日期列/时间戳相减的结果类型，显示为 7 days
- 显示的 days 表示类型特征，并非单位，不能当整数直接用
- 用 .days 属性或 apply(lambda x: x.days) 取出整数天数
为什么 Timedelta 打印成 7 days 却不能直接乘单价？::它是时间差对象而不是数值，必须先取 .days 得到整数。
Timedelta 和 Timestamp 的区别是什么？::Timestamp 是某一时间点，Timedelta 是两个时间点之间的间隔。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p26 S02E11.列与列之间的计算](https://www.bilibili.com/video/BV1ji4y157uB?p=26) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
