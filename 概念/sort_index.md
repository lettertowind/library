---
term: sort_index
aliases: [sort_index(), 按索引排序]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 27
stage: "S02E12 · 数据排序【已修证】"
order: 27
---

# sort_index

> 别名：sort_index()、按索引排序

**按索引从小到大对 Series 或 DataFrame 进行排序的方法。**

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

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
