---
term: Timestamp
aliases: [pd.Timestamp, 时间戳类型, Pandas 时间戳]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
---

# Timestamp

> 别名：pd.Timestamp、时间戳类型、Pandas 时间戳

**Pandas 中表示单个时间点的数据类型，是 datetime 的子类。**

## 解释

读取 Excel/CSV 时日期列会被自动解析成时间类型：单个值即 Timestamp 对象，整列则是 datetime64[ns]。它自带 strftime、year、month 等方法，是日期格式化和取值的操作对象。

## 有什么用

- 判断日期列读进来后到底是什么类型
- 对单个时间点取年月日或转成字符串

## 关键要点

- 单个时间点用 Timestamp，整列存储为 datetime64[ns]
- 从日期列取出的元素默认仍是 Timestamp，不是字符串
- 支持 strftime 方法与 .dt 访问器系列属性
- 若列被读成字符串，需先用 pd.to_datetime 转换

## 边界与易混淆

与标准库 datetime.datetime 兼容但不等同；与 Timedelta（时间差/间隔）容易混淆，后者表示一段时长而非某个时间点。

## 关联

- [[strftime 日期格式化]] — 组合使用
- [[datetime 模块]] — 对比项
- [[Timedelta]] — 对比项
- [[dt 访问器]] — 组合使用

## 自测

对 data['日期'] 用列表推导式取出的元素，类型是什么？能直接切片当「12月」用吗？::是 Timestamp 对象而非字符串，不能直接按字符切片，需先 strftime 或取 .month 再拼接。
Timestamp 和 Timedelta 的区别是什么？::Timestamp 表示某个具体时间点；Timedelta 表示两个时间点之间的时长，如 3 days。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p63 S03E14.坐标轴上面的日期格式](https://www.bilibili.com/video/BV1ji4y157uB?p=63) · 2026-11-17
