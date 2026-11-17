---
term: plt.show
aliases: [show, plt.show(), 显示图形]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E01 · 柱状图"
order: 48
created: 2026-11-17
updated: 2026-11-17
---

# plt.show

> 别名：show、plt.show()、显示图形

**把已经创建好的图形渲染到窗口里显示出来的函数。**

## 解释

plt.bar() 等函数只是在内存里构造了图形对象，不调用 plt.show() 就什么也看不到。它是整段绘图代码的收尾动作，通常放在最后一行（保存图片要放在它之前）。

## 有什么用

- 脚本或 Notebook 中查看绘图结果
- 调试图表样式时反复运行

## 关键要点

- 只画不显示：写了 plt.bar() 不写 plt.show() 图不会出现
- 一个脚本通常只在末尾调用一次
- plt.savefig 必须在它之前调用，否则可能保存空白图
- 在部分 IDE/Notebook 中会自动显示，容易掩盖漏写问题

## 边界与易混淆

弹出窗口会阻塞脚本执行，批量出图时通常省略 show 只做 savefig。

## 关联

- [[matplotlib.pyplot 导入]] — 前置知识
- [[plt.savefig]] — 对比项
- [[柱形图]] — 组合使用

## 自测

代码运行完没报错，但屏幕上没有图，最可能漏了什么？::漏了 plt.show()，图形对象已创建但从未被渲染显示。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p48 S03E01.柱状图](https://www.bilibili.com/video/BV1ji4y157uB?p=48) · 2026-11-17
