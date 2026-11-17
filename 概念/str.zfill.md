---
term: str.zfill
aliases: [zfill, 零填充]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# str.zfill

> 别名：zfill、零填充

**用字符 0 从左侧把字符串填充到指定宽度的方法。**

## 解释

str.zfill(width) 是 str.pad 的特例：只能用 0 填充，且只能从左侧填充。常用于编号补零对齐。

## 有什么用

- 工号、编号补零到固定位数
- 生成定长数字字符串

## 关键要点

- 只能用 0 填充
- 只能从左侧填充
- 相当于 pad(side='left', fillchar='0')

## 边界与易混淆

不能自定义填充字符或方向；需要其他字符时用 str.pad。

## 关联

- [[str.pad]] — 上位概念
- [[Series.str 访问器]] — 上位概念

## 自测

str.zfill(10) 对“张三”的结果是什么？::左侧补 8 个 0 到 10 位，即“00000000张三”。
zfill 和 pad 的关系是什么？::zfill 是 pad 的特例，固定用 0 从左侧填充。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
