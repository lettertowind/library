---
term: datetime.date
aliases: [date 类, 日期对象, 日期模块.date]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# datetime.date

> 别名：date 类、日期对象、日期模块.date

**datetime 模块中只表示“年-月-日”的日期类。**

## 解释

用 date(年, 月, 日) 构造一个日期对象，通过 .year/.month/.day 取出单独的年月日；与 timedelta 相加得到偏移后的新日期。它是按天、按年、按月生成日期序列时的构造基础。

## 有什么用

- 建立起始日期，再循环生成日期序列
- 按年填充时用 date(d.year+i, d.month, d.day) 重建日期

## 关键要点

- 构造顺序固定为年、月、日，三个参数都必填
- .year/.month/.day 是只读属性，用于拆出单段
- date 与 timedelta 相加返回新对象，原日期不变
- 只精确到天，需要时分秒时改用 datetime.datetime

## 边界与易混淆

它与 Pandas 的 Timestamp 不是一回事：date 是标准库对象，不带时间与时区。

## 关联

- [[datetime 模块]] — 上位概念
- [[Timedelta]] — 组合使用
- [[Timestamp]] — 对比项

## 自测

要让起始日期在年份上依次 +1、月日不变，怎么构造？::date(d.year + i, d.month, d.day)
date 对象能直接取出小时吗？::不能，date 只到天，小时在 datetime 对象里

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p25 S02E10.各种数据自动填充](https://www.bilibili.com/video/BV1ji4y157uB?p=25) · 2026-11-17
