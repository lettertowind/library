---
term: linestyle 线型参数
aliases: [linestyle, ls, 线型, 线条样式]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E09 · 平均线"
order: 57
created: 2026-11-17
updated: 2026-11-17
---

# linestyle 线型参数

> 别名：linestyle、ls、线型、线条样式

**Matplotlib 中指定线条样式（实线、虚线等）的参数。**

## 解释

linestyle 用短字符串描述线条画法，如 ':' 为虚线、'-' 为实线、'--' 为破折线、'-.' 为点划线。它在 plt.plot、plt.grid 等几乎所有涉及线条的接口中通用，可简写为 ls。

## 有什么用

- 区分多条曲线的视觉风格
- 让网格线、参考线弱化为虚线不抢主体

## 关键要点

- ':' 虚线、'-' 实线、'--' 破折线、'-.' 点划线
- 可简写为 ls，如 ls=':'
- 对折线、网格线、边框等线条对象均生效
- 参数名拼写要准确，少写字母会直接报错

## 关联

- [[plt.grid（网格线）]] — 组合使用
- [[plt.plot]] — 组合使用
- [[linewidth 线宽参数]] — 对比项

## 自测

想让网格线变成虚线但保留实线数据曲线，应该改哪个参数、改谁的？::只给 plt.grid 传 linestyle=':'，不动 plt.plot 的线型。


### 补充 · 2026-11-17

linestyle 决定线条的视觉样式，常用 ':' 表示点状虚线、'--' 表示虚线。平均线、阈值线等参考线通常用虚线，以区别于实际数据系列。

- linestyle=':' 为点状虚线，常用于平均线
- 实线 '-'、虚线 '--'、点线 ':'、点划线 '-.'
- 可通过 ls 简写传入
想让平均线看起来像参考线而不是数据线，linestyle 应怎么设？::设为 ':' 或 '--' 等虚线样式，避免用实线
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p57 S03E09.平均线](https://www.bilibili.com/video/BV1ji4y157uB?p=57) · 2026-11-17

线型只改变线条本身的画法，常用符号有 '-' 实线、'--' 破折线（虚线）、'-.' 点划线、':' 点线、'' 或 None 无线条。它和颜色、标记点、drawstyle 是彼此独立的样式维度，常用来在同一张图中区分多条曲线。

- '-' 实线、'--' 破折线、'-.' 点划线、':' 点线、'' 或 None 无线条
- 可简写进格式字符串，如 'r--' 表示红色虚线
- 与 drawstyle 不同：线型管线条虚实，drawstyle 管点与点之间的阶梯走法
想让折线变成阶梯状，改 linestyle 有用吗？::没用，要用 drawstyle；linestyle 只能把线变成虚线、点划线等。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p73 S03E24.样式](https://www.bilibili.com/video/BV1ji4y157uB?p=73) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p64 S03E15.网格线](https://www.bilibili.com/video/BV1ji4y157uB?p=64) · 2026-11-17
