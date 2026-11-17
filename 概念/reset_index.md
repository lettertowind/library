---
term: reset_index
aliases: [df.reset_index, 重置索引]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 21
stage: "S02E06 · 数据结构之DataFrame"
order: 21
---

# reset_index

> 别名：df.reset_index、重置索引

**将 DataFrame 索引重置为默认 0,1,2… 的方法。**

## 解释

reset_index() 生成新的默认整数索引，关键参数 drop 决定原索引的去留：drop=True 直接丢弃原索引，drop=False 把原索引降为普通列保留下来。

## 有什么用

- 索引混乱时恢复默认序号
- 把原索引当普通列保留分析

## 关键要点

- drop=True：删除原索引
- drop=False：原索引转为普通列
- 默认 drop=False
- 常与 set_index 配对使用

## 边界与易混淆

drop=False 会多出一列，可能影响后续列数统计；与 set_index 方向相反，勿混。

## 关联

- [[set_index]] — 对比项
- [[DataFrame]] — 上位概念

## 自测

reset_index(drop=True) 和 drop=False 的结果差在哪？::drop=True 丢弃原索引只留新默认索引；drop=False 把原索引保留为普通列。
什么情况下你会选 drop=False？::当原索引本身有信息价值、需要作为一列继续参与分析时。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
