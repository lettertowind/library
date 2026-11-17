---
term: isin
aliases: [Series.isin, df['列'].isin, 成员判断]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 42
stage: "S02E27 · 分组对象和创建"
order: 42
---

# isin

> 别名：Series.isin、df['列'].isin、成员判断

**判断 Series 每个元素是否属于给定列表，返回布尔序列。**

## 解释

isin 用于「某列的值是否在候选集合中」的筛选或分组。它替代了 Excel 中多条件 OR 筛选，写法简洁。取反用波浪号 ~ 加在表达式前。

## 有什么用

- 筛选指定几个类别
- 按是否属于指定集合分组
- 多值匹配替代多个 ==

## 关键要点

- df['班级'].isin(['一班','二班']) 返回 True/False 序列
- Pandas 没有 isnotin，取反用 ~df['班级'].isin([...])
- ~ 必须加在 isin 表达式前，不能加在 groupby 后面
- isin 可同时用于筛选和作为 groupby 分组键

## 边界与易混淆

只做成员判断，不支持正则或模糊匹配；模糊匹配用 str.contains。

## 关联

- [[布尔索引筛选]] — 组合使用
- [[布尔分组键]] — 组合使用
- [[str.contains]] — 对比项

## 自测

如何选出班级不属于一班、二班的所有行？::df[~df['班级'].isin(['一班','二班'])]。
isin 和 == 的区别是什么？::== 只能比单个值，isin 可一次比一个列表中的多个值。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
