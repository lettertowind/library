---
term: textprops（饼图文字样式）
aliases: [textprops, 文字样式字典, textprops={'fontsize':20}]
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E07 · 饼图"
order: 54
created: 2026-11-17
updated: 2026-11-17
---

# textprops（饼图文字样式）

> 别名：textprops、文字样式字典、textprops={'fontsize':20}

**以字典形式统一设置饼图中标签与百分比文字样式的参数**

## 解释

textprops 接收一个字典，键是文字属性名、值是属性值，作用于饼图上所有文字。常用字号 fontsize、颜色 color，需要加粗再补相应键。字典写法让样式集中配置，不用逐个文字改。

## 有什么用

- 饼图文字太小或与扇区颜色对比不足时
- 统一调整字号、颜色、粗细

## 关键要点

- 写法是字典：textprops={'fontsize': 20, 'color': 'w'}
- fontsize 控字号，color 接受颜色简写如 'w'
- 可继续加入加粗等其他文字属性键
- 字号放大后标签可能超出边界，需配合 labeldistance 调整

## 边界与易混淆

textprops 只管饼图上的文字，图例文字要用 plt.legend 的 fontsize，两者互不影响。

## 关联

- [[饼图]] — 上位概念
- [[字典]] — 前置知识
- [[Matplotlib 颜色简写]] — 组合使用

## 自测

想同时把饼图文字改成白色、字号 16，怎么写？::textprops={'fontsize': 16, 'color': 'w'}。
textprops 里的设置会影响图例文字吗？::不会，图例字号要用 plt.legend 的 fontsize 单独设。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p54 S03E07.饼图](https://www.bilibili.com/video/BV1ji4y157uB?p=54) · 2026-11-17
