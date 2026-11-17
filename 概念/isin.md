---
term: isin
aliases: [Series.isin, df['列'].isin, 成员判断]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 42
stage: "S02E27 · 分组对象和创建"
---

# isin

> 别名：Series.isin、df['列'].isin、成员判断

**判断 Series 每个元素是否属于给定列表，返回布尔序列。**

## 用法
**语法**：`Series.isin(values)`
**参数**：
- `values`：候选值集合，可以是 list、tuple、set、Series，也可以传单个标量；只做精确的成员判断，不支持正则，模糊匹配用 `str.contains`

**示例**：
```python
import pandas as pd

df = pd.DataFrame({'班级': ['一班', '二班', '三班', '一班'],
                   '姓名': ['张三', '李四', '王五', '赵六']})

print(df['班级'].isin(['一班', '二班']))
# 0     True
# 1     True
# 2    False
# 3     True
# Name: 班级, dtype: bool

print(df[~df['班级'].isin(['一班', '二班'])])
#    班级  姓名
# 2  三班  王五

print(df.groupby(df['班级'].isin(['一班', '二班']))['姓名'].count())
# 班级
# False    1
# True     3
# Name: 姓名, dtype: int64
```

## 解释

isin 用于「某列的值是否在候选集合中」的筛选或分组。它替代了 Excel 中多条件 OR 筛选，写法简洁。取反用波浪号 ~ 加在表达式前。

## 有什么用

- 筛选指定几个类别
- 按是否属于指定集合分组
- 多值匹配替代多个 ==

## 关键要点

- df['班级'].isin(['一班','二班']) 返回 True/False 序列
- Pandas 没有 isnotin，取反用 ~df['班级'].isin([...])
- ~ 必须加在 isin 表达式前，不能加在 groupby 后面
- isin 可同时用于筛选和作为 groupby 分组键

## 边界与易混淆

只做成员判断，不支持正则或模糊匹配；模糊匹配用 str.contains。

## 关联

- [[布尔索引筛选]] — 组合使用
- [[布尔分组键]] — 组合使用
- [[str.contains]] — 对比项

## 自测

如何选出班级不属于一班、二班的所有行？::df[~df['班级'].isin(['一班','二班'])]。
isin 和 == 的区别是什么？::== 只能比单个值，isin 可一次比一个列表中的多个值。


### 补充 · 2026-11-17

isin 接受一个列表（或集合），逐元素比对，返回等长的 True / False。它既能用于筛选行，也能直接作为 groupby 的分组键，把数据分成“在集合内”和“不在集合内”两组。

- 取反写 ~df['列'].isin([...])，波浪号加在整个表达式前面。
- Pandas 没有 is not in 这种写法，不要照搬 Python 的 in / not in。
- 返回布尔 Series，既可做行筛选，也可做分组键。
要统计“不属于一班和二班”的人的成绩，isin 该怎么写？::~data['班级'].isin(['一班','二班'])，作为分组键或筛选条件。
为什么不能写 data['班级'] is not in ['一班','二班']？::Python 的 in 不能作用于 Series 逐元素判断，Pandas 里用 ~isin。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p42 S02E27.分组对象和创建](https://www.bilibili.com/video/BV1ji4y157uB?p=42) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
