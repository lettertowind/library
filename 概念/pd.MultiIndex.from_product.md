---
term: pd.MultiIndex.from_product
aliases: [from_product, 笛卡尔积创建 MultiIndex]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# pd.MultiIndex.from_product

> 别名：from_product、笛卡尔积创建 MultiIndex

**用多个一维列表的笛卡尔积创建多层索引的方法。**

## 解释

from_product 接收一个列表的列表，生成各层元素的所有组合，是创建 MultiIndex 最推荐的方式。它适合层级取值需要两两组合的场景，如年份×月份、类别×品名。

## 有什么用

- 创建行或列的多层索引
- 构造总计结果的多层列索引

## 关键要点

- 参数是列表的列表，每层一个列表
- 生成各层元素的所有笛卡尔积组合
- 可用 names 参数给各层命名
- 是三种创建方式中最推荐的一种

## 边界与易混淆

注意参数外层要再套一层列表，嵌套写错会导致层级错误。

## 关联

- [[分层索引]] — 组合使用
- [[pd.MultiIndex.from_arrays]] — 对比项
- [[pd.MultiIndex.from_tuples]] — 对比项

## 自测

from_product([['a','b'],[1,2]]) 会生成哪些索引组合？::('a',1)、('a',2)、('b',1)、('b',2) 四组。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
