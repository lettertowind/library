---
term: str.contains
aliases: [contains, 包含判断]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 29
stage: "S02E14 · 筛选"
order: 29
---

# str.contains

> 别名：contains、包含判断

**判断每个字符串是否包含指定内容并返回布尔值的方法。**

## 解释

str.contains('血') 对每个元素判断是否包含指定子串，返回 True 或 False。空值默认返回 NaN，可用 na 参数指定空值结果。

## 有什么用

- 筛选包含关键词的行
- 标记数据中是否出现某内容

## 关键要点

- 返回布尔型结果
- 空值默认返回 NaN
- na 参数可设为 False、True 或自定义值
- 常与布尔索引筛选组合使用

## 边界与易混淆

默认按子串匹配；需要正则匹配时需注意参数设置。

## 关联

- [[布尔索引筛选]] — 组合使用
- [[str.startswith]] — 对比项
- [[正则表达式]] — 前置知识

## 自测

str.contains 遇到空值默认返回什么？::NaN。
如何让空值在 contains 结果中显示为 False？::设置 na=False。


### 补充 · 2026-11-17

contains 用于“包含”匹配，弥补 startswith/endswith 只能匹配首尾的不足。第一个参数可为普通字符串或正则表达式，配合 case 控制大小写。

- 写法：数据['地址'].str.contains('信阳市')
- 参数可为字符串或正则表达式
- 默认区分大小写，case=False 忽略
地址有“河南省信阳市”和“信阳市”两种写法，该用 startswith 还是 contains？::用 contains，因为“河南省信阳市”不以“信阳市”开头。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
