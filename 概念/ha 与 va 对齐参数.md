---
term: ha 与 va 对齐参数
aliases: [ha, va, horizontalalignment, verticalalignment, 水平对齐, 垂直对齐]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E04 · 添加数据标签"
order: 51
created: 2026-11-17
updated: 2026-11-17
---

# ha 与 va 对齐参数

> 别名：ha、va、horizontalalignment、verticalalignment、水平对齐、垂直对齐

**Matplotlib 文字的水平与垂直对齐参数，决定锚点落在文字框的哪个方位**

## 解释

画文字时给定的 (x, y) 是一个锚点，ha 决定文字在锚点左边、居中还是右边，va 决定在锚点上、中、下。理解成「文字框哪一边贴住坐标点」就对了，不是让文字在整张图里居中。

## 有什么用

- 柱形图标签立在柱顶而不压住柱子
- 标题、注释、图例文字的精细摆位

## 关键要点

- ha 常用取值：center、left、right
- va 常用取值：center、top、bottom
- 柱顶标签典型组合是 ha='center'、va='bottom'
- 调错对齐会让文字压在柱子上或偏离图形元素

## 边界与易混淆

对齐只相对锚点坐标生效，最终视觉位置仍由 x、y 数值决定，两者要一起调。

## 关联

- [[plt.text 数据标签]] — 组合使用
- [[plt.annotate 文本注释]] — 组合使用

## 自测

va='bottom' 的实际含义是什么？::文字框底部对齐到给定的 y 坐标，文字整体落在锚点上方
标签总往柱子左边偏，最可能该改哪个参数？::把 ha 设为 'center' 改为水平居中对齐

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p51 S03E04.添加数据标签](https://www.bilibili.com/video/BV1ji4y157uB?p=51) · 2026-11-17
