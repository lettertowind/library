---
term: 作用域声明（global 与 nonlocal）
aliases: [global, nonlocal, global 语句, nonlocal 语句]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# 作用域声明（global 与 nonlocal）

> 别名：global、nonlocal、global 语句、nonlocal 语句

**在函数内声明变量来自全局或外层函数作用域的语句。**

## 解释

global 让函数内赋值指向全局变量，nonlocal 指向最近外层函数变量。它们用于修改外层状态，但会让数据流不直观，应谨慎使用。默认函数内赋值会创建局部变量。

## 有什么用

- 在函数内修改全局配置
- 闭包中修改外层计数器
- 理解 Python 变量查找规则

## 关键要点

- global 指向全局命名空间
- nonlocal 指向外层函数局部变量
- 仅声明作用域，不创建变量
- 滥用导致隐式状态和耦合
- 与默认局部赋值规则相反

## 边界与易混淆

nonlocal 不能跨越模块全局；global 不能直接声明全局中的嵌套局部。

## 关联

- [[命名空间（globals 与 locals）]] — 前置知识
- [[Python 关键字]] — 上位概念

## 自测

函数内不给变量加 global 直接赋值，会修改全局变量吗？::不会，会创建同名局部变量。

## 出处

- [40分钟带你了解Python中所有的关键字](https://www.bilibili.com/video/BV17pLUzdEtw) · 2026-11-18
