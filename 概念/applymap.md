---
term: applymap
aliases: [DataFrame.applymap]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 45
stage: "S02E30 · 数据处理的三板斧"
---

# applymap

> 别名：DataFrame.applymap

**对 DataFrame 每个单元格逐个执行函数，返回同形状的新表。**


## 用法
**语法**：`DataFrame.applymap(func, na_action=None)`（旧版写法，pandas 2.1 起弃用，推荐使用 `DataFrame.map(func, na_action=None)`）

**参数**：
- `func`：作用于每个单元格的函数，只接收一个值、返回一个值，常配合 lambda 使用
- `na_action`：`None`（默认）表示 NaN 也会传入函数；`"ignore"` 表示跳过 NaN，原样保留

**示例**：
```python
import pandas as pd

df = pd.DataFrame({"a": [1.23456, 2.5], "b": [3.14159, 0.5]})

# 旧版写法：df.applymap(lambda x: f"{x:.2f}")，pandas 2.1 起弃用并触发 FutureWarning
print(df.map(lambda x: f"{x:.2f}"))
#       a     b
# 0  1.23  3.14
# 1  2.50  0.50

print(df.map(lambda x: f"{x:.2f}").dtypes.tolist())
# ['object', 'object']
```

## 解释

applymap 是 DataFrame 专属的逐元素方法，把每个单元格的值单独传入函数。常用于统一格式化，如保留小数位、加单位等。

## 有什么用

- 把整表数字统一格式化为保留三位小数
- 对每个单元格套用同一清洗函数

## 关键要点

- 只作用于 DataFrame，不能用于 Series
- 逐单元格执行，不感知行或列的整体结构
- 常配合 lambda 与格式化字符串使用
- 格式化后返回字符串，数值类型会改变
- 使用频率低于 map 和 apply

## 边界与易混淆

与 apply 区别：apply 按行/列整体处理，applymap 只看单个单元格，无法跨列计算。

## 关联

- [[apply]] — 对比项
- [[DataFrame]] — 上位概念

## 自测

要按行用两列算出一个新值，能用 applymap 吗？::不能，applymap 每次只拿到一个单元格，跨列计算要用 apply(axis=1)。
applymap 格式化小数后，列的数据类型会怎样？::变成字符串（object），不再是数值类型。


### 补充 · 2026-11-17

applymap 不看行也不看列，只把表中每个单元格的值单独交给函数处理，常用于全表统一格式化，比如把数字统一保留几位小数、转成字符串。它的利用率低于 map 和 apply。

- 作用对象是 DataFrame 的每个单元格，与行列方向无关
- 典型写法：数据.applymap(lambda x: f"{x:.3f}") 保留三位小数
- 整数也会被格式化成像 1.000 的带小数点形式
要按每行的身高体重算 BMI，为什么不能用 applymap？::applymap 每次只拿到一个单元格的值，拿不到同一行的身高和体重，无法做跨列计算
f"{x:.2f}" 的结果是数值还是字符串？::字符串，会改变该列的数据类型
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p45 S02E30.数据处理的三板斧](https://www.bilibili.com/video/BV1ji4y157uB?p=45) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
