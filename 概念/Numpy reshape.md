---
term: Numpy reshape
aliases: [reshape, np.arange().reshape, 改变数组形状]
kind: method
domain: 计算机/数据分析/Numpy
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 5
stage: "S01E04 · 多维数组"
order: 5
---

# Numpy reshape

> 别名：reshape、np.arange().reshape、改变数组形状

**在不改变数据的前提下把数组重排为指定形状。**

## 解释

reshape 按行优先把一维数据填充成指定的行列结构，常用于把 arange 生成的一串数变成二维数组来做索引练习。元素总数必须与目标形状匹配。

## 有什么用

- 把一维序列转成二维矩阵
- 构造练习或演示用的多维数组

## 关键要点

- 元素总数必须等于目标形状各维乘积
- 默认按行优先（C 顺序）填充
- np.arange(36).reshape(9,4) 得到 9 行 4 列

## 边界与易混淆

形状不匹配会报错；reshape 返回视图或副本取决于内存布局，不要假设一定是原数组。

## 关联

- [[Numpy 二维数组]] — 组合使用
- [[Numpy 索引]] — 前置知识

## 自测

np.arange(36).reshape(9,4) 得到几行几列？第 4 行是什么？::9 行 4 列；第 4 行是 [16,17,18,19]。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
