---
term: np.all
aliases: [all, 全部为真]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 14
stage: "S01E13 · 条件计算，排序，深潜拷贝【本季完】"
order: 14
---

# np.all

> 别名：all、全部为真

**判断数组中是否所有元素都为 True，返回单个布尔值。**

## 解释

np.all 对布尔数组做“与”归约：全部为 True 才返回 True，只要有一个 False 就返回 False。常用于校验“是否全部满足条件”。

## 有什么用

- 校验是否所有元素都满足条件
- 配合条件表达式做全称检查

## 关键要点

- 全部 True 才为 True
- 任一 False 即为 False
- 可传 axis 按轴归约
- 与 np.any 互为对偶

## 边界与易混淆

空数组上 np.all 返回 True，容易反直觉。

## 关联

- [[np.any]] — 对比项
- [[布尔数组]] — 前置知识

## 自测

布尔数组 [True, False, True] 的 np.all 结果是什么？::False，因为存在 False。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
