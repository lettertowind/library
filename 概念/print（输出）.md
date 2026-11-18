---
term: print（输出）
aliases: [print, print(), 打印输出]
kind: method
domain: 计算机/编程/Python
tags: [概念/method, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# print（输出）

> 别名：print、print()、打印输出

**把对象按可读形式输出到控制台，可用 sep 和 end 控制格式。**

## 解释

print 是调试和展示最基本的出口。多个参数会被自动转成字符串并按 sep 连接，末尾追加 end。它还能配合 * 解包把列表元素逐个当参数传入。

## 有什么用

- 调试打印变量
- 格式化输出结果

## 关键要点

- sep 控制多参数之间的分隔符，默认空格
- end 控制结尾字符，默认换行符 \n
- print(*列表) 可把列表解包成多个参数

## 边界与易混淆

改了 end 不换行会影响后续输出排版；正式输出格式化更推荐 f-string。

## 关联

- [[字符串乘法]] — 组合使用
- [[zip]] — 组合使用

## 自测

print(*people, sep=',', end='.') 中 * 起什么作用？::把 people 里的元素解包成多个独立参数，从而被 sep 分隔输出。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
