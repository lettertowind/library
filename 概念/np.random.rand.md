---
term: np.random.rand
aliases: [random.rand, rand, 随机数数组生成]
kind: method
domain: 计算机/数据分析/Numpy
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# np.random.rand

> 别名：random.rand、rand、随机数数组生成

**按参数个数生成对应维度的 [0,1) 均匀分布随机浮点数组。**

## 解释

np.random.rand 的参数个数决定输出维度：不传参数返回单个随机数，传 1 个返回一维数组，传 2 个返回二维数组，传 3 个返回三维数组。

## 有什么用

- 快速生成随机测试数据
- 初始化权重或模拟数据

## 关键要点

- 参数个数 = 输出维度，参数值 = 各维度长度
- 不传参数返回单个随机浮点数
- np.random.rand(2, 3) 生成 2 行 3 列二维数组
- 结果默认是浮点型，范围 [0, 1)

## 边界与易混淆

与标准库 random 不同，使用 np.random 无需 import random；rand 只生成均匀分布，其他分布需用别的函数。

## 关联

- [[Numpy random 随机函数]] — 上位概念
- [[Numpy 多维数组]] — 组合使用

## 自测

np.random.rand(2, 3, 3) 生成的是什么维度和形状的数组？::三维数组，形状为 (2, 3, 3)，即 2 块 3 行 3 列

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
