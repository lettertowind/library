---
term: Excel 文件
aliases: [xlsx, .xlsx 文件, Excel 工作簿]
kind: concept
domain: 数据分析/数据格式
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# Excel 文件

> 别名：xlsx、.xlsx 文件、Excel 工作簿

**以工作表单元格组织数据的二进制表格文件，列的边界由单元格位置决定。**

## 解释

Excel 不是纯文本，字段划分不依赖任何分隔符，所以读取时不存在 sep 的问题。代价是需要第三方解析库（xlrd、openpyxl），并且日期、格式、多工作表等结构更复杂。

## 有什么用

- 读取办公场景导出的报表数据
- 需要多工作表或保留格式信息的场景

## 关键要点

- 列边界由单元格位置确定，没有分隔符概念
- 一个文件可包含多个 sheet，读取时可按名称或序号取
- 读取依赖第三方引擎库，未安装会直接报错
- 日期列常被读成带时间的 Timestamp，需后续类型处理

## 边界与易混淆

纯文本、文件大、跨系统交换时 CSV 更合适；Excel 优势在人工编辑和格式呈现。

## 关联

- [[CSV 文件]] — 对比项
- [[pd.read_excel]] — 组合使用
- [[DataFrame.to_excel]] — 组合使用
- [[xlrd]] — 前置知识

## 自测

为什么 pd.read_excel 不需要 sep 参数？::Excel 里字段由单元格位置划分，不存在用某个字符分隔字段的问题。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p19 S02E04.读取与修改Excel文件](https://www.bilibili.com/video/BV1ji4y157uB?p=19) · 2026-11-17
