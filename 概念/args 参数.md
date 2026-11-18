---
term: args 参数
aliases: [args, apply 额外参数]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
---

# args 参数

> 别名：args、apply 额外参数

**apply 中把额外位置参数以元组形式透传给目标函数的关键字参数**

## 解释

调用 apply 时，pandas 先把列元素或行 Series 作为函数的第一个参数，再把 args 元组里的元素按顺序展开为后续参数。它让同一个函数可以通过改参数值复用于不同运算，是 apply 优于 map 的关键。

## 有什么用

- 给整列成绩统一加 5 分、减 5 分等参数化运算
- 复用同一个函数但换不同阈值或系数

## 关键要点

- args 必须是元组，单参数也要写成 (5,)，逗号不能省
- 写成 (5) 只是普通括号，无法正确传参
- 可与 axis 同时使用，例如 df.apply(函数, axis=1, args=(系数,))
- map 不支持额外参数，因此多参数需求首选 apply

## 边界与易混淆

args 只负责按位置透传，顺序必须与函数形参一致；关键字方式传参不在其覆盖范围内。

## 关联

- [[apply]] — 组合使用
- [[map]] — 对比项
- [[axis 参数]] — 组合使用

## 自测

df["语文"].apply(修改分数, args=(5,)) 里 5 传给了函数的哪个形参？::传给第二个形参（误差值），第一个形参 x 接收的是列里的每个分数
args=(-5,) 与 args=(-5) 有何区别？::前者是单元素元组，能正确透传；后者不是元组，参数无法被正确展开

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p45 S02E30.数据处理的三板斧](https://www.bilibili.com/video/BV1ji4y157uB?p=45) · 2026-11-17
