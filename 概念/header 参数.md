---
term: header 参数
aliases: [header, 表头参数]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 17
stage: "S02E02 · 读取txt与csv文件"
---

# header 参数

> 别名：header、表头参数

**read_excel 中指定哪一行或哪些行作为表头的参数。**

## 解释

header 默认取第 0 行作表头。遇到两行表头时传 header=[0,1]，pandas 会生成多层列索引。不设置会导致表头错乱、数据行被误当表头。

## 有什么用

- 读取多行表头的 Excel
- 修正表头错位问题

## 关键要点

- 默认 header=0，即第一行作表头
- header=[0,1] 表示前两行都作表头
- 写几就表示把第几行当表头
- 多表头不设置会导致每行都像表头

## 边界与易混淆

多层表头会带来多层列索引，后续取列和合并时需按元组访问列名。

## 关联

- [[pd.read_excel]] — 上位概念
- [[sheet_name 参数]] — 组合使用

## 自测

Excel 前两行都是表头，不设 header 直接读取会出现什么问题？::表头错乱，第二行表头会被当成数据行，列名也不正确。


### 补充 · 2026-11-17

header 默认把第 0 行当表头。文件无表头时设 header=None，Pandas 自动生成 0、1、2… 数字列名，第一行数据才被当作数据。常与 names 配合自定义列名。

- 默认 header=0，第一行当列名
- header=None 表示无表头，自动生成数字列名
- 无表头时若不设 header=None，会少一行数据
一个 7 行无表头文件直接 read_csv，shape 显示几行？为什么？::6 行；第一行被默认当表头，未计入数据行。

header 参数默认取第 0 行为表头；传入列表如 [0,1] 可把前两行设为多层列索引，从而读取带合并单元格的多层表头 Excel。它是处理多层表头数据的关键入口。

- 默认 header=0，取第一行为表头
- header=[0,1] 表示前两行作为多层列索引
- 与 index_col 配合可同时设置行、列索引
Excel 前两行是合并单元格的多层表头，read_excel 应怎么设置？::设置 header=[0,1]，把前两行作为多层列索引。

header 默认取第 0 行作列名；设为 None 表示文件没有表头，Pandas 会自动生成 0、1、2… 的整数列名，等待 names 覆盖。它是处理“脏表头”文件的第一道开关。

- header=None 表示原文件无表头
- 无表头时列名自动变为 0、1、2…
- 参数名大小写敏感，写错会报错或失效
header=None 之后列名是什么？还需要做什么？::列名变成 0、1、2… 的整数，通常再用 names=[...] 指定有意义的列名。

header 默认为 0，即第一行当列名。header=None 表示文件无表头，让 pandas 自动编号；header=[0, 1] 表示前两行共同作列名，生成多级列索引。

- 默认第 0 行是表头，因此“看到的第一行”就是第 0 行
- 几行表头就把 header 写到几，如两行写 [0, 1]
- header=None 与 names 搭配可自行指定列名
文件前两行都是表头，header=[0, 1] 后取“销售部”下面那列该怎么取？::按两级列名取，如 数据[("上半年", "销售部")]；或者先把层级拍平再按单层列名取。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p40 S02E25.Excel文件的拆分与合并](https://www.bilibili.com/video/BV1ji4y157uB?p=40) · 2026-11-17

默认 header=0，即把第一行数据当成列名，这对无表头文件是灾难：真实首行数据被吃掉、列名变成数字值。设成 None 后第一行重新变回数据行。

- header=None 表示原文件没有表头，首行仍作为数据
- None 必须大写，写小写 none 会直接报错
- 默认 header=0，把第一行当列名
一个没有表头的 Excel 忘了设 header=None，读出来会是什么样？::第一行真实数据被当成列名，列名变成数据值，且数据行数少一行。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p19 S02E04.读取与修改Excel文件](https://www.bilibili.com/video/BV1ji4y157uB?p=19) · 2026-11-17

默认 header=0 把第一行当作列名。设置 header=[0,1] 可把前两行读成多层列索引，外层是第一行，内层是第二行。它与 index_col 分工明确：header 管列标签，index_col 管行标签。

- header=0 表示用第一行做列名，是默认行为。
- header=[0,1] 把第 0、1 行读成两层列标签。
- header 管列标签，index_col 管行标签，勿混。
header=[0,1] 后数据的列索引变成什么结构？::变成两层列索引，第 0 行是外层，第 1 行是内层。
header 与 index_col 分别管什么？::header 管列标签，index_col 管行标签。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p35 S02E20.多层索引与多层索引计算](https://www.bilibili.com/video/BV1ji4y157uB?p=35) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
