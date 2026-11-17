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
---

# np.cumsum

> 别名：cumsum、累计和

**从首元素开始逐步累加，返回与展平后等长的一维数组。**

## 用法
**语法**：`np.cumsum(a, axis=None, dtype=None)`
**参数**：
- `a`：输入数组，可为列表或 ndarray
- `axis`：累计方向；`None`（默认）表示先按行优先把数组展平成一维再累计，返回一维数组；对二维数组传 `0` 沿列累计、传 `1` 沿行累计
- `dtype`：指定输出元素的数据类型，默认与输入一致

**示例**：
```python
import numpy as np

a = np.array([1, 2, 3, 4])
print(np.cumsum(a))
# [ 1  3  6 10]

b = np.array([[1, 2, 3],
              [4, 5, 6]])
print(np.cumsum(b))        # 展平后累计，长度 6
# [ 1  3  6 10 15 21]
print(np.cumsum(b, axis=1))  # 沿行累计，shape 不变
# [[ 1  3  6]
#  [ 4  9 15]]
```

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


### 补充 · 2026-11-17

每一项等于原数组从头到当前位置所有元素之和，常用来观察累计增长过程。二维数组不指定 axis 时按展平顺序累加，返回的是一维数组而不是二维数组。

- 一维：返回与输入等长的数组，每项是前缀和
- 二维不带 axis：按展平顺序（先行后列）累加，返回一维数组
- 最后一个元素等于整个数组的总和
二维数组 cumsum() 的结果为什么长度是有元素总数的一维数组？::因为默认不带 axis，按展平顺序全局累加，原二维结构被打平。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p13 S01E12.数学和统计方法](https://www.bilibili.com/video/BV1ji4y157uB?p=13) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
