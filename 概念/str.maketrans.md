---
term: str.maketrans
aliases: [maketrans, 字符映射表]
kind: method
domain: 计算机/数据分析/Python
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
stage: "S02E24 · 字符串操作（下）"
order: 39
---

# str.maketrans

> 别名：maketrans、字符映射表

**创建字符到字符（或字符串）映射表的 Python 内置方法。**

## 解释

str.maketrans(dict) 接收一个字典，把原字符映射为目标内容，生成供 translate 使用的映射表。它是 translate 的前置步骤。

## 有什么用

- 为 translate 准备逐字符替换规则
- 批量字符替换

## 关键要点

- 接收字典 {原字符: 目标内容}
- 只映射表中列出的字符
- 常与 str.translate 组合使用

## 边界与易混淆

只做逐字符映射，不适合整段字符串或正则模式替换。

## 关联

- [[translate]] — 组合使用

## 自测

maketrans 的输入是什么类型？::字典，键为原字符，值为目标替换内容。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
