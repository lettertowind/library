---
term: open 与 with 语句
aliases: [open(), with open, 文件对象, 上下文管理器]
kind: method
domain: 计算机/编程/Python
tags: [概念/method, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# open 与 with 语句

> 别名：open()、with open、文件对象、上下文管理器

**open 打开文件返回文件对象，with 保证代码块结束时自动关闭。**

## 解释

open(路径, 模式) 得到可读写的文件对象，配合 with 使用可在正常结束或抛异常时都自动关闭文件，避免句柄泄漏。读大文件时按行遍历比一次性 read() 更省内存。

## 有什么用

- 读取文本、CSV 等数据文件
- 把处理结果写入文件
- 逐行处理超大文件

## 关键要点

- 常用模式：r 读、w 覆盖写、a 追加，加 b 为二进制
- with 退出即关闭文件，无需手动 close
- for line in f 逐行读取，内存友好
- 处理中文文本建议显式指定 encoding='utf-8'

## 边界与易混淆

不用 with 就必须在 finally 中 close；二进制模式下读出的是 bytes，需要自己解码。

## 关联

- [[路径变量]] — 组合使用
- [[迭代器协议（iter 与 next）]] — 前置知识

## 自测

为什么推荐 with open(...) as f 而不是 f = open(...)？::with 在代码块结束或异常时自动关闭文件，避免句柄泄漏和数据未落盘。
模式 'w' 和 'a' 有什么区别？::'w' 会清空原文件再写，'a' 在文件末尾追加，原内容保留。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
