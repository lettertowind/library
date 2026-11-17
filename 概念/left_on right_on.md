---
term: left_on right_on
aliases: [left_on, right_on, 左右连接键参数]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 22
stage: "S02E07 · 连接查询之Merge"
---

# left_on right_on

> 别名：left_on、right_on、左右连接键参数

**merge 中分别指定左表、右表连接列的参数，用于两表键列名不同的情况。**

## 解释

当左表用「姓名」、右表用「用户名」这类不同列名做连接键时，用 left_on 和 right_on 分别指定，替代 on。

## 有什么用

- 两表连接键列名不一致时连接
- 与 right_index 配合实现列连索引

## 关键要点

- left_on 指定左表连接列，right_on 指定右表连接列
- 列名相同时用 on 更简洁
- left_on 可与 right_index=True 组合，实现列连索引

## 边界与易混淆

left_on/right_on 与 on 互斥，不要同时使用。

## 关联

- [[on 参数]] — 对比项
- [[DataFrame 合并]] — 上位概念

## 自测

左表键列叫「姓名」、右表叫「名字」，怎么连接？::pd.merge(a, b, left_on='姓名', right_on='名字')。


### 补充 · 2026-11-17

当两表的键列名不一致（如左表「姓名」、右表「name」）时，on 无法表达，需要用 left_on 和 right_on 分别写明。这也是 left_on 搭配 right_index 做索引连接时的固定写法。

- left_on 指定左表字段，right_on 指定右表字段，可同名可不同名
- 键名相同时直接用 on 更简洁
- 与 right_index=True 配合时只需写 left_on
左表字段叫「姓名」、右表叫「name」，该怎么连？::用 left_on='姓名', right_on='name'，然后用 how 指定连接方式。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p22 S02E07.连接查询之Merge](https://www.bilibili.com/video/BV1ji4y157uB?p=22) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
