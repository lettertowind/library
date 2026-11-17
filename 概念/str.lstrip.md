---
term: str.lstrip
aliases: [lstrip, 左侧去除]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# str.lstrip

> 别名：lstrip、左侧去除

**按字符集合从字符串左侧去除字符的方法。**

## 解释

str.lstrip(chars) 是 str.strip 的单侧版本，只从左边去除属于字符集合的字符。与 rstrip 配对使用。

## 有什么用

- 只清理左侧前缀
- 去除开头的多余符号

## 关键要点

- 只从左侧去除
- 参数同样是字符集合
- 与 rstrip 方向相反

## 边界与易混淆

只处理左侧，右侧不动。

## 关联

- [[str.strip]] — 上位概念
- [[str.rstrip]] — 对比项

## 自测

lstrip 和 rstrip 的区别是什么？::lstrip 只从左侧去除，rstrip 只从右侧去除。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
