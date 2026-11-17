---
term: openpyxl
aliases: [openpyxl 库, Python 读写 Excel 库]
kind: tool
domain: 数据分析/Python
tags: [概念/tool, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# openpyxl

> 别名：openpyxl 库、Python 读写 Excel 库

**Python 直接读写 xlsx 文件的底层库，pandas 读写 Excel 时依赖它。**

## 解释

openpyxl 面向单元格操作，取一整列数据往往要写循环逐行读取，代码冗长。pandas 的 read_excel 底层调用它，但对外提供了「一列即一个 Series」的抽象，省掉循环。理解这层关系就明白 pandas 方便在哪。

## 有什么用

- 需要精确控制单元格样式、合并单元格时
- pandas 读 Excel 报缺少引擎错误时安装它

## 关键要点

- 面向单元格，取整列数据通常要循环两次
- pandas.read_excel / to_excel 的底层引擎之一
- 读 xls 需换 xlrd 引擎，写 xlsx 用 openpyxl
- 适合格式微调，不适合批量数据分析

## 边界与易混淆

做数据分析时优先用 pandas 封装，只有涉及样式、公式、合并单元格才直接用它。

## 关联

- [[pd.read_excel]] — 上位概念
- [[Pandas]] — 对比项
- [[DataFrame.to_excel]] — 组合使用

## 自测

同样是读一列数据，为什么用 pandas 比用 openpyxl 代码短很多？::pandas 把整列抽象成 Series，直接按列名取；openpyxl 面向单元格，需要自己循环逐行拼数据。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p48 S03E01.柱状图](https://www.bilibili.com/video/BV1ji4y157uB?p=48) · 2026-11-17
