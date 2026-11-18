---
term: get_dummies
aliases: [str.get_dummies, 哑变量编码, one-hot 编码]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 37
stage: "S02E22 · 离散化和分箱"
---

# get_dummies

> 别名：str.get_dummies、哑变量编码、one-hot 编码

**把字符串按分隔符拆成多个 token 并生成 0/1 哑变量列的 Pandas 方法。**


## 用法
**语法**：`Series.str.get_dummies(sep='|')`

**参数**：
- `sep`：分隔符字符串，默认为 `'|'`，按它把每个字符串切成多个 token

**示例**：
```python
import pandas as pd

s = pd.Series(['近,中', '中,远', '近'], name='距离')
print(s.str.get_dummies(sep=','))
#    中  近  远
# 0  1  1  0
# 1  1  0  1
# 2  0  1  0

# 注意：pandas 顶层也有 pd.get_dummies，它做的是整列/整表 one-hot，
# 不会按分隔符拆 token；多值字段必须走 .str.get_dummies(sep=...)
print(pd.get_dummies(s).columns.tolist())
# ['近,中', '中,远', '近']
```

## 解释

Series.str.get_dummies(sep=...) 按指定分隔符切分字符串，每个出现的 token 成为一列，行内标记是否包含该 token。适合一个字段里塞了多个标签的多值字段。

## 有什么用

- 多标签字段转 one-hot
- 把'中远距离'这类复合值拆成独立特征

## 关键要点

- sep 参数指定拆分字符
- 每个 token 生成一列 0/1 标记
- 适合多值字段的特征工程
- 平时用得少，但遇到多标签场景无可替代

## 边界与易混淆

只适合分隔符清晰的多值字段；token 过多会导致列爆炸。

## 关联

- [[Series.str 访问器]] — 上位概念
- [[pivot_table]] — 对比项

## 自测

对'近距离'用 sep='距' 调用 get_dummies，会得到哪些列？::会得到'近'和'离'两列（以及数据中其他行出现的 token 列）。
get_dummies 和 pivot_table 都能做特征展开，区别在哪？::get_dummies 按分隔符拆字符串生成 0/1 列，pivot_table 按行列分组聚合数值。


### 补充 · 2026-11-17

当一列里塞了多个标签（如「中远距离」），str.get_dummies 用 sep 指定的字符切开，把所有出现过的 token 各做成一列，某行含该 token 记 1、否则记 0。它把「一列多标签」变成标准的多特征结构，方便统计与建模。

- sep='距' 按该字符切分，整行字符串被拆成 token 列表
- 所有行出现过的 token 都会成为列，缺该 token 的行记 0
- 属于 Series.str.get_dummies，与 pd.get_dummies 不是一回事
对「中远距离」用 sep='距' 展开后，哪些列会记 1？::含「中」「远」「离」的列记 1，其他 token 列记 0。
str.get_dummies 与 pd.get_dummies 的核心区别是什么？::前者是对一列字符串按分隔符切分后展开多标签；后者是把已有的类别型取值做独热编码。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p39 S02E24.字符串操作（下）](https://www.bilibili.com/video/BV1ji4y157uB?p=39) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
