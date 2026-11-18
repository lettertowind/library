---
term: dtype 参数（读取时指定列类型）
aliases: [dtype, 读取时指定类型, dtype={'序号': str}]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 25
stage: "S02E10 · 各种数据自动填充"
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


### 补充 · 2026-11-17

列里一旦有空值，Pandas 会把该列推断成 float，序号就变成 1.0、2.0；用 dtype={'序号': str, '性别': str, '日期': str} 一次性把要填充的列设为字符型，显示和后续判断都正常。

- 写法是字典：列名 → 类型，只对写到的列生效
- 自动填充场景下，参与填充的列统一设 str 最省事
- 不转 str 会导致序号带 .0、性别判断和日期运算报错
序号列填完为什么会出现 1.0、2.0？::列中有空值，Pandas 推断为 float；读取时 dtype 设 str 可避免
dtype={'序号': str} 会影响没列出的列吗？::不会，其他列仍由 Pandas 自动推断
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p25 S02E10.各种数据自动填充](https://www.bilibili.com/video/BV1ji4y157uB?p=25) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
