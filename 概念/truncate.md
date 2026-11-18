---
term: truncate
aliases: [df.truncate, 截取日期区间]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 29
stage: "S02E14 · 筛选"
---

# truncate

> 别名：df.truncate、截取日期区间

**按索引边界截取 DataFrame 子集的函数，常用于日期区间筛选。**

## 用法

**语法**：`DataFrame.truncate(before=None, after=None, axis=None, copy=None)`

**参数**：
- `before`：截取下界，保留索引 ≥ before 的数据；不写则不限制下界
- `after`：截取上界，保留索引 ≤ after 的数据；不写则不限制上界
- `axis`：截取方向，默认 `None` 表示按行索引（0）；传 `'columns'`/1 表示按列标签截取
- `copy`：是否返回副本，pandas 2.x 已弃用该参数，不必传

**示例**：
```python
import pandas as pd

s = pd.Series([10, 20, 30, 40], index=pd.to_datetime(['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01']))
s = s.sort_index()                      # 使用前必须排序
df = s.to_frame('value')

print(df.truncate(before='2020-02-01'))  # 下界：2020-02 及之后
print(df.truncate(after='2020-03-01'))   # 上界：2020-03 及之前
print(df.truncate(before='2020-02-01', after='2020-03-01'))  # 区间：[2月, 3月]
```

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


### 补充 · 2026-11-17

常用于 DatetimeIndex 上按日期范围过滤。before 保留该日期及之后，after 保留该日期及之前。

- 使用前必须将日期设为索引并转换为 datetime
- 必须对索引排序，否则结果不可靠
- before 和 after 可单独使用
truncate(before='1980') 保留哪些数据？::保留 1980 年及之后的数据。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p29 S02E14.筛选](https://www.bilibili.com/video/BV1ji4y157uB?p=29) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
