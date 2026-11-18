---
term: pd.MultiIndex.from_arrays
aliases: [from_arrays, 数组创建 MultiIndex]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 35
stage: "S01E03 · 创建数组"
---

# pd.MultiIndex.from_arrays

> 别名：from_arrays、数组创建 MultiIndex

**用多个数组按位置对应创建多层索引的方法。**


## 用法
**语法**：`pd.MultiIndex.from_arrays(arrays, sortorder=None, names=None)`
**参数**：
- `arrays`：一组数组，每个数组代表一层索引，按位置一一对应组合，各数组长度必须相同
- `sortorder`：可选整数，指定按哪一层排序，一般保持默认 `None`
- `names`：列表，为各层索引命名，长度需与层数一致；构造多层列索引时常配合 `df.columns = ...` 使用
**示例**：
```python
import pandas as pd

l1 = ["一季度"] * 3 + ["二季度"] * 2
l2 = ["1月", "2月", "3月", "4月", "5月"]
mi = pd.MultiIndex.from_arrays([l1, l2], names=["季度", "月份"])
print(mi.tolist())
# [('一季度', '1月'), ('一季度', '2月'), ('一季度', '3月'), ('二季度', '4月'), ('二季度', '5月')]
print(mi.names)
# ['季度', '月份']
```
> 一层对应 3 个月、另一层对应 2 个月，数量不等，只能用「按位置对应」的 `from_arrays`（或 `from_tuples`），不能用生成笛卡尔积的 `from_product`。

## 解释

from_arrays 接收一组数组，每个数组代表一层索引，按位置组合成多层索引。它适合已有分层数组数据的场景，但不如 from_product 直观。

## 有什么用

- 从已有分层数组创建 MultiIndex
- 按位置对应构造多层索引

## 关键要点

- 每个数组代表一层索引
- 各层按位置一一对应组合
- 可用 names 给各层命名

## 边界与易混淆

各层数组长度必须一致，否则无法按位置组合。

## 关联

- [[分层索引]] — 组合使用
- [[pd.MultiIndex.from_product]] — 对比项

## 自测

from_arrays 和 from_product 的主要区别是什么？::from_arrays 按位置对应组合已有数组，from_product 生成各层元素的所有笛卡尔积组合。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
