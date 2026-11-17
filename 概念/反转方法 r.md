---
term: 反转方法 r
aliases: [radd, rsub, rdiv, rpow, r 前缀方法]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# 反转方法 r

> 别名：radd、rsub、rdiv、rpow、r 前缀方法

**灵活算术方法中带 r 前缀的版本，交换左右操作数顺序。**

## 解释

add 是左加右，radd 是右加左；div 是左除右，rdiv 是右除左。对加法等交换运算无差别，但对减法、除法、幂次方等非交换运算结果不同。

## 有什么用

- 需要反转操作数顺序时
- 非交换运算中调整被除数/减数位置

## 关键要点

- r 表示 reverse，交换左右操作数
- 对加法、乘法等交换运算无实际影响
- 对减法、除法、幂次方结果不同
- 与 fill_value 可组合使用

## 边界与易混淆

不要误以为 r 是取反或取余，它只是交换操作数顺序。

## 关联

- [[灵活算术方法]] — 上位概念
- [[fill_value 参数]] — 组合使用

## 自测

5 rdiv 3 等价于什么？::等价于 3 / 5，即右操作数除以左操作数。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
