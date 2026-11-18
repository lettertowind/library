---
term: ord（字符转码点）
aliases: [ord, ord(), ordinals, 字符转 Unicode]
kind: method
domain: 计算机/编程/Python
tags: [概念/method, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# ord（字符转码点）

> 别名：ord、ord()、ordinals、字符转 Unicode

**把单个字符转换成它对应的 Unicode 码点整数。**

## 解释

ord 是 chr 的逆操作，名字来自 ordinals（序数）。它接受长度为 1 的字符串，返回该字符在 Unicode 表中的编号，常用来做字符比较、编码判断或密码学小练习。

## 有什么用

- 需要知道字符的数字编码时
- 字符排序、加密、编码转换场景

## 关键要点

- ord('A') 返回 65，ord('Ω') 返回对应码点
- 参数必须是长度为 1 的字符串，多字符会报错
- 与 chr 互为逆操作：chr(ord(c)) == c

## 边界与易混淆

只处理单个字符；中文、emoji 也各算一个码点，但组合字符可能由多个码点构成。

## 关联

- [[chr]] — 对比项
- [[str]] — 上位概念

## 自测

为什么 ord 不能直接传 'AB'？::它只接受单个字符，多字符无法确定返回哪个码点，会抛 TypeError。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
