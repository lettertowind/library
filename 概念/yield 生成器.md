---
term: yield 生成器
aliases: [yield, 生成器, generator, 生成器函数]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# yield 生成器

> 别名：yield、生成器、generator、生成器函数

**在函数中用 yield 逐个产出值并暂停，从而创建生成器。**

## 解释

生成器函数调用后不会立刻执行完，而是返回生成器对象。每次 next() 推进到下一个 yield 并产出值，值被取走后不会保留。它适合惰性生成大序列，节省内存。

## 有什么用

- 惰性生成大量数据
- 实现自定义迭代器
- 流式处理文件或管道

## 关键要点

- yield 暂停并产出值
- 生成器是一次性、会耗尽的
- next() 逐个取值
- list() 收集剩余值
- 调用生成器函数不执行函数体

## 边界与易混淆

生成器不能重复遍历；需要多次遍历时应转成列表或重新创建。

## 关联

- [[迭代器协议（iter 与 next）]] — 上位概念
- [[asyncawait 异步语法]] — 对比项

## 自测

生成器被 for 循环遍历完后还能再次取值吗？::不能，生成器已耗尽，需重新创建。

## 出处

- [40分钟带你了解Python中所有的关键字](https://www.bilibili.com/video/BV17pLUzdEtw) · 2026-11-18
