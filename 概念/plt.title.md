---
term: plt.title
aliases: [title, plt.title(), 图表标题, 图标题]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E01 · 柱状图"
order: 48
created: 2026-11-17
updated: 2026-11-17
---

# plt.title

> 别名：title、plt.title()、图表标题、图标题

**为当前子图（Axes）顶部添加标题文字的 Matplotlib 函数。**

## 解释

plt.title('文本') 会在当前激活的子图上方居中绘制标题。它和轴标签一样，支持 fontsize、fontweight、color 等文字样式参数，写法与 plt.text 家族一致。多子图场景下，标题只落在最后被 subplot 激活的那个子图上。

## 有什么用

- 给单张图或某个子图加说明性标题
- 通过样式参数突出主标题（加大、加粗、变色）

## 关键要点

- plt.title('文本') 设置的是当前 Axes 的标题，不是整张画布的标题
- fontsize 控制字号，fontweight='bold' 加粗，color 控制颜色
- 参数名拼错（如 fontsize 少字母）通常不报错，只是样式不生效
- 创建多个子图后，标题只加到最后一次 subplot 选中的子图上

## 边界与易混淆

口语常说“给画布加标题”，但从对象模型看作用于当前 Axes；整图级别的标题要用 suptitle。

## 关联

- [[plt.subplot 子图布局]] — 组合使用
- [[plt.xlabel 与 plt.ylabel]] — 对比项

## 自测

画了 2×2 四个子图，最后调用了一次 plt.subplot(223)，此时执行 plt.title('A') 会显示在哪里？::只显示在第 3 个子图（左下）上方，因为 title 作用于当前激活的 Axes。


### 补充 · 2026-11-17

plt.title('三年二班学生成绩') 写在绘图之后，作为整张图的总标题，区别于描述单轴的 xlabel/ylabel。常用修饰参数是 fontsize 控制字号、fontweight='bold' 加粗，让标题在视觉层级上高于轴标签。

- 第一参数是标题文本，位置参数直接传即可
- fontsize=16 调字号，fontweight='bold' 加粗
- 与 xlabel/ylabel 分工不同：一个统管全图，一个描述单轴
想让标题比轴标签更醒目，除了调大 fontsize 还能做什么？::设 fontweight='bold' 加粗，形成字号与粗细双重视觉层级。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p48 S03E01.柱状图](https://www.bilibili.com/video/BV1ji4y157uB?p=48) · 2026-11-17

plt.title('销售情况') 添加标题，若需改字号、颜色、粗细，把样式写成字典传给 fontdict。fontdict 只管标题文字，方块内部的文字样式由 squarify.plot 的 text_kwargs 控制，两者格式相似但作用对象不同。

- fontdict={'fontsize':20,'color':'black'} 用字典设置标题样式
- fontdict 中的键与 text_kwargs 类似：fontsize、color、fontweight 等
- 标题颜色要根据背景选，白底上设白色标题会看不见
想把树状图标题改成 20 号字，应该用哪个参数？::plt.title('销售情况', fontdict={'fontsize': 20})，标题样式走 fontdict，而不是 text_kwargs。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p78 S03E29.树状图](https://www.bilibili.com/video/BV1ji4y157uB?p=78) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p72 S03E23.标题及轴标签](https://www.bilibili.com/video/BV1ji4y157uB?p=72) · 2026-11-17
