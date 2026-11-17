---
term: np.any
aliases: [any, 任一为真]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 14
stage: "S01E13 · 条件计算，排序，深潜拷贝【本季完】"
---

# np.any

> 别名：any、任一为真

**判断数组中是否至少存在一个 True，返回单个布尔值。**

## 用法
**语法**：`np.any(a, axis=None, keepdims=False)`
**参数**：
- `a`：输入数组或可转换为数组的对象，通常为布尔数组或条件表达式的结果
- `axis`：归约的轴，默认为 `None` 表示把整个数组归约为一个布尔值；取 `0`、`1` 等时按轴返回布尔数组
- `keepdims`：布尔值，默认为 `False`；为 `True` 时保留被归约的维度（长度为 1）
**示例**：
```python
import numpy as np

a = np.array([[1, 3, 2],
              [6, 5, 4]])

# 条件表达式生成布尔数组，再做存在性判断
print(np.any(a > 5))          # True

# 整个数组是否至少有一个大于 5
print(np.any(a > 9))          # False

# 按列归约：每列是否存在大于 5 的元素
print(np.any(a > 5, axis=0))  # [ True False False]

# 按行归约并保留维度
print(np.any(a > 5, axis=1, keepdims=True))  # [[False]
                                             #  [ True]]
```

## 解释

np.any 对布尔数组做“或”归约：只要有一个 True 就返回 True，全为 False 才返回 False。常用于快速判断“是否存在满足条件的元素”。

## 有什么用

- 判断是否存在满足条件的元素
- 配合条件表达式做存在性检查

## 关键要点

- 至少一个 True 即为 True
- 全部 False 才为 False
- 可传 axis 按轴归约
- 与 np.all 互为对偶

## 边界与易混淆

易与 np.all 混淆：any 是“存在”，all 是“全部”。

## 关联

- [[np.all]] — 对比项
- [[布尔数组]] — 前置知识

## 自测

布尔数组 [False, False, True] 的 np.any 结果是什么？::True，因为存在一个 True。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
