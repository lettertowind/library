---
term: case 参数
aliases: [case, case=False, 大小写敏感参数]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 29
stage: "S02E14 · 筛选"
---

# case 参数

> 别名：case、case=False、大小写敏感参数

**str.contains 等字符串方法中控制是否区分大小写的布尔参数。**

## 解释

case 默认 True 表示区分大小写，设为 False 则忽略大小写。配合正则使用时也可直接在正则里写出大小写范围，而不依赖 case。

## 有什么用

- contains 忽略大小写匹配
- 正则筛选时控制大小写

## 关键要点

- 默认 case=True，区分大小写
- case=False 忽略大小写
- 用正则时可直接写 [a-cA-C] 代替 case=False

## 边界与易混淆

只对支持该参数的字符串方法有效，不是所有 str 方法都有 case 参数。

## 关联

- [[str.contains]] — 组合使用
- [[正则表达式]] — 对比项

## 自测

contains('[a-c]', case=False) 能匹配大写 A 吗？::能，case=False 忽略大小写，a-c 同时匹配 A-C。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
