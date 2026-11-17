---
term: Matplotlib 画布样式（plt.style）
aliases: [plt.style, style.use, style.available, 内置样式, 全局样式, ggplot]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E22 · 雷达图"
order: 71
created: 2026-11-17
updated: 2026-11-17
---

# Matplotlib 画布样式（plt.style）

> 别名：plt.style、style.use、style.available、内置样式、全局样式、ggplot

**Matplotlib 预置的整套图表外观主题，用 plt.style.use 可一键切换。**

## 解释

Matplotlib 自带几十种风格主题（如 ggplot、bmh 等），一次设置就能同时改变背景、网格、配色等整体观感，不必逐项手动调整。用它可以让图表快速具备统一的专业外观，也能模仿其他绘图工具（如 R 的 ggplot2）的风格。

## 有什么用

- 快速统一多张图表的视觉风格
- 需要现成的美观主题、不想逐项调样式时

## 关键要点

- print(plt.style.available) 可列出全部内置样式名
- plt.style.use('ggplot') 设置样式，名称来自 available 的输出
- 属于全局设置，作用于之后创建的图表
- 样式名建议直接复制，手写容易拼错而报错
- 与 drawstyle、linestyle 等单条曲线参数不在同一层级

## 边界与易混淆

影响的是后续新建图表的整体外观，与单条折线的连接方式、线型互不替代；对已经绘制完成的图形不回溯生效。

## 关联

- [[Matplotlib]] — 上位概念
- [[drawstyle 折线连接样式]] — 对比项
- [[plt.subplots]] — 组合使用

## 自测

怎么知道自己能用哪些画布样式、又该怎么设置？::先 print(plt.style.available) 查看全部样式名，再 plt.style.use('样式名') 设置。
设置了 plt.style.use('ggplot') 后，之前已经画好的图会变风格吗？::不会，样式只对此后创建的图表生效。


### 补充 · 2026-11-17

plt.style.use('ggplot') 加载内置样式表，统一改变背景色、线宽、网格等默认外观，不用逐个元素调参。雷达图用 ggplot 后背景变为中性灰，与半透明填充更协调。

- 写法：plt.style.use('ggplot')，可用 plt.style.available 查看全部样式
- 作用于之后绘制的所有图表，属于全局设置
- ggplot 背景为中性灰，比纯白更适合雷达图
先绘图再写 plt.style.use('ggplot')，效果如何？::新样式对已创建的图形不追溯生效，通常看不出变化；应在绘图前设置。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p71 S03E22.雷达图](https://www.bilibili.com/video/BV1ji4y157uB?p=71) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p73 S03E24.样式](https://www.bilibili.com/video/BV1ji4y157uB?p=73) · 2026-11-17
