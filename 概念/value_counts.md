---
term: value_counts
aliases: [df['列'].value_counts, 频数统计, 出现次数统计]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 33
stage: "S02E18 · 删除重复和提取重复"
---

# value_counts

> 别名：df['列'].value_counts、频数统计、出现次数统计

**统计 Series 中每个取值出现的次数并按频数排序。**

## 用法
**语法**：`Series.value_counts(normalize=False, sort=True, ascending=False, dropna=True)`
**参数**：
- `normalize`：默认 `False` 返回频数；设为 `True` 返回占比（总和为 1）
- `sort`：默认 `True` 按频数排序
- `ascending`：默认 `False` 降序；设为 `True` 则升序
- `dropna`：默认 `True` 不统计缺失值；设为 `False` 会把 NaN 也计入
**示例**：
```python
import pandas as pd

df = pd.DataFrame({'订单号': ['A1', 'A2', 'A3', 'A4', 'A5'],
                   '姓名': ['小龙女', '杨过', '小龙女', '杨过', '郭靖']})
print(df['姓名'].value_counts())
# 小龙女    2
# 杨过     2
# 郭靖     1
# Name: 姓名, dtype: int64

print(df['姓名'].value_counts(normalize=True))
# 小龙女    0.4
# 杨过     0.4
# 郭靖     0.2
# Name: 姓名, dtype: float64
```

## 解释

value_counts() 对一列数据做频数统计，返回每个取值及其出现次数。它是重复值处理的基础统计方法，可快速看出哪些值重复、重复几次。

## 有什么用

- 统计每个人下了多少次订单
- 查看某列各取值的出现频次

## 关键要点

- 返回 Series，索引为取值、值为出现次数
- 默认按次数降序排列
- 常与 duplicated 配合先看频次再处理重复

## 边界与易混淆

只做统计不修改数据；需要按频数筛选或去重仍需 drop_duplicates 或布尔索引。

## 关联

- [[duplicated]] — 前置知识
- [[unique]] — 对比项

## 自测

有订单号和姓名两列，想统计每个人对应多少订单，用什么方法？::df['姓名'].value_counts()，统计姓名出现次数即订单数。


### 补充 · 2026-11-17

value_counts 对 Series 的每个不同值计数，返回以取值作索引、次数作值的 Series，默认按次数降序。它是快速刻画分布、发现重复集中度的工具，比手工去数高效得多。

- 用法：tt['姓名'].value_counts()，结果按次数降序
- 结果中次数大于 1 的取值即为重复项
- 常用于订单表里统计每人下单次数
一列订单号一列姓名，怎么看每个人下了几单？::对姓名列做 value_counts()，每人的出现次数即下单次数
value_counts 的结果里次数>1 说明什么？::该取值在数据中重复出现，是重复记录
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p33 S02E18.删除重复和提取重复](https://www.bilibili.com/video/BV1ji4y157uB?p=33) · 2026-11-17

value_counts 把一列数据里每个不同取值出现的次数汇总成一张频数表，默认按次数降序排列。在分箱场景中，它把分箱结果当作输入，就能直接得到每个区间有多少条数据，是最常用的分段计数手段。

- 可直接对分箱结果调用：pd.value_counts(结果)
- 输出为「取值 → 出现次数」，默认降序
- 分箱结果无论是区间名、箱号还是自定义名都能统计
分箱后想同时知道每段的平均年龄，value_counts 够用吗？::不够，value_counts 只给条数；需要按分箱结果分组后做聚合（如 groupby 后取 mean）。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p37 S02E22.离散化和分箱](https://www.bilibili.com/video/BV1ji4y157uB?p=37) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
