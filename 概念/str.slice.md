---
term: str.slice
aliases: [slice, 字符串切片]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# str.slice

> 别名：slice、字符串切片

**按起止范围和步长截取字符串片段的方法。**

## 解释

str.slice(start, stop, step) 类似 Python 切片，从 start 到 stop（不含 stop）截取字符，可设置步长。越界位置显示为空字符，原值为 NaN 的仍为空值。

## 有什么用

- 截取字符串前几位
- 隔位取字符
- 按固定位置提取编码片段

## 关键要点

- stop 位置不包含在结果中
- 支持 step 步长
- 越界显示空字符，不是 NaN
- 空字符与空值要区分

## 边界与易混淆

不支持替换；需要替换切片范围时用 str.slice_replace。

## 关联

- [[str.slice_replace]] — 对比项
- [[str.get]] — 对比项
- [[Numpy 切片]] — 前置知识

## 自测

str.slice(0, 3) 取的是哪几个索引？::索引 0、1、2，共三个字符，不包含 3。
切片越界时结果是什么？::越界位置显示为空字符，原值为 NaN 的仍为空值。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
