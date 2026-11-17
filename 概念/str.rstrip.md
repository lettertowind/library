---
term: str.rstrip
aliases: [rstrip, 右侧去除]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# str.rstrip

> 别名：rstrip、右侧去除

**按字符集合从字符串右侧去除字符的方法。**

## 解释

str.rstrip(chars) 是 str.strip 的单侧版本，只从右边去除属于字符集合的字符。

## 有什么用

- 只清理右侧后缀
- 去除结尾的多余符号

## 关键要点

- 只从右侧去除
- 参数同样是字符集合
- 与 lstrip 方向相反

## 边界与易混淆

只处理右侧，左侧不动。

## 关联

- [[str.strip]] — 上位概念
- [[str.lstrip]] — 对比项

## 自测

只想去除字符串结尾的符号用哪个方法？::str.rstrip。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
