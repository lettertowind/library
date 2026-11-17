---
term: plt.tight_layout
aliases: [tight_layout, 紧凑布局, 自动调整布局, 自动适应]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E12 · 边框与间距补充"
order: 61
created: 2026-11-17
updated: 2026-11-17
---

# plt.tight_layout

> 别名：tight_layout、紧凑布局、自动调整布局、自动适应

**自动计算并调整子图间距，避免标题、轴标签与子图相互遮挡的函数。**

## 解释

当标题被上方子图压住、轴标签被裁掉时，调用一次 plt.tight_layout() 即可让 Matplotlib 依据当前内容自动收缩边距。相比手动试数值，它是首选方案，特别适合多子图布局。

## 有什么用

- 多子图时标题或标签互相重叠
- 保存图片时边缘文字被裁切

## 关键要点

- 一行调用即可自动计算边距，无需手填数值
- 应在标题、轴标签都设置好之后再调用
- 子图越多、标签越长，效果越明显
- 与 plt.subplots_adjust 功能重叠，一般择一使用

## 边界与易混淆

自动算法不保证绝对完美，极端比例的布局或手动定位的文本仍可能重叠，需要手动兜底。

## 关联

- [[plt.subplots_adjust]] — 对比项
- [[plt.subplot 子图布局]] — 组合使用

## 自测

四个子图加了大字号标题后互相压住，最省事的通用处理是什么？::在绘图和标签都设置完后调用 plt.tight_layout() 让布局自动适配。


### 补充 · 2026-11-17

它根据图形内容自动计算边距和子图间距，解决多子图标题与刻度重叠、子图拥挤等问题。日常绘图通常优先使用它，省去手动调参。

- 调用 plt.tight_layout() 即可自动适应布局，减少标题与刻度重叠。
- 对 Figure 和 Axes 中的内容都有效，无需手动设置边距参数。
- 工作中常用，讲师建议一般场景优先用自动布局。
多子图标题与 x 轴刻度重叠时，最省事的解决方法是调用哪个函数？::plt.tight_layout()
已经调用了 plt.tight_layout()，还需要再写 plt.subplots_adjust() 吗？::一般不需要，可将后者注释掉。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p61 S03E12.[补充]调整边框与子图间距](https://www.bilibili.com/video/BV1ji4y157uB?p=61) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p72 S03E23.标题及轴标签](https://www.bilibili.com/video/BV1ji4y157uB?p=72) · 2026-11-17
