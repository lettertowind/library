---
term: plt.hist
aliases: [hist, Matplotlib 直方图函数]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E17 · 直方图"
order: 66
created: 2026-11-17
updated: 2026-11-17
---

# plt.hist

> 别名：hist、Matplotlib 直方图函数

**Matplotlib 中绘制直方图的函数，自动完成分组与计数。**

## 解释

只需传入一列连续数值，plt.hist 就会自动分箱、统计每箱样本数并画出长条，无需自己先做 value_counts。它的样式参数集中在分箱（bins）与长条外观（facecolor、edgecolor、alpha）两类上。

## 有什么用

- 一行代码画出某列数值的分布
- 快速探索数值型字段的集中趋势与异常

## 关键要点

- bins 指定分箱数量或分箱边界，视频中口头称为“组距”，官方含义是分箱
- facecolor 设填充色（'b' 蓝），edgecolor 设边框色（'white' 白、'r' 红）
- 颜色值必须写英文名或色值，写成中文“白色”会报错
- alpha 控制透明度，长条粘连或颜色过深时配合边框使用
- 传入的是原始数值列（如 data['身高']），不是已统计好的频数

## 边界与易混淆

不能用来画类别频数对比，那属于 plt.bar；bins 与 pd.cut 的分箱思想相同，但一个是画图参数、一个生成区间标签。

## 关联

- [[直方图]] — 上位概念
- [[离散化与分箱]] — 组合使用

## 自测

长条彼此粘连看不清边界，改哪个参数最直接？::加 edgecolor（如 edgecolor='white'）设置边框色，也可用 alpha 降低透明度。
plt.hist(data['身高'], bins=30) 里的 30 是什么意思？::把身高的取值范围切成 30 个分箱，不是 30 这个数值本身。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p66 S03E17.直方图](https://www.bilibili.com/video/BV1ji4y157uB?p=66) · 2026-11-17
