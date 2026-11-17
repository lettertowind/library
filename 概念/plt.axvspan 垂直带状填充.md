---
term: plt.axvspan 垂直带状填充
aliases: [axvspan, plt.axvspan(), 垂直区域填充, 垂直带状填充]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E25 · 填充"
order: 74
created: 2026-11-17
updated: 2026-11-17
---

# plt.axvspan 垂直带状填充

> 别名：axvspan、plt.axvspan()、垂直区域填充、垂直带状填充

**在 x 轴指定区间内填充一条贯穿 y 方向的垂直带状区域。**

## 解释

axvspan(xmin, xmax) 接收 x 轴起止值，在两者之间铺一层色带，y 方向默认覆盖整个绘图区；v 代表 vertical。与 axhspan 相反，它强调 x 轴上的区间范围。

## 有什么用

- 突出显示 x 轴上的某个区间
- 标记时间段、阈值区间或分类范围

## 关键要点

- 参数为 xmin、xmax，填充的是 x 轴范围
- 用 facecolor 指定填充色，如 facecolor='blue'
- 支持 alpha 透明度
- v 表示垂直，与 axhspan 的水平填充相对
- 常配合 plt.axis 设置显示范围

## 边界与易混淆

填充范围由 x 轴起止值决定，不是 y 轴。

## 关联

- [[plt.axhspan 水平带状填充]] — 对比项
- [[alpha 透明度]] — 组合使用
- [[ax.axis（一次设置坐标轴四边界）]] — 组合使用

## 自测

plt.axvspan(1, 1.3) 填充的是哪个轴的范围？::x 轴，从 x=1 到 x=1.3。
axvspan 中的 v 代表什么方向？::vertical，垂直方向，即填充 x 轴区间。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p74 S03E25.填充](https://www.bilibili.com/video/BV1ji4y157uB?p=74) · 2026-11-17
