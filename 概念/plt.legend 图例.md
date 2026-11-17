---
term: plt.legend 图例
aliases: [legend, 图例, plt.legend(), loc='upper left']
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E05 · 叠加柱状图"
order: 52
created: 2026-11-17
updated: 2026-11-17
---

# plt.legend 图例

> 别名：legend、图例、plt.legend()、loc='upper left'

**Matplotlib 中根据各绘图函数的 label 参数自动生成图例说明的函数。**

## 解释

在 plt.bar()、plt.plot() 等函数里写 label 只是登记名称，不会自动显示；必须再调用 plt.legend() 才会绘制图例。loc 参数控制图例摆放位置。

## 有什么用

- 图中存在两条及以上数据系列时标明各颜色含义
- 调整图例位置避免遮挡数据

## 关键要点

- 只写 label 不调 plt.legend()，图例不会出现（可能报错提示）
- loc 控制位置，默认自动择优（通常右上角），'upper left' 为左上角
- 单条数据的柱形图/折线图不需要图例，多条数据必须加
- 未设置 label 或以 _ 开头的图元不会进入图例

## 边界与易混淆

此处 loc 是图例定位参数，与 Pandas 的标签索引器 df.loc 是完全不同的东西，不要混淆。

## 关联

- [[柱形图]] — 组合使用
- [[分组柱状图]] — 组合使用
- [[Matplotlib 中文显示配置]] — 前置知识
- [[loc]] — 对比项

## 自测

两次 plt.bar() 都写了 label，但图上没有图例，最可能漏了什么？::漏了 plt.legend()，label 只登记名称，需 legend 才渲染。
什么情况下不加图例反而是正确做法？::只有一条数据系列时，颜色含义唯一，加图例属于多此一举。


### 补充 · 2026-11-17

只有绘图时写了 label，legend() 才有内容可显示。默认往往竖排成一列，占用画布侧边；用 loc 挪位置、用 ncol 改成横排，能让图面更紧凑。堆叠柱图三层三个颜色，图例是必需的说明。

- plt.legend(loc='center', ncol=3) 表示图例居中且一行三列
- ncol 控制列数，三系列设 3 即排成一行
- loc 还可取 upper left、lower right、center left 等位置字符串
想让三个系列图例从默认的一列三行变成一行三列，加什么参数？::plt.legend(ncol=3)，需要居中再加 loc='center'
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p52 S03E05.叠加柱状图](https://www.bilibili.com/video/BV1ji4y157uB?p=52) · 2026-11-17

图例分两步：先在绘图函数里用 label 参数给这组数据起名，再调用 plt.legend() 把名字画出来。只写 label 不调 legend 不会有图例，只调 legend 而没写 label 则图例为空。位置由 loc 控制，默认右上角。

- 两步走：label='成绩' 传入 plt.bar，再 plt.legend()
- loc 控制位置：'upper left' 左上、'lower right' 右下等
- loc 位置字符串不必死记，用时查表即可
代码里写了 plt.legend()，但图例框是空的，原因是什么？::绘图函数里没有传 label 参数，没有可显示的名称。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p48 S03E01.柱状图](https://www.bilibili.com/video/BV1ji4y157uB?p=48) · 2026-11-17

图例文本来自绘图函数中的 label 参数，先设置 label 再调用 plt.legend() 才会显示。它让读者分清柱子、折线、平均线各自代表什么。

- 图例文本来自绘图函数的 label 参数
- 必须先设 label，再调用 plt.legend()
- 可同时展示柱形与平均线的含义
为什么调用 plt.legend() 后某些线条没有出现在图例里？::绘制该线条时没有设置 label 参数，图例没有可显示的文本
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p57 S03E09.平均线](https://www.bilibili.com/video/BV1ji4y157uB?p=57) · 2026-11-17

plt.legend 把各图形元素的名称集中标注，避免读者靠猜颜色对应用。除 loc 定位置外，还可用 bbox_to_anchor 做精确偏移、ncol 控制分列、fontsize 控字号。

- loc='upper right' 等定大致方位
- bbox_to_anchor=(1.1, 1.05) 微调图例相对坐标轴的偏移
- ncol=3 让图例横向分成三列排列
想让图例三项并排横排，用哪个参数？::ncol=3。
图例默认位置挡住了图形，最直接的两种解法是什么？::改 loc 换方位，或用 bbox_to_anchor 把它挪到画布外侧。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p54 S03E07.饼图](https://www.bilibili.com/video/BV1ji4y157uB?p=54) · 2026-11-17

绘图时用 label= 给每条曲线或柱子起名，再调用 legend() 把名称与图形样式对应展示。单图可用 plt.legend()，多轴组合图则要在各自坐标轴上分别调用 ax1.legend / ax2.legend。loc 决定图例位置（如 'upper left'、'upper right'），用来避开图形和数据。

- label= 命名，legend() 显式打开，缺一不可
- loc 控制位置，常用 'upper left'、'upper right'
- 双轴图中要分别为 ax1 和 ax2 设置图例
双 y 轴组合图里，为什么调一次 plt.legend() 可能漏标？::两条轴的图形分属不同 axes，需分别在 ax1 与 ax2 上调用 legend。
图例压在柱子上方怎么处理最省事？::把该轴 ylim 上限抬高留白，而不是去改图例大小。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p62 S03E13.组合图：柱形图+折线图](https://www.bilibili.com/video/BV1ji4y157uB?p=62) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p50 S03E03.分组柱状图](https://www.bilibili.com/video/BV1ji4y157uB?p=50) · 2026-11-17
