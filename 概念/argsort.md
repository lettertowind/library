---
term: argsort
aliases: [np.argsort, 排序后下标]
kind: method
domain: 数据分析/Numpy
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 14
stage: "S01E13 · 条件计算，排序，深潜拷贝【本季完】"
---

# argsort

> 别名：np.argsort、排序后下标

**返回将数组升序排列后各元素对应的原始下标。**

## 用法
**语法**：`np.argsort(a, axis=-1)`

**参数**：
- `a`：要排序的数组（array_like）
- `axis`：沿哪个轴排序，默认 `-1`，对于一维数组就是唯一的那一维；二维数组常用 `axis=0`（按列方向）或 `axis=1`（按行方向）

**示例**：
```python
import numpy as np

a = np.array([59, 29, 39])
idx = np.argsort(a)
print(idx)              # [1 2 0]：升序排列对应的原始下标
print(a[idx])           # [29 39 59]：用下标回原数组取值，得到升序结果

arr = np.array([85, 42, 91, 7, 67, 89])
top_idx = arr.argsort()[-3:]   # 末尾 3 个下标即最大的 3 个元素
print(top_idx)          # [5 2 4]
print(arr[top_idx])     # [89 91 67] -> 排序后为 [67 89 91]

print(a[np.argsort(-a)])       # [59 39 29]：取负数实现降序
print(a[np.argsort(a)[::-1]])  # [59 39 29]：把下标反转，同样得到降序
```

## 解释

argsort 不返回排序后的值，而是返回“排序后的下标数组”。拿到下标后可以用神奇索引回到原数组取值，因此常用来取最大/最小的前 n 个元素。

## 有什么用

- 获取排序后的下标顺序
- 配合 [-n:] 与神奇索引取前 n 个最大/最小值

## 关键要点

- 返回的是下标，不是排序后的值
- 默认升序排列
- 最大值对应返回下标数组的末尾
- 配合 [-n:] 截取前 n 个最大值的下标

## 边界与易混淆

默认升序；要降序需额外处理（如 [::-1]），不要误以为它直接返回值。

## 关联

- [[神奇索引]] — 组合使用
- [[Numpy 索引]] — 前置知识
- [[负索引]] — 组合使用

## 自测

arr.argsort() 返回的是什么？::把 arr 升序排列后，各元素在原数组中的下标组成的数组。
如何用 argsort 取出 arr 中最大的 3 个元素？::idx = arr.argsort(); arr[idx[-3:]]


### 补充 · 2026-11-17

np.argsort 给出“排序后各位置对应原数组的哪个下标”。用这个索引去取原数组，就得到排序结果；它保留了元素与原位置的对应关系。

- 返回索引而非值
- a[np.argsort(a)] 得到升序数组
- 降序可用 np.argsort(-a) 或索引反转
a=[59,29,39]，np.argsort(a) 返回什么？::[1,2,0]，即升序排列对应的原索引。
如何用 argsort 实现降序取值？::a[np.argsort(-a)] 或 a[np.argsort(a)[::-1]]。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
