---
term: translate
aliases: [str.translate, 字符映射替换]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 39
stage: "S02E24 · 字符串操作（下）"
order: 39
---

# translate

> 别名：str.translate、字符映射替换

**按 maketrans 生成的映射表逐字符替换字符串内容的方法。**

## 解释

Series.str.translate(table) 按映射表把字符串中的指定字符逐个替换为目标内容，未列出的字符保持不变。比 replace 更适合建立字符级映射关系。

## 有什么用

- 把'距离'中的'距''离'替换成拼音
- 字符级批量替换

## 关键要点

- 依赖 maketrans 生成的映射表
- 逐字符替换，未指定字符不变
- 与 replace 类似但更偏字符映射

## 边界与易混淆

整段字符串或复杂模式替换应使用 replace 或正则替换。

## 关联

- [[str.maketrans]] — 前置知识
- [[str.replace]] — 对比项

## 自测

translate 和 replace 的核心区别？::translate 按字符映射表逐字符替换，replace 可替换整段字符串或按模式替换。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
