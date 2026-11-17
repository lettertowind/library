---
term: pd.read_excel
aliases: [read_excel, 读取 Excel]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 19
stage: "S02E04 · 读取与修改 Excel 文件"
order: 19
---

# pd.read_excel

> 别名：read_excel、读取 Excel

**pandas 读取 Excel 文件为 DataFrame 的函数。**

## 解释

read_excel 默认读取工作簿的第一个工作表，通过 sheet_name 参数可指定单个、多个或全部工作表；通过 header 参数可指定表头行。它是所有 Excel 合并拆分任务的入口。

## 有什么用

- 读取单个 Excel 工作表
- 批量读取工作簿内全部 sheet
- 处理多行表头的 Excel

## 关键要点

- sheet_name=None 读取全部工作表，返回字典
- sheet_name 可传名称、索引或列表混合指定
- header=[0,1] 表示前两行都作为表头
- 不加 header 处理多表头会导致表头错乱

## 边界与易混淆

只读取数据，不保留格式、颜色、公式结果以外的样式；复杂格式需 VBA 或 openpyxl。

## 关联

- [[pd.ExcelWriter]] — 对比项
- [[pd.concat]] — 组合使用

## 自测

一个工作簿有 5 个 sheet，想一次全部读进来，sheet_name 该怎么写？返回什么结构？::写 sheet_name=None，返回字典，键为工作表名，值为对应 DataFrame。


### 补充 · 2026-11-17

pd.read_excel(路径) 是 Excel 数据进入 Pandas 的入口，与 to_excel 构成读写一对。它默认把第一行当表头、自动生成 RangeIndex，因此无表头文件需要配合 header、names、index_col 等参数调整。

- 基本调用：pd.read_excel(文件路径)
- 默认第一行作表头，无表头文件须设 header=None
- Excel 无分隔符概念，不需要 sep 参数
一个没有表头的 Excel 直接 read_excel 会出什么问题？::第一行数据被当成列名，同时自动生成一列 0、1、2… 的默认索引，原索引列变成普通数据列，结构错位。
为什么读 Excel 时不用像读 CSV 那样考虑 sep？::Excel 是二进制工作簿格式，单元格边界由文件结构决定，不存在文本分隔符。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
