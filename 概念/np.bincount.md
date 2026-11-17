---
term: np.bincount
aliases: [bincount, 频次统计]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 13
stage: "S01E12 · 数学和统计方法"
---

# np.bincount

> 别名：bincount、频次统计

**统计非负整数数组中每个值出现的次数。**

## 用法
**语法**：`np.bincount(x, weights=None, minlength=0)`
**参数**：
- `x`：一维、非负整数数组，元素值即频次数组的下标
- `weights`：可选，与 `x` 等长的权重数组；给出时按下标累加权重而非计数
- `minlength`：可选，指定输出数组的最小长度，默认 0（即 `max(x)+1`）
**示例**：
```python
import numpy as np

a = np.array([1, 2, 3, 3, 3, 4, 5, 6])
counts = np.bincount(a)
print(counts)                        # [0 1 1 3 1 1 1]
print(np.argmax(counts))             # 3
print(np.bincount(a, minlength=10))  # [0 1 1 3 1 1 1 0 0 0]
```

## 解释

np.bincount 返回长度为 max+1 的频次数组，下标即原值。配合 np.argmax 可求众数，但只能处理非负整数，不能直接用于浮点数或二维数组。

## 有什么用

- 统计整数频次
- 配合 argmax 求一维众数

## 关键要点

- 只接受非负整数
- 返回数组下标对应原值，值为出现次数
- 配合 np.argmax 可找众数

## 边界与易混淆

浮点数和二维数组不能直接使用，众数建议改用 Pandas。

## 关联

- [[众数]] — 组合使用
- [[np.argmax np.argmin]] — 组合使用

## 自测

为什么 np.bincount 不能直接统计浮点数组？::它用值作为下标索引频次数组，浮点数无法作为下标。


### 补充 · 2026-11-17

返回数组的下标就是被统计的整数，值是该整数出现的次数。常与 argmax 组合求众数：谁的出现次数最多，它的下标就是众数。但它只能处理非负整数，也不能直接作用于二维数组。

- 返回数组下标即原数值，元素值为出现次数
- 求众数写法：np.bincount(arr).argmax()
- 只支持非负整数，不能统计浮点数
np.bincount([1,3,3,7]) 返回什么？::返回 [0,1,0,2,0,0,0,1]：下标 1、3、7 分别出现 1、2、1 次，下标 0 因无数据计 0。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p13 S01E12.数学和统计方法](https://www.bilibili.com/video/BV1ji4y157uB?p=13) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
