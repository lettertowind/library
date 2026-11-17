---
term: np.prod
aliases: [prod, 求积]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 13
stage: "S01E12 · 数学和统计方法"
---

# np.prod

> 别名：prod、求积

**对数组所有元素求乘积，可指定 axis。**

## 用法
**语法**：`np.prod(a, axis=None)`

**参数**：
- `a`：输入数组或类似数组的对象
- `axis`：沿哪个轴求积；不指定时计算全部元素的乘积，二维数组中 `axis=0` 按列求积、`axis=1` 按行求积

**示例**：
```python
import numpy as np

a = np.array([1, 2, 3, 4, 3, 5, 3, 6])
print(np.prod(a))          # 6480

b = np.array([[1, 2], [3, 4]])
print(np.prod(b))          # 24
print(np.prod(b, axis=0))  # [3 8]（按列求积）
print(np.prod(b, axis=1))  # [2 12]（按行求积）

print(np.prod([1, 2, 0, 4]))  # 0，含 0 则结果为 0
```

## 解释

np.prod 把元素逐个相乘，不指定 axis 时返回全部元素的乘积。与 sum 结构对称，但乘积对 0 敏感，任一元素为 0 结果即为 0。

## 有什么用

- 计算连乘积、概率连乘
- 按轴求积

## 关键要点

- 不指定 axis 时返回全局乘积
- 任一元素为 0 则全局结果为 0
- 支持 axis 参数按行或按列求积

## 边界与易混淆

元素多且值大时容易溢出，实际业务中较少直接对整表求积。

## 关联

- [[np.sum]] — 对比项
- [[np.cumprod]] — 对比项

## 自测

数组 [1,2,0,4] 的 np.prod 结果是多少？为什么？::0，因为乘积中包含 0。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
