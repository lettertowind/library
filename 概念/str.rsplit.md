---
term: str.rsplit
aliases: [rsplit, 从右拆分]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
order: 38
---

# str.rsplit

> 别名：rsplit、从右拆分

**从右向左按指定字符拆分字符串的方法。**

## 解释

str.rsplit 与 str.split 行为类似，但拆分方向相反：split 从左往右，rsplit 从右往左。当只拆分有限次数时，两者结果不同。

## 有什么用

- 需要保留左侧内容、只拆分右侧部分时
- 处理路径或层级字符串

## 关键要点

- 方向与 split 相反，从右向左
- 同样支持 n 和 expand 参数
- 本课只需了解，不要求熟练

## 边界与易混淆

与 split 的差异只在限制拆分次数时明显；全拆分时结果相同。

## 关联

- [[str.split]] — 对比项
- [[Series.str 访问器]] — 上位概念

## 自测

什么情况下 rsplit 和 split 结果会不同？::当限制拆分次数 n 时，从右拆和从左拆保留的部分不同。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
