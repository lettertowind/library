---
term: sort_index
aliases: [sort_index(), 按索引排序]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 27
stage: "S02E12 · 数据排序【已修证】"
---

# sort_index

> 别名：sort_index()、按索引排序

**按索引从小到大对 Series 或 DataFrame 进行排序的方法。**

## 用法
**语法**：`DataFrame.sort_index(axis=0, ascending=True, inplace=False)` / `Series.sort_index(ascending=True, inplace=False)`
**参数**：
- `axis`：排序轴，默认 0 表示按行索引排序；1 表示按列名排序
- `ascending`：默认 True 升序，设为 False 则为降序
- `inplace`：默认 False 返回新对象；True 直接修改原表
- `level`：多层索引时指定按哪一层排序，可传层级名或序号

**示例**：
```python
import pandas as pd

s = pd.Series([90, 75, 88], index=["c", "a", "b"])
print(s.sort_index())
# a    75
# b    88
# c    90

df = pd.DataFrame({"语文": [90, 75]}, index=["b", "a"])
print(df.sort_index(ascending=False))
#    语文
# b   90
# a   75

# 多层索引按指定层排序后再查询，避免无序报错
mi = pd.DataFrame({"分": [1, 2, 3, 4]},
                  index=pd.MultiIndex.from_tuples(
                      [("数学", 2), ("语文", 1), ("数学", 1), ("语文", 2)],
                      names=["科目", "班"]))
print(mi.sort_index(level="科目").index.tolist())
# [('数学', 1), ('数学', 2), ('语文', 1), ('语文', 2)]
```

## 解释

sort_index() 用于将数据按照索引顺序重新排列，常用于索引顺序被打乱后恢复有序。与 Excel 的排序功能类似。

## 有什么用

- 索引顺序混乱时恢复排序
- 按索引整理数据

## 关键要点

- 按索引从小到大排序
- 适用于 Series 和 DataFrame
- 与 sort_values() 区别：一个按索引，一个按值

## 边界与易混淆

只按索引排序，不改变数据值本身；按值排序需用 sort_values()。

## 关联

- [[Series]] — 组合使用
- [[sort_values]] — 对比项

## 自测

sort_index() 和 sort_values() 有什么区别？::sort_index() 按索引排序，sort_values() 按数据值排序。


### 补充 · 2026-11-17

sort_index 不需要 by 参数，因为它直接按已设置的索引排序。常用于 set_index 之后恢复有序行号，或按列名排序。

- 不需要 by，按现有索引排序
- 同样支持 ascending 控制升降序
- 支持 inplace=True 直接修改原表
sort_index 为什么不需要写 by？::它按已设置的索引排序，索引本身就是要排序的键

sort_index 针对已设置好的索引排序，常用于把数据恢复到原始顺序（例如打乱或筛选后按序号归位）。它不需要 by 参数，因为索引就是唯一确定的排序依据；默认 axis=0 排索引，同样支持 inplace 控制是否修改原对象。

- 按索引排，不按数据值排，与 sort_values 分工明确
- 不需要 by，因为它已明确按索引排序
- 前提是索引已通过 set_index 设置好
为什么 sort_index 不用写 by？::排序依据是已经设置好的索引，本身唯一确定。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p27 S02E12.数据排序【已修证】](https://www.bilibili.com/video/BV1ji4y157uB?p=27) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
