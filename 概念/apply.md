---
term: apply
aliases: [Series.apply, DataFrame.apply]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 45
stage: "S02E30 · 数据处理的三板斧"
---

# apply

> 别名：Series.apply、DataFrame.apply

**对 Series 逐元素或对 DataFrame 按轴（行/列）执行函数并整合结果。**

## 用法
**语法**：`Series.apply(func, args=())` / `DataFrame.apply(func, axis=0, args=(), raw=False)`
**参数**：
- `func`：要应用的函数，可以是自定义函数、lambda 或内置函数（如 `len`），函数必须有 `return`，否则会得到 None
- `axis`：仅 DataFrame 显示。`0`（默认）按列执行，`1` 按行执行；此时每列或每行都会作为 Series 传入，索引就是列名或行索引
- `args`：传给 `func` 的额外位置参数，单元素元组中逗号不能省，写成 `args=(0.5,)`
- `raw`：仅 DataFrame 显示。默认 `False` 时传入 Series，`True` 时传入 ndarray
- `result_type`：仅 DataFrame 显示，用来控制返回类型，比如设为 `'expand'` 会把结果展开成 DataFrame
**示例**：
```python
import pandas as pd

df = pd.DataFrame({'姓名': ['张三', '李四'], '身高': [1.75, 1.60], '体重': [70, 50]})
df['姓名字数'] = df['姓名'].apply(len)

def bmi(row, base):
    return round(row['体重'] / row['身高'] ** 2 + base, 1)

df['BMI'] = df.apply(bmi, axis=1, args=(0.5,))
print(df['姓名字数'].tolist())  # [2, 2]
print(df['BMI'].tolist())       # [23.4, 20.0]
```

## 解释

apply 比 map 更通用：对 Series 是逐元素处理，对 DataFrame 则按 axis 决定把每一列或每一行作为 Series 传入函数。支持通过 args 传额外参数，是行级计算的主力方法。

## 有什么用

- 按行用身高体重计算 BMI
- 对多列分别求和/求平均
- 给成绩列统一加减分并传误差参数

## 关键要点

- axis=0 对每列执行，axis=1 对每行执行
- axis=1 时每行以 Series 传入，索引为列名
- 函数必须有 return，否则得到 None
- 多参数用 args=(5,) 传入，单元素元组逗号不能省
- 结果按原轴顺序整合成 Series 返回

## 边界与易混淆

axis 含义易与 NumPy 混淆：Pandas 中 axis=0 是沿行方向对每列聚合，不是横向相加一行。

## 关联

- [[map]] — 对比项
- [[applymap]] — 对比项
- [[axis 参数]] — 前置知识
- [[Series]] — 上位概念

## 自测

df.apply(f, axis=1) 时，函数 f 收到的参数是什么？::一行数据组成的 Series，其索引是各列列名。
为什么 BMI 计算必须用 axis=1 而不是 axis=0？::BMI 需要同一行内的身高和体重两列一起算，axis=1 才把整行作为整体传入。


### 补充 · 2026-11-17

apply 接收一个函数（自定义函数、lambda、内置函数或 NumPy 函数），自动遍历 Series 元素或 DataFrame 的行/列并返回结果。它解决的是无法用简单向量化表达、需要逐元素或逐组自定义逻辑的场景。DataFrame.apply 默认按列（axis=0），axis=1 时按行。

- Series.apply 逐元素，DataFrame.apply 逐行或逐列
- 默认 axis=0 按列，axis=1 按行
- 可传 lambda、内置函数（len）、NumPy 函数（np.sqrt）
DataFrame.apply 默认按行还是按列处理？怎么改成按行？::默认按列（axis=0），改成 axis=1 即按行。
apply 里 lambda 的参数 m 在按列和按行时分别代表什么？::按列时 m 是一列 Series，m.name 是列名；按行时 m 是一行 Series，m.name 是行索引名。

apply 有两种对象：Series.apply 逐元素处理单列；DataFrame.apply 按 axis 决定是把每一列还是每一行作为 Series 传入函数。它的核心优势是可通过 args 携带额外参数，因此比 map 更适合复杂计算。

- Series.apply 逐元素；DataFrame.apply 按 axis 逐列或逐行
- axis=0 对每列执行函数，axis=1 对每行执行函数
- axis=1 时函数收到的是该行组成的 Series，索引用列名，可用 data["身高"] 取值
df.apply(bmi, axis=1) 里 bmi 函数收到的 data 到底是什么？::是该行数据组成的一个 Series，索引是各列列名，所以能用 data["身高"] 取到值
为什么 df[["语文","数学"]].apply(sum, axis=0) 得到的是每列总和而不是每行总和？::axis=0 表示沿零轴（行标签方向）逐行向下累加，即对每一列分别聚合
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p45 S02E30.数据处理的三板斧](https://www.bilibili.com/video/BV1ji4y157uB?p=45) · 2026-11-17

Series.apply 逐元素执行；DataFrame.apply 默认按列执行（axis=0），传 axis=1 才按行执行。回调收到的参数 m：按列时是一列 Series，按行时是一行 Series，m.name 就是列名或行索引名，因此可以在回调里按名字挑选要计算的行列。

- Series.apply 逐元素；DataFrame.apply 默认 axis=0 按列，axis=1 按行
- 回调参数 m 是被处理的一行或一列 Series，m.name 给出其名字
- 可传内置函数 apply(len)、库函数 apply(np.square)、自定义函数或 lambda
数据1.apply(lambda m: ..., axis=1) 中 m 代表什么？::一行数据（一行 Series），m.name 是这行的行索引名。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p26 S02E11.列与列之间的计算](https://www.bilibili.com/video/BV1ji4y157uB?p=26) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
