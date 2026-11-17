---
term: str.partition
aliases: [partition, 三分拆分]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
order: 38
---

# str.partition

> 别名：partition、三分拆分

**按第一个分隔符把字符串拆成“前、分隔符、后”三部分的方法。**

## 解释

str.partition 固定返回三个部分：分隔符之前的内容、分隔符本身、分隔符之后的内容。与 split 不同，它保留分隔符，且只按第一个分隔符分割。

## 有什么用

- 需要保留分隔符本身时
- 把字符串拆成前缀、标记、后缀三段

## 关键要点

- 固定返回三部分，保留分隔符
- 只按第一个分隔符分割
- 分隔符不存在时返回原字符串和两个空串
- rpartition 从右向左查找分隔符

## 边界与易混淆

多个分隔符时只处理第一个；找不到分隔符不会报错，而是返回原串加两个空值。

## 关联

- [[str.split]] — 对比项
- [[str.rsplit]] — 对比项
- [[Series.str 访问器]] — 上位概念

## 自测

str.partition 和 str.split 对分隔符的处理有什么本质区别？::partition 保留分隔符作为中间部分，split 不保留分隔符。
字符串中有多个分隔符时 partition 怎么处理？::只按第一个分隔符分割，其余部分整体归入第三部分。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
