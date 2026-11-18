---
term: duplicated
aliases: [df.duplicated, 判断重复值, 重复标记]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 33
stage: "S02E18 · 删除重复和提取重复"
---

# duplicated

> 别名：df.duplicated、判断重复值、重复标记

**判断每行是否重复，返回布尔 Series 标记。**

## 用法
**语法**：`DataFrame.duplicated(subset=None, keep='first')`
**参数**：
- `subset`：用于判断重复的列，默认 `None` 表示按整行判断；也可以传单个列名字符串或列名列表
- `keep`：决定重复组中哪些行标记为 False，`'first'`（默认）表示保留第一次出现的行，`'last'` 表示保留最后一次出现的行，`False` 表示把所有重复行都标记为 True
**示例**：
```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["杨过", "小龙女", "杨过", "郭靖", "小龙女"],
    "分数": [80, 90, 85, 70, 95],
})

print(df.duplicated(subset="姓名").tolist())
# [False, False, True, False, True]

print(df.duplicated(subset="姓名", keep=False).tolist())
# [True, True, True, False, True]

print(df[df.duplicated(subset="姓名", keep=False)])
#    姓名  分数
# 0  杨过  80
# 1 小龙女  90
# 2  杨过  85
# 4 小龙女  95
```

## 解释

duplicated() 按指定列或整行判断重复，重复位置返回 True，否则 False。默认重复组中第一次出现不标记，后续出现标记为 True。它是提取重复行的前置步骤，配合布尔索引即可筛出重复数据。

## 有什么用

- 数据清洗前先定位重复行
- 配合布尔索引提取所有重复记录

## 关键要点

- 不指定 subset 时按整行判断是否完全重复
- subset 可传单列字符串或列名列表
- 默认 keep='first'，重复组首条不标记为 True
- 返回布尔 Series，可直接用于 df[布尔条件] 切片

## 边界与易混淆

duplicated 只做标记不删除数据；要得到去重后的表应使用 drop_duplicates。keep=False 时所有重复行都会被标记为 True。

## 关联

- [[drop_duplicates]] — 对比项
- [[布尔索引筛选]] — 组合使用

## 自测

df.duplicated(subset='姓名') 默认情况下，重复组中第一次出现的行返回什么？为什么？::返回 False，因为默认 keep='first'，只把重复组中后续出现的行标记为 True。
要提取所有在姓名列上重复的行（包括每组第一条），应该怎么写？::df[df.duplicated(subset='姓名', keep=False)]，keep=False 会把重复组所有行都标记为 True。


### 补充 · 2026-11-17

duplicated 不删除任何数据，只做判断：重复的位置为 True，首次出现或唯一的位置为 False。参数与 drop_duplicates 基本一致（subset、keep）。配合布尔索引即可把重复行单独提取出来。

- 不指定 subset 时按整行判断，姓名相同但其他列不同不算整行重复
- 指定 subset 后按该列判断，返回布尔 Series
- 单参数写 subset='姓名' 或直接传 ['姓名'] 效果相同
tt.duplicated('姓名') 返回的是什么？能直接看到重复的行吗？::返回布尔 Series，只标记哪些行是重复的；要看到行本身需再用 tt[dup] 做布尔索引提取
为什么 tt.duplicated() 不指定列时结果全是 False？::它按整行所有列判断，示例数据中没有任何两行完全相同，只是姓名相同不算整行重复
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p33 S02E18.删除重复和提取重复](https://www.bilibili.com/video/BV1ji4y157uB?p=33) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
