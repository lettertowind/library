---
term: bottom 参数（plt.bar 堆叠起始位置）
aliases: [bottom, bottom=, 堆叠起始位置, 条形图起点参数]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E28 · 瀑布图"
order: 77
created: 2026-11-17
updated: 2026-11-17
---

# bottom 参数（plt.bar 堆叠起始位置）

> 别名：bottom、bottom=、堆叠起始位置、条形图起点参数

**plt.bar 的参数，指定每根柱子的起始高度，堆叠时取前面各层的累计高度。**

## 解释

默认所有柱形都从 0 起画，多系列会重叠或并列。给后面几层设置 bottom，就是让它们「踩」在上一层顶部继续往上长，从而形成一根多段柱子。它决定的是起点而非长度，长度仍由第 2 个参数（高度数据）决定。

## 有什么用

- 画堆叠柱状图 / 堆积条形图
- 把多个系列合成一根柱子同时展示总量与构成

## 关键要点

- 第一层不写 bottom，等价于 bottom=0，从 x 轴底部起画
- 第二层 bottom=语文，第三层 bottom=语文+数学，层数更多就一直累加前面所有层
- bottom 是起点高度，柱子的高度仍由第 2 个参数控制，两者别混
- 第二层若不设 bottom，数学柱会从 0 起画，图上变成重叠或并排而非堆叠

## 边界与易混淆

横向条形图 barh 中对应参数叫 left 而不是 bottom；用 bottom 堆叠时各系列长度必须一致并对齐索引。

## 关联

- [[堆积柱形图]] — 组合使用
- [[柱形图]] — 上位概念
- [[叠加柱状图数据标签定位]] — 组合使用

## 自测

已有语文、数学、英语三层要堆叠，第三层 plt.bar 的 bottom 应该写成什么？::data['语文'] + data['数学']，即前两层累计高度
为什么第二层只写 plt.bar(x, data['数学']) 得不到堆叠效果？::因为没设 bottom，数学柱从 0 起画，会盖住或并列于语文柱，而不是叠在其顶部


### 补充 · 2026-11-17

不写 bottom 时柱子贴 x 轴生长；给定 bottom 后柱子从该高度向上（正 y）或向下（负 y）延伸。瀑布图、堆积柱形图都靠它实现“接着上一段继续画”。

- 瀑布图中 bottom 是变量，每轮循环执行 bottom += y 累加
- 堆积图中同一根柱的多段共用同一 x，bottom 依次叠加
- y 为负数时柱子从 bottom 向下延伸，同样受 bottom 控制
bottom 参数和 y 的关系是什么？::y 决定柱子从 bottom 起延伸多长，bottom 决定起点高度，二者共同决定柱子占据的纵向区间。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p77 S03E28.瀑布图](https://www.bilibili.com/video/BV1ji4y157uB?p=77) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p52 S03E05.叠加柱状图](https://www.bilibili.com/video/BV1ji4y157uB?p=52) · 2026-11-17
