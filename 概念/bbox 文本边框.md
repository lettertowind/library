---
term: bbox 文本边框
aliases: [bbox, bbox=dict()、set_bbox, 带边框的文本标签]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E23 · 标题及轴标签"
order: 72
created: 2026-11-17
updated: 2026-11-17
---

# bbox 文本边框

> 别名：bbox、bbox=dict()、set_bbox、带边框的文本标签

**给文字套上边框和背景色的字典参数，配合 plt.text 形成醒目标签。**

## 解释

普通数据标签只有文字，压在折线上容易看不清。bbox 用字典描述边框样式（圆角/方角）、填充色、边框颜色和线宽，把文字变成一块带底色的“贴纸”，让标签在任何背景下都醒目。

## 有什么用

- 强调图中某个关键数据点
- 在密集折线图上标出文字仍能看清

## 关键要点

- boxstyle 选边框形状，如 'round' 为圆角
- fc（facecolor）设背景填充色，可用 '0.8' 这样的灰度值
- ec（edgecolor）设边框线色，lw / linewidth 设边框线宽
- 必须作为参数传给 plt.text()，只定义字典不会显示任何东西

## 边界与易混淆

bbox 只是文本装饰，不会自动避让数据点，位置仍需手动调整（如上移到 y=2.5）以免遮挡。

## 关联

- [[plt.text 数据标签]] — 组合使用
- [[plt.annotate 文本注释]] — 组合使用

## 自测

写了 bbox = dict(boxstyle='round', fc='0.8') 但图上什么都没出现，原因是什么？::字典只是定义样式，必须把它作为 bbox 参数传给 plt.text() 或 plt.annotate() 才会绘制。
fc 和 ec 分别控制边框的什么？::fc 是 facecolor，控制框内背景填充；ec 是 edgecolor，控制边框线条颜色。


### 补充 · 2026-11-17

bbox 不是单个样式值，而是一个字典，内部的键决定背景框的外观。常用键有 facecolor（填充色）、alpha（透明度）、pad（背景框相对文字的留白大小）。写好字典后作为 bbox=字典 传给 title、xlabel、ylabel、text、annotate 等函数即可生效。

- 建议先写 bbox = dict(...) 变量再传入，结构更清晰
- facecolor 设背景填充色，alpha 设透明度（0~1）
- pad 控制背景框相对文字的留白，值越大框越大
bbox=dict(facecolor='yellow', alpha=0.2, pad=50) 中，把 pad 改成 5 会看到什么变化？::背景框相对文字变小、留白变少，文字几乎贴着框边。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p72 S03E23.标题及轴标签](https://www.bilibili.com/video/BV1ji4y157uB?p=72) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p76 S03E27.文本注释](https://www.bilibili.com/video/BV1ji4y157uB?p=76) · 2026-11-17
