---
term: np.full_like
aliases: [full_like, 按形状填充指定值]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 5
stage: "S01E04 · 多维数组"
order: 5
---

# np.full_like

> 别名：full_like、按形状填充指定值

**根据已有数组的形状创建新数组，并全部填充为指定值。**

## 解释

full_like 结合了「复用形状」和「自定义填充值」：第一个参数是参照数组，第二个参数是要填充的数值。

## 有什么用

- 需要与现有数组同形状、同填充值的数组时
- 批量生成常量矩阵

## 关键要点

- 语法：np.full_like(a, 520)，第二个参数必填
- 形状与 a 相同，元素全为填充值
- 不修改原数组
- 易错：漏写第二个参数或漏写 np 前缀

## 边界与易混淆

与 np.full 的区别：full 手动传形状元组，full_like 复用已有数组形状。

## 关联

- [[np.full]] — 对比项
- [[np.ones_like]] — 组合使用

## 自测

np.full_like(a, 520) 中两个参数分别是什么含义？::第一个是参照形状的数组 a，第二个是要填充的数值 520

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
