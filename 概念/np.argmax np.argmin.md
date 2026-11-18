---
term: np.argmax np.argmin
aliases: [argmax, argmin, 最大值下标, 最小值下标]
kind: method
domain: Numpy
tags: [概念/method, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
order: 13
stage: "S01E12 · 数学和统计方法"
---

# np.argmax np.argmin

> 别名：argmax、argmin、最大值下标、最小值下标

**返回最大值或最小值所在的位置下标，而非数值本身。**

## 用法
**语法**：`np.argmax(a, axis=None)` / `np.argmin(a, axis=None)`
**参数**：
- `a`：输入数组，可以是列表或多维数组
- `axis`：沿哪个轴查找极值下标；不写（默认 `None`）时把数组展平，返回行优先遍历下的一维下标；`axis=0` 按列找、`axis=1` 按行找，返回下标数组
**示例**：
```python
import numpy as np

a = np.array([[3, 9, 1],
              [8, 2, 5]])
print(np.argmax(a))          # 1  —— 展平后 [3,9,1,8,2,5] 的最大值 9 在下标 1
print(np.argmin(a))          # 2  —— 最小值 1 在下标 2
print(np.argmax(a, axis=0))  # [1 0 1] —— 每列最大值所在的行号
print(np.argmax(a, axis=1))  # [1 0]   —— 每行最大值所在的列号

b = np.array([4, 7, 7, 2])
print(np.argmax(b))          # 1  —— 有并列最大值时返回第一次出现的位置
```

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


### 补充 · 2026-11-17

max()/min() 给你的是最值本身，argmax()/argmin() 给你的是最值的位置。下标从 0 开始；对二维数组不指定 axis 时，返回的是按展平顺序算出的位置，而不是行列坐标。

- max()/min() 返回最值本身，argmax()/argmin() 返回位置
- 下标从 0 开始计数
- 二维不带 axis：返回展平后的下标，不是 (行, 列)
二维数组 argmax 返回 3，说明最大值在哪？::在展平后第 4 个元素，即第 2 行第 1 列，而不是行 3 列 0。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p13 S01E12.数学和统计方法](https://www.bilibili.com/video/BV1ji4y157uB?p=13) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
