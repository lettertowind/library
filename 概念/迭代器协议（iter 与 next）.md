---
term: 迭代器协议（iter 与 next）
aliases: [iter(), next(), iterator protocol, StopIteration]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# 迭代器协议（iter 与 next）

> 别名：iter()、next()、iterator protocol、StopIteration

**用 __iter__ 返回自身、用 __next__ 逐个取值，取尽时抛 StopIteration 的约定。**

## 解释

iter() 从可迭代对象取得迭代器，next() 每次取一个元素，for 循环内部正是这套机制。迭代器记录的是遍历位置，一次性使用，取完不能回退。

## 有什么用

- 手动控制遍历进度
- 处理生成器与惰性数据流
- 为自己的类实现可迭代能力

## 关键要点

- 可迭代对象不等于迭代器，前者每次 iter() 都得到新迭代器
- next(it, default) 可提供默认值避免异常
- list(迭代器) 会把它一次耗尽
- enumerate、map、filter、zip 返回的都是迭代器

## 边界与易混淆

迭代器耗尽后无法倒回，需要重遍历要用原可迭代对象再取一次；与可重复遍历的 list 等序列要区分。

## 关联

- [[enumerate]] — 组合使用
- [[filter 与 map（内置函数）]] — 组合使用
- [[zip]] — 组合使用

## 自测

对同一个迭代器连续调用两次 list() 会得到什么？::第一次拿到全部元素并耗尽迭代器，第二次得到空列表。
list 和 iter(list) 有什么区别？::list 是可迭代对象，可反复取新迭代器；iter(list) 得到一次性迭代器，遍历后耗尽。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
