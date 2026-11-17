---
term: Excel 无表头文件处理
aliases: [无表头读取, header=None 组合写法, Excel 表头修复]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 19
stage: "S02E04 · 读取与修改Excel文件"
---

# Excel 无表头文件处理

> 别名：无表头读取、header=None 组合写法、Excel 表头修复

**用 header=None + names + index_col 一次性把无表头 Excel 读成规范表的写法。**

## 用法
**语法**：`pd.read_excel(io, header=None, names=[...], index_col=0)`
**参数**：
- `io`：文件路径或文件对象，如 `'data.xlsx'`
- `header=None`：声明首行不是表头，避免数据首行被当作列名
- `names`：列表，按顺序指定各列列名，长度与数据列数一致
- `index_col`：指定哪一列作行索引，`0` 表示第一列；不设会多出一列 0、1、2… 的默认索引
- `sheet_name`：工作表名或序号，默认读第一个工作表
**示例**：
```python
import pandas as pd

# 造一个无表头 Excel：第一列是序号，后两列是成绩
pd.DataFrame([[1, '张三', 90], [2, '李四', 85]]).to_excel('raw.xlsx', header=False, index=False)

# 三步一次给全：关自动表头、给列名、定索引
df = pd.read_excel('raw.xlsx', header=None, names=['编号', '姓名', '成绩'], index_col=0)
print(df)
#     姓名  成绩
# 编号
# 1   张三  90
# 2   李四  85
```

## 解释

无表头 Excel 直接读取会导致首行数据被当列名、索引错位。标准解法是在 read_excel 中同时声明“没有表头”“列名叫什么”“哪列作索引”，读入即得到带表头带索引的干净 DataFrame。

## 有什么用

- 读取导出系统生成的裸数据 Excel
- 批量修复结构不规范的工作簿

## 关键要点

- 三步：header=None 关自动表头、names 给列名、index_col 定索引
- 顺序无关，但三者需同时给全才不产生冗余列
- 参数名大小写必须正确
- 处理后可直接 to_excel 写回原路径

## 边界与易混淆

仅解决结构问题，不解决数据类型和日期格式问题。

## 关联

- [[header 参数]] — 组合使用
- [[names 参数]] — 组合使用
- [[index_col 参数]] — 组合使用
- [[pd.read_excel]] — 上位概念

## 自测

只设 header=None 不设 index_col，读出来会多出什么？::会多出一列 0、1、2… 的默认索引，而原本的序号列仍作为普通数据列存在。


### 补充 · 2026-11-17

无表头文件直接读会同时踩两个坑：首行数据被当成列名，原索引列旁边又多出一列自动索引。标准解法是一次性在 read_excel 里声明「无表头 + 自定义列名 + 指定索引列」。

- 标准写法：read_excel(路径, header=None, names=[...], index_col='序号')
- 三步含义：声明无表头 → 给列名 → 指定索引列
- 漏写 header=None：首行数据被当列名并且丢失
给出读取无表头 Excel 并指定序号为索引的完整参数组合。::pd.read_excel(路径, header=None, names=['序号','姓名','年龄','手机地址','入职日期'], index_col='序号')
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p19 S02E04.读取与修改Excel文件](https://www.bilibili.com/video/BV1ji4y157uB?p=19) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
