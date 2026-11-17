---
term: DateFormatter
aliases: [DateFormatter, mdates.DateFormatter, 日期刻度格式, %Y%m%d]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E14 · 日期格式"
order: 63
created: 2026-11-17
updated: 2026-11-17
---

# DateFormatter

> 别名：DateFormatter、mdates.DateFormatter、日期刻度格式、%Y%m%d

**按 %Y/%m/%d 等占位符把日期刻度显示成指定样式的时间格式器。**

## 解释

把日期列画到轴上后，刻度默认显示时间戳样式，用 DateFormatter 可换成“年-月-日”“年月日中文”等任意组合。可通过 import matplotlib.dates as mdates 或 mpl.dates 调用。分离年、月、日还可自定义分隔符。

## 有什么用

- 时间序列折线图的 x 轴刻度可读化
- 把刻度改成中文年月日或只保留月日

## 关键要点

- %Y 年（大写）、%m 月、%d 日（小写），大小写不能混
- 分隔符随你写：'%Y*%m*%d'、'%Y年%m月%d日'
- 用法：ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
- 刻度拥挤时只保留年月或月日，别硬塞完整日期

## 边界与易混淆

前提是数据已是 datetime 类型（或已用 pd.to_datetime 转换），字符串日期不会生效。

## 关联

- [[刻度定位器与格式器（Locator Formatter）]] — 上位概念
- [[FormatStrFormatter]] — 对比项
- [[plt.gca 与 plt.gcf]] — 组合使用

## 自测

要让刻度显示成“2020年01月05日”，格式串怎么写？::'%Y年%m月%d日'
设置 DateFormatter 后刻度还是原样，最可能的原因？::x 轴数据仍是字符串而非 datetime 类型，或方法没写成 set_major_formatter。


### 补充 · 2026-11-17

把 DateFormatter 设置到 x 轴的 major formatter 上，Matplotlib 仍把轴当作真正的时间轴，只是把刻度文本按指定格式渲染。与用 strftime 造字符串列表不同，它保留了时间的连续性，可以配合定位器控制刻度间隔。

- 格式符与 strftime 通用：%Y-%m-%d、%m月%d日
- 需配合 ax.xaxis.set_major_formatter 生效
- 与定位器（如 MonthLocator、MultipleLocator）搭配控制刻度密度
同样是把日期显示成「12月1日」，用 DateFormatter 和用 strftime 生成列表再绘图，本质差异在哪？::DateFormatter 保留真实时间轴，刻度可按时间规律自动定位；strftime 方案把 x 轴变成字符串分类轴，刻度按序号等距排布。
想让 x 轴每月只出现一个刻度并按「2020-12」显示，需要哪两类对象配合？::MonthLocator 之类的定位器控制刻度位置，DateFormatter 控制刻度文字格式。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p63 S03E14.坐标轴上面的日期格式](https://www.bilibili.com/video/BV1ji4y157uB?p=63) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p68 S03E19.坐标轴【下】](https://www.bilibili.com/video/BV1ji4y157uB?p=68) · 2026-11-17
