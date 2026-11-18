---
term: str.get
aliases: [get, 取指定位置字符]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
---

# str.get

> 别名：get、取指定位置字符

**获取字符串中指定索引位置的单个字符的方法。**

## 用法
**语法**：`Series.str.get(i)`

**参数**：
- `i`：整型，要取出的字符索引位置，从 0 开始；负数表示从末尾倒数（如 -1 取末字符）；越界或原值为 NaN 时该位置返回 NaN

**示例**：
```python
import pandas as pd

s = pd.Series(['python', 'pandas', 'numpy'])
print(s.str.get(0).tolist())   # ['p', 'p', 'n']
print(s.str.get(-1).tolist())  # ['n', 's', 'y']
print(s.str.get(9).tolist())   # [nan, nan, nan]，越界返回 NaN，整列可能变 float64

# 取范围请改用 str.slice（旧版写法 s.str[1:3] 仍可用，但推荐 slice）
print(s.str.slice(1, 3).tolist())  # ['yt', 'an', 'um']
```

## 解释

str.get(i) 按索引取出每个字符串的第 i 个字符，索引从 0 开始。参数只能是整型；越界或原值为空时返回 NaN，并可能导致整列变成 float64。

## 有什么用

- 提取固定位置的字符，如首字母
- 从编码字符串中取某一位

## 关键要点

- 索引从 0 开始
- 参数只能传 int，不能传浮点
- 越界返回 NaN，整列可能变 float64
- 原列有空值时也可能导致 float64

## 边界与易混淆

只能取单个字符，不能取范围；取范围要用 str.slice。

## 关联

- [[str.slice]] — 对比项
- [[负索引]] — 前置知识
- [[Series.str 访问器]] — 上位概念

## 自测

str.get(2) 取的是第几个字符？::第 3 个字符，因为索引从 0 开始。
为什么 str.get 之后整列可能变成 float64？::因为越界或空值位置返回 NaN，整列被提升为浮点型。


### 补充 · 2026-11-17

常用于 split 之后只取某一段。参数必须是整数，位置越界不报错而是给出 NaN，因此结果列可能被整体提升为 float64。

- 参数必须是整数位置，不能传标签
- 越界返回 NaN，不会抛异常
- 全部越界时结果 dtype 可能变成 float64
对一列长度不一的字符串用 str.get(5) 会发生什么？::不足 6 位的返回 NaN，不报错
取单点用 get，取一段区间用什么？::str.slice
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p38 S02E23.字符串操作（上）](https://www.bilibili.com/video/BV1ji4y157uB?p=38) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
