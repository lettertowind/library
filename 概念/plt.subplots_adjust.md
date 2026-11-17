---
term: plt.subplots_adjust
aliases: [subplots_adjust, 手动调整边距, wspace, hspace, left/top/bottom 参数]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E03 · 分组柱状图"
order: 50
created: 2026-11-17
updated: 2026-11-17
---

# plt.subplots_adjust

> 别名：subplots_adjust、手动调整边距、wspace、hspace、left/top/bottom 参数

**手动设置子图四周留白和子图之间横纵间距的布局调整函数。**

## 解释

它暴露布局的四个外边距（left、right、top、bottom）和两个间距（wspace、hspace），取值都是画布比例。想精确定位标题位置、给某侧留出大量空白时用它，数值靠反复试调确定。

## 有什么用

- 需要精细控制边距、自动布局不满足时
- 给大标题或图例预留固定空白

## 关键要点

- left/top/bottom/right 用 0~1 的比例控制画布四周留白
- wspace、hspace 控制子图之间的水平与垂直间距
- top 调小可给标题腾出空间，bottom 调大会压缩下方空间
- 没有唯一正确数值，需按画布大小和子图数量试调
- 通常在绘图结束、show 之前调用

## 边界与易混淆

与 tight_layout 作用目标相同但方式相反（手动 vs 自动），混用时以最后一次调用为准。

## 关联

- [[plt.tight_layout]] — 对比项
- [[plt.subplot 子图布局]] — 组合使用

## 自测

标题仍然和上方子图挤在一起，想手动把顶部留白加大，应调哪个参数？::调小 top 的值（如 0.8），给顶部让出更多空间，必要时再配合 hspace。


### 补充 · 2026-11-17

当刻度标签被裁掉或图例贴边时，用 fig.subplots_adjust 手动留白。参数取 0–1 的比例值，表示图形距画布边缘或子图之间保留的空间。

- 用法：fig = plt.gcf(); fig.subplots_adjust(left=0.1, bottom=0.3)
- left=0.1 表示图形距画布左边约 10%，bottom=0.3 距下边约 30%
- 一般只调左边距和下边距，其余交给自动布局
标签旋转 45 度后被裁掉，该加什么参数？::增大 bottom 边距，如 fig.subplots_adjust(bottom=0.3)。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p50 S03E03.分组柱状图](https://www.bilibili.com/video/BV1ji4y157uB?p=50) · 2026-11-17

通过 wspace、hspace 控制子图之间的水平和垂直间距，通过 left、right、top、bottom 控制子图区域与画布边缘的距离。适合对布局有精确要求的场景。

- wspace 控制子图水平间距，hspace 控制垂直间距，数值越大分得越开。
- left、right、top、bottom 是子图区域相对画布的边界比例（0~1），right 表示右边界位置而非右侧留白。
- 示例取值：wspace=0.5、hspace=0.3、left=0.125、right=0.9、bottom=0.1。
plt.subplots_adjust 中哪个参数控制子图之间的垂直间距？::hspace
right 参数表示子图右侧留白还是子图区域的右边界位置？::右边界位置（0~1 的比例值）
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p61 S03E12.[补充]调整边框与子图间距](https://www.bilibili.com/video/BV1ji4y157uB?p=61) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p72 S03E23.标题及轴标签](https://www.bilibili.com/video/BV1ji4y157uB?p=72) · 2026-11-17
