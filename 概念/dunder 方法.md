---
term: dunder 方法
aliases: [魔术方法, magic methods, 双下划线方法, 特殊方法]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# dunder 方法

> 别名：魔术方法、magic methods、双下划线方法、特殊方法

**名称前后各带双下划线、由 Python 特定语法触发的方法。**

## 解释

例如 __add__ 定义 + 的行为，__mul__ 定义 * 的行为。没有定义时，自定义对象不能直接相加/相乘。它让对象接入 Python 的内置语法和协议。

## 有什么用

- 让自定义对象支持 +、*、| 等操作符
- 自定义打印和开发者表示

## 关键要点

- 前后各两个下划线
- 由操作符或内置函数触发
- __add__ 对应 +，__mul__ 对应 *
- 可返回字符串、对象或其他实例

## 边界与易混淆

不要随意发明 dunder 名称；应使用 Python 规定的方法名。

## 关联

- [[实例方法]] — 上位概念
- [[__str__ 与 __repr__]] — 下位概念

## 自测

smeg + bosch 报“不支持该操作”，最可能缺哪个方法？::缺少 __add__ 方法。

## 出处

- [【中文字幕】最强Python教学-20分钟学会面向对象编程](https://www.bilibili.com/video/BV1m7L1zaEH8) · 2026-11-18
