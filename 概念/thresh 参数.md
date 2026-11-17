---
term: thresh 参数
aliases: [thresh, 非缺失值阈值, dropna thresh]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 31
stage: "S02E16 · 处理缺失值"
---

# thresh 参数

> 别名：thresh、非缺失值阈值、dropna thresh

**dropna 中规定行/列至少保留多少个非缺失值才不被删除。**

## 解释

thresh=n 表示非缺失值数量少于 n 的行或列会被删除，达到 n 的保留。它按非空值计数，而不是按空值计数，这是最容易说反的地方。

## 有什么用

- 按数据完整度筛选行列
- 剔除缺失过多的样本

## 关键要点

- thresh 计的是非缺失值数量
- 少于 thresh 才删除，等于或大于则保留
- 与 how 是两种不同的删除条件
- 实际使用频率不高

## 边界与易混淆

易与 how='all' 混淆：how 看是否全空，thresh 看非空个数。

## 关联

- [[dropna 参数（透视表）]] — 上位概念
- [[how 参数]] — 对比项

## 自测

dropna(thresh=3) 会删除什么样的行？::非缺失值少于 3 个的行。
thresh 统计的是空值还是非空值？::非空值（非缺失值）。


### 补充 · 2026-11-17

dropna 中要求行或列至少保留多少个非空值，否则删除。

- 判断依据是非空值数量，不是空值数量
- thresh=2 表示至少要保留 2 个非空值
- 常与 axis 组合，可对列做同样的阈值判断
- 使用频率低于 how 和 subset，知道含义即可
## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
