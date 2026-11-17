---
term: apply
aliases: [Series.apply, DataFrame.apply]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 45
stage: "S02E30 · 数据处理的三板斧"
order: 45
---

# apply

> 别名：Series.apply、DataFrame.apply

**对 Series 逐元素或对 DataFrame 按轴（行/列）执行函数并整合结果。**

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

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
