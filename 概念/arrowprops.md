---
term: arrowprops
aliases: [箭头样式字典, arrowprops=dict()]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E27 · 文本注释"
order: 76
created: 2026-11-17
updated: 2026-11-17
---

# arrowprops

> 别名：箭头样式字典、arrowprops=dict()

**plt.annotate 中控制箭头外观的字典参数，给出后才绘制箭头。**

## 解释

arrowprops 用 dict 的形式集中设置箭头的颜色、粗细、头部形状和连接路径，避免一堆零散关键字参数。它决定“箭头长什么样”，而不是“指向哪里”；指向哪里仍由 xy 控制。

## 有什么用

- 给注释增加可见的箭头
- 调整箭头的颜色、粗细以匹配图表的视觉风格

## 关键要点

- color 设置箭头颜色，width 控制线宽，过大会粗得吓人
- shrink 是收缩比例：数值越大箭头尾巴越短，越小尾巴越长
- headwidth 控制箭头头部宽度，headlength 控制头部长度
- connectionstyle 键可把直线箭头换成折线、弧线等变形样式

## 边界与易混淆

shrink 的语义与直觉相反（数值大不等于箭头长），调参时要按“尾巴长短”来判断而不是按数字大小。

## 关联

- [[plt.annotate 文本注释]] — 上位概念
- [[connectionstyle 变形箭头]] — 下位概念

## 自测

希望箭头尾巴更长、更远离文字，shrink 应该调大还是调小？::调小。shrink 越大，箭头尾巴越短。
width 和 headwidth 分别影响箭头的什么部位？::width 影响箭头杆身（线条）宽度，headwidth 影响箭头头部（尖端）的宽度。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p76 S03E27.文本注释](https://www.bilibili.com/video/BV1ji4y157uB?p=76) · 2026-11-17
