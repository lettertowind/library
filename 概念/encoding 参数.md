---
term: encoding 参数
aliases: [encoding, 编码参数, encoding='utf-8']
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 17
stage: "S02E02 · 读取txt与csv文件"
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


### 补充 · 2026-11-17

CSV 另存时若不是 UTF-8，read_csv 会直接抛错。修法有两种：在外部把文件另存为 UTF-8，或在代码里写 pd.read_csv(路径, encoding='utf-8')。真实的大数据文件往往无法在外部改编码，只能靠代码指定。

- 标准写法 encoding='utf-8'，口述里的「uf 8 / utf 杠八」即此
- 优先外部统一存成 UTF-8，跨团队文件更省事
- 大数据文件改不了编码，只能在代码里加参数
read_csv 报编码错误又没法改源文件，应怎么处理？::在 read_csv 中加 encoding='utf-8'（或文件实际编码）指定。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p26 S02E11.列与列之间的计算](https://www.bilibili.com/video/BV1ji4y157uB?p=26) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
