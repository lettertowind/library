---
term: right_index 参数
aliases: [right_index, right_index=True, 索引连接]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 22
stage: "S02E07 · 连接查询之Merge"
order: 22
---

# right_index 参数

> 别名：right_index、right_index=True、索引连接

**merge 中设为 True 时用右表索引作为连接键的参数，默认 False。**

## 解释

当右表已把姓名等设为索引时，不必先 reset_index 还原成列，直接 right_index=True 就能用左表的列去匹配右表索引。对大数据表尤其省事。

## 有什么用

- 右表以业务主键为索引时直接连接
- 避免对大表做索引还原操作

## 关键要点

- 默认 False，需手工设为 True
- 常与 left_on 搭配：左表列连右表索引
- 对称地有 left_index=True，用左表索引做键
- 连接方式仍由 how 控制，默认内连接

## 边界与易混淆

索引连接不要求键列同名；若两侧都用索引则同时设 left_index 和 right_index。

## 关联

- [[DataFrame 合并]] — 上位概念
- [[left_on right_on]] — 组合使用
- [[set_index]] — 前置知识

## 自测

右表已用姓名做索引，左表姓名在普通列，如何内连接？::pd.merge(left, right, left_on='姓名', right_index=True)。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
