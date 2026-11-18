---
term: chr
aliases: [chr(), 码点转字符, Unicode 码点转字符]
kind: method
domain: 计算机/编程/Python
tags: [概念/method, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# chr

> 别名：chr()、码点转字符、Unicode 码点转字符

**把 Unicode 码点整数转换成对应的单个字符。**

## 解释

chr 是 ord 的逆操作。传入一个整数，返回该编号在 Unicode 表中对应的字符：`chr(65)` 得到 `'A'`，`chr(97)` 得到 `'a'`。两者满足 `chr(ord(c)) == c`。

## 有什么用

- 由编号生成字符，例如按序号生成 a、b、c
- 处理编码、字符集转换时做码点与字符的互转
- 加密、混淆等需要按码点运算的小工具

## 关键要点

- 参数必须是整数，合法范围是 `0` 到 `0x10FFFF`（1114111）
- 超出范围抛 `ValueError`，传字符串抛 `TypeError`
- `chr(ord(c)) == c`，与 ord 严格互逆
- 常见码点：`chr(10)` 是换行 `\n`，`chr(9)` 是制表符

## 边界与易混淆

与 `bytes.decode` 不同：chr 处理的是单个码点，decode 处理的是字节序列按编码规则还原文本。另外 `chr(0)` 返回空字符 `\x00`，不是空字符串。

## 关联

- [[ord（字符转码点）]] — 互逆操作
- [[str]] — 返回值的类型

## 自测

`chr(97)` 返回什么？::返回小写字母 `'a'`，因为 97 是 a 的 Unicode 码点。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
