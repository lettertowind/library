---
term: np.argmax np.argmin
aliases: [argmax, argmin, 最大值下标, 最小值下标]
kind: method
domain: 计算机/数据分析/Numpy
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# np.argmax np.argmin

> 别名：argmax、argmin、最大值下标、最小值下标

**返回最大值或最小值所在的位置下标，而非数值本身。**

## 解释

argmax/argmin 解决“最大值在哪”的问题。二维数组不指定 axis 时返回展平后的下标，与行优先遍历顺序有关；指定 axis 则返回沿该轴的下标数组。

## 有什么用

- 定位极值位置
- 找销量最高的商品序号

## 关键要点

- 返回的是下标不是值
- 二维数组默认返回展平后的下标
- 展平顺序为行优先，下标与行列需换算
- 可配合 axis 按行或按列找极值位置

## 边界与易混淆

二维数组直接取到的下标是一维展平下标，不能直接当行列坐标用。

## 关联

- [[np.max np.min]] — 组合使用
- [[np.bincount]] — 组合使用

## 自测

3x3 数组最大值在第 2 行第 1 列，np.argmax 返回什么？::返回展平下标 3（行优先：0,1,2 为第一行，3 为第二行第一列）。
argmax 和 max 的区别是什么？::max 返回值，argmax 返回该值所在的下标。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
