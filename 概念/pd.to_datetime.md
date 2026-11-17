---
term: pd.to_datetime
aliases: [to_datetime, 转日期格式]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 29
stage: "S02E14 · 筛选"
order: 29
---

# pd.to_datetime

> 别名：to_datetime、转日期格式

**把字符串或数值列转换为 Pandas datetime 日期类型的函数。**

## 解释

to_datetime 将出生日期等文本列解析为 datetime64 类型，使日期比较、按年月索引、dt 访问器等操作可用。可作用于列，也可作用于索引。

## 有什么用

- 日期列转日期格式
- 转换日期索引
- 为日期筛选做准备

## 关键要点

- 对列：数据['出生日期'] = pd.to_datetime(数据['出生日期'])
- 对索引：数据.index = pd.to_datetime(数据.index)
- 不转换日期格式，日期筛选可能无法正常工作

## 边界与易混淆

格式不规范的日期字符串可能解析失败或需指定 format 参数。

## 关联

- [[日期筛选三部曲]] — 组合使用
- [[dt 访问器]] — 前置知识

## 自测

把日期索引转为日期格式怎么写？::数据.index = pd.to_datetime(数据.index)。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
