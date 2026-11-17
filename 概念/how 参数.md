---
term: how 参数
aliases: [how, 连接类型参数, how='left', how='outer']
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 22
stage: "S02E07 · 连接查询之Merge"
---

# how 参数

> 别名：how、连接类型参数、how='left'、how='outer'

**merge 中指定连接类型的参数，取 inner/left/right/outer。**

## 解释

how 决定合并时保留哪些记录：inner 取交集，left/right 以一侧为基准，outer 取并集。它是控制合并结果范围的关键开关。

## 有什么用

- 控制合并后保留的记录范围
- 实现类似 VLOOKUP 的补字段

## 关键要点

- inner：交集，默认值，可省略不写
- left：以左表为基准，右表匹配不到补空值
- right：以右表为基准，与 left 对称
- outer：并集，保留两侧全部记录，缺失处为 NaN
- outer 可理解为左连接与右连接结果的组合

## 边界与易混淆

left/right 对表顺序敏感；outer 结果范围与顺序无关，但列顺序仍受左右表位置影响。

## 关联

- [[DataFrame 合并]] — 上位概念
- [[on 参数]] — 组合使用

## 自测

想给主表补充维度字段、且主表记录一条不能少，应选哪种 how？::how='left'，以主表为左表做左连接。
outer 连接后某行右表字段为 NaN，说明什么？::该行连接键在右表中没有匹配记录。


### 补充 · 2026-11-17

how 决定哪些行被保留：inner 取交集，left 以左表为准，right 以右表为准，outer 取并集。默认 inner，其他三种必须显式写出。

- inner：两表都能匹配的行，默认值可省略
- left：左表全保留，右表无匹配处为 NaN
- right：右表全保留，左表无匹配处为 NaN
想保留右表全部记录并带出左表信息，how 应设为什么？::how='right'。

how 决定结果保留哪一侧的记录：inner 取交集、left 保左表、right 保右表、outer 取并集，缺失处统一补 NaN。它是关键语义开关，一旦不是内连接就必须写明，不能依赖默认。

- 默认值为 inner，等价于不写
- 取值 left/right/outer 时必须显式写出
- 连接类型只影响保留哪些行，不影响匹配规则本身
为什么 how='left' 时行数可能比左表还多？::因为保留的是左表行的匹配结果：左表某键在右表匹配到多行时，该行会被展开成多行。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p22 S02E07.连接查询之Merge](https://www.bilibili.com/video/BV1ji4y157uB?p=22) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
