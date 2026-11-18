---
term: range 范围对象
aliases: [range, range(), 步长 step]
kind: method
domain: 计算机/编程/Python
tags: [概念/method, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# range 范围对象

> 别名：range、range()、步长 step

**按起始、结束、步长生成一串整数，供循环或构造序列使用。**

## 解释

range 有三种写法：range(stop)、range(start, stop)、range(start, stop, step)。它返回的是惰性范围对象而非列表，所以内存占用小。步长可以为负，用于倒序遍历。

## 有什么用

- for 循环控制次数
- 生成等差整数序列

## 关键要点

- 结束位置永远不包含自身
- 第三个参数是步长，可为负实现倒序
- range(10, 0) 为空，需写成 range(10, 0, -1)

## 边界与易混淆

只接受整数；需要浮点步长时要借助 numpy.arange。

## 关联

- [[range 结束位置不含自身]] — 下位概念
- [[reversed]] — 组合使用

## 自测

为什么 range(10, 0) 一个数都不产生？::默认步长为 +1，从 10 出发无法“增加”到小于 0 的终点，故为空。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
