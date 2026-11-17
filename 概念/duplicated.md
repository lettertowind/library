---
term: duplicated
aliases: [df.duplicated, 判断重复值, 重复标记]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 33
stage: "S02E18 · 删除重复和提取重复"
order: 33
---

# duplicated

> 别名：df.duplicated、判断重复值、重复标记

**判断每行是否重复，返回布尔 Series 标记。**

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

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
