---
term: str.split
aliases: [split, 字符串拆分]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# str.split

> 别名：split、字符串拆分

**按指定字符把字符串拆分成列表的方法。**

## 解释

str.split 将每个字符串按分隔符切开，默认返回列表形式。可通过 n 控制拆分次数，通过 expand=True 把拆分结果展开成多列，效果类似 Excel 的分列。

## 有什么用

- 把“满血激活”拆成状态和动作
- 按分隔符把一列拆成多列
- 只拆分前 N 个分隔符

## 关键要点

- 默认 n=-1，全部分隔符都参与拆分
- n=1 表示只拆分第一个分隔符
- expand=True 将列表展开为多列
- 分隔符本身不出现在结果中

## 边界与易混淆

expand=True 时列数由最大拆分数量决定；空值仍保持为空。

## 关联

- [[Series.str 访问器]] — 上位概念
- [[str.rsplit]] — 对比项
- [[str.partition]] — 对比项

## 自测

str.split('血', expand=True) 和 str.split('血') 的结果差异是什么？::前者把拆分结果展开成多列，后者每行仍是一个列表。
n 参数默认值是多少，含义是什么？::默认 -1，表示所有分隔符都参与拆分。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
