---
term: round（舍入）
aliases: [round, round(), ndigits, 四舍五入]
kind: method
domain: 计算机/编程/Python
tags: [概念/method, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# round（舍入）

> 别名：round、round()、ndigits、四舍五入

**按指定小数位数对数字舍入，位数可为正、零或负。**

## 解释

round(x, ndigits) 中 ndigits 控制保留几位：正数保留小数位，0 取整，负数则对整数部分（十位、百位）舍入。不传 ndigits 时返回整数。

## 有什么用

- 结果保留小数位
- 把数字粗粒度取整到十位百位

## 关键要点

- round(1.23456, 3) 约为 1.235
- round(49, -1) 返回 50，负位数舍入到十位
- round 采用银行家舍入，0.5 不一定进位

## 边界与易混淆

浮点精度会让结果看似“四舍五入不准”；需要精确十进制舍入应用 decimal 模块。

## 关联

- [[地板除与取余（ 与 %）]] — 对比项

## 自测

round(12345, -3) 得到什么，为什么？::12000；负数 ndigits 表示对千位做舍入。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
