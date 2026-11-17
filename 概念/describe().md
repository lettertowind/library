---
term: describe()
aliases: [df.describe, 统计摘要, 描述性统计]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 32
stage: "S02E17 · 数学统计函数"
---

# describe()

> 别名：df.describe、统计摘要、描述性统计

**一次性输出数值列 count/mean/std/min/分位数/max 的统计摘要方法。**

## 用法
**语法**：`DataFrame.describe(percentiles=None, include=None, exclude=None)`
**参数**：
- `percentiles`：指定要输出的分位数，传入 0~1 之间的列表，默认 `[.25, .5, .75]`
- `include`：指定要统计的列类型，`'all'` 表示包含非数值列，也可写 `'number'`、`'object'`
- `exclude`：排除某类列，与 `include` 配合使用，如 `exclude='object'`
**示例**：
```python
import pandas as pd

df = pd.DataFrame({'姓名': ['张三', '李四', '王五', '赵六'],
                   '语文': [88, 92, 76, 95],
                   '数学': [90, 85, 79, 98]})

print(df.describe())
#             语文        数学
# count   4.000000   4.000000
# mean   87.750000  88.000000
# std     8.539126   8.286535
# min    76.000000  79.000000
# 25%    82.000000  83.500000
# 50%    90.000000  88.500000
# 75%    93.500000  93.500000
# max    95.000000  98.000000

print(df['语文'].describe()['50%'])  # 90.0，即中位数
print(df.describe(include='all').columns.tolist())  # ['姓名', '语文', '数学']
```

## 解释

describe() 是 Pandas 中最常用的快速概览工具，对 DataFrame 调用时自动跳过非数值列，只对数值列计算统计量。它把多个常用统计指标打包成一张表，省去逐列逐函数调用的麻烦。

## 有什么用

- 拿到新数据集先做整体数值分布概览
- 快速判断某列是否存在异常值或缺失

## 关键要点

- 只统计数值列，姓名等非数值列自动忽略
- 返回 count、mean、std、min、25%/50%/75% 分位数、max
- 50% 分位数即中位数
- 可先选列再调用，如 df['语文'].describe()
- 多列用 df[['语文','数学']].describe() 控制范围

## 边界与易混淆

不统计非数值列；需要分类列统计时应改用 value_counts 或 include='all' 参数。

## 关联

- [[DataFrame]] — 上位概念
- [[Series]] — 组合使用
- [[分位数]] — 组合使用
- [[标准差]] — 组合使用

## 自测

一个含姓名、性别、语文成绩的 DataFrame 调用 describe()，结果里会出现姓名列吗？为什么？::不会。describe() 默认只对数值列计算统计量，姓名是字符串列会被跳过。
describe() 结果中的 50% 那一行对应哪个统计量？::中位数（median）。


### 补充 · 2026-11-17

对 DataFrame 或选定的列调用 describe()，会返回一张汇总表：count、mean、std、min、25%、50%、75%、max。它解决的是「拿到一份数据先快速摸清家底」的问题，不用逐个调用 mean()、std()。计算时自动跳过姓名、性别等非数值列，只对数值列生效。

- 只统计数值列，字符类列被自动忽略
- 默认输出 8 个统计量：count/mean/std/min/25%/50%/75%/max
- df[['语文','数学']].describe() 可把统计范围限定到指定列
一张含姓名、性别、语文、数学、英语的成绩表调用 df.describe()，结果里会出现哪几列的统计？::只有语文、数学、英语等数值列，姓名和性别被自动跳过。
同事只关心语文成绩的中位数，为什么直接看 describe() 的 50% 那行是对的？::50% 分位数的定义就是中位数，与 median() 结果一致。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p32 S02E17.数学统计函数](https://www.bilibili.com/video/BV1ji4y157uB?p=32) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
