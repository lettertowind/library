---
term: np.cumsum
aliases: [cumsum, 累计和]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 13
stage: "S01E12 · 数学和统计方法"
order: 13
---

# np.cumsum

> 别名：cumsum、累计和

**从首元素开始逐步累加，返回与展平后等长的一维数组。**

## 解释

np.cumsum 返回每一步的累计和，而不是最终总和。二维数组调用时按行优先展平后累计，结果是一维数组，长度等于元素总数。

## 有什么用

- 观察累计增长过程
- 计算累计销售额、累计收益

## 关键要点

- 返回数组长度等于元素总数
- 二维数组按展平顺序累计，结果降为一维
- 首元素为 0 时第一项为 0，后续正常累加

## 边界与易混淆

不要与 np.sum 混淆：cumsum 保留每一步中间结果，sum 只给最终值。

## 关联

- [[np.sum]] — 对比项
- [[np.cumprod]] — 对比项

## 自测

对 3x3 数组调用 np.cumsum 不指定 axis，返回几个元素？::9 个，按行优先展平后逐步累加。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
