---
term: 字典构造 DataFrame
aliases: [dict 建表, pd.DataFrame(dict)]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 21
stage: "S02E06 · 数据结构之DataFrame"
---

# 字典构造 DataFrame

> 别名：dict 建表、pd.DataFrame(dict)

**用字典的键作列名、值作列数据来创建 DataFrame 的写法。**

## 用法
**语法**：`pd.DataFrame(data=None, index=None, columns=None)`
**参数**：
- `data`：字典时，键作为列名，值（通常是列表）作为该列数据；各列表长度不一致时按最长的列对齐，缺的位置补 NaN
- `index`：行索引，省略时自动生成 0~n-1
- `columns`：指定列顺序，也可用于从字典中挑选部分键
**示例**：
```python
import pandas as pd

df = pd.DataFrame({'序号': [1, 2], '姓名': ['叶问', '李小龙']})
print(df)
#    序号   姓名
# 0   1   叶问
# 1   2  李小龙

# 各列长度不一致时 pd.DataFrame 会直接报错，必须补齐或删掉多余项
df2 = pd.DataFrame({'a': [1, 2, 3], 'b': [10, 20, 30]})
print(df2)
```

## 解释

pd.DataFrame({...}) 接收字典时，键自动成为列名，值（通常是列表）成为该列各行数据。这是手工造小表最直观的方式，数值不加引号、字符串加引号。

## 有什么用

- 快速构造演示或测试用的小型二维表
- 把已有字典数据转成表格

## 关键要点

- 键是列名，值通常是列表表示一列数据
- 数值不加引号，字符串必须加引号
- 键名应唯一，列表内的值可以重复
- 各列列表长度应一致，否则会补缺失值

## 边界与易混淆

只适合小数据量手工构造，大批量数据应从文件读取。

## 关联

- [[DataFrame]] — 上位概念
- [[Series]] — 组合使用
- [[set_index]] — 组合使用

## 自测

pd.DataFrame({'序号':[1,2],'姓名':['叶问','李小龙']}) 生成的表有几列几行？::两列（序号、姓名）两行。
如果字典里两个列表长度不同会怎样？::Pandas 会按最长列对齐，短列缺失位置补 NaN。


### 补充 · 2026-11-17

字典的 key 成为列名，value 则是这一列的各行取值（通常写成列表）。这样不必先有文件，就能在代码里直接造出数据表再导出。

- key 作为列名，必须唯一
- value 用列表表示该列的多行取值，取值可以重复
- 字符串要加引号，数值不加引号
字典里两个 key 都叫“姓名”会发生什么？::后一个会覆盖前一个，字典的 key 必须唯一，最后表里只剩一列“姓名”。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p16 S02E01.数据类型与新建文件](https://www.bilibili.com/video/BV1ji4y157uB?p=16) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
