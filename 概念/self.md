---
term: self
aliases: [当前实例引用, instance reference]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# self

> 别名：当前实例引用、instance reference

**类方法中指向当前实例的引用。**

## 解释

self 让属性绑定到正确的对象上：创建 smeg 时 self 指向 smeg，创建 bosch 时指向 bosch。方法调用时 Python 自动把实例传给 self，不需要手动传入。它只是惯例名称，可以改名但不建议。

## 有什么用

- 在 __init__ 中绑定属性
- 在实例方法中访问当前对象的数据

## 关键要点

- 指向当前正在使用的实例
- 调用方法时自动传入
- 属性必须写成 self.xxx
- 可改名但社区惯例用 self

## 边界与易混淆

self 不是关键字，改名代码仍可运行；但可读性和惯例会变差。

## 关联

- [[实例方法]] — 组合使用
- [[__init__ 初始化器]] — 组合使用
- [[对象（实例）]] — 前置知识

## 自测

调用 smeg.turn_on() 时，turn_on 的 self 指向谁？::指向 smeg 这个实例。

## 出处

- [【中文字幕】最强Python教学-20分钟学会面向对象编程](https://www.bilibili.com/video/BV1m7L1zaEH8) · 2026-11-18
