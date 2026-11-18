---
term: 模式匹配（matchcase）
aliases: [match/case, 模式匹配, structural pattern matching]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# 模式匹配（matchcase）

> 别名：match/case、模式匹配、structural pattern matching

**Python 3.10+ 用 match 和 case 对值做结构化分支匹配的语法。**

## 解释

match 后接待匹配表达式，case 定义模式和可选守卫条件。它比 if/elif 更适合解构列表、字典、对象等结构。match 与 case 是软关键字，_ 可作通配模式。

## 有什么用

- 多分支条件判断
- 解构并匹配数据结构
- 替代冗长 if/elif 链

## 关键要点

- 3.10 引入，需注意版本
- case 可带守卫条件
- 支持结构化模式与通配符 _
- match/case 是软关键字
- 可读性优先，避免 match match

## 边界与易混淆

不是所有多分支都该用；简单条件用 if/elif 更清晰。

## 关联

- [[软关键字]] — 上位概念
- [[Python 关键字]] — 上位概念

## 自测

match/case 相比 if/elif 的优势场景？::需要按数据结构解构匹配、或需要模式守卫时更清晰。

## 出处

- [40分钟带你了解Python中所有的关键字](https://www.bilibili.com/video/BV17pLUzdEtw) · 2026-11-18
