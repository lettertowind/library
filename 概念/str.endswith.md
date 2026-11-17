---
term: str.endswith
aliases: [endswith, 结尾判断]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# str.endswith

> 别名：endswith、结尾判断

**判断字符串是否以指定内容结尾的方法。**

## 解释

str.endswith 对每个元素判断是否以指定内容结尾，返回布尔值。用法与 str.startswith 对称，同样支持 na 参数。

## 有什么用

- 筛选以某后缀结尾的记录
- 按文件扩展名分类

## 关键要点

- 返回布尔值
- 支持 na 参数
- 与 startswith 方向相反

## 边界与易混淆

只判断结尾，不判断包含。

## 关联

- [[str.startswith]] — 对比项
- [[Series.str 访问器]] — 上位概念

## 自测

判断字符串是否以“.csv”结尾用哪个方法？::str.endswith('.csv')。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
