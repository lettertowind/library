---
term: join 方法
aliases: [join, DataFrame.join, left.join(right)]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 23
stage: "S02E08 · 连接查询之join与Merge总结"
---

# join 方法

> 别名：join、DataFrame.join、left.join(right)

**DataFrame 按索引对齐横向拼接另一张表的简便方法。**

## 用法
**语法**：`DataFrame.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False)`
**参数**：
- `other`：要拼接的另一个 DataFrame，也可以是列表，一次拼接多个表
- `on`：用左表的这一列去匹配右表的索引；不写则按左表索引对齐（与 merge 的 on 语义不同）
- `how`：连接方式，`'left'`（默认）、`'right'`、`'inner'`、`'outer'`
- `lsuffix` / `rsuffix`：左右表列名重复时，分别附加到列名后面的后缀
- `sort`：是否按连接键对结果排序，默认 `False`
**示例**：
```python
import pandas as pd

left = pd.DataFrame({'name': ['A', 'B', 'C']}, index=[1, 2, 3])
right = pd.DataFrame({'score': [85, 90, 78]}, index=[2, 3, 4])
print(left.join(right))
#    name  score
# 1     A    NaN   <- 索引 1 无对应，补空值
# 2     B   85.0
# 3     C   90.0
print(left.join(right, how='inner'))   # 只保留两表都有的索引
#   name  score
# 2    B     85
# 3    C     90
```

## 解释

join 语法简单，默认按索引把右表列横向拼到左表右侧，索引不一致处补空值。功能比 merge 有限，适合简单横向拼接，复杂场景建议用 merge。

## 有什么用

- 按索引快速横向拼接两表
- 一次连接多个 DataFrame

## 关键要点

- 默认按索引对齐，而非按同名列
- 索引不一致时对应位置产生空值
- on 参数是左表列匹配右表索引，与 merge 不同
- 支持列表一次连接多个表：left.join([right, right2])
- 功能有限，实际项目建议优先用 merge

## 边界与易混淆

join 的 on 语义与 merge 的 on 不同；默认按索引对齐，容易因索引不一致产生大量空值。

## 关联

- [[DataFrame 合并]] — 对比项
- [[索引对齐]] — 前置知识

## 自测

left.join(right) 默认按什么对齐？::按索引对齐，把右表列横向拼到左表右侧。
join 的 on='k' 与 merge 的 on='k' 有何不同？::join 是左表的 k 列去匹配右表的索引；merge 是左右表同名列 k 相互匹配。


### 补充 · 2026-11-17

left.join(right) 直接把右表横向放到左表旁边，默认以索引作为对齐依据；索引对不上的位置补空值。也可以用 on 指定左表的某一列去匹配右表的索引，还可以传入列表一次连接多张表。它写法极简，但正因为只按索引对齐，复杂场景很受限。

- 默认按索引横向对齐，索引不一致的位置为空
- on 参数指定用左表哪一列去匹配右表的索引，与 merge 的 on 语义不同
- 支持列表形式一次连接多表：left.join([right, right2])
left.join(right) 时两表索引不完全重合，结果会怎样？::按索引对齐取并集，任一侧没有匹配值的位置填空值，不会报错。
要一次把 right 和 right2 拼到 left 上，join 怎么写？为什么 merge 不能这么写？::写成 left.join([right, right2])；merge 一次只能合并两张表，多表需要链式多次调用。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p23 S02E08.连接查询之join与Merge总结](https://www.bilibili.com/video/BV1ji4y157uB?p=23) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
