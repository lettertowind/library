---
term: filter 与 map（内置函数）
aliases: [filter(), map(), 过滤与映射, 惰性迭代器函数]
kind: method
domain: 计算机/编程/Python
tags: [概念/method, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# filter 与 map（内置函数）

> 别名：filter()、map()、过滤与映射、惰性迭代器函数

**按函数筛选元素（filter）或逐元素变换（map）的内置工具，返回惰性迭代器。**

## 解释

filter 保留使函数返回真的元素，map 把函数应用到每个元素上；两者都不立即计算，需要 list() 才看到结果，因此内存占用小。它们是函数式写法的入口，函数参数常直接用 lambda。

## 有什么用

- 数据清洗时筛选记录
- 批量转换字段格式（如统一大写）
- 替代 for 循环收集结果

## 关键要点

- 都返回迭代器，遍历一次即耗尽
- filter 的函数传 None 时按真值过滤，可剔除空值
- 比列表推导式省内存，但可读性略差
- 与 zip、enumerate 同属返回迭代器的内置函数族

## 边界与易混淆

与 Pandas 的 Series.map 完全不同：后者向量化并返回 Series、按索引对齐；内置 map 返回迭代器。

## 关联

- [[lambda 表达式]] — 组合使用
- [[真值判断（Truthiness）]] — 前置知识
- [[map]] — 对比项
- [[迭代器协议（iter 与 next）]] — 上位概念

## 自测

filter(f, xs) 与 [x for x in xs if f(x)] 的关键区别？::前者返回惰性迭代器、边取边算且省内存；后者一次性生成完整列表。
为什么 print(filter(f, xs)) 看不到结果？::filter 返回的是迭代器对象，需要 list() 转换才能看到元素。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
