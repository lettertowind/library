---
term: enumerate
aliases: [enumerate(), 枚举函数, 带下标的遍历]
kind: method
domain: 数据分析/Python
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# enumerate

> 别名：enumerate()、枚举函数、带下标的遍历

**Python 内置函数，遍历可迭代对象时同时返回下标和元素值**

## 解释

for i, v in enumerate(列表) 让循环一次拿到两个值：索引和元素本身，省去手动维护计数器。绘图时索引恰好就是柱子或数据点在坐标轴上的位置，因此特别顺手。

## 有什么用

- 循环中需要同时使用索引和值
- 给柱形图/折线图逐点加标签时提供 x 坐标

## 关键要点

- 写法是 for 下标, 元素 in enumerate(序列)
- 默认下标从 0 开始，可用 start 参数改起始值
- 下标天然对应柱形图第几根柱子的 x 位置
- 与 zip 的区别：enumerate 产下标，zip 并列多个序列

## 边界与易混淆

只适用于可迭代对象；遍历字典时产出的是键而非值。

## 关联

- [[plt.text 数据标签]] — 组合使用
- [[zip]] — 对比项

## 自测

for x, y in enumerate([3,5,7]) 第一次循环 x 和 y 分别是多少？::x=0，y=3
为什么说 enumerate 的下标可以直接当柱形图的 x 坐标？::因为 plt.bar 默认按 0,1,2…顺序排柱子，第 n 根柱子的中心就在 x=n

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p51 S03E04.添加数据标签](https://www.bilibili.com/video/BV1ji4y157uB?p=51) · 2026-11-17
