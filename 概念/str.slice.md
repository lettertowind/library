---
term: str.slice
aliases: [slice, 字符串切片]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
---

# str.slice

> 别名：slice、字符串切片

**按起止范围和步长截取字符串片段的方法。**

## 用法
**语法**：`Series.str.slice(start=None, stop=None, step=None)`

**参数**：
- `start`：切片起始位置（含）；默认 `None` 表示从开头（或配合负 `step` 从末尾）算起
- `stop`：切片结束位置（**不含**）；默认 `None` 表示取到末尾
- `step`：步长，默认为 1；负值表示反向取字符

**示例**：
```python
import pandas as pd

s = pd.Series(["2020A01", "2021B02", None])
print(s.str.slice(0, 4).tolist())   # ['2020', '2021', None]  截前 4 位
print(s.str.slice(4, 5).tolist())   # ['A', 'B', None]       取第 5 个字符
print(s.str.slice(None, None, 2).tolist())  # ['20A1', '21B2', None] 隔位取
print(s.str.slice(0, 99).tolist())  # ['2020A01', '2021B02', None] 越界取全部，NaN 仍为 None
```
提示：`str.slice` 只截取不替换，需替换片段用 `str.slice_replace`；等价写法 `s.str[0:4]`，但 `str.slice` 可读性更好，且不会与取列操作混淆。

## 解释

str.slice(start, stop, step) 类似 Python 切片，从 start 到 stop（不含 stop）截取字符，可设置步长。越界位置显示为空字符，原值为 NaN 的仍为空值。

## 有什么用

- 截取字符串前几位
- 隔位取字符
- 按固定位置提取编码片段

## 关键要点

- stop 位置不包含在结果中
- 支持 step 步长
- 越界显示空字符，不是 NaN
- 空字符与空值要区分

## 边界与易混淆

不支持替换；需要替换切片范围时用 str.slice_replace。

## 关联

- [[str.slice_replace]] — 对比项
- [[str.get]] — 对比项
- [[Numpy 切片]] — 前置知识

## 自测

str.slice(0, 3) 取的是哪几个索引？::索引 0、1、2，共三个字符，不包含 3。
切片越界时结果是什么？::越界位置显示为空字符，原值为 NaN 的仍为空值。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
