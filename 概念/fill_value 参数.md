---
term: fill_value 参数
aliases: [fill_value, 透视表缺失值填充]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 43
stage: "S02E28 · 数据透视表"
---

# fill_value 参数

> 别名：fill_value、透视表缺失值填充

**pivot_table 中把结果缺失值替换为指定值的参数。**

## 解释

透视结果中某些行列组合可能没有数据，形成空值，参与后续计算会污染统计。fill_value=0 可把这些空值统一替换成 0，保证计算正常。实际数据中若确定可能有空值，应主动加上该参数。

## 有什么用

- 透视结果存在空值时保证后续计算正确
- 导出前清理结果中的 NaN

## 关键要点

- 常见写法 fill_value=0
- 空值参与计算会得到空值，影响统计
- 与 fillna 作用类似，但作用于透视结果

## 边界与易混淆

只影响透视结果中的缺失值，不修改原始数据。

## 关联

- [[pivot_table]] — 组合使用
- [[fillna]] — 对比项

## 自测

透视结果有空值时，为什么后续求和可能出错？::任何数与缺失值参与计算都可能得到缺失值，统计结果被污染。


### 补充 · 2026-11-17

在 add/sub/div 等方法中，fill_value 指定当参与运算的某一方在该位置为缺失值时，用该值代替参与计算，从而避免结果传播为 NaN。

- 只在灵活算术方法中生效，普通运算符不支持
- 常见取值 fill_value=0
- 只作用于缺失值，不作用于 inf
fill_value=0 会修改原始 Series 吗？::不会，它只在本次运算中临时把缺失值当 0 处理。

透视后某些单元格可能没有数据而显示 NaN。fill_value 可在结果中统一填充这些缺失值，常见写法是 fill_value=0。若缺失值参与后续计算，容易让结果仍为缺失值，因此有缺失时应加上。

- 常见写法 fill_value=0。
- 只替换透视结果中的缺失值。
- 有缺失值时建议显式加上。
fill_value=0 和 fillna(0) 有什么区别？::fill_value 填透视结果缺失值；fillna 填原 DataFrame 的缺失值。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p43 S02E28.数据透视表](https://www.bilibili.com/video/BV1ji4y157uB?p=43) · 2026-11-17

它替代了“先 fillna 再运算”的两步操作，把填充和计算合并成一次调用。填充只发生在本次运算的缺失位置上，不会改动原始数据。

- 只作用于对齐后缺失的位置，不修改原对象
- 参数名是 fill_value，误写成 value 会报错
- 与 fillna 的区别：fillna 改数据，fill_value 只管这一次运算
fill_value=0 会不会把原 DataFrame 里的空值改成 0？::不会。它只在这一次运算中把缺失位置当作 0 参与计算，原数据仍是空值。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p34 S02E19.算数运算与数据对齐](https://www.bilibili.com/video/BV1ji4y157uB?p=34) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
