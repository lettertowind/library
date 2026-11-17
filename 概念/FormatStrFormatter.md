---
term: FormatStrFormatter
aliases: [FormatStrFormatter, 刻度格式字符串, %.2f, 百分比刻度]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E13 · 组合图"
order: 62
created: 2026-11-17
updated: 2026-11-17
---

# FormatStrFormatter

> 别名：FormatStrFormatter、刻度格式字符串、%.2f、百分比刻度

**用 printf 风格格式串（如 '%.2f'）控制数值刻度文字的格式器。**

## 解释

把它传给 set_major_formatter，刻度数字就按格式串渲染：%.2f 保留两位小数，%.1f、%.3f 改数字即可。要显示百分号须写成 '%.2f%%'，其中第一个百分号是转义。它只处理数值型刻度。

## 有什么用

- 刻度保留固定小数位
- 把比例刻度显示成百分比

## 关键要点

- '%.2f' 保留两位小数，'%.1f'/'%.3f' 改数字即可
- 百分比写法 '%.2f%%'，少一个 % 会报错或丢百分号
- 导入：from matplotlib.ticker import FormatStrFormatter
- 用法：ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))

## 边界与易混淆

只管数值刻度；日期刻度要用 DateFormatter，用 %f 处理日期无效。

## 关联

- [[刻度定位器与格式器（Locator Formatter）]] — 上位概念
- [[DateFormatter]] — 对比项
- [[MultipleLocator]] — 组合使用

## 自测

想把刻度显示为带两位小数的百分比，格式串怎么写？::'%.2f%%'
日期轴上用 FormatStrFormatter('%.2f') 会怎样？::无效，日期刻度必须用 DateFormatter。


### 补充 · 2026-11-17

通过 axis.set_major_formatter(mtick.FormatStrFormatter('%.2f%%')) 使用，格式串里的 %.2f 控制小数位，%% 转义为一个真实的百分号。它把刻度值原样套进格式串输出，因此不会自动把 0.38 变成 38%。

- 格式串中 %% 才输出一个实际的百分号，单个 % 会报错
- %.2f%% 表示保留两位小数并追加百分号
- 它只格式化，不会把 0.38 乘成 38%
为什么 FormatStrFormatter('%.2f%%') 用在 0~1 小数上会显示成 0.38%？::它只把刻度值套进格式串并加百分号，不做“乘 100”的换算。
格式串里写 %.2f% 会出什么问题？::单个 % 在格式串中是转义起始符，会报错，必须写 %% 才能输出一个百分号。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p62 S03E13.组合图：柱形图+折线图](https://www.bilibili.com/video/BV1ji4y157uB?p=62) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p68 S03E19.坐标轴【下】](https://www.bilibili.com/video/BV1ji4y157uB?p=68) · 2026-11-17
