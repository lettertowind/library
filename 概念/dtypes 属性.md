---
term: dtypes 属性
aliases: [dtypes, 数据类型查看]
kind: metric
domain: 数据分析/Pandas
tags: [概念/metric, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 16
stage: "S02E01 · 数据类型与新建文件"
---

# dtypes 属性

> 别名：dtypes、数据类型查看

**返回 DataFrame 每列数据类型的属性。**

## 解释

dtypes 显示各列类型，如 object 表示字符串类、int64 表示 64 位整型。用于读取后检查类型是否符合预期，为后续计算和转换做准备。

## 有什么用

- 检查各列数据类型
- 发现类型异常如数字被读成 object

## 关键要点

- object 通常对应字符串
- int64 为 64 位整型
- 不同列类型可不同

## 边界与易混淆

dtypes 是属性；单列类型可用 data['列'].dtype 查看。

## 关联

- [[DataFrame]] — 上位概念
- [[astype(str)]] — 组合使用

## 自测

年龄列显示 object 可能意味着什么？::该列被当作字符串，可能含非数字字符或读取时未识别为数值。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
