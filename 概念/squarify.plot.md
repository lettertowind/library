---
term: squarify.plot
aliases: [squarify.plot(), 树状图绘制函数]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E29 · 树状图"
order: 78
created: 2026-11-17
updated: 2026-11-17
---

# squarify.plot

> 别名：squarify.plot()、树状图绘制函数

**squarify 绘制树状图的主函数，用参数控制面积、标签、颜色和文字。**

## 解释

一次调用即可生成完整树状图。sizes 决定矩形面积，label 显示分类名称，value 在名称下方显示数值，color/edgecolor/linewidth 控制填充色与边框，alpha 控制透明度，text_kwargs 用字典设置块内文字样式。

## 有什么用

- 传入数值列与名称列直接出图
- 为分类销售数据定制配色和标注

## 关键要点

- sizes 决定块面积，是树状图的数值核心
- label 显示分类名，value 显示数值，二者都不影响面积
- color 是填充色，edgecolor 是边框色，不要混用
- linewidth 过大（如 10）会让块看起来被边框挤开，3 左右较合适
- text_kwargs 用字典设置 fontsize、color、fontweight 等块内文字样式

## 边界与易混淆

sizes、label、value 长度需与类别数一致，颜色列表长度也应匹配；块内字号过大会溢出矩形。

## 关联

- [[squarify]] — 上位概念
- [[树状图]] — 下位概念
- [[plt.title]] — 对比项

## 自测

sizes 和 value 都传入销售数量列，为什么两个都要设？::sizes 决定矩形块面积大小，value 只是把数字写在块上；不设 value 时块上只有分类名没有数字。
想让相邻矩形块之间有白色分隔线，应该调哪两个参数？::edgecolor='white' 设边框颜色，linewidth 设边框宽度（如 3）。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p78 S03E29.树状图](https://www.bilibili.com/video/BV1ji4y157uB?p=78) · 2026-11-17
