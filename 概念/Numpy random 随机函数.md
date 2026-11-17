---
term: Numpy random 随机函数
aliases: [np.random, random 模块, 随机数生成]
kind: tool
domain: 数据分析/Numpy
tags: [概念/tool, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 11
stage: "S01E10 · random随机函数"
---

# Numpy random 随机函数

> 别名：np.random、random 模块、随机数生成

**Numpy 中用于生成随机数、随机抽样和随机排列的函数集合。**

## 用法

**语法**：`np.random.函数名(参数)`（`np.random` 是子模块，要先 `import numpy as np`）

**参数**：
- `size`：输出形状，整数或元组，如 `size=(2, 3)` 生成 2 行 3 列
- `low` / `high`：随机整数的范围，左闭右开，如 `randint(1, 10)` 生成 1–9
- `seed`：随机种子，用 `np.random.seed(42)` 固定，保证每次运行结果相同

**示例**：
```python
import numpy as np

np.random.seed(42)                    # 固定种子，结果可复现
print(np.random.rand(3))              # [0.37454012 0.95071431 0.73199394] 0–1 随机小数
print(np.random.randint(1, 10, 3))    # [7 4 8] 1–9 的随机整数
print(np.random.rand(2, 3))           # 2 行 3 列的随机矩阵
```

## 解释

np.random 提供生成随机数、随机整数、随机抽样、打乱顺序等功能，常用于模拟数据、初始化参数和随机划分数据集。本节按“了解即可”处理，知道其用途即可。

## 有什么用

- 生成模拟数据
- 随机抽样与打乱数据
- 机器学习参数初始化

## 关键要点

- 属于 Numpy 的随机数子模块 np.random
- 可生成随机数、随机整数、随机抽样、随机排列
- 本节定位为“了解即可”，不要求深入掌握
- 常配合随机种子保证结果可复现

## 边界与易混淆

本节仅作了解性内容，不展开具体函数细节；与 Python 标准库 random 模块不同，注意区分。

## 关联

- [[孙兴华 Python 数据分析三部曲]] — 上位概念

## 自测

np.random 主要解决什么问题？::生成随机数、随机抽样和随机排列，用于模拟数据、初始化参数和随机划分数据集。
Numpy 的 random 与 Python 标准库 random 是同一个东西吗？::不是，np.random 是 Numpy 的子模块，功能更偏向数组化随机运算。


### 补充 · 2026-11-17

np.random 提供多种随机数生成函数，可直接生成任意维度的随机数组，无需再导入标准库 random。本课仅初步了解，后续会专门讲解。

- 使用 np.random 不必再 import random
- 功能强于 Python 标准库 random
- rand 按参数个数决定维度
使用 Numpy 随机数时还需要 import random 吗？::不需要，直接使用 np.random 即可

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
