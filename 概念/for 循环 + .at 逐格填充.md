---
term: for 循环 + .at 逐格填充
aliases: [循环填充, 遍历索引填值, for i in 数据.index]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
---

# for 循环 + .at 逐格填充

> 别名：循环填充、遍历索引填值、for i in 数据.index

**用 for 遍历行索引、再用 .at 逐格写入，模拟 Excel 下拉填充。**

## 用法
**语法**：`数据.at[行标签, 列标签]`、`数据['列'].at[行标签]`
**参数**：
- `行标签`：要定位的行索引值，循环里直接用 `数据.index` 给出的 `i`
- `列标签`：DataFrame 版需要，写列名如 `'序号'`；先取单列后用 `Series.at` 则只传一个标签
- 不支持切片、列表或多值：`.at` 一次只定位一个标量格子
**示例**：
```python
import pandas as pd
df = pd.DataFrame({'序号': [None]*3, '性别': [None]*3, '日期': [None]*3}, dtype=str)
start = pd.Timestamp('2020-01-01')
for i in df.index:
    df['序号'].at[i] = str(i + 1)                                   # 序号 i+1
    df['性别'].at[i] = '男' if i % 2 == 0 else '女'                  # 奇偶判断
    df['日期'].at[i] = (start + pd.Timedelta(days=i)).strftime('%Y-%m-%d')
print(df['序号'].tolist())   # ['1', '2', '3']
print(df['性别'].tolist())   # ['男', '女', '男']
print(df['日期'].tolist())   # ['2020-01-01', '2020-01-02', '2020-01-03']
```

## 解释

拿到 数据.index 就拿到了 0、1、2…… 的行号，序号填 i+1，性别用 i%2 判断，日期用起始日期加偏移，一个循环能生成整列序列。本质是把 Excel 的“拖拽规律”翻译成代码规律。

## 有什么用

- 批量补全序号、性别、日期等有规律的列
- 把 Excel 下拉填充行为搬进 Pandas 脚本

## 关键要点

- 数据.index 提供行号序列，是填充的驱动变量
- 优先写 数据['列'].at[i]，先取单列再定位，比整表 .at[i,'列'] 省内存
- 填充前用 dtype 把相关列统一设为 str，否则易报错或显示成 1.0
- 必须先填完再 set_index，顺序颠倒会打乱循环依据

## 边界与易混淆

逐格写是 Python 级循环，几十万行会很慢；大数据应改用向量化构造或 map/apply。

## 关联

- [[.at 索引器]] — 组合使用
- [[自动填充]] — 下位概念
- [[set_index]] — 前置知识

## 自测

为什么性别列写成 数据['性别'].at[i] 而不是每次 数据.at[i,'性别']？::先取出单列再按行定位，避免每次在整张表上查找，省内存也更快
填充后序号显示 1.0、2.0 是什么原因？::列里有空值，Pandas 推断成浮点型；读取时把该列 dtype 设为 str 可避免

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p25 S02E10.各种数据自动填充](https://www.bilibili.com/video/BV1ji4y157uB?p=25) · 2026-11-17
