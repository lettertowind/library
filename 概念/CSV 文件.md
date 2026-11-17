---
term: CSV 文件
aliases: [CSV, 逗号分隔值文件, comma-separated values]
kind: concept
domain: 数据分析/数据格式
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# CSV 文件

> 别名：CSV、逗号分隔值文件、comma-separated values

**用逗号分隔字段的纯文本表格文件。**

## 解释

CSV 以纯文本保存二维表格，每行一条记录，字段间用逗号分隔。它体积小、通用性强，适合存储和交换大数据，Pandas 可直接读取分析。

## 有什么用

- 存储和交换表格数据
- 替代 Excel 处理大数据

## 关键要点

- 纯文本格式，字段默认用逗号分隔
- 可用 read_csv 直接读取
- 大数据场景常替代 Excel
- 也可用 read_table 配合 sep=',' 读取

## 边界与易混淆

CSV 没有统一编码和表头规范，读取时需注意 sep、header、encoding。

## 关联

- [[pd.read_csv]] — 组合使用
- [[TSV 文件]] — 对比项

## 自测

CSV 文件为什么适合存大数据？::纯文本、结构简单、体积相对小且通用，便于程序读写。


### 补充 · 2026-11-17

结构扁平、数据从第一行开始，不像 Excel 那样带空行空列和样式，所以读写都更省事。实际工作中的大数据多数以 CSV/TXT 存放，几 G 的 Excel 双击就会卡死，那种场景才是 Pandas 的主场。

- 默认逗号分隔，也可能是 Tab 分隔，读取时要看 sep
- 从 Excel 右键“另存为 CSV”即可生成
- 数据从第一行开始，通常不需要 skiprows、usecols
同一份数据，为什么读 CSV 不需要 skiprows？::CSV 是纯文本、数据从第一行开始，没有 Excel 那种表头上方的空行和左侧空列
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p25 S02E10.各种数据自动填充](https://www.bilibili.com/video/BV1ji4y157uB?p=25) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p17 S02E02.读取txt与csv文件](https://www.bilibili.com/video/BV1ji4y157uB?p=17) · 2026-11-17
