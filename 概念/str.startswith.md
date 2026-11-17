---
term: str.startswith
aliases: [startswith, 开头判断]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
order: 38
---

# str.startswith

> 别名：startswith、开头判断

**判断字符串是否以指定内容开头的方法。**

## 解释

str.startswith('满') 对每个元素判断是否以指定字符开头，返回布尔值。与 str.endswith 配对使用，同样支持 na 参数处理空值。

## 有什么用

- 筛选以某前缀开头的记录
- 按开头字符分类数据

## 关键要点

- 返回布尔值
- 支持 na 参数处理空值
- 与 endswith 方向相反

## 边界与易混淆

只判断开头，不判断包含；判断包含用 str.contains。

## 关联

- [[str.endswith]] — 对比项
- [[str.contains]] — 对比项
- [[Series.str 访问器]] — 上位概念

## 自测

str.startswith 和 str.contains 的判断范围有何不同？::startswith 只判断开头，contains 判断任意位置是否包含。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
