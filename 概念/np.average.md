---
term: np.average
aliases: [average, 加权平均, weights]
kind: method
domain: 计算机/数据分析/Numpy
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 13
stage: "S01E12 · 数学和统计方法"
order: 13
---

# np.average

> 别名：average、加权平均、weights

**按权重计算加权平均，权重通过 weights 参数传入。**

## 解释

np.average 在普通平均基础上引入权重，公式为 Σ(w·x)/Σw。当各数据重要性不同（如不同占比的科目成绩）时，加权平均比算术平均更合理。

## 有什么用

- 计算加权成绩、加权评分
- 不同占比数据的综合平均

## 关键要点

- weights 参数传入各元素权重
- 公式为权重乘积之和除以权重之和
- 不传 weights 时退化为算术平均

## 边界与易混淆

权重之和不必为 1，函数会自动除以权重总和。

## 关联

- [[np.mean]] — 对比项
- [[加权平均]] — 上位概念

## 自测

np.average 不传 weights 时和 np.mean 有什么区别？::结果相同，退化为算术平均。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
