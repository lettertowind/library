---
term: truncate
aliases: [df.truncate, 截取日期区间]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# truncate

> 别名：df.truncate、截取日期区间

**按索引边界截取 DataFrame 子集的函数，常用于日期区间筛选。**

## 解释

truncate 通过 before 和 after 参数指定截取边界，返回边界之前或之后（或之间）的数据。用于日期筛选时要求索引已转为日期格式并排序。

## 有什么用

- 查询某日期之后的数据
- 查询某日期之前的数据
- 截取两个日期之间的区间

## 关键要点

- before 指定下界，after 指定上界
- 使用前日期索引必须已排序
- 参数按需使用，不必同时写 before 和 after
- copy 等参数暂不需重点掌握

## 边界与易混淆

索引未排序时 truncate 不能正常工作；非日期索引也可用但主要用于日期区间。

## 关联

- [[sort_index]] — 前置知识
- [[日期范围查询]] — 组合使用
- [[set_index]] — 前置知识

## 自测

truncate(before='1980') 返回的是什么数据？::返回索引在 1980 及之后的数据（下界为 1980）。
truncate 使用前为什么必须先排序索引？::truncate 依赖索引有序才能正确判断边界，未排序时函数不能正常工作。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
