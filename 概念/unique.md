---
term: unique
aliases: [np.unique, 取唯一值]
kind: method
domain: Numpy
tags: [概念/method, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
order: 14
stage: "S01E13 · 条件计算，排序，深潜拷贝【本季完】"
---

# unique

> 别名：np.unique、取唯一值

**返回数组中的唯一值，通常为数组形式。**

## 用法
**语法**：`np.unique(ar)`
**参数**：
- `ar`：需要取出唯一值的输入数组，可以是数值、字符串等类型；也接受列表，可以传入一维或二维数组。
**示例**：
```python
import numpy as np

names = np.array(['杨过', '小龙女', '杨过', '郭靖', '小龙女'])
print(np.unique(names))
# ['小龙女' '杨过' '郭靖']

scores = np.array([88, 76, 88, 92, 76])
print(np.unique(scores))
# [76 88 92]
```
注意：结果默认按取值升序排序，不保留首次出现的顺序；只返回该列的唯一值，不保留分数等其他字段，需要保留完整行时改用 `drop_duplicates`。

## 解释

np.unique 对一列数据取出所有不重复的值，只返回该列本身，不保留其他字段。它适合快速看有哪些取值，但去重后想保留完整行信息时不如 Pandas 的 drop_duplicates 方便。

## 有什么用

- 快速查看某列有哪些不同取值
- 统计前先了解字段取值集合

## 关键要点

- 返回结果是数组或列表形式
- 只返回该列唯一值，不保留其他字段
- 与 drop_duplicates 相比丢失行上下文

## 边界与易混淆

需要去重后保留完整字段（如分数、班级）时应改用 drop_duplicates，而不是 unique。

## 关联

- [[drop_duplicates]] — 对比项
- [[value_counts]] — 组合使用

## 自测

为什么分析中取唯一姓名时更常用 drop_duplicates 而不是 np.unique？::np.unique 只返回姓名本身，丢失分数等其他字段；drop_duplicates 去重后保留完整行信息。


### 补充 · 2026-11-17

np.unique 对数组去重，输出每个值只出现一次的新数组。默认会排序，因此结果顺序不是首次出现顺序。

- 默认对唯一值排序
- 对字符串数组同样适用
- 类似 Power BI 的去重建新表
np.unique 的结果默认是原始出现顺序吗？::不是，默认会排序。

unique 最初在 NumPy 中学到，用在 Pandas 的某一列上时返回该列的唯一值列表，顺序通常是出现顺序（np.unique 会排序）。它只输出值本身，不携带其他列的信息，因此不适合需要保留整行明细的场景。

- 用法：tt['姓名'].unique()，返回唯一值列表
- 只给值不给行，其他列信息会丢失
- 需要保留分数等字段时应改用 drop_duplicates
想看到每个姓名及其分数、只要每人一条记录，用 unique 可以吗？::不行，unique 只返回唯一值列表，丢掉分数等字段，应使用 drop_duplicates(subset='姓名')
unique 和 value_counts 的输出差别是什么？::unique 输出去重后的取值列表；value_counts 输出每个取值及其出现次数
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p33 S02E18.删除重复和提取重复](https://www.bilibili.com/video/BV1ji4y157uB?p=33) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
