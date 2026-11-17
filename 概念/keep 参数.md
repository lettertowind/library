---
term: keep 参数
aliases: [keep, 保留策略, keep='first', keep=False]
kind: concept
domain: 计算机/数据分析/Pandas
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 33
stage: "S02E18 · 删除重复和提取重复"
order: 33
---

# keep 参数

> 别名：keep、保留策略、keep='first'、keep=False

**控制重复值保留策略的参数：first、last 或 False。**

## 解释

keep 决定重复组中保留哪条记录。first 保留第一次出现（默认），last 保留最后一次出现，False 删除所有重复项只留从未重复的记录。drop_duplicates 和 duplicated 都支持该参数。

## 有什么用

- 按业务需要保留首条或末条记录
- 只保留从未重复过的干净记录

## 关键要点

- 默认 keep='first' 保留第一次出现
- keep='last' 保留最后一次出现
- keep=False 删除所有重复项
- False 是布尔值，不能写成字符串 'False'

## 边界与易混淆

keep=False 在 duplicated 中会把重复组所有行标记为 True，在 drop_duplicates 中则整组删除，两者语义一致但结果形式不同。

## 关联

- [[drop_duplicates]] — 组合使用
- [[duplicated]] — 组合使用

## 自测

keep=False 写成 keep='False' 会怎样？::错误，'False' 是字符串不是布尔值，参数不生效或报错，必须写不加引号的 False。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
