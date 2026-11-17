---
term: method 参数（fillna）
aliases: [method, ffill, bfill, pad, backfill, 填充方向参数]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 31
stage: "S02E16 · 处理缺失值"
---

# method 参数（fillna）

> 别名：method、ffill、bfill、pad、backfill、填充方向参数

**fillna 中控制用前值还是后值填充的参数。**

## 解释

method 决定填充时取哪个方向的有效值：ffill/pad 用前一个有效值向下填，bfill/backfill 用后一个有效值向上填。配合 axis=1 可把上下方向变成左右方向。

## 有什么用

- 时间序列、有序数据的空缺补全
- 需要保持数据趋势连续性的场景

## 关键要点

- ffill 与 pad 等价，用前值填充
- bfill 与 backfill 等价，用后值填充
- axis=0 是上下方向，axis=1 是左右方向
- 四个选项看似重复，实际可先掌握 ffill/bfill

## 边界与易混淆

新版 Pandas 推荐直接用 df.ffill()/df.bfill()，method 参数已弃用。

## 关联

- [[fillna]] — 上位概念
- [[axis 参数]] — 组合使用
- [[shift]] — 对比项

## 自测

ffill 和 bfill 的填充方向分别是什么？::ffill 用前值向下填，bfill 用后值向上填。
怎样实现左右方向的填充？::设置 axis=1 配合 method 参数。


### 补充 · 2026-11-17

method 决定填充值从哪里来：ffill 取前面的有效值，bfill 取后面的有效值，pad 和 backfill 是它们的别名式写法，多数教程认为行为一致。填充方向还受 axis 影响，axis=0 是上下传播，axis=1 变成左右传播。

- method='ffill' 用前面的值填充，axis=0 时表现为向下填
- method='bfill' 用后面的值填充，axis=0 时表现为向上填
- pad 常被视为等价于 ffill，backfill 常被视为等价于 bfill
数据默认 axis=0，method='bfill' 的填充方向和「用哪个值」分别是什么？::向上填充，用空值下方最近的一个非空值来填补它。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p31 S02E16.处理缺失值](https://www.bilibili.com/video/BV1ji4y157uB?p=31) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
