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
---

# pd.read_excel

> 别名：read_excel、读取 Excel

**pandas 读取 Excel 文件为 DataFrame 的函数。**

## 用法
**语法**：`pd.read_excel(io, sheet_name=0, header=0, names=None, index_col=None, usecols=None, nrows=None)`
**参数**：
- `io`：文件路径或类文件对象
- `sheet_name`：默认 0，读取第一个工作表；可传入表名、索引或列表；传 `None` 会读取全部工作表，并返回字典
- `header`：表头所在行号，默认 0；`header=None` 表示没有表头，`header=[0,1]` 表示前两行都作为表头
- `names`：自定义列名列表，常与 `header=None` 配合使用
- `index_col`：指定某列作为行索引
- `usecols`：只读取指定的列
- `nrows`：只读取前 n 行
**示例**：
```python
import pandas as pd

with pd.ExcelWriter("demo.xlsx") as w:
    pd.DataFrame({"姓名": ["杨过", "小龙女"], "分数": [90, 95]}).to_excel(w, sheet_name="一班", index=False)
    pd.DataFrame({"姓名": ["郭靖"], "分数": [88]}).to_excel(w, sheet_name="二班", index=False)

sheets = pd.read_excel("demo.xlsx", sheet_name=None)   # 一次读全部工作表，返回字典
print(list(sheets))                                    # ['一班', '二班']
print(sheets["二班"]["分数"].tolist())                 # [88]
```

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

它是 Excel 数据进入 pandas 的唯一主入口，与 to_excel 构成方向相反的一对。返回值总是 DataFrame，之后所有清洗、改表头、设索引都基于这个对象进行。

- 与 to_excel 方向相反：Excel → DataFrame
- 不需要 sep，Excel 无分隔符概念
- 无表头文件要配 header=None 与 names 一起用
read_excel 与 to_excel 在数据流向上有什么区别？::read_excel 把 Excel 读成 DataFrame，to_excel 把 DataFrame 写成 Excel，两者方向相反。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p19 S02E04.读取与修改Excel文件](https://www.bilibili.com/video/BV1ji4y157uB?p=19) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
