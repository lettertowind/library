---
term: Matplotlib 颜色简写
aliases: [color 参数, 单字母颜色, 颜色名, color='y']
kind: concept
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E28 · 瀑布图"
order: 77
created: 2026-11-17
updated: 2026-11-17
---

# Matplotlib 颜色简写

> 别名：color 参数、单字母颜色、颜色名、color='y'

**Matplotlib 支持用单字母简写、颜色名、十六进制或 RGB 元组来指定颜色。**

## 解释

单字母是最短的写法，r/g/b/k/w/y/c/m 各有固定含义；也可以用 'yellow'、'#FFCC00' 或 (r, g, b) 元组。注意简写和全称并非总是一一对应，例如 'y' 是偏暗的土黄，而 'yellow' 才是鲜亮的金黄色。

## 有什么用

- 给柱形图、折线图指定系列颜色
- 用颜色编码类别语义（如红盈绿亏）

## 关键要点

- 常用简写：r 红、g 绿、b 蓝、k 黑、w 白、y 土黄、c 青、m 品红
- 'y' 与 'yellow' 视觉差别明显，需要鲜黄必须写全称
- 也可用十六进制 '#FF0000' 或 (r,g,b) 元组精确定色
- 同一图内用颜色区分类别时，应同时配 label 保证图例可读

## 边界与易混淆

单字母简写在灰度打印或色弱场景下不可靠，需配合线型或标记区分。

## 关联

- [[柱形图]] — 组合使用
- [[plt.legend 图例]] — 组合使用

## 自测

color='y' 和 color='yellow' 画出来一样吗？::不一样，'y' 是暗黄/土黄，'yellow' 是明亮的金黄色。


### 补充 · 2026-11-17

- b 蓝、r 红、g 绿、c 青、m 洋红、y 黄、k 黑、w 白
- 也可写英文单词，如 'blue'、'red'
- 十六进制写 'xxxxxx' 形式，可从取色工具复制
- colors 参数可传颜色列表，按顺序对应各扇区

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p77 S03E28.瀑布图](https://www.bilibili.com/video/BV1ji4y157uB?p=77) · 2026-11-17
