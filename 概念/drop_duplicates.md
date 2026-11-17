---
term: drop_duplicates
aliases: [去重, 删除重复值]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 33
stage: "S02E18 · 删除重复和提取重复"
order: 33
---

# drop_duplicates

> 别名：去重、删除重复值

**pandas 中删除重复行或重复值、返回去重结果的方法。**

## 解释

drop_duplicates 对 Series 或 DataFrame 去重。拆分任务中常对分类列（如“部门”）去重再转列表，得到唯一分组键，避免重复拆分同一组。

## 有什么用

- 获取某列的唯一值列表
- 拆分前确定分组键
- 数据清洗去重

## 关键要点

- 对列使用：数据['部门'].drop_duplicates()
- 返回去重后的 Series，不修改原数据
- 常配合 list() 转成可遍历列表
- DataFrame 上使用可按指定列去重

## 边界与易混淆

只按值相等去重，不做模糊匹配；含空格或大小写差异的会被视为不同值。

## 关联

- [[布尔索引筛选]] — 组合使用

## 自测

按部门拆分前为什么要先 drop_duplicates？不去重会怎样？::不去重则部门名重复出现，循环会多次拆分同一部门并反复覆盖写入。


### 补充 · 2026-11-17

drop_duplicates() 按 subset 指定的列判断重复并删除，keep 控制保留策略：first 保留首条、last 保留末条、False 删除所有重复项。inplace=True 时直接修改原数据。它是数据清洗中最常用的去重手段。

- subset 单列传字符串，多列传列表
- keep='first' 默认保留第一次出现
- keep='last' 保留最后一次出现
df.drop_duplicates(subset='姓名', keep=False) 的结果里还剩哪些人？::只剩从未在姓名列重复过的人，所有出现过重复的姓名整组都被删除。
按姓名和班级两列去重，subset 应该怎么写？::subset=['姓名', '班级']，多列必须用列表。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
