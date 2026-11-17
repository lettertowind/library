---
term: keep 参数
aliases: [keep, 保留策略, keep='first', keep=False]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 33
stage: "S02E18 · 删除重复和提取重复"
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


### 补充 · 2026-11-17

keep 控制 drop_duplicates 和 duplicated 对重复组的处理方式：first 保留首次出现、last 保留最后一次、False 视为全部重复而一并剔除。选不同值会让结果集完全不同，是去重前必须想清楚的一步。

- 'first' 是默认值，保留第一次出现的记录
- 'last' 保留最后一次出现的记录，常用于留最新状态
- False 表示删除所有重复项，只留下从未重复过的记录
想筛出「只出现过一次」的姓名记录，keep 该怎么写？::keep=False，删掉所有重复项，只留下从未重复过的记录
keep=False 写成 keep='False' 会有什么问题？::False 是布尔值不能加引号，写成字符串会报错或得不到预期结果
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p33 S02E18.删除重复和提取重复](https://www.bilibili.com/video/BV1ji4y157uB?p=33) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
