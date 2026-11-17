---
term: describe()
aliases: [df.describe, 统计摘要, 描述性统计]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# describe()

> 别名：df.describe、统计摘要、描述性统计

**一次性输出数值列 count/mean/std/min/分位数/max 的统计摘要方法。**

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

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
