---
term: insert 方法
aliases: [DataFrame.insert, 指定位置插入列]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 44
stage: "S02E29 · vlookup"
order: 44
---

# insert 方法

> 别名：DataFrame.insert、指定位置插入列

**在 DataFrame 指定列位置插入一列，原地修改不返回新表。**

## 解释

insert(loc, column, value) 把一列插到第 loc 个列位置，原有列依次右移。它是原地操作，返回值是 None，不能写成 df = df.insert(...)。

## 有什么用

- 调整列顺序，把某列移到指定位置
- 在固定位置补充新字段

## 关键要点

- loc 是列位置整数，0 表示最前面
- 原地修改，不要赋值接收返回值
- 常与「取出列→drop 原列→insert」配合实现列移动
- 插入列名不能与已有列重名，否则报错

## 边界与易混淆

insert 只能插列不能插行；插行需用 concat 或 loc 赋值。

## 关联

- [[drop]] — 组合使用
- [[DataFrame]] — 上位概念

## 自测

把总分列插到第二列位置，loc 应传几？::1（0 基位置，第二列即索引 1）。
写 结果 = 结果.insert(0,'总分',s) 会有什么问题？::insert 原地修改且返回 None，结果变量会被赋成 None，原表其实已改好但变量丢了。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
