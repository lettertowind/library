---
term: Matplotlib
aliases: [matplotlib, mpl, Python 绘图库]
kind: tool
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E01 · 柱状图"
order: 48
created: 2026-11-17
updated: 2026-11-17
---

# Matplotlib

> 别名：matplotlib、mpl、Python 绘图库

**Python 最主流的静态数据可视化绘图库，靠 pyplot 接口出图。**

## 解释

Matplotlib 把画布、坐标轴、图元分层管理，最上层提供 pyplot 这套「状态机式」快捷接口，写一行画一笔。它与 pandas 配合极顺：pandas 负责读数和清洗，Matplotlib 直接把列数据画成图。安装用 pip3 install matplotlib。

## 有什么用

- 把 DataFrame 的列直接画成柱形图、折线图等
- 生成可保存为图片的报告图表

## 关键要点

- 安装命令：pip3 install matplotlib，类 Unix 环境用 pip3
- 绘图入口模块是 matplotlib.pyplot，惯例导入为 plt
- 底层对象体系（Figure/Axes）比 pyplot 更灵活，后续课程展开
- 安装失败多为网络原因，重试即可

## 边界与易混淆

偏静态出版级图表；交互式网页可视化通常用 plotly、pyecharts。

## 关联

- [[matplotlib.pyplot 导入]] — 下位概念
- [[柱形图]] — 组合使用
- [[import pandas as pd]] — 组合使用

## 自测

为什么数据分析和绘图常是 pandas + Matplotlib 的组合，而不是只用一个？::pandas 擅长读文件、清洗、聚合出干净的数据列，Matplotlib 只负责把数值画成图形，各司其职。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p48 S03E01.柱状图](https://www.bilibili.com/video/BV1ji4y157uB?p=48) · 2026-11-17
