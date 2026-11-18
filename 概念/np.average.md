---
term: np.average
aliases: [average, 加权平均, weights]
kind: method
domain: Numpy
tags: [概念/method, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
order: 13
stage: "S01E12 · 数学和统计方法"
---

# np.average

> 别名：average、加权平均、weights

**按权重计算加权平均，权重通过 weights 参数传入。**

## 用法

**语法**：`np.average(a, axis=None, weights=None, returned=False)`

**参数**：
- `a`：待求平均的数组，也可以是列表
- `axis`：沿指定轴求平均，默认 `None`，即对全部元素求平均
- `weights`：权重数组，形状需与 `a` 一致（指定 `axis` 时可为一维）；不传则退化为算术平均
- `returned`：为 `True` 时返回 `(平均值, 权重之和)` 元组，默认只返回平均值

**示例**：

```python
import numpy as np

scores = np.array([80, 90, 70])
weights = np.array([0.5, 0.3, 0.2])   # 权重之和不必为 1

print(np.average(scores, weights=weights))  # 81.0
print(np.average(scores))                   # 80.0，不传 weights 退化为算术平均
print(np.average(scores, weights=weights, returned=True))  # (81.0, 1.0)
```

## 解释

np.average 在普通平均基础上引入权重，公式为 Σ(w·x)/Σw。当各数据重要性不同（如不同占比的科目成绩）时，加权平均比算术平均更合理。

## 有什么用

- 计算加权成绩、加权评分
- 不同占比数据的综合平均

## 关键要点

- weights 参数传入各元素权重
- 公式为权重乘积之和除以权重之和
- 不传 weights 时退化为算术平均

## 边界与易混淆

权重之和不必为 1，函数会自动除以权重总和。

## 关联

- [[np.mean]] — 对比项
- [[加权平均]] — 上位概念

## 自测

np.average 不传 weights 时和 np.mean 有什么区别？::结果相同，退化为算术平均。


### 补充 · 2026-11-17

与 mean 不同，average 允许每个数值拥有不同权重，真正体现各值在整体中的占比。不传 weights 时退化为普通算术平均，传入后按加权公式计算，二维数组同样适用。

- 公式：x̄_w = Σwᵢxᵢ / Σwᵢ
- 权重是百分比且总和为 1 时，简化为 Σwᵢxᵢ
- 权重大小代表该值的重要程度或占比
加权平均与算术平均的本质区别是什么？::加权平均给每个值不同权重，体现其占比或重要程度；算术平均视所有值同等重要。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p13 S01E12.数学和统计方法](https://www.bilibili.com/video/BV1ji4y157uB?p=13) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
