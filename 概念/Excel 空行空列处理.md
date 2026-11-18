---
term: Excel 空行空列处理
aliases: [skiprows + usecols 组合, 跳过空行选择列区, 脏表头修复]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
---

# Excel 空行空列处理

> 别名：skiprows + usecols 组合、跳过空行选择列区、脏表头修复

**用 skiprows 跳过表头上方空行、usecols 选有效列区，把脏 Excel 读成规整表。**

## 用法
**语法**：`pd.read_excel(path, header=None, skiprows=..., usecols=...)`

**参数**：
- `header`：表头所在行序号；没有表头传 `None`
- `skiprows`：跳过开头若干行（如标题、说明行）
- `usecols`：只读取指定列，跳过空列

**示例**：
```python
import pandas as pd
from io import BytesIO

# 用内存里的 Excel 演示，避免依赖外部文件
buf = BytesIO()
pd.DataFrame([[None, None], ['姓名', '成绩'], ['张三', 90]]).to_excel(buf, index=False, header=False)
buf.seek(0)

df = pd.read_excel(buf, header=1)     # 第 1 行作表头，跳过顶部空行
print(df.columns.tolist())            # ['姓名', '成绩']
```

## 解释

真实 Excel 常从第 9 行才开始有数据、左边还空着几列，直接 read_excel 会读进一堆 NaN 列并让表头错位。两个参数一配合，读进来就是干净表格。

## 有什么用

- 读取上方带说明行、标题行的报表
- 只取报表中某几列，忽略无关列

## 关键要点

- skiprows=n 表示跳过最前面 n 行，第 n+1 行被当作表头
- 少跳一行会把表头读进数据区，造成列名错位
- usecols='F:I' 直接类比 Excel 的 F 到 I 列区域写法
- CSV 一般从头开始存数据，不需要这两个参数

## 边界与易混淆

多级表头、合并单元格的表格靠这两个参数不够，还要配合 header 或手工重塑。

## 关联

- [[skiprows 参数]] — 上位概念
- [[usecols 参数]] — 上位概念
- [[pd.read_excel]] — 组合使用

## 自测

表头在第 7 行、上面 6 行是空的，skiprows 该写多少？::写 6，跳过前 6 行后第 7 行正好成为列名
为什么说 CSV 比 Excel 好读？::CSV 数据通常从第一行开始、结构扁平，不需要跳过空行和选列区

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p25 S02E10.各种数据自动填充](https://www.bilibili.com/video/BV1ji4y157uB?p=25) · 2026-11-17
