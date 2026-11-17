---
term: txt 转 csv
aliases: [txt 转 csv, 文本转 csv, to_csv 转换]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 17
stage: "S02E02 · 读取txt与csv文件"
order: 17
---

# txt 转 csv

> 别名：txt 转 csv、文本转 csv、to_csv 转换

**用 read_csv 读 txt 再 to_csv 写出为 csv 的两步转换法。**

## 解释

实际大数据分析更推荐 csv 而非 txt。转换只需 read_csv 读入、to_csv 写出两步；若乱码可在读或写时指定 encoding='utf-8'。

## 有什么用

- 把 txt 数据规范为 csv
- 统一数据格式便于后续分析

## 关键要点

- 两步：read_csv 读入 + to_csv 写出
- 乱码时读写都可加 encoding='utf-8'
- 大数据分析优先用 csv 存储

## 边界与易混淆

转换会重写文件，注意不要覆盖原始数据。

## 关联

- [[pd.read_csv]] — 组合使用
- [[DataFrame.to_excel]] — 对比项

## 自测

txt 转 csv 的核心两行代码是什么？::data = pd.read_csv('data.txt')；data.to_csv('data.csv')。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
