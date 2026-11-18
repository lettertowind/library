---
term: slice（切片对象）
aliases: [slice, slice(), 切片对象, 可复用切片]
kind: method
domain: 计算机/编程/Python
tags: [概念/method, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# slice（切片对象）

> 别名：slice、slice()、切片对象、可复用切片

**把 start/stop/step 封装成一个可复用的切片对象，用于下标中。**

## 解释

nums[0:5:2] 里的冒号语法其实等价于 slice(0, 5, 2)。显式创建 slice 对象后，可以在多处索引中重复使用，切片规则只在一个地方维护。

## 有什么用

- 同一套切片规则反复使用
- 把切片逻辑作为参数传递

## 关键要点

- slice(None, None, 2) 等价于 [::2]
- slice(None, None, -1) 等价于反转
- 切片对象可以像变量一样保存、传参

## 边界与易混淆

slice 只描述位置规则，不含数据；对支持 __getitem__ 的对象才生效。

## 关联

- [[负索引]] — 前置知识
- [[str.slice（Pandas）]] — 对比项

## 自测

把 [::2] 提成变量有什么好处？::切片规则集中定义一次，多处复用，改动时不用逐个改冒号表达式。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
