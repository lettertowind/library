---
term: str.match
aliases: [match, 正则匹配判断]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# str.match

> 别名：match、正则匹配判断

**判断字符串是否匹配指定正则表达式并返回布尔值的方法。**

## 解释

Series.str.match(pattern) 对每个元素做正则匹配，返回 True/False。常用于按模式筛选或标记数据，如判断状态列是否符合'两位数字+激'的格式。

## 有什么用

- 按正则模式筛选行
- 标记符合格式的数据

## 关键要点

- 返回布尔 Series
- pattern 用原始字符串 r'...' 书写
- \d 表示数字，{2} 表示出现两次
- 注意中英文符号切换导致匹配失败

## 边界与易混淆

match 从字符串开头匹配；需要提取内容用 extract，需要替换用 replace。

## 关联

- [[str.extract]] — 对比项
- [[str.replace]] — 对比项

## 自测

str.match(r'\d{2}激') 对 '满血激活' 返回什么？::False，因为开头不是两位数字。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
