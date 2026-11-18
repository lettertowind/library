---
term: 类型检查（isinstance 与 issubclass）
aliases: [isinstance(), issubclass(), 类型判断]
kind: method
domain: 计算机/编程/Python
tags: [概念/method, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# 类型检查（isinstance 与 issubclass）

> 别名：isinstance()、issubclass()、类型判断

**判断对象是否为某类型的实例、或一个类是否为另一个类的子类。**

## 解释

isinstance 检查实例与类型的关系，可传类型元组一次匹配多种；issubclass 只作用于类，判断继承关系。因为会考虑继承，isinstance 比 type(x) == T 更通用。

## 有什么用

- 校验函数入参类型
- 对不同数据结构分支处理
- 封装工具函数时做类型兼容判断

## 关键要点

- 优先用 isinstance 而非 type(x) == T，前者兼容子类
- 第二个参数可传元组，如 (str, int)
- bool 是 int 的子类，isinstance(True, int) 为 True
- issubclass 的第一个参数必须是类，否则报 TypeError

## 边界与易混淆

isinstance 无法区分「这个列表装的是数字还是字符串」，只判断外层类型；过度类型检查也会破坏鸭子类型风格。

## 关联

- [[type() 函数]] — 对比项
- [[类]] — 前置知识
- [[面向对象编程]] — 前置知识

## 自测

isinstance(True, int) 和 issubclass(int, bool) 分别是什么？::True 和 False：bool 继承自 int，反向不成立。
为什么要用 isinstance 而不是 type(x) == int？::isinstance 会把子类实例也算进去（如 True 算 int），更符合多态使用习惯。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
