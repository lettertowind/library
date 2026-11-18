---
term: pd.MultiIndex.from_product
aliases: [from_product, 笛卡尔积创建 MultiIndex]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 35
stage: "S02E20 · 多层索引与多层索引计算"
---

# pd.MultiIndex.from_product

> 别名：from_product、笛卡尔积创建 MultiIndex

**用多个一维列表的笛卡尔积创建多层索引的方法。**


## 用法

**语法**：`pd.MultiIndex.from_product(iterables, sortorder=None, names=None)`

**参数**：
- `iterables`：列表的列表，每层一个可迭代对象，元素做笛卡尔积
- `names`：列表，给各层索引起名，长度需与层数一致
- `sortorder`：整数，指定索引排序层级，一般不用

**示例**：
```python
import pandas as pd

mi = pd.MultiIndex.from_product([["a", "b"], [1, 2]], names=["x", "y"])
print(mi)
# MultiIndex([('a', 1), ('a', 2), ('b', 1), ('b', 2)], names=['x', 'y'])

s = pd.Series([10, 20, 30, 40], index=mi)
print(s)
# x  y
# a  1    10
#    2    20
# b  1    30
#    2    40
# dtype: int64
```

## 解释

from_product 接收一个列表的列表，生成各层元素的所有组合，是创建 MultiIndex 最推荐的方式。它适合层级取值需要两两组合的场景，如年份×月份、类别×品名。

## 有什么用

- 创建行或列的多层索引
- 构造总计结果的多层列索引

## 关键要点

- 参数是列表的列表，每层一个列表
- 生成各层元素的所有笛卡尔积组合
- 可用 names 参数给各层命名
- 是三种创建方式中最推荐的一种

## 边界与易混淆

注意参数外层要再套一层列表，嵌套写错会导致层级错误。

## 关联

- [[分层索引]] — 组合使用
- [[pd.MultiIndex.from_arrays]] — 对比项
- [[pd.MultiIndex.from_tuples]] — 对比项

## 自测

from_product([['a','b'],[1,2]]) 会生成哪些索引组合？::('a',1)、('a',2)、('b',1)、('b',2) 四组。


### 补充 · 2026-11-17

传入列表的列表，pandas 取各层的所有取值两两组合，生成完整的多层索引。它也常用于「给已有结构加一层外壳」：把单元素列表作为外层，就能把现有列整体挂到「合计」之下。

- 各层取值的数量相乘，等于生成索引的总长度
- 外层写成 ["合计"] 这样的列表，才能正确形成一层
- 外层不用列表包起来，层级结构会写错
要把现有单层列索引整体挂到「合计」这一层下面，怎么构造？::pd.MultiIndex.from_product([["合计"], 总计.columns])，外层必须放在列表里。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p35 S02E20.多层索引与多层索引计算](https://www.bilibili.com/video/BV1ji4y157uB?p=35) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
