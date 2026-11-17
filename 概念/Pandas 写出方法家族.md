---
term: Pandas 写出方法家族
aliases: [to_* 方法, 文件写出方法]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 16
stage: "S02E01 · 数据类型与新建文件"
order: 16
---

# Pandas 写出方法家族

> 别名：to_* 方法、文件写出方法

**DataFrame 上以 to_ 开头、按目标格式命名的一组导出方法。**

## 解释

Pandas 把导出不同格式统一成 to_格式名 的方法命名规则，如 to_csv、to_excel、to_sql。学会一个就基本会全部，切换格式只需改方法名和文件后缀。

## 有什么用

- 选择合适格式保存分析结果
- 快速迁移到新文件格式

## 关键要点

- 命名规律是 to_ + 目标格式
- to_csv、to_excel、to_sql 最常用
- 换格式通常只改方法名和后缀
- JSON 等格式也有对应方法但非重点

## 边界与易混淆

不同格式支持的参数不同，不能假设参数完全通用。

## 关联

- [[to_csv]] — 下位概念
- [[DataFrame.to_excel]] — 下位概念
- [[to_sql]] — 下位概念

## 自测

要新增导出 JSON，按命名规律方法名大概是什么？::to_json。
为什么说掌握三种写出方法基本够用？::因为其他格式写法大同小异，只需改方法名和后缀。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
