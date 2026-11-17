---
term: str.repeat
aliases: [repeat, 字符串重复]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
order: 38
---

# str.repeat

> 别名：repeat、字符串重复

**把每个字符串重复指定次数的方法。**

## 解释

str.repeat(n) 将每个元素重复 n 次，返回重复后的字符串。空值可通过 na 参数转换。

## 有什么用

- 生成重复文本
- 构造测试数据

## 关键要点

- 参数为重复次数
- 支持 na 参数处理空值
- 作用于每个元素内部

## 边界与易混淆

与 DataFrame 层面的重复行操作不同，repeat 只重复字符串内容。

## 关联

- [[Series.str 访问器]] — 上位概念

## 自测

str.repeat(3) 对“张三”的结果是什么？::“张三张三张三”。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
