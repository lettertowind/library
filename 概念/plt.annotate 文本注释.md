---
term: plt.annotate 文本注释
aliases: [annotate, 文本注释, 箭头注释]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E27 · 文本注释"
order: 76
created: 2026-11-17
updated: 2026-11-17
---

# plt.annotate 文本注释

> 别名：annotate、文本注释、箭头注释

**在图表上写说明文字，并可用箭头指向被说明的数据点。**

## 解释

annotate 用来解释“这个点是谁/发生了什么”，而不是简单标出数值。它把“箭头指向点”（xy）和“文字显示位置”（xytext）拆成两个坐标分别控制，再用 arrowprops 画箭头，所以能让一段说明文字和远处的数据点建立视觉联系。

## 有什么用

- 在多人业绩图里指出“某个人在这里”
- 标注异常点、极值点或需要额外解释的位置
- 给图表关键位置加文字说明而非干巴巴的数值

## 关键要点

- xy 是箭头指向的目标点，xytext 是文字显示位置，两者可以分离
- 只给 xy 不设 xytext，文字会落在目标点附近
- 不传 arrowprops 一般只有文字没有箭头
- x 轴用字符串类别时，xytext 无法做加减乘除微调
- 中文注释需先配置中文字体，否则报错或乱码

## 边界与易混淆

如果只想在点上标出数值，用 plt.text() 更直接；注释数量多时箭头会互相遮挡，反而降低可读性。

## 关联

- [[arrowprops]] — 组合使用
- [[plt.text 数据标签]] — 对比项
- [[bbox 文本边框]] — 组合使用
- [[connectionstyle 变形箭头]] — 组合使用

## 自测

想让人物说明文字位于点上方 0.5 个单位、箭头仍指向该点，应该改哪个参数？::改 xytext 的 y 值（如从 2 改为 2.5），xy 保持不变。
为什么给 annotate 传了 arrowprops 才有箭头？::annotation 默认只渲染文字，箭头是 arrowprops 被显式给出（哪怕空 dict）后才绘制的装饰。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p76 S03E27.文本注释](https://www.bilibili.com/video/BV1ji4y157uB?p=76) · 2026-11-17
