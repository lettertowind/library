---
term: index 参数
aliases: [index=, 索引参数]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 20
stage: "S02E05 · 数据结构之Series"
---

# index 参数

> 别名：index=、索引参数

**pd.Series() 中用于指定自定义索引的参数。**

## 用法
**语法**：`pd.Series(data, index=None)`

**参数**：
- `data`：数据值，可以是列表、字典等；放在第一个位置。
- `index`：自定义索引，接收一个列表，长度必须与 `data` 一致，否则报错。

**示例**：
```python
import pandas as pd

数据 = pd.Series(
    ["孙兴华", "男", "20岁", "2000-01-01"],
    index=["a", "b", "c", "d"]
)
print(数据)
# a          孙兴华
# b             男
# c           20岁
# d    2000-01-01
# dtype: object

print(数据.index)
# Index(['a', 'b', 'c', 'd'], dtype='object')
```

## 解释

创建 Series 时，通过 index 参数传入一个列表，可以将默认的整数索引替换为自定义索引。常用于索引和数据分别存放在两个列表中的场景。

## 有什么用

- 创建 Series 时指定自定义索引
- 将两个列表组合成带索引的 Series

## 关键要点

- index 参数接收一个列表
- pd.Series() 中先放值，再通过 index= 指定索引
- 可将默认的 0,1,2,3 替换为自定义索引如 a,b,c,d

## 边界与易混淆

index 列表长度必须与数据值长度一致，否则报错。

## 关联

- [[Series]] — 组合使用

## 自测

用两个列表创建 Series 时，值和索引分别放在哪里？::值放在 pd.Series() 的第一个位置，索引列表通过 index= 参数传入。


### 补充 · 2026-11-17

pandas 写 Excel 时默认把行索引也写成一列，导致打开文件多出一列数字。设 index=False 就能去掉，让输出和原始表格一致。

- to_excel(路径, index=False) 是最常用的去索引写法
- 读取时用 index_col 指定某列作索引，是相反方向的操作
- 默认不去索引，是新手输出“多一列数字”的根源
为什么用 to_excel 写出的表打开后左边多了一列 0、1、2？::默认写出了行索引，加 index=False 即可。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p40 S02E25.Excel文件的拆分与合并](https://www.bilibili.com/video/BV1ji4y157uB?p=40) · 2026-11-17

默认索引是 0、1、2… 的数字序列，用 index= 可以换成自定义标签（如 a、b、c、d 或姓名、性别、年龄）。使用两个列表时，第一个列表做值、index= 指定另一个列表做索引，顺序不能颠倒。

- 写在 pd.Series() 关键字参数位置，形如 index=["a","b","c","d"]
- 索引长度必须与值的长度一致
- 直接传列表指定索引在实际工作中较少见，更常见的是用字典
pd.Series(列表A, index=列表B) 中哪个是数据？::列表A 是数据值，列表B 是索引标签。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p20 S02E05.数据结构之Series](https://www.bilibili.com/video/BV1ji4y157uB?p=20) · 2026-11-17

index 决定透视结果的行标签，即按谁分组。多个分组条件时写成列表，结果会形成多级行索引。它只管行方向分组，不负责选择显示哪些数值列。

- 单条件写 index='部门'，多条件写列表。
- 结果先按第一字段分组，再列下一级。
- 不同部门下允许出现重名人员。
想按部门和销售人员两个条件做行分组，index 怎么写？::index=['部门','销售人员']
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p43 S02E28.数据透视表](https://www.bilibili.com/video/BV1ji4y157uB?p=43) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
