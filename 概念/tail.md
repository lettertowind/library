---
term: tail
aliases: [df.tail, 查看后几行]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 21
stage: "S02E06 · 数据结构之DataFrame"
order: 21
---

# tail

> 别名：df.tail、查看后几行

**返回 DataFrame 末尾若干行的方法，默认 5 行。**

## 解释

tail(n) 查看表格最后 n 行，默认 n=5。它与 head 对称，常用于快速检查数据尾部是否有异常或确认数据末尾内容。

## 有什么用

- 快速预览数据末尾
- 检查追加数据是否正确

## 关键要点

- 默认返回后 5 行
- tail(n) 返回后 n 行
- 与 head 对称使用
- 返回的是新 DataFrame，不改原表

## 边界与易混淆

只做预览，不改变数据；行数不足 n 时返回全部行。

## 关联

- [[head()]] — 对比项
- [[DataFrame]] — 上位概念

## 自测

表只有 7 行，df.tail() 返回几行？::返回后 5 行，因为默认参数是 5。
head 和 tail 一起用能帮你判断什么？::快速确认数据首尾是否完整、有无异常或错位。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
