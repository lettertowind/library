---
term: level 参数（groupby）
aliases: [level, 按索引层级分组, groupby(level=...)]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 41
stage: "S02E26 · 分组与聚合 groupby基础部分"
order: 41
---

# level 参数（groupby）

> 别名：level、按索引层级分组、groupby(level=...)

**groupby 中 level 指定按多层索引的某一层级分组，而非按列值分组。**

## 解释

当「班级」「性别」已被 set_index 提升为索引层级后，用 level='班级' 即可按班级聚合，无需再引用列名。它让分组键与索引结构解耦，是多层索引数据分析的关键写法。

## 有什么用

- 按多层索引的某一层汇总
- 配合 axis=1 按列层级汇总季度
- 避免重复把索引层还原成列

## 关键要点

- 必须先用 set_index 把分组列提升为索引层级
- 写法：df.groupby(level='班级').median()
- 可显式选列：groupby(level='班级')[['语文','数学']].median()
- 未设索引直接用 level 会报错或结果异常
- 整体聚合时所有剩余列必须是数值列

## 边界与易混淆

level 只认索引层级名，不认普通列名；若分组列还在列里，需先 set_index 或改用列名分组。

## 关联

- [[分层索引]] — 前置知识
- [[set_index]] — 前置知识
- [[groupby]] — 组合使用

## 自测

df 中「班级」还是普通列，能直接 groupby(level='班级') 吗？::不能，需先 set_index(['班级','性别']) 把它提升为索引层级。
level 分组出错时首先该检查什么？::索引是否已正确设置、参与聚合的列是否都是数值列。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
