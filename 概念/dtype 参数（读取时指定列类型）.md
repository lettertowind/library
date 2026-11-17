---
term: dtype 参数（读取时指定列类型）
aliases: [dtype, 读取时指定类型, dtype={'序号': str}]
kind: concept
domain: 计算机/数据分析/Pandas
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 25
stage: "S02E10 · 各种数据自动填充"
order: 25
---

# dtype 参数（读取时指定列类型）

> 别名：dtype、读取时指定类型、dtype={'序号': str}

**read_excel/read_csv 中按列名指定读取后数据类型的参数，可传字典。**

## 解释

在读取阶段就用 dtype 把序号、性别、日期等列设为 str，可以避免自动填充时出现 1.0、2.0 这类浮点显示或类型报错。它比读入后再 astype 更早、更省事。

## 有什么用

- 自动填充前统一列类型
- 防止数字列被读成浮点
- 保留前导零的编号列

## 关键要点

- 可传字典 {'序号': str, '性别': str, '日期': str}
- 在读取时生效，比读后再转换更干净
- 自动填充场景建议相关列统一设 str
- 与 astype 的区别是发生在读取阶段

## 边界与易混淆

设成 str 后数值运算需先转回数值类型，不要一刀切全表设 str。

## 关联

- [[astype(str)]] — 对比项
- [[pd.read_excel]] — 组合使用
- [[自动填充]] — 前置知识

## 自测

读取时用 dtype 设 str 和读入后再 astype(str) 有什么实质差别？::dtype 在解析阶段就按目标类型读入，避免中间出现浮点；astype 是读入后再转换，可能已经产生 1.0 这类中间值。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
