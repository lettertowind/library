---
term: margins 参数
aliases: [margins, 小计总计参数]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 43
stage: "S02E28 · 数据透视表"
order: 43
---

# margins 参数

> 别名：margins、小计总计参数

**pivot_table/crosstab 中控制是否添加行列小计总计的参数。**

## 解释

margins 默认 False，设为 True 后在行和列方向增加小计与总计。关键点是小计方式跟随 aggfunc：求和时小计是求和，平均时小计是平均，计数时小计是计数，不能简单理解为固定求和。

## 有什么用

- 透视表/交叉表需要行列合计时
- 报表中展示分组小计

## 关键要点

- 默认 False，不显示小计
- 设为 True 增加行列小计总计
- 小计方式跟随 aggfunc，不是固定求和
- pivot_table 和 crosstab 都支持

## 边界与易混淆

易错点：误以为 margins 永远是对行列求和。

## 关联

- [[pivot_table]] — 组合使用
- [[crosstab]] — 组合使用
- [[aggfunc 参数]] — 组合使用

## 自测

aggfunc='mean' 且 margins=True 时，小计行是什么值？::按平均聚合得到的小计，不是求和。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
