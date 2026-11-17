---
term: plt.savefig
aliases: [savefig, 保存图片, plt.savefig()]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E07 · 饼图"
order: 54
created: 2026-11-17
updated: 2026-11-17
---

# plt.savefig

> 别名：savefig、保存图片、plt.savefig()

**把当前图形按指定路径和格式写成图片文件的函数。**

## 解释

除了在窗口里点保存按钮，更常用代码批量保存图表。路径参数建议显式带上扩展名（.png/.jpg），否则可能生成无后缀或格式不明的文件。它必须写在 plt.show() 之前，因为窗口关闭后图形状态会被清空。

## 有什么用

- 把图表批量导出成报告插图
- 自动化脚本定时生成图片

## 关键要点

- 显式写扩展名，如 plt.savefig('C:/图.png')
- 调用顺序在 plt.show() 之前，否则可能存出空白图
- 支持绝对路径，路径分隔可用正斜杠避免转义
- 格式由扩展名推断，也可用 format 参数指定

## 边界与易混淆

保存的是「当前图」，多图场景需配合 figure 对象或用分图保存。

## 关联

- [[plt.show]] — 对比项
- [[matplotlib.pyplot 导入]] — 前置知识
- [[plt.tight_layout]] — 组合使用

## 自测

为什么 savefig 写在 show 后面常常存出一张白图？::show 关闭窗口后当前图形状态被清空，savefig 拿不到可绘制的图元。


### 补充 · 2026-11-17

plt.savefig 按给定路径与扩展名写文件，常用参数 dpi 控制分辨率、bbox_inches 控制裁切范围。要在 plt.show() 之前调用，否则可能保存到空白画布。

- 传文件路径即可，扩展名决定格式，路径建议用原始字符串 r''
- dpi 默认 100，导出 640×480；dpi=200 得 1280×960
- dpi=300 得 1920×1440，接近高清水平
保存的图里混进了看不见的坐标轴，加什么参数处理？::bbox_inches='tight'。
为什么建议路径写成 r'C:\...'？::原始字符串避免反斜杠被当作转义字符。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p54 S03E07.饼图](https://www.bilibili.com/video/BV1ji4y157uB?p=54) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p48 S03E01.柱状图](https://www.bilibili.com/video/BV1ji4y157uB?p=48) · 2026-11-17
