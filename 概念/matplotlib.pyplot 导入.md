---
term: matplotlib.pyplot 导入
aliases: [import matplotlib.pyplot as plt, pyplot, plt 别名]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E01 · 柱状图"
order: 48
created: 2026-11-17
updated: 2026-11-17
---

# matplotlib.pyplot 导入

> 别名：import matplotlib.pyplot as plt、pyplot、plt 别名

**用 import matplotlib.pyplot as plt 引入绘图接口，后续所有图都靠 plt 调用。**

## 解释

pyplot 是 Matplotlib 的快捷绘图接口，把「当前图」「当前坐标轴」藏在一个全局状态里，所以 plt.bar()、plt.title() 这类函数不用传对象就能作用在同一张图上。行业惯例统一起别名 plt，与 np、pd 并列。

## 有什么用

- 任何 Matplotlib 绘图脚本的第一行导入
- 配合 pandas 读取的列数据直接作图

## 关键要点

- 约定别名：Numpy→np，Pandas→pd，Matplotlib.pyplot→plt
- 别名可以自取，但改了别人读不懂代码
- pyplot 函数作用于「当前图」，因此调用顺序影响结果
- 导入后不调用任何绘图函数不会有任何输出

## 边界与易混淆

面向对象写法（fig, ax = plt.subplots()）不依赖全局状态，复杂多子图时更推荐。

## 关联

- [[Matplotlib]] — 上位概念
- [[plt.show]] — 组合使用
- [[import pandas as pd]] — 对比项

## 自测

plt.xlabel('姓名') 没有传入任何图对象，它怎么知道要改哪张图？::pyplot 维护了一个「当前图/当前坐标轴」的全局状态，函数默认作用在最近创建的那张图上。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p48 S03E01.柱状图](https://www.bilibili.com/video/BV1ji4y157uB?p=48) · 2026-11-17
