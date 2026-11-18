---
term: DataFrame 构造
aliases: [创建 DataFrame, pd.DataFrame, DataFrame 创建方式]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
---

# DataFrame 构造

> 别名：创建 DataFrame、pd.DataFrame、DataFrame 创建方式

**用嵌套列表、字典或多个 Series 生成二维表的方法。**

## 用法
**语法**：`pd.DataFrame(data=None, index=None, columns=None, dtype=None)`
**参数**：
- `data`：二维数据，可为嵌套列表（每个子列表是一行）、字典（key 当列名、value 当该列的等长值列表）、`{s.name: s}` 形式的多个 Series，或二维 ndarray
- `index`：行索引，默认 RangeIndex 0、1、2…
- `columns`：列名，用列表数据而不指定时列名为 0、1、2…
- `dtype`：统一指定元素类型，通常省略，由 pandas 自行推断
**示例**：
```python
import pandas as pd
# 字典：key 是列名，value 是等长的值列表
print(pd.DataFrame({'a': [1, 2], 'b': [3, 4]}))
#    a  b
# 0  1  3
# 1  2  4
# 嵌套列表：每个子列表一行，必须配 columns 才有列名
print(pd.DataFrame([[1, 2], [3, 4]], columns=['x', 'y']))
#    x  y
# 0  1  2
# 1  3  4
# 多个 Series：{s.name: s} 按列组合，索引自动对齐
s1 = pd.Series([1, 2], index=['r1', 'r2'], name='x')
s2 = pd.Series([3, 4], index=['r1', 'r2'], name='y')
print(pd.DataFrame({'x': s1, 'y': s2}))
#     x  y
# r1  1  3
# r2  2  4
```

## 解释

pd.DataFrame() 接收数据并按 columns、index 参数组织成表。嵌套列表是“外层列表装若干子列表，每个子列表是一行”；字典是“key 当列名、value 当该列的值列表”；也可以用多个 Series 组合。真实工作中更常直接读取文件。

## 有什么用

- 手写少量测试数据验证逻辑
- 把散落的多个 Series 拼成一张表
- 理解 DataFrame 由什么构成

## 关键要点

- 嵌套列表需配 columns 指定列名，否则列名是 0、1、2
- 字典创建时 key 是列名，value 是等长的值列表
- 多个 Series 可用 {s.name: s} 按列组合，索引自动对齐
- 用 [s1, s2, s3] 列表方式组合会把 Series 当行，行列互换
- 字典键值对之间漏写逗号是最常见的报错原因

## 边界与易混淆

列表方式组合多个 Series 相当于把一维转二维，看起来像透视表，日常业务里很少这么建表。

## 关联

- [[DataFrame]] — 上位概念
- [[Series]] — 组合使用
- [[字典]] — 前置知识
- [[索引对齐]] — 组合使用
- [[pd.read_csv]] — 对比项

## 自测

pd.DataFrame({'a':[1,2],'b':[3,4]}) 的列名和行索引分别是什么？::列名 a、b；行索引默认 RangeIndex 0、1
用 [s1, s2, s3] 而不是 {s1.name: s1, ...} 组合，结果差异在哪？::列表方式把每个 Series 当成一行，行列被转置；字典方式让每个 Series 成为一列


### 补充 · 2026-11-17

最简形式 pd.DataFrame(np.array([[1,2,3],...]), columns=list('xyz'), index=list('abc'))：数据是二维数组，columns 给列名，index 给行名。两者都是关键字参数，先后无所谓；用 list('xyz') 比逐个手写引号逗号简洁得多。

- columns=list('xyz')、index=list('abc') 快速命名行列
- 关键字参数顺序无关，先写 index 也行
- 手工建 3×3 小表便于上下对照验证运算结果
pd.DataFrame(arr, columns=list('xyz'), index=list('abc')) 得到几行几列？::3 行 3 列，行名 a/b/c，列名 x/y/z。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p26 S02E11.列与列之间的计算](https://www.bilibili.com/video/BV1ji4y157uB?p=26) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p21 S02E06.数据结构之DataFrame](https://www.bilibili.com/video/BV1ji4y157uB?p=21) · 2026-11-17
