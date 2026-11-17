---
term: SWITCH 函数
aliases: [SWITCH, Excel SWITCH, DAX SWITCH]
kind: method
domain: 数据分析/Excel
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# SWITCH 函数

> 别名：SWITCH、Excel SWITCH、DAX SWITCH

**Excel/DAX 中按多个分支条件返回不同结果的判断函数。**

## 解释

SWITCH 依次拿表达式去匹配若干候选值，命中哪个就返回对应结果，可带一个默认值兜底，本质是多分支 if。在报表里常用来按分数段、年龄段、等级给数据打标签。Pandas 的 cut 能一次性批量完成同类工作，因此课程把它当作 cut 的对照物。

## 有什么用

- Excel/DAX 报表中做多条件分类打标
- 按区间给数值字段生成文字标签

## 关键要点

- 结构为 SWITCH(表达式, 值1, 结果1, …, 默认值)
- 多分支判断，比多层嵌套 IF 更易读
- 条件需逐个列举，区间分箱写起来冗长
- Pandas 用 cut + labels 可批量替代该场景

## 边界与易混淆

SWITCH 擅长少量离散取值映射，连续数值按区间分箱时条件要一个个写，不如 cut/qcut 直接传边界或箱数。

## 关联

- [[pd.cut]] — 对比项
- [[离散化与分箱]] — 组合使用

## 自测

同样是按分数段打标签，SWITCH 和 cut 在使用方式上的根本差别是什么？::cut 只需传入一个分界点列表就能对整列数据批量打标签；SWITCH 要把每个分支条件逐条写出来。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p37 S02E22.离散化和分箱](https://www.bilibili.com/video/BV1ji4y157uB?p=37) · 2026-11-17
