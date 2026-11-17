---
term: shadow 参数（阴影）
aliases: [shadow, shadow=True, 阴影参数, 3D 饼图效果]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E07 · 3D饼图补充"
order: 55
created: 2026-11-17
updated: 2026-11-17
---

# shadow 参数（阴影）

> 别名：shadow、shadow=True、阴影参数、3D 饼图效果

**plt.pie 的布尔参数，控制是否给饼图加阴影以模拟立体感。**

## 解释

默认 shadow=False，不显示阴影；设为 True 后，Matplotlib 会在扇区边缘绘制一层投影，使二维饼图看起来凸起。视频里所说的“Matplotlib 3D 饼图”就是把它设为 True，本质只是阴影装饰，不是三维坐标变换。

## 有什么用

- 让二维饼图快速产生立体观感
- 模仿 Excel 中饼图的 3D 效果

## 关键要点

- 默认值为 False，写 shadow=True 才出现阴影
- 所谓“3D 饼图”只有一个开关：shadow=True
- 阴影不改变扇区角度、位置或任何数据，纯属视觉装饰
- 与 C4D 等三维软件渲染的真三维图形有本质区别

## 边界与易混淆

它不是真 3D：没有透视、旋转、深度坐标，不能用于三维可视化需求；真三维需用 mplot3d 或专业三维软件。易与 explode 混淆——explode 改位置，shadow 只改外观。

## 关联

- [[饼图]] — 组合使用
- [[explode 参数（扇区分离）]] — 对比项

## 自测

有人问“Matplotlib 怎么画 3D 饼图”，最准确的回答是什么？::Matplotlib 没有真正的 3D 饼图，只有 plt.pie(shadow=True) 的阴影效果，只是视觉上的立体感。
把 shadow 从 False 改成 True，饼图各扇区的角度会变化吗？::不会，只增加阴影装饰，几何和数据都不变。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p55 S03E07.[补充]3D饼图](https://www.bilibili.com/video/BV1ji4y157uB?p=55) · 2026-11-17
