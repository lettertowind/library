---
term: np.mean
aliases: [mean, 平均数, 算术平均]
kind: method
domain: Numpy
tags: [概念/method, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
order: 13
stage: "S01E12 · 数学和统计方法"
---

# np.mean

> 别名：mean、平均数、算术平均

**计算算术平均数，即总和除以元素个数。**

## 用法
**语法**：`np.mean(a, axis=None, dtype=None, keepdims=False)`

**参数**：
- `a`：待计算的数组或可转换为数组的序列
- `axis`：沿哪个轴求均值；`None`（默认）表示对整个数组求均值，`0` 表示按列求均值，`1` 表示按行求均值
- `dtype`：计算时使用的数据类型，默认沿用输入数组的类型
- `keepdims`：是否保留被约简的维度，默认 `False` 表示不保留

**示例**：
```python
import numpy as np

a = np.array([1, 2, 3, 3, 3, 4, 5, 6])
print(np.mean(a))            # 3.375

b = np.array([[1, 2], [3, 4]])
print(np.mean(b))            # 2.5
print(np.mean(b, axis=0))    # [2. 3.]
print(np.mean(b, axis=1))    # [1.5 3.5]
```

## 解释

np.mean 是最常用的集中趋势指标，但对极端值敏感。视频强调不能所有场景都直接求平均数，要结合中位数、众数、加权平均选择。

## 有什么用

- 计算平均分、平均销售额
- 按轴求均值

## 关键要点

- 等于 sum 除以元素个数
- 受极端值影响大
- 支持 axis 参数按行或按列求均值

## 边界与易混淆

收入、房价等分布不均的数据，平均数容易失真，应参考中位数。

## 关联

- [[np.median]] — 对比项
- [[np.average]] — 对比项
- [[中位数]] — 对比项

## 自测

为什么收入数据只看平均数可能误导？::少数极高收入会把平均数拉高，不能代表多数人的中间水平。


### 补充 · 2026-11-17

np.mean 对一组数值求和后除以个数，是计算平均线 y 值的标准方法。相比手工求和，它能直接作用于数组或 DataFrame 列，减少出错。

- 给平均线提供 y 值：np.mean(销售量)
- 避免手工求和再除以 n
- 可对 DataFrame 列 data['销售量'] 直接求均值
要用 DataFrame 的“销售量”列计算平均线位置，怎么写？::np.mean(data['销售量'])
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p57 S03E09.平均线](https://www.bilibili.com/video/BV1ji4y157uB?p=57) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
