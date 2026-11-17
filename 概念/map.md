---
term: map
aliases: [Series.map, 映射方法]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 45
stage: "S02E30 · 数据处理的三板斧"
order: 45
---

# map

> 别名：Series.map、映射方法

**对 Series 每个元素按字典或函数做一对一映射，返回同长度新 Series。**

## 解释

map 是 Series 专属方法，把整列的每个值逐个传入字典或函数，得到映射后的新值并按原位置返回。适合分类转换、编码替换等整列统一处理。

## 有什么用

- 把性别列男/女映射为先生/女士
- 用字典把编码列翻译成中文标签
- 对整列套用简单单参数函数

## 关键要点

- 只作用于 Series，不能直接对 DataFrame 调用
- 可接收字典（键为原值）或函数（单参数）
- 映射不到的值返回 NaN，需注意缺失
- 单参数场景优先用 map，多参数改用 apply
- 赋值回原列即覆盖修改，赋给新列则保留原值

## 边界与易混淆

与 replace 易混：map 是整列逐值映射，replace 是表内具体值替换；map 不支持多参数。

## 关联

- [[Series]] — 上位概念
- [[apply]] — 对比项
- [[replace]] — 对比项

## 自测

性别列用字典 map 后出现 NaN，最可能的原因是什么？::原列中存在字典里没有的键，映射不到就返回 NaN。
要给整列成绩统一加 5 分，用 map 还是 apply 更合适？为什么？::单参数可用 map；若函数还需第二个参数（误差值），则必须用 apply 的 args 传参。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
