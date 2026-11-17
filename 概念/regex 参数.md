---
term: regex 参数
aliases: [regex=True, 正则替换参数, regex]
kind: concept
domain: 计算机/数据分析/Pandas
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 36
stage: "S02E21 · 数据替换"
order: 36
---

# regex 参数

> 别名：regex=True、正则替换参数、regex

**replace() 中控制是否把模式按正则表达式解释的开关参数。**

## 解释

设置 regex=True 后，replace() 的第一个参数被当作正则表达式处理，可用字符类、范围等模式批量匹配，例如 '[A-Z]' 匹配任意大写字母。不设置时 pandas 把模式当普通字符串查找。

## 有什么用

- 按字符范围或模式批量替换
- 复杂匹配规则下替代冗长的列表枚举

## 关键要点

- regex=True 时第一个参数按正则解释
- 不写 regex=True，'[A-Z]' 会被当普通字符串，通常匹配不到
- 不需要额外 import re，直接配合 replace() 使用
- 模式不是正则时不要随意开启 regex=True

## 边界与易混淆

只影响 replace() 对模式的解释方式，不改变替换目标范围（整表还是单列仍由调用对象决定）。

## 关联

- [[replace]] — 组合使用
- [[正则表达式]] — 前置知识

## 自测

data.replace('[A-Z]','88') 没有加 regex=True，结果会怎样？::pandas 把 '[A-Z]' 当普通字符串查找，通常找不到匹配内容，数据基本不变。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
