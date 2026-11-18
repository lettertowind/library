---
term: DataFrame 合并
aliases: [merge, 连接查询, DataFrame join]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 23
stage: "S02E08 · 连接查询之join与Merge总结"
---

# DataFrame 合并

> 别名：merge、连接查询、DataFrame join

**按共同键把两个 DataFrame 连接成一张表的方法。**

## 用法
**语法**：`pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, suffixes=('_x', '_y'))`

**参数**：
- `left` / `right`：要连接的两个 DataFrame，左右顺序决定 left/right 连接的基准表
- `how`：连接方式，`'inner'`（默认，只保留键匹配的行）、`'left'`、`'right'`、`'outer'`（全外连接，两侧全保留）
- `on`：连接键列名，单列名做单键连接，传列表如 `['姓名','门派']` 做多键连接；不写时默认取两表同名列
- `left_on` / `right_on`：两表连接列名不同时分别指定
- `left_index` / `right_index`：设为 `True` 时用索引作连接键，如左表列连右表索引写 `left_on='姓名', right_index=True`
- `suffixes`：两表存在同名非键列时加的后缀，默认 `('_x', '_y')`

**示例**：
```python
import pandas as pd

left = pd.DataFrame({'姓名': ['叶问', '李小龙', '孙兴华'], '次数一': [0, 1, 2]})
right = pd.DataFrame({'姓名': ['李小龙', '孙兴华', '黄飞鸿'], '次数二': [1, 2, 3]})

print(pd.merge(left, right))                  # 默认 how='inner'：2 行，李小龙、孙兴华
print(pd.merge(left, right, on='姓名', how='left'))   # 3 行，叶问的次数二为 NaN
print(pd.merge(left, right, on='姓名', how='outer'))  # 4 行，叶问与黄飞鸿各缺一侧
# 键有重复值会膨胀：左表姓名重复时，匹配行按组合展开，需先去重
```

## 解释

Pandas 的合并操作类似 SQL 连接查询，支持内连接、左连接、右连接和全外连接，通过共同列或索引把两张表拼在一起，是关系型数据整合的核心手段。

## 有什么用

- 整合多张关联表
- 替代 VLOOKUP 做批量匹配

## 关键要点

- 四种连接：内、左、右、全外
- 内连接只保留键匹配的行
- 左/右连接保留一侧全部行
- 全外连接保留两侧所有行

## 边界与易混淆

键不唯一会产生笛卡尔积式膨胀；连接列类型不一致会导致匹配失败。

## 关联

- [[DataFrame]] — 上位概念
- [[pd.concat]] — 对比项

## 自测

内连接和左连接的结果行数差异来自哪里？::内连接只保留两表键都匹配的行；左连接保留左表全部行，右表无匹配处填 NaN。
合并键存在重复值时会发生什么？::匹配行会成倍组合，结果行数膨胀，需要先去重或确认键唯一。


### 补充 · 2026-11-17

merge 是 Pandas 中基于键（通常是列名）的连接方式，类似 SQL 的 JOIN。它支持 inner、outer、left、right 等连接方式，适用于字段有关联但结构不同的表。与 concat 的沿轴连接不同，merge 基于键值匹配。

- 基于键（列名）匹配连接，类似 SQL JOIN
- 支持 inner、outer、left、right 连接方式
- 与 concat 的区别：concat 沿轴连接，merge 按键匹配
concat 和 merge 的核心区别是什么？::concat 沿轴直接连接，merge 基于键（列）匹配连接。

pd.merge 是 Pandas 中对应 SQL 连接查询的核心方法，通过 on 指定对齐列、how 指定连接类型，把右表字段匹配进左表或做集合式整合。它是多表数据整合的首选方式，比 join 更灵活。

- 核心三要素：on 指定连接列、how 指定连接方式、suffixes 区分同名列
- 默认 how='inner'，只保留左右表都匹配的记录
- 左/右连接对表顺序敏感，需明确基准表
不写 how 参数时，merge 默认保留哪些记录？::只保留左右表连接键都匹配的记录，即内连接。
为什么说左连接和右连接对表顺序敏感，而全外连接不敏感？::左/右连接以某一侧为基准，换顺序基准就变；全外连接保留两侧全部记录，结果范围与顺序无关。

pd.merge 是 Pandas 中最常用的表连接方法，思想与 SQL 的 JOIN 一致：根据连接键把两个表的行匹配起来，再拼成一张宽表。它解决的是「同一实体信息分散在多张表」时的整合问题。

- 默认按两表同名列做内连接，how='inner' 可省略
- on 传单列名做单键连接，传列表做多键连接
- 左表列连右表索引用 left_on + right_index=True
左表 6 行、右表 3 行，按姓名内连接后结果有 5 行，可能是什么原因？::连接键存在重复值，匹配时按组合展开，行数不等于任一原表行数。
为什么说左连接类似 VLOOKUP？::都以左表为基准保留全部记录，再从右表把匹配到的字段「取」过来，取不到则为空。

pd.merge(左表, 右表, how=..., on=...) 按共同字段对齐两表行，并把右表列追加到左表列后面。它是 Pandas 里实现 Excel VLOOKUP 的标准手段：左表作标准，右表提供要匹配的列。右表通常先用 loc[:, ['键','目标列']] 裁到最少列，再参与合并。

- 第一参数为左表（基准表），第二参数为右表（供数列）
- on 指定连接键，how 指定连接方式，二者共同决定结果行集
- 右表先 loc[:, ['学号','总分']] 裁剪，避免无关列混入结果
merge 与 concat 的核心区别是什么？::merge 按连接键对内容做对齐（类 SQL JOIN），concat 按轴方向直接堆叠，不关心内容是否对得上。
为什么 merge 前通常先用 loc 裁剪右表？::merge 会带入右表全部列，裁到连接键+目标列可让结果干净、避免列名冲突。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p44 S02E29.vlookup](https://www.bilibili.com/video/BV1ji4y157uB?p=44) · 2026-11-17

Pandas 提供三条路径：concat 沿轴拼接、merge 按键（字段）连接、join 按索引连接。日常优先 concat，其次 merge，join 相对弱、不优先使用。

- concat 按轴拼，不需要键；merge 按字段键拼
- join 方法基于索引，能力较弱，一般不优先
- concat 的 join 参数 ≠ DataFrame.join 方法，别混
要按共同的“学号”字段把两张表关联起来，应该用哪个工具？::merge（按字段键连接），而不是 concat。
三张同字段的表要上下叠成一张，用 concat 还是 merge？::concat，默认 axis=0 纵向堆叠即可。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p24 S02E09.连接查询之concat](https://www.bilibili.com/video/BV1ji4y157uB?p=24) · 2026-11-17

merge 是把两张表按连接键做行匹配的操作，思路与 SQL 的 join 一致。它默认是内连接、默认用同名共有列作键，因此最简单的写法 pd.merge(左表, 右表) 就能跑通；要改变行为就显式给 on 和 how。

- 默认按同名共有列做内连接，on 与 how='inner' 可省略
- 改写为非内连接时必须显式写 how
- concat 是行/列方向的拼接合并，merge 是按键的连接查询，二者不同
同事说「把两张表 merge 一下」，和「concat 一下」是同一件事吗？::不是。concat 是沿行或列方向拼接，merge 是按连接键做匹配，逻辑上对应 SQL 的 join。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p22 S02E07.连接查询之Merge](https://www.bilibili.com/video/BV1ji4y157uB?p=22) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
