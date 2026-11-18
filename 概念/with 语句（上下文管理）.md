---
term: with 语句（上下文管理）
aliases: [with, with 语句, 上下文管理器, context manager]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# with 语句（上下文管理）

> 别名：with、with 语句、上下文管理器、context manager

**保证代码块结束时自动执行清理动作（如关闭文件）的语法结构。**

## 解释

with open('a.txt', 'r') as f: 在块内拿到文件对象，块结束（即使抛异常）自动关闭文件，避免忘记 close 造成资源泄漏。open 的 'r' 是默认读取模式，内容可用 read() 取出。

## 有什么用

- 读写文件、数据库连接、锁等需释放的资源

## 关键要点

- 'r' 为读取模式，也是 open 的默认模式
- 块正常结束或异常退出都会触发清理
- 依赖对象的 __enter__ / __exit__ 协议

## 边界与易混淆

只能管理支持上下文管理器协议的对象；不能用它替代真正的异常处理逻辑。

## 关联

- [[open()]] — 组合使用

## 自测

为什么 with 比手动 f.close() 更安全？::块内一旦抛异常，close() 可能被跳过；with 在退出时统一执行清理，异常路径也不会漏。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
