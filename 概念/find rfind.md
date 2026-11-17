---
term: find rfind
aliases: [str.find, str.rfind, 查找字符位置]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 39
stage: "S02E24 · 字符串操作（下）"
order: 39
---

# find rfind

> 别名：str.find、str.rfind、查找字符位置

**返回子串首次出现位置的字符串方法，找不到返回 -1。**

## 解释

find 从左往右查找，rfind 从右往左查找，均可指定起始和结束位置。找不到时返回 -1 而不报错，适合需要容错判断的场景。

## 有什么用

- 定位日期中横杠的位置
- 判断子串是否存在

## 关键要点

- 索引从 0 开始
- 可指定起始/结束位置控制查找范围
- 找不到返回 -1，不报错
- rfind 从右往左找

## 边界与易混淆

与 index/rindex 区别：后者找不到会抛异常。

## 关联

- [[index rindex]] — 对比项
- [[Series.str 访问器]] — 上位概念

## 自测

'2020-05-01' 中 str.find('-', 5) 返回什么？::返回 7，即第二个横杠的位置。
find 找不到目标时返回什么？::返回 -1。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
