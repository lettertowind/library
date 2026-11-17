---
term: index rindex
aliases: [str.index, str.rindex]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 39
stage: "S02E24 · 字符串操作（下）"
order: 39
---

# index rindex

> 别名：str.index、str.rindex

**与 find 类似但找不到目标时会抛出异常的查找方法。**

## 解释

index 从左往右、rindex 从右往左查找子串位置。与 find 的唯一关键差异是找不到时报错而非返回 -1，适合'必须存在'的断言场景。

## 有什么用

- 确定子串一定存在时定位位置
- 需要失败即报错的校验

## 关键要点

- index 从左往右，rindex 从右往左
- 找不到时抛异常
- 与 find/rfind 形成容错与严格的对比

## 边界与易混淆

数据脏、可能缺失时用 find 更安全。

## 关联

- [[find rfind]] — 对比项

## 自测

什么场景下应优先用 index 而不是 find？::当子串必须存在、希望缺失时立即报错暴露问题时。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
