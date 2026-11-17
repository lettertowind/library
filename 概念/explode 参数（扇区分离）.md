---
term: explode 参数（扇区分离）
aliases: [explode, explode=(), 扇区分离, 扇区偏移参数]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E07 · 3D饼图补充"
order: 55
created: 2026-11-17
updated: 2026-11-17
---

# explode 参数（扇区分离）

> 别名：explode、explode=()、扇区分离、扇区偏移参数

**控制饼图各扇区从圆心向外偏移多少的元组参数。**

## 解释

explode 接收一个与扇区数量等长的元组，每个元素是对应扇区沿半径方向的偏移比例。0 表示留在原位，非 0 表示向外分离，常用来突出需要强调的那一块（如占比最大的分类）。

## 有什么用

- 突出显示某个扇区
- 在汇报图中强调关键分类

## 关键要点

- 传元组，元素个数要与扇区/标签数量一致
- 元素为 0 不分离，非 0 则向外偏移
- 偏移量是相对半径的比例（如 0.1），不是绝对像素
- 与 shadow 分工不同：explode 改位置，shadow 改外观

## 边界与易混淆

元组长度与数据不匹配会报错或错位；分离过多扇区会让图形散乱，通常只分离 1 块。

## 关联

- [[饼图]] — 组合使用
- [[shadow 参数（阴影）]] — 对比项

## 自测

5 个扇区只想让第 3 块分离出来，explode 该怎么写？::explode=(0, 0, 0.1, 0, 0)，其余位置保持 0。
explode 里写 0.2 表示偏移 0.2 像素吗？::不是，是相对饼图半径的比例偏移。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p55 S03E07.[补充]3D饼图](https://www.bilibili.com/video/BV1ji4y157uB?p=55) · 2026-11-17
