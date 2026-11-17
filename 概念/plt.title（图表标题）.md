---
term: plt.title（图表标题）
aliases: [title, plt.title(), 图表标题, 图标题]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E12 · 新增子图或区域"
order: 60
created: 2026-11-17
updated: 2026-11-17
---

# plt.title（图表标题）

> 别名：title、plt.title()、图表标题、图标题

**为当前坐标轴或指定坐标轴设置图表标题。**

## 解释

plt.title 面向当前轴设置标题；在面向对象接口中对应 ax.set_title。多子图或子区域中，应分别对每个 Axes 设置标题，避免标题张冠李戴。

## 有什么用

- 给单图设置标题
- 给子图或子区域分别命名

## 关键要点

- Axes 对象用 set_title 设置本轴标题。
- 多子图中应分别调用 ax.set_title，避免设到错误的当前轴。
- 复制绘图代码后要同步修改变量名和标题文字。
- 标题文字应能区分主图与内部小图。

## 边界与易混淆

plt.title 作用于“当前轴”，多图场景下不如 ax.set_title 明确。

## 关联

- [[面向对象绘图接口（Axes 方法）]] — 组合使用
- [[子区域（画中画）]] — 组合使用

## 自测

多子图场景中如何给某一个子图单独设标题？::用该子图返回的 Axes 对象调用 set_title，如 ax.set_title('销售量')。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p60 S03E12.新增子图或区域](https://www.bilibili.com/video/BV1ji4y157uB?p=60) · 2026-11-17
