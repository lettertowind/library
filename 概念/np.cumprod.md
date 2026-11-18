---
term: np.cumprod
aliases: [cumprod, 累计积]
kind: method
domain: Numpy
tags: [概念/method, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
order: 13
stage: "S01E12 · 数学和统计方法"
---

# np.cumprod

> 别名：cumprod、累计积

**从首元素开始逐步累乘，返回展平后等长的一维数组。**

## 用法
**语法**：`np.cumprod(a, axis=None, dtype=None)`

**参数**：
- `a`：输入数组，可以是列表或 ndarray，元素按数组的存储顺序依次参与连乘
- `axis`：沿哪个轴累乘；默认为 `None`，此时先展平数组，再按展平顺序累乘，返回一维数组
- `dtype`：指定返回数组的数据类型，默认沿用 `a` 的 dtype

**示例**：
```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(np.cumprod(a))            # [  1   2   6  24 120]

b = np.array([[1, 2], [3, 4]])
print(np.cumprod(b))            # [ 1  2  6 24]，二维按展平顺序累乘
print(np.cumprod(b, axis=0))    # [[1 2]
                                #  [3 8]]，沿行方向逐列累乘

print(np.cumprod(np.array([0, 2, 3])))  # [0 0 0]，首项为 0 则后续全为 0
```

## 解释

np.cumprod 与 cumsum 对称，返回每一步的累计乘积。首项若为 0，后续所有累计积都为 0，因此演示时首项不能设为 0。

## 有什么用

- 计算复利式累计增长
- 观察连乘过程

## 关键要点

- 返回长度等于元素总数的一维数组
- 首项为 0 会导致后续全部为 0
- 二维数组按展平顺序累乘

## 边界与易混淆

数值增长极快，容易溢出，业务中使用场景有限。

## 关联

- [[np.cumsum]] — 对比项
- [[np.prod]] — 对比项

## 自测

为什么演示 cumprod 时数组首项不能设为 0？::因为 0 乘任何数都是 0，后续累计积会全部变成 0。


### 补充 · 2026-11-17

与 cumsum 一一对应，只是把加法换成乘法。使用时要注意首元素不能是 0，否则后续所有累积积都会变成 0；二维数组默认同样按展平顺序计算并返回一维结果。

- 一维：每项为前缀乘积，最后一项等于全部元素之积
- 首元素不能为 0，否则后面全部被乘成 0
- 建议首元素设为 1，保证累积有意义
为什么做累积积时首元素不能设成 0？::0 乘以任何数都是 0，之后所有累积积都会变成 0，失去意义。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p13 S01E12.数学和统计方法](https://www.bilibili.com/video/BV1ji4y157uB?p=13) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
