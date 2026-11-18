---
term: iloc
aliases: [df.iloc, 位置索引]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 21
stage: "S02E06 · 数据结构之DataFrame"
---

# iloc

> 别名：df.iloc、位置索引

**按行列的整数位置查询 DataFrame 元素的索引器。**

## 用法
**语法**：`df.iloc[行位置, 列位置]`
**参数**：
- `行位置`：整数、整数切片或整数列表，从 0 开始，与索引标签无关；切片不包含结束位置
- `列位置`：整数、整数切片或整数列表，按列在 DataFrame 中的物理顺序编号
**示例**：
```python
import pandas as pd

df = pd.DataFrame({'语文': [90, 80, 70], '数学': [85, 95, 75]}, index=['A', 'B', 'C'])
print(df.iloc[0, 0])        # 90（第 0 行第 0 列，跟标签 'A' 无关）
print(df.iloc[0:2, 1])      # A    85 / B    95（切片不含结束位置）
print(df.iloc[[0, 2], :])   # 按序号挑第 1、3 行，返回整张子表
```
说明：`loc` 按标签取数、`iloc` 按位置取数，二者不要混用，避免「标签恰好是整数」时取错。

## 解释

iloc 完全基于数据的位置编号（从 0 开始）取数，语法为 df.iloc[行位置, 列位置]。无论索引标签被改成什么，位置编号始终不变，适合按第几行第几列取数。

## 有什么用

- 按第几行第几列取数
- 索引标签混乱时仍能稳定定位

## 关键要点

- 语法 df.iloc[行位置, 列位置]
- 位置始终从 0 开始，与标签无关
- 切片时不包含结束位置
- 常用于循环或按序号取数

## 边界与易混淆

易与 loc 混淆；位置是物理顺序，数据排序变化后同一位置对应内容会变。

## 关联

- [[loc]] — 对比项
- [[DataFrame]] — 上位概念

## 自测

df 的 index 被设为 ['A','B','C']，df.iloc[0,0] 取到的是什么？::第 0 行第 0 列的数据，即物理位置第一行第一列，与标签无关。
为什么说 iloc 比 loc 更适合按序号批量取数？::因为 iloc 只认从 0 开始的位置编号，不受索引标签改动影响。


### 补充 · 2026-11-17

iloc 完全无视标签，只看物理位置：第 0 行第 0 列永远是表里的左上角。因此无论 index 被改成什么，iloc 的写法都不变。位置切片遵循 Python 惯例，不含结束位。

- 写法 df.iloc[行位置, 列位置]，如 df.iloc[0, 0]
- 位置从 0 开始，与标签内容无关
- 位置切片不含结束位，iloc[0:3] 取 0、1、2 三行
表被 set_index 成中文姓名后，想取第 3 行第 2 列该用哪个索引器？::iloc，写作 df.iloc[2, 1]；loc 需要标签名
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p21 S02E06.数据结构之DataFrame](https://www.bilibili.com/video/BV1ji4y157uB?p=21) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
