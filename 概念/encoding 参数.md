---
term: encoding 参数
aliases: [encoding, 编码参数, encoding='utf-8']
kind: concept
domain: 计算机/数据分析/Pandas
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# encoding 参数

> 别名：encoding、编码参数、encoding='utf-8'

**读写文件时指定字符编码的参数，常用 utf-8 解决乱码。**

## 解释

文件保存编码与读取编码不一致时会出现乱码，尤其中国大陆系统默认编码非 utf-8。读取时传 encoding='utf-8'，写出时 to_csv 也可指定。

## 有什么用

- 解决中文乱码
- 统一读写编码

## 关键要点

- 读取与写出都可指定 encoding
- 中文乱码常见原因是编码不匹配
- utf-8 是常用统一编码

## 边界与易混淆

编码需与文件实际保存编码一致，猜错仍会乱码。

## 关联

- [[pd.read_csv]] — 组合使用
- [[DataFrame.to_excel]] — 对比项

## 自测

读取 txt 出现乱码，最直接的参数修正是什么？::加 encoding='utf-8'（或文件实际编码）。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
