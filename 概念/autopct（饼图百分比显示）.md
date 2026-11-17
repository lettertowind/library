---
term: autopct（饼图百分比显示）
aliases: [autopct, autopct='%1.2f%%', 百分比显示参数]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E07 · 饼图"
order: 54
created: 2026-11-17
updated: 2026-11-17
---

# autopct（饼图百分比显示）

> 别名：autopct、autopct='%1.2f%%'、百分比显示参数

**饼图参数，用格式字符串在每个扇区上显示该部分的百分比**

## 解释

autopct 接受一个旧式 % 格式字符串，Matplotlib 会把每个扇区的占比按该格式渲染成文字贴在扇区上。保留几位小数、要不要带百分号，全靠字符串本身决定。

## 有什么用

- 需要在饼图上直接读出占比数值时
- 控制百分比的小数位数与是否需要百分号

## 关键要点

- '%1.2f%%' 保留两位小数并显示百分号，如 28.00%
- '%1.1f%%' 保留一位小数，如 28.0%
- 两个 %% 中一个用于转义、一个用于显示百分号
- 删掉两个 %% 后只显示数值不带百分号
- 显示的是占比而非原始数值，原始数值需另用标签或图例说明

## 边界与易混淆

autopct 控制文字内容与格式，文字的位置由 pctdistance 控制，字号颜色由 textprops 控制，三者别混。

## 关联

- [[饼图]] — 上位概念
- [[labeldistance 与 pctdistance（标签与百分比距离）]] — 组合使用
- [[textprops（饼图文字样式）]] — 组合使用

## 自测

autopct='%1.1f%%' 与 autopct='%1.1f' 显示出来的差别是什么？::前者带百分号，后者只显示数字。
想让百分比保留三位小数，格式串怎么写？::'%1.3f%%'。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p54 S03E07.饼图](https://www.bilibili.com/video/BV1ji4y157uB?p=54) · 2026-11-17
