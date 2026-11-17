---
term: 标记点（marker）
aliases: [marker, 标记点, 数据点标记, 'o', markersize]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E10 · 画布和子图"
order: 58
created: 2026-11-17
updated: 2026-11-17
---

# 标记点（marker）

> 别名：marker、标记点、数据点标记、'o'、markersize

**在折线图上标出每个数据点位置的符号，如 'o' 表示实心圆点。**

## 解释

默认折线只画线不画点，加上 marker 后每个数据点都会显示一个符号，读者能一眼看出具体取值落在哪里。它和颜色、线型一样，是 plt.plot 中相互独立的样式维度，可以自由组合。

## 有什么用

- 数据点较少时突出每个点的位置
- 同图对比多条曲线时，用不同标记点加以区分

## 关键要点

- 最常用的是 'o'（实心圆点），另有 '*'、's'、'^'、'+' 等
- 可写进格式字符串简写，如 'ro-' 表示红色圆点加实线
- 点太多时可调小 markersize 或干脆不设标记
- 标记点、颜色、线型是三个互不冲突的样式维度

## 边界与易混淆

数据点密集时标记会互相重叠、显得杂乱，此时宁可只用线型区分。

## 关联

- [[plt.plot]] — 组合使用
- [[plot 格式字符串]] — 组合使用
- [[linestyle 线型参数]] — 对比项

## 自测

'ro-' 这三个字符分别代表什么？::r 表示红色，o 表示用圆点标记数据点，- 表示实线连接。
折线图上数据点很多时，加 marker 有什么风险？::标记会彼此重叠、显得杂乱，应缩小 markersize 或不用标记。


### 补充 · 2026-11-17

marker 决定符号样式（如 'o' 圆点、'*' 星号），markersize 决定符号大小。加上标记点后，即使折线很密也能一眼看出实际采样了哪些数据点。它只影响视觉呈现，不改变数据。

- marker 设样式：'*' 星号、'o' 圆点等
- markersize 设标记大小，如 markersize=10
- 仅影响视觉表现，不改变数据
折线图里想让数据点用星号且放大一些，该写哪些参数？::marker='*' 与 markersize=10。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p58 S03E10.画布和子图](https://www.bilibili.com/video/BV1ji4y157uB?p=58) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p73 S03E24.样式](https://www.bilibili.com/video/BV1ji4y157uB?p=73) · 2026-11-17
