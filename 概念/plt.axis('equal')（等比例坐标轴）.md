---
term: plt.axis('equal')（等比例坐标轴）
aliases: [axis('equal'), 等比例坐标轴, 保持正圆, set_aspect]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E07 · 饼图"
order: 54
created: 2026-11-17
updated: 2026-11-17
---

# plt.axis('equal')（等比例坐标轴）

> 别名：axis('equal')、等比例坐标轴、保持正圆、set_aspect

**让两个坐标轴单位长度一致，从而保证圆形图形不被压扁**

## 解释

默认坐标轴会随画布比例自动拉伸，圆可能被画成椭圆。axis('equal') 强制 x、y 单位等长，饼图就稳定保持正圆。它设置的是坐标轴比例，不是坐标轴范围。

## 有什么用

- 饼图、散点图中需要保持真实比例时
- 画布比例改动后图形变形

## 关键要点

- 作用是把圆变回正圆，不是设置数据范围
- 与 ax.axis([xmin,xmax,ymin,ymax]) 传列表的用法完全不同
- 横向对比数据时应谨慎使用，等比例会压缩留白

## 边界与易混淆

别与设置四边界的 ax.axis([xmin, xmax, ymin, ymax]) 混淆，同名函数两种用法含义不同。

## 关联

- [[饼图]] — 组合使用
- [[ax.axis（一次设置坐标轴四边界）]] — 对比项

## 自测

饼图被压成椭圆，一行代码怎么修？::plt.axis('equal')。
axis('equal') 和 axis([0,10,0,10]) 是一回事吗？::不是，前者设坐标轴比例，后者设坐标轴的四条边界。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p54 S03E07.饼图](https://www.bilibili.com/video/BV1ji4y157uB?p=54) · 2026-11-17
