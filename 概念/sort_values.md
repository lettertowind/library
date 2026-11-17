---
term: sort_values
aliases: [sort_values(), 按值排序]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 27
stage: "S02E12 · 数据排序【已修证】"
---

# sort_values

> 别名：sort_values()、按值排序

**按数据值对 Series 或 DataFrame 进行排序的方法。**

## 用法
**语法**：`DataFrame.sort_values(by, ascending=True, inplace=False)`；`Series.sort_values(ascending=True, inplace=False)`

**参数**：
- `by`：DataFrame 用于指定排序键，单个字段传字符串，多字段传列表（列表顺序即优先级）；Series 没有此参数
- `ascending`：默认 `True` 表示升序，`False` 表示降序；多个排序字段时传入与 `by` 等长的布尔值列表
- `inplace`：默认 `False`，返回新的对象；`True` 时直接修改原对象并返回 `None`

**示例**：
```python
import pandas as pd

df = pd.DataFrame({'姓名': ['张三', '李四', '王五'],
                   '语文': [85, 92, 85],
                   '数学': [90, 78, 88]})

print(df.sort_values(by='语文'))
#    姓名  语文  数学
# 0  张三  85  90
# 2  王五  85  88
# 1  李四  92  78

print(df.sort_values(by=['语文', '数学'], ascending=[False, True]))
#    姓名  语文  数学
# 1  李四  92  78
# 2  王五  85  88
# 0  张三  85  90
```

## 解释

sort_values() 用于将数据按照值的大小或顺序排列。在 DataFrame 中通常配合 by 参数指定按哪一列排序，例如 df.sort_values(by='入职日期')。功能类似 Excel 的排序。

## 有什么用

- 按某列的值排序
- 对日期、数值等排序

## 关键要点

- 按数据值排序
- DataFrame 中用 by= 指定排序列
- 与 Excel 的排序功能类似

## 边界与易混淆

按索引排序需用 sort_index()；多列排序可传列表给 by。

## 关联

- [[Series]] — 组合使用
- [[DataFrame]] — 组合使用
- [[sort_index]] — 对比项

## 自测

在 DataFrame 中按“入职日期”列排序应该怎么写？::df.sort_values(by='入职日期')


### 补充 · 2026-11-17

sort_values 是 Pandas 最常用的排序方法，默认按列值对行排序。通过 by 指定排序键，ascending 控制方向，inplace 控制是否改原表。

- by 单字段写字符串，多字段写列表，列表顺序即优先级
- ascending 默认 True 升序，False 为降序
- 多字段时 ascending 也写列表，与 by 一一对应
按语文降序、数学升序排序，by 和 ascending 怎么写？::by=['语文','数学'], ascending=[False, True]
多字段排序后数学列看起来不是全局升序，为什么？::数学只在前一字段语文相同的分组内排序，不保证整列独立有序

sort_values() 关心的是数据内容而不是行号，参数写排序依据的列名即可。例如按「入职日期」排序后，日期会从 1 月 1 日到 1 月 7 日依次排列，而索引保持跟着原行走。

- 参数写列名：数据.sort_values("入职日期")
- 方法后面必须带括号，不带括号不会执行
- 默认升序，方向由 ascending 控制
想按「入职日期」从早到晚排列表格用哪个方法？::sort_values("入职日期")，默认升序。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p20 S02E05.数据结构之Series](https://www.bilibili.com/video/BV1ji4y157uB?p=20) · 2026-11-17

画条形图或柱形图前常用它排序，让条形按分数从高到低排列，图形更易读。用 by 指定排序列，用 ascending 指定升降序，用 inplace 决定是否直接修改原表。

- by 指定排序列名，多列排序传入列名列表
- ascending=False 为降序，默认 True 为升序
- inplace=True 原地修改并返回 None，否则返回新表
执行 df.sort_values('分数', ascending=False) 之后，df 本身变了吗？::没变，返回的是排序后的新表；要改原表需 inplace=True 或把结果重新赋值给 df。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p49 S03E02.条形图](https://www.bilibili.com/video/BV1ji4y157uB?p=49) · 2026-11-17

sort_values 是 Pandas 最常用的排序方法，按「值」而非「索引」排序，用 by 指定排序依据，ascending 控制方向，inplace 控制是否修改原对象。它既能做单字段排序，也能通过 by 传列表做多字段优先级排序，还能配合 axis=1 做横向排序。

- 单字段：by='语文'；多字段：by=['语文','数学']，优先级从左到右
- ascending=False 降序、True 升序，多字段时可传列表逐列控制
- inplace=True 直接改原数据，False 返回新对象
sort_values 和 sort_index 的核心区别一句话说清？::前者按数据值排序，后者按索引排序。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p27 S02E12.数据排序【已修证】](https://www.bilibili.com/video/BV1ji4y157uB?p=27) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
