---
term: lambda 表达式
aliases: [匿名函数, lambda]
kind: concept
domain: 数据分析/Python
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
stage: "S02E11 · 列与列之间的计算"
order: 26
---

# lambda 表达式

> 别名：匿名函数、lambda

**用一行写出无名函数的语法，形式为 lambda 参数: 返回值。**

## 解释

lambda 用于定义临时的小函数，常作为参数直接传给 apply、map 等。它省去 def 定义再传名的步骤，适合逻辑只有一句的场景。在 pandas 中常用于条件赋值，如 lambda x: 5 if x != '汉' else 0。

## 有什么用

- apply 中写简短变换
- 条件判断赋值
- 临时函数传参

## 关键要点

- 语法：lambda 参数: 表达式
- 只能写单个表达式，不能写多行语句
- 常与 apply / map 组合
- 三元写法可做条件分支：x if 条件 else y

## 边界与易混淆

逻辑复杂时应改用 def 具名函数，可读性更好。

## 关联

- [[apply]] — 组合使用
- [[map]] — 组合使用

## 自测

lambda x: 5 if x != '汉' else 0 对汉族返回什么？::返回 0，因为条件 x != '汉' 不成立。


### 补充 · 2026-11-17

写法 lambda x: 表达式，冒号后只放一个表达式并自动返回其值。它与 def 定义的函数对 apply 完全等价，但不用起名、不用写 return，是数据清洗里最常见的回调写法；也能内嵌条件表达式完成分支判断。

- 只有单表达式，不能写多行语句块
- lambda x: x + 3 等价于 def 加 return x + 3
- 可嵌条件：lambda x: 5 if x != '汉' else 0
数据['单价'].apply(lambda x: x + 3) 实现了什么？::把单价列每个元素都加 3，返回新列。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p26 S02E11.列与列之间的计算](https://www.bilibili.com/video/BV1ji4y157uB?p=26) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
