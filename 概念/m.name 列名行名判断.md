---
term: m.name 列名行名判断
aliases: [m.name, Series.name, 按名称选择性应用]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 26
stage: "S02E11 · 列与列之间的计算"
order: 26
---

# m.name 列名行名判断

> 别名：m.name、Series.name、按名称选择性应用

**在 apply 回调中用 Series 的 name 属性判断当前列名或行索引名，实现只对指定列/行运算。**

## 解释

DataFrame.apply 的回调参数 m 是一个 Series，m.name 在按列时是列名、按行时是行索引名。用 lambda m: np.sqrt(m) if m.name == 'x' else m 即可只对 x 列开方，其余原样返回；用 m.name in ['x','y'] 可对多列生效。

## 有什么用

- 只对指定列做变换
- 只对指定行做变换（配 axis=1）
- 多列/多行批量选择处理

## 关键要点

- 按列时 m.name 是列名，按行时是行索引名
- 条件不满足时返回 m 本身即保持原样
- 用 in 列表可一次选多列或多行
- 需与 axis 配合决定按行还是按列

## 边界与易混淆

依赖回调参数是 Series；若用其他方式遍历则无 m.name。

## 关联

- [[apply]] — 组合使用
- [[axis 参数]] — 前置知识
- [[lambda 表达式]] — 组合使用

## 自测

如何只对 x、y 两列开方而 z 列不变？::数据.apply(lambda m: np.sqrt(m) if m.name in ['x','y'] else m)。
按行 apply 时 m.name 代表什么？::代表当前行的行索引名称。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
