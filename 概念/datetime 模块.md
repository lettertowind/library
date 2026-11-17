---
term: datetime 模块
aliases: [datetime, Python 日期时间模块]
kind: tool
domain: 数据分析/Python
tags: [概念/tool, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
stage: "S02E10 · 各种数据自动填充"
order: 25
---

# datetime 模块

> 别名：datetime、Python 日期时间模块

**Python 标准库中处理日期与时间间隔的模块，提供 date、timedelta 等类。**

## 解释

datetime 模块接口比 time 模块更直观，是 Python 中做日期运算的主力。自动填充日期时主要用它的 date 类表示具体日期、timedelta 类表示时间间隔。

## 有什么用

- 构造起始日期
- 日期加减天数/周数
- 计算两个日期的间隔

## 关键要点

- date 类有 year、month、day 属性
- timedelta 表示时间间隔，可精确到微秒
- timedelta 没有月和年参数，加月加年要自己算
- 常用导入写法 import datetime as 别名

## 边界与易混淆

time 模块偏底层、部分方法平台相关；日期业务运算优先用 datetime。

## 关联

- [[Timedelta]] — 下位概念
- [[累加月算法]] — 组合使用

## 自测

为什么日期自动填充不能直接用 timedelta 加一个月？::timedelta 只支持天、秒、周等固定长度单位，没有“月”参数，月份长度不固定需自行算法。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
