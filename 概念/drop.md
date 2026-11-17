---
term: drop
aliases: [df.drop, DataFrame.drop, 删除行列]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 30
stage: "S02E15 · 数据删除 drop函数"
order: 30
---

# drop

> 别名：df.drop、DataFrame.drop、删除行列

**按标签删除 DataFrame 或 Series 的行/列的方法。**

## 解释

drop 是 Pandas 中删除数据的核心方法，通过指定行标签或列标签来移除对应数据。默认按行（axis=0）操作，删除列需显式设置 axis=1。它默认返回新对象而不修改原数据，需配合 inplace 或赋值使用。

## 有什么用

- 删除不需要的行记录
- 删除多余的列字段
- 数据清洗时剔除指定标签的数据

## 关键要点

- 删除单行直接写行标签：df.drop(2)
- 删除多行用 labels 列表：df.drop(labels=[1,3])
- 删除列必须设 axis=1，默认 axis=0 按行
- 删除后原索引不会自动重排，保留原标签
- 默认 inplace=False，返回新对象，原数据不变

## 边界与易混淆

drop 按标签删除，不是按位置；要按位置删需先查标签。与 del 语句、pop 方法的区别在于 drop 可批量且返回新对象。

## 关联

- [[axis 参数]] — 组合使用
- [[inplace 参数]] — 组合使用
- [[labels 参数]] — 组合使用
- [[DataFrame]] — 上位概念

## 自测

df.drop(2) 和 df.drop(labels=[2]) 效果一样吗？为什么？::一样。单标签可直接传，多标签必须用 labels 列表；单标签传列表也合法。
执行 df.drop('语文', axis=1) 后直接 print(df)，为什么语文列还在？::因为 inplace 默认 False，drop 返回新对象，原 df 未被修改，需赋值或设 inplace=True。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
