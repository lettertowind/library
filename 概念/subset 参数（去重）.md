---
term: subset 参数（去重）
aliases: [subset, 按列去重参数, 判断重复的列, 多列组合去重]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
---

# subset 参数（去重）

> 别名：subset、按列去重参数、判断重复的列、多列组合去重

**在去重/判重函数中指定参与比较的列，可传单列名或列名列表。**

## 解释

subset 告诉 Pandas 用哪些列来判断重复。不传时按整行所有列比较；传一列则只看该列；传列表则按多列组合判断，例如姓名加班级相同才算重复。它决定了去重的粒度。

## 有什么用

- 只按姓名去重而忽略分数差异
- 按姓名+班级等多列组合判断同一人同一班

## 关键要点

- 单列写 subset='姓名'，多列写 subset=['姓名','班级']
- 多列表示组合重复：所有指定列都相同时才算重复
- 不传 subset 默认按整行全部列判断
- 视频字幕里的 subst 是误写，真实参数名是 subset

## 边界与易混淆

subset 中的列名必须真实存在，拼错会直接报 KeyError

## 关联

- [[drop_duplicates]] — 组合使用
- [[duplicated]] — 组合使用

## 自测

subset=['姓名','班级'] 表示什么意思？::只有当姓名和班级都相同时才判定为重复，属于多列组合去重
不写 subset 直接 drop_duplicates() 是按什么判断重复？::按整行所有列判断，只有整行完全相同才算重复

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p33 S02E18.删除重复和提取重复](https://www.bilibili.com/video/BV1ji4y157uB?p=33) · 2026-11-17
