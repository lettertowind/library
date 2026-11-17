---
term: 刻度定位器与格式器（Locator Formatter）
aliases: [Locator, Formatter, set_major_locator, set_major_formatter, 主刻度定位器, 主刻度格式器]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E19 · 坐标轴【下】"
order: 68
created: 2026-11-17
updated: 2026-11-17
---

# 刻度定位器与格式器（Locator Formatter）

> 别名：Locator、Formatter、set_major_locator、set_major_formatter、主刻度定位器、主刻度格式器

**Matplotlib 中分别决定“刻度画在哪”和“刻度显示成什么文字”的两套对象。**

## 解释

每个轴（xaxis/yaxis）都配有 major/minor 的 locator 与 formatter。定位器管位置，格式器管文本，通过 set_major_locator、set_major_formatter 替换默认实现即可自定义刻度。两者互不干扰：换定位器不会改变文字样式，换格式器也不会移动刻度。

## 有什么用

- 把刻度改成某数的倍数
- 把刻度显示成小数、百分比或日期

## 关键要点

- ax.xaxis.set_major_locator(...) 决定刻度位置
- ax.xaxis.set_major_formatter(...) 决定刻度文字
- 定位器与格式器多需从 matplotlib.ticker 导入
- 方法名写错不会报错，只是设置静默失效，务必核对拼写

## 边界与易混淆

易混：定位器管位置、格式器管文本，二者不可互换；对 y 轴操作要把 xaxis 换成 yaxis。

## 关联

- [[MultipleLocator]] — 下位概念
- [[FormatStrFormatter]] — 下位概念
- [[DateFormatter]] — 下位概念
- [[plt.gca 与 plt.gcf]] — 前置知识

## 自测

刻度位置没问题但数字显示成 3.141593，该换定位器还是格式器？::换格式器，用 set_major_formatter 设置显示格式。
写了 set_major_formater 程序不报错但图没变化，原因？::方法名拼写错误，设置未生效。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p68 S03E19.坐标轴【下】](https://www.bilibili.com/video/BV1ji4y157uB?p=68) · 2026-11-17
