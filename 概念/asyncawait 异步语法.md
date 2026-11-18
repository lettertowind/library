---
term: asyncawait 异步语法
aliases: [async, await, 异步函数, 协程语法]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# asyncawait 异步语法

> 别名：async、await、异步函数、协程语法

**用 async def 定义协程、用 await 等待异步结果，实现单线程并发。**

## 解释

async def 声明的函数调用后返回协程对象，需事件循环运行。await 用于等待可等待对象完成并取结果，常用于 IO 密集任务。它不是多线程，也不会自动并行 CPU 计算。

## 有什么用

- 网络请求、数据库访问等 IO 并发
- 用 asyncio 组织异步任务
- 避免阻塞事件循环

## 关键要点

- async def 定义协程函数
- await 等待可等待对象
- 需 asyncio 等事件循环运行
- 适合 IO 密集而非 CPU 密集
- 阻塞调用会卡住事件循环

## 边界与易混淆

async/await 不等于多线程或多进程；CPU 密集任务仍需并行方案。

## 关联

- [[Python 关键字]] — 上位概念
- [[yield 生成器]] — 对比项

## 自测

调用 async def 函数会直接执行函数体吗？::不会，返回协程对象，需事件循环调度执行。

## 出处

- [40分钟带你了解Python中所有的关键字](https://www.bilibili.com/video/BV17pLUzdEtw) · 2026-11-18
