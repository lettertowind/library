---
term: sort 参数（concat）
aliases: [sort, sort=True, 排序参数]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 24
stage: "S02E09 · 连接查询之concat"
order: 24
---

# sort 参数（concat）

> 别名：sort、sort=True、排序参数

**concat 中控制是否按索引排序的参数，默认为 True。**

## 解释

当 concat 沿 axis=1 横向拼接时，sort 参数决定结果是否按索引排序。默认 True 会自动排序索引；设为 False 则保持原顺序。该参数在数据合并中不是重点，但了解可避免意外排序。

## 有什么用

- 控制横向拼接后索引是否自动排序
- 需要保持原始索引顺序时设为 False

## 关键要点

- 默认 True，自动按索引排序
- 设为 False 保持原索引顺序
- 主要影响 axis=1 横向拼接的结果

## 边界与易混淆

sort 参数只影响索引排序，不影响数据内容。

## 关联

- [[pd.concat]] — 组合使用
- [[sort_index]] — 对比项

## 自测

concat 横向拼接时不想让索引自动排序，应设置什么？::sort=False。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
