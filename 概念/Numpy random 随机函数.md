---
term: Numpy random 随机函数
aliases: [np.random, random 模块, 随机数生成]
kind: tool
domain: 计算机/数据分析/Numpy
tags: [概念/tool, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# Numpy random 随机函数

> 别名：np.random、random 模块、随机数生成

**Numpy 中用于生成随机数、随机抽样和随机排列的函数集合。**

## 解释

np.random 提供生成随机数、随机整数、随机抽样、打乱顺序等功能，常用于模拟数据、初始化参数和随机划分数据集。本节按“了解即可”处理，知道其用途即可。

## 有什么用

- 生成模拟数据
- 随机抽样与打乱数据
- 机器学习参数初始化

## 关键要点

- 属于 Numpy 的随机数子模块 np.random
- 可生成随机数、随机整数、随机抽样、随机排列
- 本节定位为“了解即可”，不要求深入掌握
- 常配合随机种子保证结果可复现

## 边界与易混淆

本节仅作了解性内容，不展开具体函数细节；与 Python 标准库 random 模块不同，注意区分。

## 关联

- [[孙兴华 Python 数据分析三部曲]] — 上位概念

## 自测

np.random 主要解决什么问题？::生成随机数、随机抽样和随机排列，用于模拟数据、初始化参数和随机划分数据集。
Numpy 的 random 与 Python 标准库 random 是同一个东西吗？::不是，np.random 是 Numpy 的子模块，功能更偏向数组化随机运算。


### 补充 · 2026-11-17

np.random 提供多种随机数生成函数，可直接生成任意维度的随机数组，无需再导入标准库 random。本课仅初步了解，后续会专门讲解。

- 使用 np.random 不必再 import random
- 功能强于 Python 标准库 random
- rand 按参数个数决定维度
使用 Numpy 随机数时还需要 import random 吗？::不需要，直接使用 np.random 即可

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
